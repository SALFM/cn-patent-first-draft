#!/usr/bin/env python3
"""Heuristically check claim numbering in a Markdown patent draft."""

from __future__ import annotations

import re
import sys
from pathlib import Path


CLAIM_HEADING_RE = re.compile(r"^##\s+.*权利要求书\s*$")
HEADING_RE = re.compile(r"^##\s+")
NUMBER_RE = re.compile(r"^\s*(\d+)\.\s+")


def extract_claim_section(lines: list[str]) -> list[tuple[int, str]]:
    start = None
    for index, line in enumerate(lines):
        if CLAIM_HEADING_RE.match(line.strip()):
            start = index + 1
            break

    if start is None:
        return list(enumerate(lines, start=1))

    result: list[tuple[int, str]] = []
    for index in range(start, len(lines)):
        line = lines[index]
        if HEADING_RE.match(line.strip()):
            break
        result.append((index + 1, line))
    return result


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python scripts/check_claim_numbering.py <markdown-file>")
        return 2

    path = Path(argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        return 2

    lines = path.read_text(encoding="utf-8").splitlines()
    section = extract_claim_section(lines)
    numbers: list[tuple[int, int]] = []

    for line_no, line in section:
        match = NUMBER_RE.match(line)
        if match:
            numbers.append((line_no, int(match.group(1))))

    if not numbers:
        print("Warning: no claim numbers like '1.' were found.")
        return 0

    errors: list[str] = []
    seen: set[int] = set()
    for line_no, number in numbers:
        if number in seen:
            errors.append(f"duplicate claim number {number} at line {line_no}")
        seen.add(number)

    expected = list(range(1, len(numbers) + 1))
    actual = [number for _, number in numbers]
    if actual != expected:
        errors.append(f"claim numbers are not consecutive: expected {expected}, found {actual}")

    if errors:
        print("Claim numbering check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Claim numbering check passed: {actual}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
