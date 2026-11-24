#!/usr/bin/env python3
"""Worst App Idea Ever Pitched: PuddleWatch.

Writes one sentence pitching the worst, most useless app imaginable
to /output/entry.txt (or ./output/entry.txt when /output is not
writable). Deterministic: the entry text is a fixed constant.
"""

import os
import sys

ENTRY = (
    "PuddleWatch is the AI app that photographs every puddle you step "
    "around, rates its splash potential, and emails your friends a "
    "weekly report so they know exactly which puddles you heroically "
    "avoided, for only five dollars a month."
)


def main() -> int:
    if not (1 <= len(ENTRY) <= 240):
        print(f"entry is {len(ENTRY)} chars, must be 1-240", file=sys.stderr)
        return 1
    if ENTRY != ENTRY.strip() or "  " in ENTRY:
        print("entry has stray whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
    except OSError:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
