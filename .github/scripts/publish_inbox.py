#!/usr/bin/env python3
"""Move plain markdown/text files from _inbox/ into _posts/ as Jekyll posts.

For each file in _inbox/ (except README.md):
  * Title: taken from a leading "# Heading" line (which is then removed from
    the body), otherwise derived from the filename.
  * Date: today (in $TZ), unless the filename already starts with YYYY-MM-DD-.
  * Front matter: only title + date are written; layout/author come from the
    defaults in _config.yml.
  * Files that already have front matter are moved as-is (just dated).

Prints the titles of published posts, one per line.
"""
import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INBOX = ROOT / "_inbox"
POSTS = ROOT / "_posts"
DATE_PREFIX = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.*)$")
SKIP = {"readme.md", ".gitkeep"}


def slugify(text):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "post"


def split_title(body):
    """Return (title, body_without_title) if the first non-blank line is '# ...'."""
    lines = body.splitlines()
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        m = re.match(r"^#\s+(.+?)\s*#*\s*$", line)
        if m:
            rest = "\n".join(lines[i + 1:]).lstrip("\n")
            return m.group(1), rest
        break
    return None, body


def unique_path(path):
    candidate, n = path, 2
    while candidate.exists():
        candidate = path.with_name(f"{path.stem}-{n}{path.suffix}")
        n += 1
    return candidate


def publish(src, today):
    stem = src.stem
    m = DATE_PREFIX.match(stem)
    date, name = (m.group(1), m.group(2)) if m else (today, stem)

    text = src.read_text(encoding="utf-8").lstrip("﻿")

    if text.startswith("---"):
        fm = re.search(r"^title:\s*[\"']?(.+?)[\"']?\s*$", text.split("\n---", 1)[0], re.M)
        title = fm.group(1) if fm else name
        out = text
    else:
        title, body = split_title(text)
        if not title:
            title = re.sub(r"[-_]+", " ", name).strip().title() or "Untitled"
        front = f"---\ntitle: {json.dumps(title)}\ndate: {date}\n---\n\n"
        out = front + body.rstrip() + "\n"

    dest = unique_path(POSTS / f"{date}-{slugify(name)}.md")
    dest.write_text(out, encoding="utf-8")
    src.unlink()
    return title, dest


def main():
    today = datetime.date.today().isoformat()
    published = []
    for src in sorted(INBOX.iterdir()):
        if not src.is_file() or src.name.lower() in SKIP:
            continue
        if src.suffix.lower() not in {".md", ".markdown", ".txt"}:
            print(f"skipping {src.name}: not .md/.txt", file=sys.stderr)
            continue
        title, dest = publish(src, today)
        print(f"{src.name} -> {dest.relative_to(ROOT)}", file=sys.stderr)
        published.append(title)
    print("\n".join(published))


if __name__ == "__main__":
    main()
