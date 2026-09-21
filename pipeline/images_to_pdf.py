"""
images_to_pdf.py — Combine multiple transcript images into a single PDF.

Usage:
    python pipeline/images_to_pdf.py <image1> [<image2> ...] --output transcripts/pending/course_01.pdf

    # Or use a glob pattern (wrap in quotes on Windows):
    python pipeline/images_to_pdf.py "screenshots/*.png" --output transcripts/pending/course_01.pdf

    # Sort automatically by filename (default: alphabetical):
    python pipeline/images_to_pdf.py "slides/*.jpg" --output transcripts/pending/course_01.pdf --sort

Supported input formats: .png, .jpg, .jpeg, .tiff, .tif, .bmp, .webp

The resulting PDF is saved to --output (default: transcripts/pending/images_combined.pdf).
Pass it straight to run_pipeline.py and EasyOCR will extract the text automatically.
"""

from __future__ import annotations

import argparse
import glob
import sys
from pathlib import Path

SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".tiff", ".tif", ".bmp", ".webp"}


def images_to_pdf(image_paths: list[Path], output_path: Path) -> None:
    """Combine a list of image files into a single multi-page PDF.

    Args:
        image_paths: Ordered list of image file paths.
        output_path: Destination PDF path.
    """
    from PIL import Image

    if not image_paths:
        print("ERROR: No image files provided.", file=sys.stderr)
        sys.exit(1)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    images: list[Image.Image] = []
    for p in image_paths:
        ext = p.suffix.lower()
        if ext not in SUPPORTED_EXTENSIONS:
            print(f"  Skipping unsupported file: {p.name}", file=sys.stderr)
            continue
        img = Image.open(str(p)).convert("RGB")
        images.append(img)
        print(f"  Added: {p.name}")

    if not images:
        print("ERROR: No valid images found.", file=sys.stderr)
        sys.exit(1)

    first, rest = images[0], images[1:]
    first.save(
        str(output_path),
        format="PDF",
        save_all=True,
        append_images=rest,
        resolution=200,
    )
    print(f"\nPDF created: {output_path}")
    print(f"Pages      : {len(images)}")
    print(f"\nNext step:")
    print(f"  Drop it in transcripts/pending/ and invoke the Orchestrator Agent to process it.")


def _resolve_paths(inputs: list[str], sort: bool) -> list[Path]:
    """Expand globs, resolve to Path objects, optionally sort."""
    paths: list[Path] = []
    for item in inputs:
        expanded = glob.glob(item, recursive=True)
        if expanded:
            paths.extend(Path(p) for p in expanded)
        else:
            # Treat as literal path
            p = Path(item)
            if p.exists():
                paths.append(p)
            else:
                print(f"WARNING: Not found, skipping: {item}", file=sys.stderr)

    if sort:
        paths.sort(key=lambda p: p.name)

    return paths


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Combine transcript images into a single PDF for OCR processing."
    )
    parser.add_argument(
        "images",
        nargs="+",
        help="Image file paths or glob patterns (e.g. 'slides/*.png')",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="transcripts/pending/images_combined.pdf",
        help="Output PDF path (default: transcripts/pending/images_combined.pdf)",
    )
    parser.add_argument(
        "--sort",
        action="store_true",
        default=True,
        help="Sort images alphabetically by filename before combining (default: True)",
    )
    parser.add_argument(
        "--no-sort",
        dest="sort",
        action="store_false",
        help="Preserve the order images were passed in (disables --sort)",
    )
    args = parser.parse_args()

    print(f"\nFLOWCAL Knowledge Hub — Image to PDF Combiner")
    print(f"{'='*50}\n")

    image_paths = _resolve_paths(args.images, args.sort)
    output_path = Path(args.output)

    print(f"Output : {output_path}")
    print(f"Images : {len(image_paths)} file(s) found\n")

    images_to_pdf(image_paths, output_path)


if __name__ == "__main__":
    main()
