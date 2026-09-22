#!/usr/bin/env python3
"""Process the external volume interface transcript end-to-end."""

import sys
import os
import json
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

# Add pipeline to path
sys.path.insert(0, r'c:\Hackathon\AgentVerse')

from pipeline.extract import extract
from pipeline.clean import clean

# Configuration
TRANSCRIPT_FILE = r'c:\Hackathon\AgentVerse\transcripts\pending\video_66fo5e3lkqt_19_160_1220x686_transcript.txt'
KO_DIR = Path(r'c:\Hackathon\AgentVerse\knowledge\objects')
ARTIFACT_DIR = Path(r'c:\Hackathon\AgentVerse\knowledge\artifacts\run-20260922-external-volume-interface')
ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)

def word_count(text: str) -> int:
    """Count words in text."""
    return len(text.split())

def extract_heading(block: str, max_chars: int = 60) -> str:
    """Extract a heading from the first sentence of a block."""
    match = re.match(r'^([^.!?]*[.!?])', block)
    if match:
        heading = match.group(1).strip()
        heading = heading.rstrip('.!?').strip()
        if len(heading) > max_chars:
            heading = heading[:max_chars].rsplit(' ', 1)[0]
        return heading
    return block[:max_chars].strip()

def extract_key_points(block: str, max_points: int = 5) -> List[str]:
    """Extract key points from a block."""
    sentences = re.split(r'[.!?]\s+', block)
    key_points = []
    
    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) > 20 and len(key_points) < max_points:
            sentence = re.sub(r'^[^a-z]*', '', sentence, flags=re.IGNORECASE)
            if sentence:
                key_points.append(sentence)
    
    return key_points

def simple_similarity(text1: str, text2: str) -> float:
    """Calculate simple text similarity based on shared terms."""
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    
    if not words1 or not words2:
        return 0.0
    
    intersection = len(words1 & words2)
    union = len(words1 | words2)
    
    return intersection / union if union > 0 else 0.0

def slugify(title: str) -> str:
    """Convert title to kebab-case slug."""
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'\s+', '-', slug).strip('-')
    slug = re.sub(r'-+', '-', slug)
    return slug[:50]

def main():
    """Main processing function."""
    print("=" * 70)
    print("KNOWLEDGE EXTRACTION - EXTERNAL VOLUME INTERFACE")
    print("=" * 70)
    
    # Step 1: Extract and clean
    print("\n[1/6] Loading and cleaning transcript...")
    raw_text = extract(TRANSCRIPT_FILE)
    raw_char_count = len(raw_text)
    clean_text = clean(raw_text)
    clean_char_count = len(clean_text)
    
    print(f"  Raw: {raw_char_count:,} chars → Clean: {clean_char_count:,} chars")
    
    # Step 2: Split into topic blocks
    print("\n[2/6] Splitting into topic blocks...")
    paragraphs = clean_text.split('\n\n')
    topic_blocks = [p.strip() for p in paragraphs if p.strip() and word_count(p) >= 20]
    
    print(f"  Found {len(topic_blocks)} topic blocks")
    
    # Step 3: Extract headings and key points
    print("\n[3/6] Extracting headings and key points...")
    topics = []
    for i, block in enumerate(topic_blocks, 1):
        heading = extract_heading(block)
        key_points = extract_key_points(block)
        topics.append({
            "index": i,
            "heading": heading,
            "key_points": key_points,
            "body": block
        })
    
    print(f"  Extracted {len(topics)} topics")
    
    # Step 4: Load existing KOs
    print("\n[4/6] Loading existing Knowledge Objects...")
    existing_kos = {}
    for ko_file in sorted(KO_DIR.glob('ko-*.json')):
        try:
            with open(ko_file, 'r') as f:
                ko = json.load(f)
                existing_kos[ko['id']] = ko
        except Exception as e:
            print(f"  Warning: Error loading {ko_file.name}: {e}")
    
    print(f"  Loaded {len(existing_kos)} existing KOs")
    
    # Step 5: Match topics against KOs
    print("\n[5/6] Matching topics against Knowledge Objects...")
    topic_matches = []
    for topic in topics:
        topic_text = topic['heading'] + ' ' + ' '.join(topic['key_points'])
        
        best_match = None
        best_score = 0.0
        
        for ko_id, ko in existing_kos.items():
            ko_text = ko['title'] + ' ' + ' '.join(ko.get('tags', []))
            for section in ko.get('sections', []):
                ko_text += ' ' + section['heading']
            
            score = simple_similarity(topic_text, ko_text)
            if score > best_score:
                best_score = score
                best_match = (ko_id, ko, score)
        
        if best_score >= 0.45:
            match_type = "existing-ko"
            matched_ko_id = best_match[0]
        else:
            match_type = "new-ko-existing-category"
            matched_ko_id = None
        
        topic_matches.append({
            "topic_index": topic['index'],
            "heading": topic['heading'],
            "match_type": match_type,
            "matched_ko_id": matched_ko_id,
            "match_score": best_score if best_match else 0.0
        })
    
    # Step 6: Create or update KOs
    print("\n[6/6] Creating/updating Knowledge Objects...")
    created_kos = []
    updated_kos = []
    
    for match in topic_matches:
        topic = topics[match['topic_index'] - 1]
        
        if match['match_type'] == 'existing-ko':
            ko_id = match['matched_ko_id']
            ko = existing_kos[ko_id]
            
            section_exists = any(
                simple_similarity(section['heading'], topic['heading']) > 0.75
                for section in ko['sections']
            )
            
            if not section_exists:
                new_section = {
                    "heading": topic['heading'],
                    "body": topic['body'],
                    "key_points": topic['key_points']
                }
                ko['sections'].append(new_section)
                ko['version'] = ko.get('version', 1) + 1
                ko['updated_at'] = datetime.now().strftime('%Y-%m-%d')
                
                new_source = {
                    "transcript": Path(TRANSCRIPT_FILE).name,
                    "extracted_at": datetime.now().strftime('%Y-%m-%d')
                }
                
                source_exists = any(
                    s['transcript'] == new_source['transcript']
                    for s in ko.get('sources', [])
                )
                if not source_exists:
                    ko['sources'] = ko.get('sources', []) + [new_source]
                
                updated_kos.append(ko_id)
                
                ko_file = KO_DIR / f"{ko_id}.json"
                with open(ko_file, 'w') as f:
                    json.dump(ko, f, indent=2)
        
        elif match['match_type'] == 'new-ko-existing-category':
            slug = slugify(topic['heading'])
            ko_id = f"ko-{slug}"
            
            counter = 1
            while ko_id in existing_kos or (KO_DIR / f"{ko_id}.json").exists():
                ko_id = f"ko-{slug}-{counter}"
                counter += 1
            
            category = "core-features/imports.md"
            
            new_ko = {
                "id": ko_id,
                "slug": slug,
                "title": topic['heading'],
                "category": category,
                "status": "draft",
                "summary": topic['key_points'][0] if topic['key_points'] else topic['heading'],
                "sections": [{
                    "heading": topic['heading'],
                    "body": topic['body'],
                    "key_points": topic['key_points']
                }],
                "tags": ["external-volume", "manual-entry", "meter-input"],
                "sources": [{
                    "transcript": Path(TRANSCRIPT_FILE).name,
                    "extracted_at": datetime.now().strftime('%Y-%m-%d')
                }],
                "relationships": [],
                "faqs": [],
                "version": 1,
                "created_at": datetime.now().strftime('%Y-%m-%d'),
                "updated_at": datetime.now().strftime('%Y-%m-%d'),
                "published_pages": []
            }
            
            created_kos.append(ko_id)
            existing_kos[ko_id] = new_ko
            
            ko_file = KO_DIR / f"{ko_id}.json"
            with open(ko_file, 'w') as f:
                json.dump(new_ko, f, indent=2)
    
    # Step 7: Save extraction artifact
    print("\n[7/7] Saving extraction artifact...")
    extraction_artifact = {
        "run_id": "run-20260922-external-volume-interface",
        "agent": "knowledge-extraction",
        "generated_at": datetime.now().isoformat(),
        "source_transcript": Path(TRANSCRIPT_FILE).name,
        "topics": topic_matches,
        "knowledge_objects": created_kos + updated_kos,
        "unmatched_topics": []
    }
    
    artifact_file = ARTIFACT_DIR / "artifact-extraction.schema.json"
    with open(artifact_file, 'w') as f:
        json.dump(extraction_artifact, f, indent=2)
    
    print(f"  Saved to: {artifact_file}")
    
    # Summary
    print("\n" + "=" * 70)
    print("PROCESSING SUMMARY")
    print("=" * 70)
    print(f"Topics extracted: {len(topics)}")
    print(f"Knowledge Objects created: {len(created_kos)}")
    print(f"Knowledge Objects updated: {len(updated_kos)}")
    print(f"Total affected: {len(created_kos) + len(updated_kos)}")
    
    if created_kos:
        print(f"\nCreated KOs:")
        for ko_id in created_kos:
            print(f"  • {ko_id}")
    
    if updated_kos:
        print(f"\nUpdated KOs:")
        for ko_id in updated_kos:
            print(f"  • {ko_id}")
    
    print("\n" + "=" * 70)

if __name__ == '__main__':
    main()
