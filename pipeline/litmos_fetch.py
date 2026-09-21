"""
litmos_fetch.py — Download course content from Litmos via the REST API.

Fetches all modules for a course and saves any downloadable files
(PDFs, attachments) into transcripts/pending/ for pipeline processing.

Requirements:
  - A Litmos API key (admin: Settings > Integrations > API > Generate API Key)
  - Your Litmos account's source name (the subdomain, e.g. "mycompany"
    from https://mycompany.litmos.com)

Credentials are read from a .env file in the project root (never hardcode them):

    # .env
    LITMOS_API_KEY=your_api_key_here
    LITMOS_SOURCE=your_company_subdomain

Usage:
    # List all available courses (find the course IDs you want)
    python pipeline/litmos_fetch.py --list-courses

    # Download all content from a specific course
    python pipeline/litmos_fetch.py --course-id <id>

    # Download from multiple courses
    python pipeline/litmos_fetch.py --course-id <id1> --course-id <id2>
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from urllib.parse import urljoin

PROJECT_ROOT = Path(__file__).parent.parent
PENDING_DIR = PROJECT_ROOT / "transcripts" / "pending"

# Litmos REST API base
_BASE_URL = "https://api.litmos.com/v1.svc/"

# Module types that contain downloadable/readable content
_CONTENT_TYPES = {"PDF", "Presentation", "Document", "Attachment", "CourseModule"}


def _load_credentials() -> tuple[str, str]:
    """Load API key and source name from .env file or environment variables."""
    env_path = PROJECT_ROOT / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, val = line.partition("=")
                os.environ.setdefault(key.strip(), val.strip())

    api_key = os.environ.get("LITMOS_API_KEY", "")
    source = os.environ.get("LITMOS_SOURCE", "")

    if not api_key or not source:
        print(
            "\nERROR: Litmos credentials not found.\n"
            "Create a .env file in the project root:\n\n"
            "    LITMOS_API_KEY=your_api_key_here\n"
            "    LITMOS_SOURCE=your_company_subdomain\n\n"
            "To get an API key: Litmos admin panel → Settings → Integrations → API\n",
            file=sys.stderr,
        )
        sys.exit(1)

    return api_key, source


def _get(path: str, api_key: str, source: str, params: dict | None = None) -> list | dict:
    """Make an authenticated GET request to the Litmos API."""
    try:
        import requests
    except ImportError:
        raise RuntimeError("Install requests: pip install requests")

    url = urljoin(_BASE_URL, path)
    query = {"apikey": api_key, "source": source, "format": "json"}
    if params:
        query.update(params)

    resp = requests.get(url, params=query, timeout=30)
    resp.raise_for_status()
    return resp.json()


def _download_file(url: str, dest: Path, api_key: str, source: str) -> bool:
    """Download a file from a URL to dest. Returns True on success."""
    try:
        import requests
    except ImportError:
        raise RuntimeError("Install requests: pip install requests")

    params = {"apikey": api_key, "source": source}
    resp = requests.get(url, params=params, timeout=60, stream=True)
    if resp.status_code != 200:
        return False

    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)
    return True


def list_courses(api_key: str, source: str) -> None:
    """Print all available courses."""
    print("\nFetching courses from Litmos...\n")
    courses = _get("courses", api_key, source)
    if not courses:
        print("No courses found.")
        return

    print(f"{'ID':<40} {'Name'}")
    print("-" * 80)
    for course in courses:
        print(f"{course.get('Id', ''):<40} {course.get('Name', '')}")
    print(f"\n{len(courses)} course(s) found.")
    print("\nUse --course-id <ID> to download content from a specific course.")


def fetch_course(course_id: str, api_key: str, source: str) -> None:
    """Download all available content files for a course."""
    print(f"\nFetching modules for course: {course_id}")
    modules = _get(f"courses/{course_id}/modules", api_key, source)

    if not modules:
        print("  No modules found for this course.")
        return

    downloaded = 0
    skipped = 0
    for module in modules:
        mod_name = module.get("Name", "unnamed")
        mod_type = module.get("Type", "")
        download_url = module.get("DownloadUrl") or module.get("Url") or ""

        if not download_url:
            print(f"  [skip] '{mod_name}' ({mod_type}) — no download URL")
            skipped += 1
            continue

        # Derive a filename
        ext = _guess_extension(mod_type, download_url)
        safe_name = _safe_filename(f"{course_id}_{mod_name}{ext}")
        dest = PENDING_DIR / safe_name

        if dest.exists():
            print(f"  [skip] '{mod_name}' — already in pending/")
            skipped += 1
            continue

        print(f"  [download] '{mod_name}' ({mod_type}) → {safe_name}")
        ok = _download_file(download_url, dest, api_key, source)
        if ok:
            downloaded += 1
            print(f"             Saved to transcripts/pending/{safe_name}")
        else:
            print(f"             WARNING: download failed for '{mod_name}'")
            skipped += 1

    print(f"\n  Downloaded: {downloaded}  |  Skipped: {skipped}")
    if downloaded:
        print("\nNext step — files are in transcripts/pending/; invoke the Orchestrator Agent to process them.")


def _guess_extension(mod_type: str, url: str) -> str:
    """Guess a file extension from the module type or URL."""
    type_map = {
        "PDF": ".pdf",
        "Presentation": ".pdf",
        "Document": ".docx",
        "Attachment": "",
    }
    if mod_type in type_map:
        return type_map[mod_type]
    # Try to get extension from URL
    url_path = url.split("?")[0]
    suffix = Path(url_path).suffix
    return suffix if suffix else ".pdf"


def _safe_filename(name: str) -> str:
    """Strip characters unsafe for filenames."""
    import re
    name = re.sub(r'[\\/:*?"<>|]', "_", name)
    return name[:120]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fetch course content from Litmos and save to transcripts/pending/."
    )
    parser.add_argument(
        "--list-courses",
        action="store_true",
        help="List all available courses with their IDs.",
    )
    parser.add_argument(
        "--course-id",
        action="append",
        metavar="ID",
        dest="course_ids",
        help="Course ID to download. Repeat for multiple courses.",
    )
    args = parser.parse_args()

    if not args.list_courses and not args.course_ids:
        parser.print_help()
        sys.exit(0)

    api_key, source = _load_credentials()
    PENDING_DIR.mkdir(parents=True, exist_ok=True)

    if args.list_courses:
        list_courses(api_key, source)

    if args.course_ids:
        for course_id in args.course_ids:
            fetch_course(course_id, api_key, source)


if __name__ == "__main__":
    main()
