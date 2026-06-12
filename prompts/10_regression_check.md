# Phase 10：回归检查

## 目标

检查定向修复是否关闭原问题，是否引入新问题，并确认权利要求、说明书、摘要、术语和附图建议仍然一致。

## 输入

- 修订后的草案。
- routing tickets。
- 上轮 review scorecard。

## 输出

按 `templates/regression_check.md` 输出回归检查结果。
回归检查后必须输出或更新 `templates/iteration_decision.md` 所需的状态决策输入。

## 禁止事项

- 不得仅凭“已修改”判定问题关闭。
- 不得忽略新增问题。
- 不得跳过禁止编造检查。
- 不得只凭评分决定继续或停止。

## 质量门

- 检查已关闭问题、未关闭问题、新引入问题。
- 检查权利要求支持、说明书支持、摘要同步、术语同步、附图建议同步、格式和禁止编造。
- 附图建议同步的判断重点是关键技术特征是否被建议图覆盖、每张图应包含内容是否清楚；正式附图未提供不单独导致质量门失败。
- 回归检查后必须更新每个 ticket 状态：`Fixed`、`Open`、`Deferred`、`Needs User Facts` 或 `Risk Accepted`。
- `Fixed` 只能用于已经修复并通过回归检查的 ticket。
- 若修复失败或引入新问题，保持或改回 `Open`，并说明原因。
- 若问题必须依赖用户真实事实，标为 `Needs User Facts`。
- 主体/程序信息缺失默认不标为 `Needs User Facts`，除非用户明确要求正式申请字段。
- 若风险已披露且不阻断当前版本，标为 `Risk Accepted` 或 `Deferred`。
- 判断修复是否引入新问题，并为新问题生成 routing ticket 或说明不生成原因。
- 最后进行 Iteration Decision，输出 PASS、REVISE、NEEDS_USER_FACTS、RISK_ACCEPTED 或 STOP_LIMIT。

## 失败时如何处理

如存在可基于现有材料修复的 Open Major 或 Medium ticket，结果状态应为 REVISE。若只剩需要用户事实、可接受风险或已达到最大安全轮次，应输出对应终止状态，并列入最终剩余风险。
