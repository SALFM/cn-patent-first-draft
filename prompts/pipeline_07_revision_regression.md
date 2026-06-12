# Pipeline 07：Revision & Regression Decision

## 目标

基于 Open 且 AI 可修复的 routing tickets 进行定向修复，然后回归检查并输出结果状态。

## 输入

- 当前草案版本。
- Review & Routing handoff。
- routing tickets。
- `prompts/09_targeted_revision.md`。
- `prompts/10_regression_check.md`。
- `templates/regression_check.md`。
- `templates/iteration_decision.md`。

## 输出

- 修订后的草案版本。
- 每个 ticket 的处理结果和回归后状态。
- 新增问题列表。
- Iteration Decision：PASS / REVISE / NEEDS_USER_FACTS / RISK_ACCEPTED / STOP_LIMIT。
- `templates/phase_scorecard.md`。
- `templates/phase_handoff.md`。

## 质量门

- 只修复 Open 且可基于现有材料修复的 ticket。
- 不得修复 Needs User Facts ticket，除非用户已经补充事实。
- 回归检查必须确认权利要求、说明书、摘要、术语和附图建议同步。
- 附图建议同步重点检查建议图是否覆盖关键特征、是否写清图中应包含内容；不得把建议图写成正式附图。
- 主体/程序信息默认不是修复对象。
- 若修复引入新问题，必须生成新 ticket 或说明不生成原因。

## 交接要求

若结果状态为 REVISE，controller 决定是否开启下一轮 Review / Revision 对话。若结果状态为 PASS、NEEDS_USER_FACTS、RISK_ACCEPTED 或 STOP_LIMIT，controller 决定是否进入 Final Packaging 或停止。
