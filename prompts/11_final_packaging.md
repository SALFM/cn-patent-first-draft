# Phase 11：最终输出

## 目标

按新版闭环格式输出最终草案、迭代日志、迭代状态决策记录、最终评分卡和剩余风险。

## 输入

- 最终修订版草案。
- 迭代日志。
- Iteration Decision。
- 最终 review scorecard。
- regression check。
- 剩余 Deferred、Needs User Facts、Risk Accepted tickets。

## 输出

按 `templates/closed_loop_output.md` 输出完整结果，包含：

- 最终权利要求书。
- 最终说明书。
- 最终摘要。
- 发明画像、技术特征矩阵、附图绘制建议。
- 评分卡、支持映射、迭代状态决策记录、剩余风险。

## 禁止事项

- 不得遗漏完整权利要求、说明书或摘要。
- 不得把低质量风险稿说成高质量终稿。
- 不得删除 `[待补充]` 或待确认事项来制造完成感。
- 不得在结果状态为 `REVISE` 时包装成最终稿。
- 不得隐藏 Needs User Facts 或 Risk Accepted ticket。

## 质量门

- 最终打包前必须读取 Iteration Decision。
- 只有结果状态为 `PASS`、`NEEDS_USER_FACTS`、`RISK_ACCEPTED` 或 `STOP_LIMIT` 时才能进入最终输出。
- 如果状态为 `REVISE`，不得包装成最终稿，应继续下一轮；如已达到最大安全轮次，应先通过 Iteration Decision 改为 `STOP_LIMIT` 并说明停止原因。
- 15 个新版标题齐全且顺序正确。
- 最终评分、结果状态和停止原因明确。
- 最终结果状态明确。
- 剩余风险分级清楚。
- 附图建议不被写成正式附图，并且每张建议图说明图中应包含的部件/模块/步骤/关系。
- 正式附图未提供不作为默认最终打包失败原因；主体/程序信息缺失默认不进入技术草案风险清单。
- 不允许存在 Open 状态的 Major ticket；Major ticket 只能是 Fixed、Needs User Facts 或 Risk Accepted。

## 失败时如何处理

如无法达到质量门，先返回 Iteration Decision 判断。如果状态为 NEEDS_USER_FACTS、RISK_ACCEPTED 或 STOP_LIMIT，输出当前可达最高质量版本，并明确剩余风险、缺失事实和下一步补充事项；如果状态仍为 REVISE，则继续修复或说明为何触发 STOP_LIMIT。
