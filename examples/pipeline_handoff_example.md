# Phase Handoff / 阶段交接包

## 一、交接元信息

| 项目 | 内容 |
|---|---|
| Case ID | CASE-PIPE-001 |
| 当前阶段 | Claim Architecture |
| 当前草案版本 | v0 |
| 当前 Codex Thread | [待补充] |
| 上游 Codex Thread | [待补充] |
| 生成时间 | [待补充] |

## 二、输入摘要

- 用户原始技术交底：一种可快速调宽的管线临时固定夹。
- 上游产物路径或摘要：Feature Matrix 已列出 U 形底座、导向槽、弧形夹爪、按压滑块、复位弹簧和防滑垫。
- 本阶段使用的模板 / schema / prompt：`prompts/pipeline_04_claim_architecture.md`、`templates/phase_scorecard.md`、`templates/phase_handoff.md`。
- 本阶段禁止补写的真实事实：夹爪尺寸、弹簧规格、真实测试数据、正式附图、现有技术文献。

## 三、本阶段输出产物

| 产物 | 路径或摘要 | 是否完整 | 备注 |
|---|---|---|---|
| Claim Scope Ladder | 已生成最宽、中等、窄范围 fallback | 是 | 参数缺失已标记 `[待补充]` |
| 独立权利要求候选 | 保留 U 形底座、导向槽、弧形夹爪、按压滑块斜面和复位弹簧 | 是 | 未写入安装孔细节 |
| 从属权利要求布局 | 防滑垫纹路、燕尾槽、限位盖板、安装结构 | 部分 | 材料和参数需用户确认 |

## 四、阶段评分摘要

- 阶段总分：8.2 / 10
- 阶段结果状态：PASS
- 是否允许进入下一阶段：是
- 阻断问题：无 Open Major
- 主要扣分原因：真实现有技术和关键参数缺失，需在后续风险中披露。

## 五、Open Issues / Routing Tickets

| Ticket ID | 严重程度 | 问题 | 状态 | 建议路由 | 是否阻断下一阶段 |
|---|---|---|---|---|---|
| WR-001 | Medium | 参数和材料缺失 | Needs User Facts | Specification / Remaining Risks | 否 |
| WR-002 | Minor | 替代驱动件暂未进入权利要求 | Risk Accepted | Review / Business Decision | 否 |

## 六、需用户补充事实

| 序号 | 需补充事实 | 原因 | 不补充时处理 |
|---|---|---|---|
| 1 | 弹簧规格、适配管径范围、斜面角度 | 支撑从属权利要求和实施例 | 标记 `[待补充]` 并进入剩余风险 |

## 七、下一阶段指令

- 下一阶段：Specification
- 下一阶段 Codex 是否应开启新对话：是
- 下一阶段必须读取的产物：Feature Matrix、Claim Scope Ladder、本 handoff
- 下一阶段必须处理的 tickets：WR-001
- 下一阶段不得改动的稳定产物：独权核心结构组合

## 八、下一阶段 Prompt

```text
请使用 cn-patent-first-draft skill 的 Pipeline 05：Specification, Drawing Plan & Initial Draft 阶段。读取本阶段 handoff、Feature Matrix 和 Claim Scope Ladder，生成说明书支撑、附图绘制建议和 v0 草案。不得编造参数、测试数据、正式附图或现有技术。输出阶段评分卡和新的阶段交接包。
```
