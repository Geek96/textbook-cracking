#!/usr/bin/env python3
"""Structural validator for a Textbook Cracking wiki. Standard library only."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


# "proof" (math), "case-study"/"week" (CS), "document-entry" (primary-source
# reader) are each one content model's own detail-page type; add a new one
# here when a new content model under references/content-models/ needs it.
# "practice-problems" (math, optional/on-request — see content-models/math.md)
# is Agent-original problems, distinct from "proof" (textbook-faithful).
# "mcq-practice"/"mcq-answers"/"coding-practice" (CS, optional/on-request —
# see content-models/cs.md "Week practice") are the CS-model equivalent:
# per-week MCQs with a separated answer key, plus link-only curated
# external coding problems — never the professor's or a judge site's own
# problem text.
ALLOWED_TYPES = {"moc", "chapter-summary", "concept", "proof", "practice-problems", "case-study", "document-entry", "week", "mcq-practice", "mcq-answers", "coding-practice", "image-gallery"}
ALLOWED_CALLOUTS = {
    "abstract", "summary", "tldr", "info", "note", "tip", "hint",
    "important", "warning", "caution", "attention",
}
MANAGED_START = re.compile(r'<!-- agent-managed:start id="([^"]+)" -->')
MANAGED_END = "<!-- agent-managed:end -->"
WIKILINK = re.compile(r"!?(?:\[\[)([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
CALLOUT = re.compile(r"^> \[!([A-Za-z0-9_-]+)\][+-]?", re.MULTILINE)


def parse_frontmatter(text: str) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, ["frontmatter must start on line 1"]
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, ["frontmatter closing delimiter is missing"]
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line or line[0].isspace() or line.lstrip().startswith("-"):
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            if key in fields:
                errors.append(f"duplicate frontmatter field: {key}")
            fields[key] = value.strip().strip('"')
    return fields, errors


# Real, non-.md link targets this validator needs to resolve directly
# (PDF source links, image assets). Deliberately NOT using pathlib's
# generic `Path.suffix` to decide "this target already has an extension" —
# several content models mandate filenames with an embedded numbered-dot
# prefix (math: "Theorem 4.3 - ... - 证明.md"; primary-source reader:
# "96. Petition of ... (1865).md"), and pathlib's naive last-dot sniffing
# misreads the number as a bogus extension, silently skipping the ".md"
# append this branch exists to do. Checking for a known extension by
# strings avoids that class of false failure across every content model
# without each one needing its own workaround.
KNOWN_LINK_EXTENSIONS = (".md", ".pdf", ".png", ".jpg", ".jpeg", ".gif", ".svg")


def resolve_link(wiki_root: Path, source: Path, target: str) -> bool:
    target = target.strip()
    if not target or target.startswith(("http://", "https://")):
        return True
    raw = Path(target)
    has_known_extension = raw.name.lower().endswith(KNOWN_LINK_EXTENSIONS)
    candidates = []
    if has_known_extension:
        candidates.extend([wiki_root / raw, source.parent / raw])
        # Non-.md asset links (PDFs, images) are frequently written relative
        # to the course root rather than wiki_root — e.g. "raw/files/.../HW
        # 1.pdf" or "wiki/assets/annotated-pdfs/....pdf", an established
        # convention for forward links out of textbook_breakdown/ into the
        # course's raw/ snapshot or wiki/assets/. wiki_root is always
        # "<course>/wiki/textbook_breakdown", so the course root is two
        # levels up; check it too.
        course_root = wiki_root.parent.parent
        candidates.append(course_root / raw)
        basename = raw.name
    else:
        candidates.extend([wiki_root / f"{target}.md", source.parent / f"{target}.md"])
        basename = f"{raw.name}.md"
    if basename.lower().endswith(".md"):
        candidates.extend(wiki_root.rglob(basename))
    elif has_known_extension and raw == Path(raw.name):
        # Bare-filename asset embed/link (no folder component), e.g.
        # "![[photo.jpg]]" — mirrors Obsidian's own resolution, which finds
        # a matching file anywhere in the vault by basename rather than
        # requiring a path. Search the whole course tree, not just
        # wiki_root, since images commonly live under wiki/assets/.
        candidates.extend(wiki_root.parent.parent.rglob(basename))
    return any(path.exists() for path in candidates)


def validate_file(path: Path, wiki_root: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    problems: list[str] = []
    fields, fm_errors = parse_frontmatter(text)
    problems.extend(fm_errors)

    page_type = fields.get("type")
    if page_type not in ALLOWED_TYPES:
        problems.append(f"unsupported or missing type: {page_type!r}")

    h1_count = len(re.findall(r"^# ", text, re.MULTILINE))
    if h1_count != 1:
        problems.append(f"expected exactly one H1, found {h1_count}")

    starts = MANAGED_START.findall(text)
    ends = text.count(MANAGED_END)
    if not starts or len(starts) != ends:
        problems.append(f"managed marker mismatch: {len(starts)} starts, {ends} ends")
    if len(starts) != len(set(starts)):
        problems.append("duplicate agent-managed id in one file")

    if text.count("$$") % 2:
        problems.append("unbalanced block-math delimiter $$")

    for callout in CALLOUT.findall(text):
        if callout.lower() not in ALLOWED_CALLOUTS:
            problems.append(f"non-standard callout type: {callout}")

    # A wikilink's alias pipe must be escaped as `\|` when the link sits
    # inside a Markdown table cell (otherwise the table parser splits the
    # cell early) — that escape is a table-syntax requirement, not part of
    # the wikilink itself, so unescape it before extracting link targets.
    # Left un-unescaped, the stray backslash lands inside the captured
    # target string and breaks every resolution below it.
    text_for_links = text.replace("\\|", "|")
    for target in WIKILINK.findall(text_for_links):
        if target.startswith("raw/"):
            continue
        if not resolve_link(wiki_root, path, target):
            problems.append(f"unresolved wikilink: [[{target}]]")

    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("wiki_root", type=Path)
    args = parser.parse_args()
    root = args.wiki_root.resolve()
    if not root.is_dir():
        print(f"ERROR: not a directory: {root}", file=sys.stderr)
        return 2

    files = sorted(root.rglob("*.md"))
    failures = 0
    for path in files:
        problems = validate_file(path, root)
        if problems:
            failures += 1
            print(f"FAIL {path.relative_to(root)}")
            for problem in problems:
                print(f"  - {problem}")
        else:
            print(f"OK   {path.relative_to(root)}")

    print(f"\nChecked {len(files)} Markdown files; {failures} failed.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
