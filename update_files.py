#!/usr/bin/env python3
"""
Scan content folders → files.json + assets/files.json

Discovers any top-level directory that contains .py / .txt / .md files
(so adding e.g. lectures/ or projects/ and re-running is enough).

  python update_files.py
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEXT_EXT = {".py", ".txt", ".md"}
SKIP_DIRS = {
    "assets",
    ".git",
    ".github",
    "__pycache__",
    "node_modules",
    ".venv",
    "venv",
    "dist",
    "build",
}
# Preferred order when present; any other folders follow alphabetically
PREFERRED = ["exams", "labs", "exercises", "seminars", "lectures", "projects"]
MAX_FILE_BYTES = 500_000


def list_section(folder: Path) -> list[dict]:
    if not folder.is_dir():
        return []
    groups: list[dict] = []
    subdirs = sorted(
        [p for p in folder.iterdir() if p.is_dir() and p.name not in SKIP_DIRS],
        key=lambda p: p.name,
        reverse=True,
    )
    for sub in subdirs:
        items = []
        for f in sorted(sub.rglob("*")):
            if not f.is_file():
                continue
            if f.suffix.lower() not in TEXT_EXT:
                continue
            if f.stat().st_size > MAX_FILE_BYTES:
                continue
            items.append(
                {"name": f.name, "path": f.relative_to(ROOT).as_posix()}
            )
        if items:
            groups.append({"group": sub.name, "items": items})

    loose = []
    for f in sorted(folder.glob("*")):
        if (
            f.is_file()
            and f.suffix.lower() in TEXT_EXT
            and f.stat().st_size <= MAX_FILE_BYTES
        ):
            loose.append(
                {"name": f.name, "path": f.relative_to(ROOT).as_posix()}
            )
    if loose:
        groups.insert(0, {"group": "(root)", "items": loose})
    return groups


def discover_sections() -> list[str]:
    found = []
    for p in ROOT.iterdir():
        if not p.is_dir() or p.name in SKIP_DIRS or p.name.startswith("."):
            continue
        has = any(
            f.is_file() and f.suffix.lower() in TEXT_EXT
            for f in p.rglob("*")
            if f.is_file()
        )
        if has:
            found.append(p.name)

    ordered = [s for s in PREFERRED if s in found]
    ordered += sorted(s for s in found if s not in PREFERRED)
    return ordered


def main() -> None:
    sections = discover_sections()
    data: dict[str, list] = {}
    for name in sections:
        data[name] = list_section(ROOT / name)

    text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    for out in (ROOT / "files.json", ROOT / "assets" / "files.json"):
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
        print("OK -", out)

    print(f"Sections: {', '.join(sections) or '(none)'}")
    for key in sections:
        n_groups = len(data[key])
        n_files = sum(len(g["items"]) for g in data[key])
        print(f"  {key}: {n_groups} groups, {n_files} files")


if __name__ == "__main__":
    main()
