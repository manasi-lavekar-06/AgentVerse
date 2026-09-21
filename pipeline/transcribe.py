"""
transcribe.py — Transcribe a video or audio file to text using OpenAI Whisper.

Runs entirely locally — no API key, no data leaves your machine.
Whisper models are downloaded once from Hugging Face on first use.

Model sizes (tradeoff: accuracy vs. speed/download size):
  tiny   ~39 MB   fastest, lowest accuracy
  base   ~74 MB   good balance for clear speech (default)
  small  ~244 MB  better accuracy
  medium ~769 MB  high accuracy
  large  ~1.5 GB  best accuracy, slow on CPU

Usage:
    # Transcribe a single video and save the transcript to transcripts/pending/
    python pipeline/transcribe.py video.mp4

    # Transcribe with a larger model for better accuracy
    python pipeline/transcribe.py video.mp4 --model small

    # Transcribe without saving (just print to screen)
    python pipeline/transcribe.py video.mp4 --print-only

    # Transcribe all videos in a folder
    python pipeline/transcribe.py "videos/*.mp4"

Supported formats: .mp4, .mkv, .avi, .mov, .wmv, .mp3, .wav, .m4a, .webm
"""

from __future__ import annotations

import argparse
import glob
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
PENDING_DIR = PROJECT_ROOT / "transcripts" / "pending"

_VIDEO_EXTENSIONS = {".mp4", ".mkv", ".avi", ".mov", ".wmv", ".webm"}
_AUDIO_EXTENSIONS = {".mp3", ".wav", ".m4a", ".ogg", ".flac"}
_ALL_EXTENSIONS = _VIDEO_EXTENSIONS | _AUDIO_EXTENSIONS


def _ensure_ffmpeg() -> None:
    """Add the imageio-ffmpeg bundled binary to PATH so Whisper can find it."""
    import os
    try:
        import imageio_ffmpeg
        ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
        ffmpeg_dir = os.path.dirname(ffmpeg_exe)
        os.environ["PATH"] = ffmpeg_dir + os.pathsep + os.environ.get("PATH", "")
    except ImportError:
        pass  # imageio-ffmpeg not installed; fall back to system ffmpeg if present


def _load_audio_with_bundled_ffmpeg(file_path: Path) -> "np.ndarray":
    """Extract audio from a video/audio file using the imageio-ffmpeg bundled binary.

    Returns a float32 numpy array at 16 kHz mono (what Whisper expects),
    bypassing Whisper's own load_audio which requires 'ffmpeg' on PATH.
    """
    import subprocess
    import tempfile
    import numpy as np
    import soundfile as sf
    import imageio_ffmpeg

    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        subprocess.run(
            [
                ffmpeg_exe,
                "-y",            # overwrite without asking
                "-i", str(file_path),
                "-ar", "16000",  # 16 kHz — Whisper's required sample rate
                "-ac", "1",      # mono
                "-f", "wav",
                tmp_path,
            ],
            check=True,
            capture_output=True,
        )
        audio, _ = sf.read(tmp_path, dtype="float32")
    finally:
        Path(tmp_path).unlink(missing_ok=True)

    return audio


def transcribe(
    file_path: str | Path,
    model_size: str = "base",
    print_only: bool = False,
) -> str:
    """Transcribe a video/audio file and optionally save to transcripts/pending/.

    Args:
        file_path: Path to the video or audio file.
        model_size: Whisper model to use (tiny/base/small/medium/large).
        print_only: If True, print transcript to stdout instead of saving.

    Returns:
        Transcribed text string.
    """
    try:
        import whisper
    except ImportError:
        print(
            "\nERROR: openai-whisper is not installed.\n"
            "Run:  .venv\\Scripts\\pip install openai-whisper\n",
            file=sys.stderr,
        )
        sys.exit(1)

    # Ensure the bundled ffmpeg from imageio-ffmpeg is on PATH so Whisper can
    # decode video/audio without requiring a system ffmpeg install.
    _ensure_ffmpeg()

    path = Path(file_path).resolve()
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    ext = path.suffix.lower()
    if ext not in _ALL_EXTENSIONS:
        raise ValueError(
            f"Unsupported format: '{ext}'. "
            f"Supported: {', '.join(sorted(_ALL_EXTENSIONS))}"
        )

    print(f"\n[Whisper] Loading model '{model_size}' (downloads on first use)...")
    model = whisper.load_model(model_size)

    print(f"[Whisper] Extracting audio from: {path.name}")
    audio = _load_audio_with_bundled_ffmpeg(path)

    print(f"[Whisper] Transcribing...")
    result = model.transcribe(audio, fp16=False, language="en")
    text: str = result["text"].strip()

    if print_only:
        print("\n" + "-" * 60)
        print(text)
        print("-" * 60)
        return text

    # Save to transcripts/pending/ as a .txt file
    PENDING_DIR.mkdir(parents=True, exist_ok=True)
    out_name = path.stem + "_transcript.txt"
    out_path = PENDING_DIR / out_name
    out_path.write_text(text, encoding="utf-8")

    print(f"[Whisper] Saved transcript → transcripts/pending/{out_name}")
    print(f"          {len(text.split()):,} words extracted.\n")
    print("Next step — invoke the Orchestrator Agent to process the transcript.\n")

    return text


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Transcribe video/audio files to text using OpenAI Whisper (local)."
    )
    parser.add_argument(
        "files",
        nargs="+",
        help="Video/audio file paths or glob patterns (e.g. 'videos/*.mp4')",
    )
    parser.add_argument(
        "--model",
        default="base",
        choices=["tiny", "base", "small", "medium", "large"],
        help="Whisper model size (default: base). Use 'small' or 'medium' for better accuracy.",
    )
    parser.add_argument(
        "--print-only",
        action="store_true",
        help="Print transcript to stdout only; do not save to transcripts/pending/.",
    )
    args = parser.parse_args()

    # Expand globs
    paths: list[Path] = []
    for pattern in args.files:
        expanded = glob.glob(pattern, recursive=True)
        if expanded:
            paths.extend(Path(p) for p in expanded)
        else:
            p = Path(pattern)
            if p.exists():
                paths.append(p)
            else:
                print(f"WARNING: Not found, skipping: {pattern}", file=sys.stderr)

    if not paths:
        print("ERROR: No input files found.", file=sys.stderr)
        sys.exit(1)

    for path in paths:
        transcribe(path, model_size=args.model, print_only=args.print_only)


if __name__ == "__main__":
    main()
