#!/usr/bin/env python3
"""Lightweight warnings for pipeline handoff Markdown output."""

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

REQUIRED_PATTERNS = [
    "阶段结果状态",
    "是否允许进入下一阶段",
    "下一阶段",
    "下一阶段 Prompt",
]


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python scripts/check_pipeline_handoff.py <markdown-file>")
        return 2

    path = Path(argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        return 2

    text = path.read_text(encoding="utf-8")
    warnings: list[str] = []

    if not any(state in text for state in RESULT_STATES):
        warnings.append("missing pipeline result state")

    for pattern in REQUIRED_PATTERNS:
        if pattern not in text:
            warnings.append(f"missing required handoff field: {pattern}")

    if warnings:
        print("Pipeline handoff warnings:")
        for warning in warnings:
            print(f"- {warning}")
    else:
        print("Pipeline handoff check passed.")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
