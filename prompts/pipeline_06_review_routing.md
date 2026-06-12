# Pipeline 06：Review & Routing

## 目标

对当前草案进行多角色审查评分，并把每个 weakness 路由成可执行 ticket。

## 输入

- 当前草案版本。
- 上游 handoff 和 pipeline state。
- `prompts/07_multi_persona_review.md`。
- `prompts/08_weakness_routing.md`。
- `templates/review_scorecard.md`。
- `templates/routing_tickets.md`。

## 输出

- 多角色审查意见。
- 总评分和维度评分。
- Major / Medium / Minor weaknesses。
- 每个 weakness 的处理属性：AI 可修复 / 需用户事实 / 可接受风险 / 阻断型问题。
- routing tickets。
- `templates/phase_scorecard.md`。
- `templates/phase_handoff.md`。

## 质量门

- 每个 weakness 必须生成 ticket。
- ticket 必须有 route、修改对象、修改指令、验收标准和状态。
- 需要真实事实的问题必须标为 Needs User Facts。
- 可接受风险必须说明风险内容和接受原因。
- 主体/程序信息缺失默认不生成 ticket；正式附图缺失默认不作为阻断问题。若建议附图不完整，应路由为可基于现有材料修复的 Drawing Recommendation ticket。

## 交接要求

若存在可基于现有材料修复的 Open Major 或 Medium ticket，下一阶段为 Revision。若只剩用户事实或可接受风险，交给 controller 判断 NEEDS_USER_FACTS 或 RISK_ACCEPTED。
