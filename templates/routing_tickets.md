# Weakness Routing Tickets / 弱点路由工单

| Ticket ID | Weakness | 严重程度 | Route | 修改对象 | 修改指令 | 验收标准 | 状态 |
|---|---|---|---|---|---|---|---|
| WR-001 | [待补充] | Major / Medium / Minor | [待补充] | 权利要求 / 说明书 / 摘要 / 术语表 / 附图建议 / 支持映射 / 格式 / 其他 | [待补充] | [待补充] | Open / Fixed / Deferred / Needs User Facts / Risk Accepted |

## 使用规则

- 每个审查发现的问题都必须生成或关联一个 ticket。
- ticket 的状态只能是 `Open`、`Fixed`、`Deferred`、`Needs User Facts`、`Risk Accepted` 之一。
- `Open` 表示尚未处理或修复失败。
- `Fixed` 表示已修复，并通过回归检查。
- `Deferred` 表示暂缓处理，但不阻断当前草案输出。
- `Needs User Facts` 表示需要用户补充真实事实，AI 不能继续自主修复。
- `Risk Accepted` 表示风险已披露，当前版本接受该风险。
- ticket 的验收标准应可检查，例如“权利要求 1 删除非必要细节，说明书 [0008] 支撑新增从权特征”。
- 不得生成没有 route、没有修改对象或没有验收标准的泛泛问题。
- 最终输出前不允许存在 Open 状态的 Major ticket；Major ticket 只能是 Fixed、Needs User Facts 或 Risk Accepted。
- Needs User Facts 必须进入“剩余风险与需用户确认事项”；Risk Accepted 必须说明风险内容和接受原因。
