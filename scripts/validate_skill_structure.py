#!/usr/bin/env python3
"""Validate the closed-loop skill repository structure."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "SKILL.md",
    "README.md",
    "templates/closed_loop_output.md",
    "templates/drawing_recommendation.md",
    "templates/review_scorecard.md",
    "templates/routing_tickets.md",
    "templates/regression_check.md",
    "templates/iteration_decision.md",
    "templates/pipeline_state.md",
    "templates/phase_scorecard.md",
    "templates/phase_handoff.md",
    "schemas/iteration_decision.schema.json",
    "schemas/pipeline_state.schema.json",
    "schemas/phase_scorecard.schema.json",
    "schemas/phase_handoff.schema.json",
    "prompts/pipeline_00_controller.md",
    "prompts/pipeline_01_intake.md",
    "prompts/pipeline_02_invention_mining.md",
    "prompts/pipeline_03_feature_matrix.md",
    "prompts/pipeline_04_claim_architecture.md",
    "prompts/pipeline_05_specification_drawing_draft.md",
    "prompts/pipeline_06_review_routing.md",
    "prompts/pipeline_07_revision_regression.md",
    "prompts/pipeline_08_final_packaging.md",
    "scripts/check_pipeline_handoff.py",
    "schemas",
    "prompts",
]

REQUIRED_KEYWORDS = [
    "闭环",
    "弱点路由",
    "回归检查",
    "多角色专利审查模拟",
    "附图绘制建议",
    "结果状态",
    "PASS",
    "REVISE",
    "NEEDS_USER_FACTS",
    "RISK_ACCEPTED",
    "STOP_LIMIT",
    "最大轮数只是安全上限",
    "迭代次数不是目标",
    "Pipeline Controller",
    "多 Codex",
    "阶段交接包",
    "自动开启新对话",
]


def main() -> int:
    errors: list[str] = []

    for relative in REQUIRED_PATHS:
        path = ROOT / relative
        if not path.exists():
            errors.append(f"missing required path: {relative}")

    skill_path = ROOT / "SKILL.md"
    if skill_path.exists():
        text = skill_path.read_text(encoding="utf-8")
        for keyword in REQUIRED_KEYWORDS:
            if keyword not in text:
                errors.append(f"SKILL.md missing keyword: {keyword}")

    prompts_dir = ROOT / "prompts"
    if prompts_dir.exists():
        prompt_count = len(list(prompts_dir.glob("*.md")))
        if prompt_count < 12:
            errors.append(f"prompts/ should contain at least 12 markdown files, found {prompt_count}")

    schemas_dir = ROOT / "schemas"
    if schemas_dir.exists():
        schema_count = len(list(schemas_dir.glob("*.schema.json")))
        if schema_count < 8:
            errors.append(f"schemas/ should contain at least 8 schema files, found {schema_count}")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed: closed-loop skill structure is complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
