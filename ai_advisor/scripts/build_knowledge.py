"""Run manually: python scripts/build_knowledge.py (from the ai_advisor/ directory)

Regenerates knowledge/*.md from repo-root source docs. Requires python-docx
(see requirements-dev.txt) - NOT a runtime dependency of the deployed app.

Re-run whenever the source docx files or analytics_consulting_framework_v3.md
change, then hand-review knowledge/background.md before committing - docx
paragraph extraction can mangle line breaks and loses table formatting.
"""

from pathlib import Path

from docx import Document

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parents[1] / "knowledge"

DOCX_SOURCES = [
    ("Personal Mission.docx", "## Personal Mission"),
    ("Personal Vision.docx", "## Personal Vision"),
    ("Decision_Capability_Philosophy.docx", "## Decision Capability & Philosophy"),
    ("Framework Origins Pitch.docx", "## Framework Origins"),
]


def extract_docx_text(path: Path) -> str:
    doc = Document(str(path))
    return "\n\n".join(p.text for p in doc.paragraphs if p.text.strip())


def build_background_md() -> None:
    sections = ["# Marcin Duda - Background, Philosophy & Mission"]
    for filename, heading in DOCX_SOURCES:
        src = ROOT / filename
        if not src.exists():
            print(f"WARNING: missing {src}, skipping")
            continue
        sections.append(f"{heading}\n\n{extract_docx_text(src)}")
    (OUT / "background.md").write_text("\n\n---\n\n".join(sections), encoding="utf-8")


def build_framework_md() -> None:
    src = ROOT / "analytics_consulting_framework_v3.md"
    (OUT / "framework.md").write_text(src.read_text(encoding="utf-8"), encoding="utf-8")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    build_background_md()
    build_framework_md()
    print("Knowledge base rebuilt in", OUT)
