# Pipeline 08：Final Packaging

## 目标

在 controller 确认结果状态允许最终输出后，生成完整闭环专利草案结果。

## 输入

- Pipeline State。
- 最终草案版本。
- 所有阶段 handoff 和 scorecard。
- Iteration Decision。
- `prompts/11_final_packaging.md`。
- `templates/closed_loop_output.md`。

## 输出

- `templates/closed_loop_output.md` 格式的完整结果。
- 阶段执行记录和迭代状态决策记录。
- 最终权利要求书、说明书、摘要。
- 术语统一表、支持映射、附图绘制建议。
- 最终评分卡、剩余风险和需用户确认事项。

## 质量门

- 只有 PASS、NEEDS_USER_FACTS、RISK_ACCEPTED 或 STOP_LIMIT 可以进入最终打包。
- REVISE 状态不得包装成最终稿。
- 不允许存在未解释的 Open Major ticket。
- Needs User Facts 和 Risk Accepted 必须进入剩余风险。
- 正式附图未提供不作为默认最终打包失败原因；最终输出必须包含可执行的建议附图方案和每张图应包含的内容。
- 主体/程序信息缺失默认不进入技术草案风险清单，除非用户明确要求正式申请字段。

## 交接要求

最终阶段 Codex 不再开启下一对话。若发现仍为 REVISE，应退回 controller，并说明应该返回的阶段和 tickets。
