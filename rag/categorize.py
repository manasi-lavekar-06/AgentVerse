"""categorize.py — one-time setup step: derive a category taxonomy from the
product's own help documentation before any transcript can be processed.

This repo's Knowledge Objects are always filed under a `category` (a docs/ page path).
For FLOWCAL those categories were hand-designed; to reuse this tool for a *different*
product, someone must first tell it what categories to use — by pointing it at that
product's existing help doc (an exported TOC, article list, or help-center outline).
`build_categories()` reads that file, asks the LLM to propose a small tab/page taxonomy,
and writes it to knowledge/categories.json. Until that file exists, rag/pipeline.py
refuses to run (see `require_categories()`).

CLI:
    python -m rag.categorize <help_doc_path> [--product "Product Name"]
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from pipeline.clean import clean
from pipeline.extract import extract

from rag import config

_REPO_ROOT = Path(__file__).resolve().parent.parent
CATEGORIES_PATH = _REPO_ROOT / "knowledge" / "categories.json"

_CATEGORIZE_SYSTEM_PROMPT = """You are setting up the category taxonomy for a product \
knowledge hub, from that product's existing help documentation (a table of contents, \
article list, or help-center outline). Propose 3-8 top-level nav tabs, and under each, \
2-8 page categories that the source material's topics would sensibly file under. Each \
page category needs a docs/-relative path, a short label, and a one-sentence description \
of what belongs there. Respond with strict JSON only, matching this shape:
{
  "product": string,
  "tabs": [
    { "name": string,  // nav tab label, e.g. "Core Features"
      "pages": [ { "path": string,  // e.g. "core-features/example.md"
                   "label": string,
                   "description": string } ] }
  ]
}"""


def has_categories() -> bool:
    return CATEGORIES_PATH.exists()


def require_categories() -> dict:
    """Load the category taxonomy, or raise if setup hasn't been run yet."""
    if not has_categories():
        raise RuntimeError(
            "No category taxonomy found at knowledge/categories.json. Run "
            "`python -m rag.categorize <path-to-your-product's-help-doc>` (or use the "
            "standalone app's Categorize step) before processing any transcript."
        )
    return json.loads(CATEGORIES_PATH.read_text(encoding="utf-8"))


def flat_pages(categories: dict) -> list[dict]:
    """Flatten {tabs:[{name, pages:[...]}]} into one list of {path, label, description, tab}."""
    pages = []
    for tab in categories.get("tabs", []):
        for page in tab.get("pages", []):
            pages.append({**page, "tab": tab.get("name", "")})
    return pages


def build_categories(help_doc_path: str | Path, product_name: str | None = None) -> dict:
    """Extract + clean a help doc, ask the LLM to propose a category taxonomy, and save it."""
    path = Path(help_doc_path)
    raw_text = extract(path)
    text = clean(raw_text)

    client = config.get_client()
    settings = config.load_model_settings()
    user_content = json.dumps(
        {"product": product_name or "", "help_doc_excerpt": text[:12000]}, ensure_ascii=False
    )
    response = client.chat.completions.create(
        model=settings.chat_model,
        response_format={"type": "json_object"},
        temperature=0.2,
        messages=[
            {"role": "system", "content": _CATEGORIZE_SYSTEM_PROMPT},
            {"role": "user", "content": user_content},
        ],
    )
    categories = json.loads(response.choices[0].message.content)
    categories["generated_at"] = datetime.now(timezone.utc).isoformat()
    categories["source_help_doc"] = path.name

    CATEGORIES_PATH.parent.mkdir(parents=True, exist_ok=True)
    CATEGORIES_PATH.write_text(json.dumps(categories, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return categories


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Derive the category taxonomy from a product's help doc.")
    parser.add_argument("help_doc_path")
    parser.add_argument("--product", default=None, help="Product name (optional, improves category naming).")
    args = parser.parse_args()

    result = build_categories(args.help_doc_path, args.product)
    page_count = sum(len(t.get("pages", [])) for t in result.get("tabs", []))
    print(f"Wrote knowledge/categories.json: {len(result.get('tabs', []))} tabs, {page_count} pages.")
