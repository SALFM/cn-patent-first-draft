# cn-patent-first-draft

`cn-patent-first-draft` 是一个默认闭环迭代式 Codex skill，用于根据技术交底生成中国发明或实用新型专利技术草案。

它不是单次初稿生成器。每次执行都必须先生成 `v0` 草案，再进行审查、弱点路由、定向修复、回归检查和结果状态决策。只有结果状态为 `REVISE` 时才继续修复；状态为 `PASS`、`NEEDS_USER_FACTS`、`RISK_ACCEPTED` 或 `STOP_LIMIT` 时停止自我迭代并输出当前最佳草案。

输出面向专利代理师、律师或企业法务继续加工，不构成法律意见，不承诺受理、公开、授权、维持有效或规避侵权/无效风险。

## 核心定位

本 skill 重点生成和优化：

- 发明画像；
- 技术特征矩阵；
- Claim Scope Ladder 和权利要求布局；
- 权利要求书；
- 说明书；
- 摘要；
- 术语统一表；
- 权利要求-说明书-附图支持映射；
- 建议附图方案；
- 多角色审查评分卡；
- 弱点路由 tickets；
- 回归检查和迭代状态决策；
- 剩余风险与需用户确认事项。

本 skill 默认不处理正式申请请求书字段。申请人、发明人、代理机构、优先权、分案、同日双报等主体/程序信息默认不进入技术草案，也不会因为缺失触发 `NEEDS_USER_FACTS`。

## 没有普通模式

本 skill 不提供非迭代的普通模式或单轮初稿模式。

默认执行形态是在当前对话中完成完整闭环：

```text
技术交底
→ v0 草案
→ Review
→ Weakness Routing
→ Targeted Revision
→ Regression Check
→ Iteration Decision
→ 最终输出
```

当用户明确要求 `Pipeline Controller`、多 Codex、自动开启新对话或分阶段执行时，可以使用 Pipeline Controller 阶段编排。但 Pipeline 只是把同一套闭环拆成多个阶段执行，不是普通模式。

## 结果状态驱动

迭代次数不是目标，结果状态才是主控制器。

每轮回归检查后必须输出一个结果状态：

| 状态 | 含义 | 是否继续 |
|---|---|---|
| `PASS` | 当前信息条件下主要质量门已通过 | 停止 |
| `REVISE` | 存在可基于现有材料修复的问题 | 继续 |
| `NEEDS_USER_FACTS` | 剩余问题必须依赖用户补充真实技术事实 | 停止 |
| `RISK_ACCEPTED` | 剩余风险已披露且不阻断当前草案交付 | 停止 |
| `STOP_LIMIT` | 达到安全上限或继续迭代没有实质收益 | 停止 |

最大修复轮次只是安全上限：

- 快速强度：最多 1 个修复轮次；
- 标准强度：最多 3 个修复轮次；
- 深度强度：最多 5 个修复轮次。

“最多”不是“必须”。不允许为了凑轮次而重复改写，也不允许为了通过状态判断而编造事实。

## 建议附图方案

本 skill 不要求用户先提供正式附图。

如果没有正式附图，skill 仍应输出建议附图方案，说明每张图：

- 为什么需要；
- 要表达哪些技术特征；
- 图中应包含哪些部件、模块、步骤、箭头或连接关系；
- 建议使用哪些附图标记；
- 对应哪些权利要求特征；
- 支撑说明书中的哪些段落；
- 后续绘制正式线条图时需要确认哪些技术事实。

不得把建议图写成已经存在的正式附图，不得使用“如图 1 所示”作为未确认事实。

## 禁止编造

skill 不能编造：

- 现有技术文献、专利号、论文、检索结论；
- 公开日期、公开方式或真实检索结果；
- 实验条件、实验数据、测试结果、性能指标；
- 产品结构、关键参数、材料牌号；
- 已经存在的正式附图、正式图号、正式图名或正式附图标记；
- 申请人、发明人、身份证号、统一社会信用代码、代理机构、代理师、优先权、申请号、分案、同日双报等主体/程序信息。

缺失技术事实应使用 `[待补充]` 或“建议用户确认”。主体/程序信息默认不进入技术草案；只有用户明确要求正式申请字段时，才可按用户提供的真实信息照录。

## 推荐调用

```text
请使用 cn-patent-first-draft skill，根据以下技术交底生成中国发明/实用新型专利技术草案。

请按照结果状态驱动闭环执行：先生成 v0 草案，再审查、路由、修复、回归检查和状态判断。
只有状态为 REVISE 且问题可基于现有材料修复时，才继续下一轮。
状态为 PASS、NEEDS_USER_FACTS、RISK_ACCEPTED 或 STOP_LIMIT 时，请停止自我迭代并输出当前最佳草案。

附图请输出建议图方案，并说明每张图应包含哪些部件、连接关系、步骤或模块。
不要为了凑轮次重复改写，也不要编造现有技术、实验数据、产品结构、参数、正式附图或主体/程序信息。

技术交底：
...
```

## Pipeline Controller

Pipeline Controller 适合长交底、复杂方案或希望保留阶段交接记录的任务。

标准阶段为：

```text
Intake
→ Invention Mining
→ Feature Matrix
→ Claim Architecture
→ Specification / Drawing Plan / Initial Draft
→ Review / Routing
→ Revision / Regression Decision
→ Final Packaging
```

每个阶段 Codex 必须输出：

- 阶段产物；
- `templates/phase_scorecard.md` 阶段评分卡；
- `templates/phase_handoff.md` 阶段交接包；
- 阶段结果状态；
- 下一阶段建议。

只有 controller 可以决定是否开启下一阶段新对话。阶段 Codex 不得自行开启下一对话，也不得越级完成后续阶段。

## 输出格式

默认且唯一的最终输出模板是 `templates/closed_loop_output.md`。

最终输出标题为：

```markdown
# 闭环专利草案生成结果
```

必须包含 15 个部分：

1. 本轮生成边界与风险声明
2. 输入解析与缺失信息分级
3. 发明画像
4. 技术特征矩阵
5. 权利要求布局策略
6. 附图绘制建议
7. 迭代日志
8. 迭代状态决策记录
9. 最终权利要求书
10. 最终说明书
11. 最终摘要
12. 术语统一表
13. 权利要求-说明书-附图支持映射
14. 最终审查评分卡
15. 剩余风险与需用户确认事项

`templates/patent_draft_output.md` 仅作为历史兼容参考保留，不作为执行模式，不得用于绕过闭环审查、路由、回归检查和状态决策。

## 目录结构

| 路径 | 用途 |
|---|---|
| `SKILL.md` | skill 主规则 |
| `LEGAL_BASIS.md` | 法律和规则依据摘要 |
| `references/` | 原始法规、指南和内部资料 |
| `reference_summaries/` | 原始资料摘要和规则映射 |
| `templates/` | 最终输出和中间产物模板 |
| `prompts/` | 各阶段可复用 prompt |
| `schemas/` | 关键产物 JSON Schema |
| `scripts/` | 轻量校验脚本 |
| `examples/` | 最小输入、闭环输出和 Pipeline 交接示例 |
| `docs/` | 使用说明、FAQ 和维护说明 |

## 校验

推荐在修改后运行：

```bash
python scripts/validate_skill_structure.py
python scripts/check_section_order.py examples/closed_loop_example_output.md
python scripts/check_iteration_decision.py examples/closed_loop_example_output.md
python scripts/check_pipeline_handoff.py examples/pipeline_handoff_example.md
python scripts/check_pipeline_handoff.py templates/phase_handoff.md
python scripts/check_banned_fabrication_markers.py examples/closed_loop_example_output.md
python scripts/check_claim_numbering.py examples/closed_loop_example_output.md
```

JSON Schema 解析检查：

```bash
python -c "import json, pathlib; [json.load(open(p, encoding='utf-8')) for p in pathlib.Path('schemas').glob('*.json')]; print('All schemas parsed OK')"
```

这些脚本只做结构和启发式检查，不替代专利代理师、律师或企业法务的专业审查。

## 安装到 Codex

从本仓库安装：

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo SALFM/cn-patent-first-draft --path .
```

如果本地开发安装，可将整个目录复制到：

```text
%USERPROFILE%\.codex\skills\cn-patent-first-draft
```

安装后重启 Codex 以加载新 skill。

## 免责声明

本 skill 仅用于辅助整理技术交底、生成专利技术草案和提示风险。最终申请策略、权利要求范围、法律风险、提交文本和程序文件，应由专利代理师、律师、企业法务或相关专业人员审查确认。
