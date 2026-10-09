#!/usr/bin/env python3
"""Data-free checks for the Phase 1 BRFSS research repository.

Validates structure, notebook JSON, links, metadata and Git file hygiene.
Never imports the notebook, downloads source data or loads/retrains saved models.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = (
    "Cardiovascular Machine Learning Research: BRFSS-Based Classification "
    "of Prevalent Self-Reported Myocardial Infarction and Coronary Heart "
    "Disease with Temporal Validation"
)
STEM = "03_brfss_2023_first_look_optimised"
NOTEBOOK = f"notebooks/{STEM}.ipynb"
REPORT = f"reports/{STEM}.html"  # Public report; local PDF is deliberately ignored.

REQUIRED = [
    ".gitignore",
    ".github/workflows/repository-checks.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
    "README.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "LICENSE",
    "requirements.txt",
    "research_log.md",
    "data/README.md",
    "docs/PROJECT_STATUS.md",
    "docs/data_dictionary.md",
    "docs/dataset_selection.md",
    "docs/research_protocol.md",
    NOTEBOOK,
    REPORT,
    "artifacts/models/brfss_2023_gradient_boosting_locked.joblib",
    "artifacts/models/brfss_2023_logistic_regression_locked.joblib",
    "artifacts/provenance/research_manifest.json",
    "artifacts/provenance/dataset_provenance.json",
    "artifacts/tables/primary_performance.csv",
    "artifacts/figures/roc_internal_vs_temporal.png",
]

errors = []
warnings = []


def error(message):
    errors.append(message)


def warning(message):
    warnings.append(message)


def read_text(path):
    return (ROOT / path).read_text(encoding="utf-8-sig")


print("BRFSS RESEARCH REPOSITORY AUDIT")
print("-" * 55)

for relative_path in REQUIRED:
    p = ROOT / relative_path
    if not p.is_file() or p.stat().st_size == 0:
        error(f"Missing or empty required file: {relative_path}")

# Keep the exact locked study title even if Markdown heading markers split it.
readme_path = ROOT / "README.md"
if readme_path.is_file():
    readme = read_text("README.md")
    no_headings = re.sub(r"(?m)^\s{0,3}#{1,6}\s+", "", readme)
    normalized = " ".join(no_headings.replace("**", "").split())
    if TITLE not in normalized:
        error("README is missing the exact official research title")
    for link in (NOTEBOOK, REPORT):
        if link not in readme:
            error(f"README must link to {link}")
    if f"reports/{STEM}.pdf" in readme:
        warning("README refers to a local-only PDF; verify it is labelled as unavailable on GitHub")
    if "03_brfss_2023_first_look_FINAL_LOCKED" in readme:
        error("README still refers to the superseded FINAL_LOCKED filename")

# Check notebook structure without running a single cell.
notebook_path = ROOT / NOTEBOOK
if notebook_path.is_file():
    try:
        notebook = json.loads(notebook_path.read_text(encoding="utf-8-sig"))
        cells = notebook["cells"]
        if notebook.get("nbformat") != 4 or not isinstance(cells, list):
            error("Notebook should have nbformat 4 and a list of cells")
        else:
            code_count = sum(c.get("cell_type") == "code" for c in cells)
            opening_markdown = " ".join(
                "".join(c.get("source", []))
                for c in cells[:5]
                if c.get("cell_type") == "markdown"
            )
            if TITLE not in " ".join(opening_markdown.split()):
                error("Notebook opening Markdown is missing the official study title")
            if code_count < 50:
                warning(f"Only {code_count} code cells found; check the selected notebook")
            print(f"Notebook JSON OK ({len(cells)} total cells; {code_count} code cells)")
    except (OSError, UnicodeError, ValueError, KeyError, TypeError) as exc:
        error(f"Cannot read notebook structure: {exc}")

# Validate machine-readable provenance JSON without changing its content.
for relative_path in (
    "artifacts/provenance/research_manifest.json",
    "artifacts/provenance/dataset_provenance.json",
):
    p = ROOT / relative_path
    if p.is_file():
        try:
            json.loads(read_text(relative_path))
        except (OSError, ValueError, TypeError) as exc:
            error(f"Invalid JSON in {relative_path}: {exc}")

if (ROOT / "artifacts/provenance/git_provenance.json").is_file():
    warning(
        "git_provenance.json exists; check whether it records the old deleted "
        "Git history. Do not mislabel historical hashes as new-repo commits."
    )

# Validate CFF metadata on CI. Local use without PyYAML remains possible.
cff_path = ROOT / "CITATION.cff"
if cff_path.is_file():
    try:
        import yaml
        cff = yaml.safe_load(read_text("CITATION.cff"))
        if not isinstance(cff, dict):
            error("CITATION.cff must contain a YAML mapping")
        else:
            if cff.get("title") != TITLE:
                error("CITATION.cff title differs from the official research title")
            version = cff.get("version")
            if version is not None and str(version) != "0.1.0":
                error("CITATION.cff version must be 0.1.0 for the planned Phase 1 release")
            if cff.get("date-released"):
                warning("CITATION.cff has a release date; confirm it matches the published tag")
            if cff.get("doi"):
                warning("CITATION.cff has a DOI; verify it was actually issued")
    except ImportError:
        warning("PyYAML not installed locally: CFF parse skipped (CI installs PyYAML)")
    except (OSError, UnicodeError, ValueError, TypeError) as exc:
        error(f"Unable to parse CITATION.cff: {exc}")

# Check both tracked AND untracked candidate files, so checks also work before first commit.
try:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT, capture_output=True, check=True
    )
    candidates = [s for s in result.stdout.decode("utf-8", errors="replace").split("\0") if s]
    for name in candidates:
        p = Path(name)
        parts = p.parts
        if p.suffix.lower() == ".xpt" or any(part in (".venv", "venv", "__pycache__", ".git") for part in parts):
            error(f"Sensitive or generated file slated for Git: {name}")
        file_path = ROOT / p
        if file_path.is_file() and file_path.stat().st_size >= 95_000_000:
            error(f"File is too large for normal Git tracking (>=95 MB): {name}")

    # Git should ignore these paths even when local raw data or PDF is absent on CI.
    for path in (
        "data/raw/brfss/2023/LLCP2023.XPT",
        "data/raw/brfss/2024/LLCP2024.XPT",
        "data/raw/brfss/2025/LLCP2025.XPT",
        f"reports/{STEM}.pdf",
        ".venv/pyvenv.cfg",
    ):
        ignored = subprocess.run(
            ["git", "check-ignore", "-q", "--", path],
            cwd=ROOT, capture_output=True
        )
        if ignored.returncode != 0:
            error(f".gitignore does not exclude expected local-only file: {path}")
    print(f"Git candidate-file audit OK ({len(candidates)} files inspected)")
except (OSError, subprocess.CalledProcessError) as exc:
    error(f"Git candidate-file audit could not run: {exc}")

for message in warnings:
    print("WARNING:", message)
for message in errors:
    print("ERROR:", message)
print(f"Result: {len(errors)} error(s), {len(warnings)} warning(s)")
sys.exit(1 if errors else 0)
