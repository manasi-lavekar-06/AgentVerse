"""
extract.py — Format-aware text extractor.

Dispatches on file extension and returns a raw text string.
Supported formats: .pdf, .docx, .txt, .srt, .vtt
Image formats (OCR): .png, .jpg, .jpeg, .tiff, .tif, .bmp, .webp

For image-based PDFs (scanned transcripts) the extractor automatically
detects pages that contain no selectable text and falls back to OCR
via EasyOCR — a pure pip package, no system binaries required.
On first use, EasyOCR downloads its English language model (~100 MB).
"""

from __future__ import annotations

from pathlib import Path

# Minimum characters on a PDF page before we consider it "has text".
# Pages with fewer characters are treated as image-only and OCR'd.
_OCR_FALLBACK_THRESHOLD = 20

# EasyOCR reader is cached here after first initialisation so the model
# is only loaded once per process (loading takes a few seconds).
_easyocr_reader = None


def extract(file_path: str | Path) -> str:
    """Extract raw text from a transcript file.

    Args:
        file_path: Absolute or relative path to the source file.

    Returns:
        Raw text content as a single string.

    Raises:
        ValueError: If the file extension is not supported.
        FileNotFoundError: If the file does not exist.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    ext = path.suffix.lower()

    if ext == ".pdf":
        return _extract_pdf(path)
    elif ext == ".docx":
        return _extract_docx(path)
    elif ext == ".txt":
        return _extract_txt(path)
    elif ext == ".srt":
        return _extract_srt(path)
    elif ext == ".vtt":
        return _extract_vtt(path)
    elif ext in (".png", ".jpg", ".jpeg", ".tiff", ".tif", ".bmp", ".webp"):
        return _extract_image(path)
    else:
        raise ValueError(
            f"Unsupported file format: '{ext}'. "
            "Supported: .pdf, .docx, .txt, .srt, .vtt, .png, .jpg, .jpeg, .tiff, .bmp, .webp"
        )


def _extract_pdf(path: Path) -> str:
    """Extract text from a PDF, falling back to OCR for image-only pages."""
    import fitz  # PyMuPDF

    doc = fitz.open(str(path))
    pages: list[str] = []
    has_image_pages = False

    for page_num, page in enumerate(doc):
        text = page.get_text().strip()
        if len(text) >= _OCR_FALLBACK_THRESHOLD:
            pages.append(text)
        else:
            # Image-only page — render and OCR
            has_image_pages = True
            ocr_text = _ocr_pdf_page(page)
            if ocr_text.strip():
                pages.append(ocr_text)

    doc.close()

    if has_image_pages:
        print(
            f"      [OCR] {path.name}: one or more pages were image-only — "
            "OCR was applied automatically."
        )

    return "\n\n".join(pages)


def _get_ocr_reader():
    """Return a cached EasyOCR reader for English (loaded once per process)."""
    global _easyocr_reader
    if _easyocr_reader is None:
        import easyocr
        print("      [OCR] Initialising EasyOCR (first run downloads ~100 MB model)...")
        _easyocr_reader = easyocr.Reader(["en"], verbose=False)
    return _easyocr_reader


def _ocr_pdf_page(page) -> str:
    """Render a PyMuPDF page to a numpy array and run EasyOCR on it."""
    import io

    import fitz
    import numpy as np
    from PIL import Image

    # Render at 300 DPI for good OCR accuracy
    mat = fitz.Matrix(300 / 72, 300 / 72)
    pix = page.get_pixmap(matrix=mat, colorspace=fitz.csRGB)
    img = Image.open(io.BytesIO(pix.tobytes("png")))
    img_array = np.array(img)

    reader = _get_ocr_reader()
    results = reader.readtext(img_array, detail=0)
    return "\n".join(results)


def _extract_image(path: Path) -> str:
    """Run EasyOCR on a standalone image file."""
    import numpy as np
    from PIL import Image

    img = Image.open(str(path)).convert("RGB")
    img_array = np.array(img)
    reader = _get_ocr_reader()
    results = reader.readtext(img_array, detail=0)
    return "\n".join(results)


def _extract_docx(path: Path) -> str:
    from docx import Document

    doc = Document(str(path))
    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    return "\n\n".join(paragraphs)


def _extract_txt(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _extract_srt(path: Path) -> str:
    import srt

    raw = path.read_text(encoding="utf-8", errors="replace")
    subtitles = list(srt.parse(raw))
    lines = [sub.content.strip() for sub in subtitles if sub.content.strip()]
    return " ".join(lines)


def _extract_vtt(path: Path) -> str:
    import webvtt

    captions = webvtt.read(str(path))
    lines = [caption.text.strip() for caption in captions if caption.text.strip()]
    return " ".join(lines)
