# Pipeline 04：Claim Architecture

## 目标

基于技术特征矩阵设计 Claim Scope Ladder 和权利要求布局。

## 输入

- Feature Matrix handoff。
- 技术特征矩阵。
- `prompts/03_claim_architecture.md`。
- `templates/claim_scope_ladder.md`。

## 输出

- Claim Scope Ladder。
- 独立权利要求候选。
- 从属权利要求 fallback ladder。
- 主题布局建议：产品 / 方法 / 系统 / 设备 / 介质 / 程序产品 / 实用新型结构。
- `templates/phase_scorecard.md`。
- `templates/phase_handoff.md`。

## 质量门

- 独权不得塞入明显非必要细节。
- 独权不得宽到没有说明书支撑路径。
- 从权必须形成可用于审查意见答复或商业保护的 fallback。
- 不得引入用户未披露的结构、步骤、参数或实验事实。

## 交接要求

下一阶段建议通常为 Specification。若权利要求核心缺少事实依据，应返回 Feature Matrix 或进入 NEEDS_USER_FACTS。
