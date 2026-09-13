#!/usr/bin/env python3
"""Flag invented-metric language in markdown/text. Local only. Exit 1 if hits."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PATTERNS = [
    (r"\btrusted by\s+\d", "trusted-by count"),
    (r"\b\d[\d,]*\+?\s+(users|customers|downloads|subscribers|founders)\b", "user/download count"),
    (r"\b(made|earned|revenue of|mrr)\s+\$?\d", "revenue claim"),
    (r"\b\d+(\.\d+)?%\s+(conversion|open rate|ctr|close rate)\b", "rate claim"),
    (r"\bonly\s+\d+\s+left\b", "fake scarcity"),
    (r"\b\d+(\.\d+)?\s*/\s*5\s+(stars|rating)\b", "star rating"),
]

SKIP_DIR = {".git", "node_modules", ".cursor"}
OK_IF_BLIND_NEAR = re.compile(r"\bBLIND\b", re.I)


def scan(text: str, path: Path) -> list[str]:
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        if OK_IF_BLIND_NEAR.search(line):
            continue
        for pat, label in PATTERNS:
            if re.search(pat, line, re.I):
                hits.append(f"{path}:{i}: {label}: {line.strip()[:120]}")
    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description="Lint invented metrics. Write BLIND or omit.")
    ap.add_argument("paths", nargs="*", default=["."], help="files or dirs (default: .)")
    args = ap.parse_args()
    hits: list[str] = []
    for raw in args.paths:
        p = Path(raw)
        files = [p] if p.is_file() else [
            f for f in p.rglob("*")
            if f.is_file()
            and f.suffix.lower() in {".md", ".txt", ".html"}
            and SKIP_DIR.isdisjoint(f.parts)
        ]
        for f in files:
            hits.extend(scan(f.read_text(encoding="utf-8", errors="ignore"), f))
    if not hits:
        print("blind-lint: clean")
        return 0
    print("blind-lint: hits (write BLIND or drop the number)")
    print("\n".join(hits))
    return 1


if __name__ == "__main__":
    sys.exit(main())
