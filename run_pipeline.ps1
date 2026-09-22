<#
.SYNOPSIS
    One-shot runner for the AgentVerse transcript -> knowledge hub pipeline.

.DESCRIPTION
    Runs every step from the README in order:
      1. Create .venv (if missing) and install requirements.txt (only if not already satisfied)
      2. Transcribe every video/audio file found in -VideoFolder into transcripts/pending/
      3. Pause so you can invoke the Orchestrator Agent in Copilot Chat to process the
         pending transcripts (this step is LLM-driven and cannot be scripted from the shell)
      4. Build (or serve) the mkdocs site so the changes are reflected

.PARAMETER VideoFolder
    Folder containing the downloaded videos to transcribe.

.PARAMETER Model
    Whisper model size: tiny/base/small/medium/large (default: base).

.PARAMETER Serve
    Run 'mkdocs serve' (live-reload dev server) instead of 'mkdocs build'.

.EXAMPLE
    .\run_pipeline.ps1 -VideoFolder "C:\Videos\Batch1" -Model small -Serve
#>

param(
    [Parameter(Mandatory = $true)]
    [string]$VideoFolder,

    [ValidateSet("tiny", "base", "small", "medium", "large")]
    [string]$Model = "base",

    [switch]$Serve
)

$ErrorActionPreference = "Stop"
$RepoRoot = $PSScriptRoot
Set-Location $RepoRoot

function Write-Step($msg) {
    Write-Host "`n==> $msg" -ForegroundColor Cyan
}

# ---------------------------------------------------------------------------
# 1. Virtual environment + dependencies (skipped if already set up)
# ---------------------------------------------------------------------------
$venvPython = Join-Path $RepoRoot ".venv\Scripts\python.exe"
$venvPip = Join-Path $RepoRoot ".venv\Scripts\pip.exe"

if (-not (Test-Path $venvPython)) {
    Write-Step "Creating virtual environment (.venv)"
    python -m venv .venv
}
else {
    Write-Step "Virtual environment already exists - skipping creation"
}

Write-Step "Checking Python dependencies"
$depsOk = $true
& $venvPython -c "import whisper, mkdocs, fitz, docx, srt, webvtt, easyocr, PIL, requests, imageio_ffmpeg, soundfile" 2>$null
if ($LASTEXITCODE -ne 0) {
    $depsOk = $false
}

if ($depsOk) {
    Write-Host "All required packages already installed - skipping install." -ForegroundColor Green
}
else {
    Write-Step "Installing dependencies from requirements.txt"
    & $venvPip install -r requirements.txt
}

# ---------------------------------------------------------------------------
# 2. Transcribe every video/audio file in the given folder
# ---------------------------------------------------------------------------
Write-Step "Scanning '$VideoFolder' for video/audio files"

if (-not (Test-Path $VideoFolder)) {
    Write-Error "Video folder not found: $VideoFolder"
    exit 1
}

$extensions = @(".mp4", ".mkv", ".avi", ".mov", ".wmv", ".webm", ".mp3", ".wav", ".m4a", ".ogg", ".flac")
$videoFiles = Get-ChildItem -Path $VideoFolder -File -Recurse |
    Where-Object { $extensions -contains $_.Extension.ToLower() }

if ($videoFiles.Count -eq 0) {
    Write-Warning "No supported video/audio files found in '$VideoFolder'. Skipping transcription."
}
else {
    Write-Host "Found $($videoFiles.Count) file(s) to transcribe:" -ForegroundColor Green
    $videoFiles | ForEach-Object { Write-Host "  - $($_.FullName)" }

    Write-Step "Transcribing with Whisper model '$Model' (this can take a while)"
    foreach ($file in $videoFiles) {
        & $venvPython pipeline/transcribe.py "$($file.FullName)" --model $Model
    }
}

# ---------------------------------------------------------------------------
# 3. Orchestrator Agent - manual step, requires Copilot Chat
# ---------------------------------------------------------------------------
Write-Step "Ready for the Orchestrator Agent"
Write-Host @"
Transcripts are saved in transcripts/pending/.

Now, in VS Code:
  1. Open GitHub Copilot Chat.
  2. Select the 'Orchestrator Agent'.
  3. Send this prompt:
       Process all pending transcripts in transcripts/pending/ end-to-end.

This step runs an LLM agent pipeline (Extraction -> Enrichment -> Visualization ->
Publishing -> Search) and cannot be automated from a shell script.
"@ -ForegroundColor Yellow

Read-Host "Press Enter here once the Orchestrator Agent has finished publishing (transcripts moved to transcripts/processed/)"

# ---------------------------------------------------------------------------
# 4. Build / serve the site so changes are reflected
# ---------------------------------------------------------------------------
$mkdocsExe = Join-Path $RepoRoot ".venv\Scripts\mkdocs.exe"

if ($Serve) {
    Write-Step "Starting mkdocs dev server (Ctrl+C to stop)"
    & $mkdocsExe serve
}
else {
    Write-Step "Building the site (mkdocs build)"
    & $mkdocsExe build
    Write-Host "`nDone. Output is in the 'site/' folder. Run with -Serve to preview live." -ForegroundColor Green
}
