#!/usr/bin/env python3
"""Lightweight warnings for iteration-decision Markdown output."""

from __future__ import annotations

import sys
from pathlib import Path


RESULT_STATES = [
    "PASS",
    "REVISE",
    "NEEDS_USER_FACTS",
    "RISK_ACCEPTED",
    "STOP_LIMIT",
]


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python scripts/check_iteration_decision.py <markdown-file>")
        return 2

    path = Path(argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        return 2

    text = path.read_text(encoding="utf-8")
    warnings: list[str] = []

    if not any(state in text for state in RESULT_STATES):
        warnings.append("missing iteration result state: PASS / REVISE / NEEDS_USER_FACTS / RISK_ACCEPTED / STOP_LIMIT")

    if "是否继续迭代" not in text:
        warnings.append("missing decision field: 是否继续迭代")

    if "停止原因" not in text and "继续原因" not in text:
        warnings.append("missing decision reason: 停止原因 or 继续原因")

    if warnings:
        print("Iteration decision warnings:")
        for warning in warnings:
            print(f"- {warning}")
    else:
        print("Iteration decision check passed.")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
