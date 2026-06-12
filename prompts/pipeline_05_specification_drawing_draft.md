# Pipeline 05：Specification, Drawing Plan & Initial Draft

## 目标

基于权利要求布局生成说明书支撑、附图绘制建议和 v0 草案。

## 输入

- Claim Architecture handoff。
- Claim Scope Ladder 和权利要求候选。
- `prompts/04_specification_builder.md`。
- `prompts/05_drawing_recommendation.md`。
- `prompts/06_initial_draft.md`。

## 输出

- 说明书支撑结构。
- 实施例、变形例、替代方案和参数/模块/步骤支撑说明。
- 附图绘制建议、建议图号、建议图名、图中应包含的部件/模块/步骤/关系和建议标记。
- v0 权利要求书、说明书、摘要、术语表和支持映射。
- `templates/phase_scorecard.md`。
- `templates/phase_handoff.md`。

## 质量门

- 每个权利要求核心特征必须有说明书支撑路径。
- 附图建议必须覆盖关键结构、步骤、模块或数据流，并说明每张图应包含什么。
- 无真实附图时，不得写成“如图所示”或正式附图已存在。
- 无正式附图不影响本阶段默认通过；只要建议图方案足够清楚即可进入 Review。
- 摘要不得加入说明书和权利要求没有支持的新内容。

## 交接要求

下一阶段建议通常为 Review。若说明书无法支撑权利要求，应返回 Claim Architecture 或进入 REVISE。
