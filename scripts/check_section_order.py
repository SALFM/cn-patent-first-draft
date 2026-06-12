#!/usr/bin/env python3
"""Check whether a closed-loop output Markdown file contains required headings in order."""

from __future__ import annotations

import sys
from pathlib import Path


EXPECTED_HEADINGS = [
    "# 闭环专利草案生成结果",
    "## 一、本轮生成边界与风险声明",
    "## 二、输入解析与缺失信息分级",
    "## 三、发明画像",
    "## 四、技术特征矩阵",
    "## 五、权利要求布局策略",
    "## 六、附图绘制建议",
    "## 七、迭代日志",
    "## 八、迭代状态决策记录",
    "## 九、最终权利要求书",
    "## 十、最终说明书",
    "## 十一、最终摘要",
    "## 十二、术语统一表",
    "## 十三、权利要求-说明书-附图支持映射",
    "## 十四、最终审查评分卡",
    "## 十五、剩余风险与需用户确认事项",
]


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python scripts/check_section_order.py <markdown-file>")
        return 2

    path = Path(argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        return 2

    lines = [line.strip() for line in path.read_text(encoding="utf-8").splitlines()]
    position = -1
    errors: list[str] = []

    for heading in EXPECTED_HEADINGS:
        try:
            next_position = lines.index(heading, position + 1)
        except ValueError:
            errors.append(f"missing or out-of-order heading: {heading}")
            continue
        position = next_position

    if errors:
        print("Section order check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Section order check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
