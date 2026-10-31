#!/usr/bin/env python3
"""Builds the skill packages into dist/.

    python3 tools/build.py

- dist/prd-consultive.zip: the full folder (claude.ai, ChatGPT, Gemini and coding agents).
- dist/SKILL.md: everything in one file, for apps that only accept a single SKILL.md.
  Carries the text of the references, the profile and the HTML skeleton; photos come from the published link.
"""

import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "plugins" / "prd-consultive" / "skills" / "prd-consultive"
DIST = ROOT / "dist"
APPENDICES = [
    "profile.md",
    "references/process.md",
    "references/board.md",
    "references/interview.md",
    "references/stack.md",
    "references/prd-template.md",
    "references/plan-template.md",
    "references/html.md",
    "assets/skeleton.html",
]
NOTICE = (
    "\n> **Single-file version.** The files this document mentions (`profile.md`, `references/...`, "
    "`assets/skeleton.html`) are appended at the end, each under the heading `Appendix: <path>`. "
    "Read the appendix whenever the text says to read the file. The photo script isn't included in this version: "
    "use the photos from the published link (see the `references/html.md` appendix).\n"
)


def full_zip():
    target = DIST / "prd-consultive.zip"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
        for file in sorted(SKILL.rglob("*")):
            if file.is_file() and file.name != ".DS_Store" and "__pycache__" not in file.parts:
                z.write(file, Path("prd-consultive") / file.relative_to(SKILL))
    return target


def single_file():
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    frontmatter_end = text.index("\n---", 4) + 4
    parts = [text[:frontmatter_end], NOTICE, text[frontmatter_end:]]
    for path in APPENDICES:
        content = (SKILL / path).read_text(encoding="utf-8").rstrip()
        parts.append(f"\n\n---\n\n# Appendix: {path}\n\n")
        if path.endswith(".html"):
            parts.append(f"````html\n{content}\n````")
        else:
            parts.append(re.sub(r"(?m)^# ", "## ", content))
    target = DIST / "SKILL.md"
    target.write_text("".join(parts) + "\n", encoding="utf-8")
    return target


if __name__ == "__main__":
    DIST.mkdir(exist_ok=True)
    for built in (full_zip(), single_file()):
        print(f"{built.relative_to(ROOT)}  {built.stat().st_size // 1024} KB")
