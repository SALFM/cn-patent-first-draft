#!/usr/bin/env python3
"""Warn about expressions that may indicate fabricated facts in a patent draft."""

from __future__ import annotations

import re
import sys
from pathlib import Path


PATTERNS = [
    ("possible fabricated prior-art search result", re.compile(r"经检索发现\s*CN[A-Z0-9.\-]+", re.IGNORECASE)),
    ("possible fabricated experiment percentage", re.compile(r"实验结果表明[^。\n]{0,40}提高了\s*\d+(?:\.\d+)?\s*%")),
    ("possible unconfirmed drawing reference", re.compile(r"如图\s*\d+\s*所示")),
]


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python scripts/check_banned_fabrication_markers.py <text-file>")
        return 2

    path = Path(argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        return 2

    warnings: list[str] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        for label, pattern in PATTERNS:
            if pattern.search(line):
                warnings.append(f"line {line_no}: {label}: {line.strip()}")

    if warnings:
        print("Warnings only: please manually verify whether these facts were provided by the user.")
        for warning in warnings:
            print(f"- {warning}")
    else:
        print("No banned fabrication markers found.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
