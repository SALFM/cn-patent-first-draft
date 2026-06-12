# Phase 8：弱点路由

## 目标

将审查发现的问题映射到 Weakness Routing Table，并生成可执行 routing tickets。

## 输入

- Review scorecard。
- 多角色审查意见。
- 当前草案版本。

## 输出

按 `templates/routing_tickets.md` 输出 routing tickets。

## 禁止事项

- 不得只列问题而不指定修改对象。
- 不得把需要用户事实确认的问题写成已修复。
- 不得把无关重构列入修复指令。
- 不得生成没有 route、没有修改对象或没有验收标准的泛泛问题。
- 不得把可接受风险伪装成已经修复。

## 质量门

- 每个 weakness 都有 Ticket ID、严重程度、Route、修改对象、修改指令、验收标准和状态。
- Route 必须对应 SKILL.md 中的 Weakness Routing Table 或明确说明为“其他”。
- Major weakness 优先处理。
- 每个 weakness 必须生成 routing ticket；不得遗漏 Medium 或 Minor weakness。
- ticket 初始状态只能是：
  - `Open`：可由 AI 基于现有材料修复，等待定向修复；
  - `Needs User Facts`：必须用户补充真实事实，AI 不能自主修复；
  - `Risk Accepted`：风险已披露且当前版本可接受。
- `Open` ticket 必须有可执行 route 和可检查验收标准。
- `Needs User Facts` ticket 必须列明缺少的真实事实。
- `Risk Accepted` ticket 必须列明风险内容和接受原因。
- 申请人、发明人、代理机构、优先权等主体/程序信息缺失默认不生成 ticket；用户明确要求正式申请字段时，才作为非技术待确认事项披露。
- 正式附图缺失默认不生成阻断型 ticket；如建议附图不完整，应生成 `Open` ticket 要求补全建议图内容、图中组成和对应关系。

## 失败时如何处理

如 weakness 无法分类，创建 `Route: Other`，说明原因，并在下一轮回归检查中确认是否需要新增路由规则。
