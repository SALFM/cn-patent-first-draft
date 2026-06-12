# Pipeline 00：Controller / 多 Codex 调度器

## 目标

作为父级 controller，按阶段创建或延续 Codex 对话，读取每个阶段的 Phase Handoff、Phase Scorecard 和 Pipeline State，并根据结果状态决定下一步。

## 适用场景

仅当用户明确要求 pipeline mode、多 Codex、自动开启新对话、分阶段执行或类似表达时使用。未明确要求 Pipeline 时，默认在当前对话执行同一套结果状态驱动闭环；不得降级为非迭代普通模式或单轮初稿模式。

## Controller 职责

- 维护 `templates/pipeline_state.md`。
- 为每个阶段准备输入包、阶段 prompt、必须读取的上游产物和禁止事项。
- 如果当前环境提供 Codex thread 工具，controller 可以创建下一阶段新对话；否则在当前对话输出“下一阶段 prompt”和交接包。
- 读取阶段 Codex 的 `templates/phase_handoff.md` 和 `templates/phase_scorecard.md`。
- 根据结果状态决定是否进入下一阶段、返回修复、停止等待用户事实或进入最终打包。

## 禁止事项

- 不得让阶段 Codex 自己开启下一对话。
- 不得在 `REVISE` 状态下包装最终稿。
- 不得为了推进阶段而忽略 Open Major ticket。
- 不得把缺失真实事实写成确定事实。

## 调度规则

1. 先执行 Intake。
2. 每个阶段完成后读取 handoff 和 scorecard。
3. 若阶段结果状态为 `PASS`，进入下一阶段。
4. 若为 `REVISE`，创建修复阶段或返回上游阶段。
5. 若为 `NEEDS_USER_FACTS`，停止自动调度并列出用户必须补充的信息。
6. 若为 `RISK_ACCEPTED`，可进入下一阶段或最终打包，但必须保留风险说明。
7. 若为 `STOP_LIMIT`，停止自动调度并输出当前最佳产物、停止原因和未关闭问题。

## 标准阶段顺序

Intake -> Invention Mining -> Feature Matrix -> Claim Architecture -> Specification -> Drawing Plan -> Initial Draft -> Review -> Routing -> Revision -> Regression Decision -> Final Packaging

Review / Routing / Revision / Regression Decision 可以按结果状态循环，但只有 Regression Decision 输出 `REVISE` 时才继续修复轮次。

## 每次调度输出

- 当前 pipeline state 摘要。
- 已完成阶段和阶段得分。
- 当前结果状态。
- 下一阶段名称。
- 下一阶段新 Codex prompt。
- 若停止，停止状态、停止原因和需用户补充事项。
