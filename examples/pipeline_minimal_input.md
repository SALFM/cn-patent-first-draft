# Pipeline 模式最小输入示例

请使用 cn-patent-first-draft skill 的 Pipeline Controller 模式，根据以下技术交底生成中国发明/实用新型专利草案。

要求：

- 请拆分为 Intake、Invention Mining、Feature Matrix、Claim Architecture、Specification / Drawing Plan / Initial Draft、Review / Routing、Revision / Regression Decision、Final Packaging 阶段。
- 每个阶段由独立 Codex 对话执行，并输出阶段产物、阶段评分卡和阶段交接包。
- 父级 controller 读取 handoff 和 scorecard 后，根据结果状态决定是否自动开启下一阶段新对话。
- 只有 controller 可以开启下一对话；阶段 Codex 不得自行开启。
- 只有状态为 REVISE 且 ticket 可基于现有材料修复时才进入修复阶段。
- PASS、NEEDS_USER_FACTS、RISK_ACCEPTED 或 STOP_LIMIT 时停止自我迭代或进入最终打包。
- 不要为了推进阶段编造现有技术、实验数据、产品结构、参数、已经存在的正式附图、申请人、发明人或程序信息。申请人、发明人、代理机构、优先权等主体/程序信息默认不进入技术草案；附图请输出建议图方案并说明每张图应包含什么。

技术交底：

[在此粘贴技术交底]
