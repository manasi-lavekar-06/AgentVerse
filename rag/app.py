"""app.py — standalone local web app for the FLOWCAL Knowledge Hub pipeline.

The single entry point for someone who downloaded this as a packaged app (no VS Code,
no Copilot): configure an API key, categorize their product's help doc once, then
upload transcripts and browse the generated site — all from a browser tab against a
local server. Run directly with `python -m rag.app` (opens a browser automatically),
or packaged into an exe (see packaging/README.md).
"""

from __future__ import annotations

import shutil
import threading
import webbrowser
from pathlib import Path

from flask import Flask, redirect, request, send_from_directory, url_for
from werkzeug.utils import secure_filename

from rag import user_settings
from rag.categorize import CATEGORIES_PATH, build_categories, has_categories, require_categories

_REPO_ROOT = Path(__file__).resolve().parent.parent
PENDING_DIR = _REPO_ROOT / "transcripts" / "pending"
SITE_DIR = _REPO_ROOT / "site"
UPLOADS_DIR = _REPO_ROOT / "rag" / ".uploads"

app = Flask(__name__)


def _layout(title: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{title} · Knowledge Hub</title>
<style>
  body {{ font-family: -apple-system, Segoe UI, Arial, sans-serif; max-width: 760px;
          margin: 2.5rem auto; padding: 0 1.25rem; color: #1a2233; background: #f5f6f9; }}
  nav a {{ margin-right: 1rem; color: #1a2742; font-weight: 600; text-decoration: none; }}
  nav {{ margin-bottom: 1.75rem; padding-bottom: 1rem; border-bottom: 2px solid #dde2ed; }}
  h1 {{ color: #1a2742; }}
  .card {{ background: #fff; border: 1px solid #dde2ed; border-radius: 10px; padding: 1.25rem 1.5rem; margin-bottom: 1rem; }}
  .ok {{ color: #059669; font-weight: 700; }}
  .missing {{ color: #dc2626; font-weight: 700; }}
  label {{ display: block; margin-top: 0.75rem; font-weight: 600; font-size: 0.9rem; }}
  input[type=text], input[type=password], select {{ width: 100%; padding: 0.5rem; margin-top: 0.25rem;
          border: 1px solid #dde2ed; border-radius: 6px; box-sizing: border-box; }}
  button {{ margin-top: 1.25rem; background: #E65100; color: #fff; border: none; padding: 0.6rem 1.2rem;
          border-radius: 6px; font-weight: 700; cursor: pointer; }}
  pre {{ background: #0f1928; color: #e3e7f0; padding: 1rem; border-radius: 8px; overflow-x: auto; }}
</style></head>
<body>
<nav>
  <a href="/">Dashboard</a>
  <a href="/settings">Settings</a>
  <a href="/categorize">Categorize</a>
  <a href="/run">Run Pipeline</a>
  <a href="/hub/">Open Knowledge Hub</a>
</nav>
<h1>{title}</h1>
{body}
</body></html>"""


@app.route("/")
def dashboard():
    configured = user_settings.is_configured()
    categorized = has_categories()
    body = f"""
<div class="card">
  <p>API keys configured: <span class="{'ok' if configured else 'missing'}">{"Yes" if configured else "No — go to Settings"}</span></p>
  <p>Product categorized: <span class="{'ok' if categorized else 'missing'}">{"Yes" if categorized else "No — go to Categorize"}</span></p>
</div>
<div class="card">
  <p>Setup order: <b>1) Settings</b> (API key) &rarr; <b>2) Categorize</b> (your product's help doc, once) &rarr;
  <b>3) Run Pipeline</b> (upload transcripts, repeatable) &rarr; <b>4) Open Knowledge Hub</b> (browse the result).</p>
</div>"""
    return _layout("Dashboard", body)


@app.route("/settings", methods=["GET", "POST"])
def settings():
    if request.method == "POST":
        provider = request.form.get("provider", "openai")
        values = {
            "OPENAI_API_KEY": request.form.get("openai_api_key", "").strip(),
            "AZURE_OPENAI_ENDPOINT": request.form.get("azure_endpoint", "").strip(),
            "AZURE_OPENAI_API_KEY": request.form.get("azure_api_key", "").strip(),
            "AZURE_OPENAI_API_VERSION": request.form.get("azure_api_version", "2024-10-21").strip(),
            "AZURE_OPENAI_EMBEDDING_DEPLOYMENT": request.form.get("azure_embedding_deployment", "").strip(),
            "AZURE_OPENAI_CHAT_DEPLOYMENT": request.form.get("azure_chat_deployment", "").strip(),
        }
        if provider == "openai":
            values = {"OPENAI_API_KEY": values["OPENAI_API_KEY"]}
        user_settings.save_user_settings(values)
        user_settings.apply_to_environment()
        return redirect(url_for("settings", saved=1))

    saved = request.args.get("saved")
    current = user_settings.load_user_settings()
    body = f"""
{'<div class="card"><p class="ok">Settings saved.</p></div>' if saved else ''}
<div class="card">
  <p>Choose your provider and enter its details. Keys are stored only on this machine
  (~/.flowcal-hub/settings.json) — never committed to the repo.</p>
  <form method="post">
    <label>Provider</label>
    <select name="provider" onchange="document.getElementById('azure').style.display=this.value=='azure'?'block':'none'; document.getElementById('openai').style.display=this.value=='openai'?'block':'none';">
      <option value="openai">OpenAI</option>
      <option value="azure">Azure OpenAI</option>
    </select>
    <div id="openai">
      <label>OpenAI API Key</label>
      <input type="password" name="openai_api_key" value="{current.get('OPENAI_API_KEY', '')}">
    </div>
    <div id="azure" style="display:none">
      <label>Azure OpenAI Endpoint</label>
      <input type="text" name="azure_endpoint" placeholder="https://<resource>.openai.azure.com" value="{current.get('AZURE_OPENAI_ENDPOINT', '')}">
      <label>Azure OpenAI API Key</label>
      <input type="password" name="azure_api_key" value="{current.get('AZURE_OPENAI_API_KEY', '')}">
      <label>API Version</label>
      <input type="text" name="azure_api_version" value="{current.get('AZURE_OPENAI_API_VERSION', '2024-10-21')}">
      <label>Embedding Deployment Name</label>
      <input type="text" name="azure_embedding_deployment" value="{current.get('AZURE_OPENAI_EMBEDDING_DEPLOYMENT', '')}">
      <label>Chat Deployment Name</label>
      <input type="text" name="azure_chat_deployment" value="{current.get('AZURE_OPENAI_CHAT_DEPLOYMENT', '')}">
    </div>
    <button type="submit">Save</button>
  </form>
</div>"""
    return _layout("Settings", body)


@app.route("/categorize", methods=["GET", "POST"])
def categorize_view():
    if request.method == "POST":
        if not user_settings.is_configured():
            return _layout("Categorize", '<div class="card"><p class="missing">Configure an API key in Settings first.</p></div>')
        file = request.files.get("help_doc")
        if not file or not file.filename:
            return _layout("Categorize", '<div class="card"><p class="missing">Choose a file first.</p></div>')
        UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
        dest = UPLOADS_DIR / secure_filename(file.filename)
        file.save(dest)
        product = request.form.get("product", "").strip() or None
        result = build_categories(dest, product)
        page_count = sum(len(t.get("pages", [])) for t in result.get("tabs", []))
        body = f"""<div class="card"><p class="ok">Wrote knowledge/categories.json — {len(result.get('tabs', []))} tabs, {page_count} pages.</p>
        <pre>{_escape(str(result))}</pre></div>"""
        return _layout("Categorize", body)

    existing = require_categories() if has_categories() else None
    status = f'<p class="ok">Already categorized ({CATEGORIES_PATH.name}) — re-uploading replaces it.</p>' if existing else '<p class="missing">Not categorized yet. The pipeline will refuse to run until you do this.</p>'
    body = f"""
<div class="card">{status}</div>
<div class="card">
  <p>Upload your product's existing help documentation (an exported TOC, article list,
  or help-center outline — PDF/DOCX/TXT). This is a one-time step per product; it tells
  the pipeline what page categories to file new Knowledge Objects under.</p>
  <form method="post" enctype="multipart/form-data">
    <label>Product name (optional)</label>
    <input type="text" name="product" placeholder="e.g. Acme Billing">
    <label>Help doc file</label>
    <input type="file" name="help_doc" required>
    <button type="submit">Categorize</button>
  </form>
</div>"""
    return _layout("Categorize", body)


@app.route("/run", methods=["GET", "POST"])
def run_view():
    if request.method == "POST":
        if not user_settings.is_configured():
            return _layout("Run Pipeline", '<div class="card"><p class="missing">Configure an API key in Settings first.</p></div>')
        if not has_categories():
            return _layout("Run Pipeline", '<div class="card"><p class="missing">Categorize your product first.</p></div>')
        file = request.files.get("transcript")
        if not file or not file.filename:
            return _layout("Run Pipeline", '<div class="card"><p class="missing">Choose a transcript file first.</p></div>')
        PENDING_DIR.mkdir(parents=True, exist_ok=True)
        dest = PENDING_DIR / secure_filename(file.filename)
        file.save(dest)

        from rag.pipeline import run as run_pipeline

        try:
            result = run_pipeline(str(dest), publish=True)
        except Exception as exc:  # surfaced to the user, not a stack trace
            return _layout("Run Pipeline", f'<div class="card"><p class="missing">Run failed: {_escape(str(exc))}</p></div>')

        pub = result.get("publishing", {})
        body = f"""<div class="card"><p class="ok">Done — run_id {result['run_id']}</p>
        <p>Knowledge Objects touched: {_escape(str(result['extraction']['knowledge_objects']))}</p>
        <p>FAQs added: {result['enrichment']['faqs_added']}</p>
        <p>Pages created: {_escape(str(pub.get('pages_created', [])))}</p>
        <p>Pages updated: {_escape(str(pub.get('pages_updated', [])))}</p>
        <p><a href="/hub/">Open the Knowledge Hub &rarr;</a></p></div>"""
        return _layout("Run Pipeline", body)

    body = """
<div class="card">
  <p>Upload a transcript (PDF/DOCX/TXT/SRT/VTT or a video/audio file) to draft, enrich,
  and publish it into the site in one step.</p>
  <form method="post" enctype="multipart/form-data">
    <label>Transcript file</label>
    <input type="file" name="transcript" required>
    <button type="submit">Run Pipeline</button>
  </form>
</div>"""
    return _layout("Run Pipeline", body)


@app.route("/hub/")
@app.route("/hub/<path:filename>")
def hub(filename: str = "index.html"):
    if not SITE_DIR.exists() or not any(SITE_DIR.iterdir()):
        _build_site()
    return send_from_directory(SITE_DIR, filename)


def _build_site() -> None:
    import subprocess

    subprocess.run(["mkdocs", "build"], cwd=_REPO_ROOT, check=False)


def _escape(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def main() -> None:
    port = 8765
    threading.Timer(1.0, lambda: webbrowser.open(f"http://127.0.0.1:{port}/")).start()
    app.run(host="127.0.0.1", port=port, debug=False)


if __name__ == "__main__":
    main()
