# 维护者指南

本文档说明如何维护 `cn-patent-first-draft` 项目。维护时应优先保持规则可追溯、文件结构稳定、示例和模板一致。

## 如何新增参考资料

新增法规、审查指南、内部要求或模板资料时：

1. 将原始文件放入 `references/`。
2. 保留清晰可识别的中文文件名，必要时包含版本日期。
3. 不要覆盖旧文件，除非确认只是同一资料的清晰命名修正。
4. 更新 `reference_summaries/00_file_inventory.md`，说明新增文件用途、版本和状态。
5. 判断新增资料是否会影响 `SKILL.md`、`LEGAL_BASIS.md`、模板或示例。

原始资料是规则追溯基础，不应随意删除。

## 如何更新法规摘要

更新摘要时建议按顺序进行：

1. 阅读新增或替换的 `references/` 原始资料。
2. 更新对应的 `reference_summaries/` 文件。
3. 如果新资料影响多个规则模块，同步更新 `reference_summaries/99_integrated_rule_map.md`。
4. 在摘要中写明规则来源、适用边界和对 skill 的影响。
5. 遇到新旧规则冲突时，优先说明冲突处理逻辑，不要静默替换。

摘要应便于维护者和使用者理解，不应只堆砌法规条文。

## 如何修改模板

模板位于 `templates/`：

- `technical_disclosure_form.md` 影响用户输入字段。
- `patent_draft_output.md` 影响固定输出结构。
- `self_checklist.md` 影响交付前自检。
- `term_table.md` 影响术语统一表。

修改模板时应检查：

- 是否仍与 `SKILL.md` 的固定输出格式一致。
- 是否仍保留 `[待补充]` 的缺失处理方式。
- 是否避免引导用户编造现有技术、实验数据、附图和主体信息。
- 是否需要同步更新 `examples/example_output.md`。
- 是否需要同步更新 `README.md` 和 `docs/USAGE.md`。

## 如何修改 SKILL.md

`SKILL.md` 是主规则文件，修改应谨慎。

建议遵守：

- 只在有明确法规、审查指南、内部要求或项目需求依据时修改业务规则。
- 修改前先确认对应依据已经进入 `references/` 和 `reference_summaries/`。
- 不要大幅改写既有规则，除非规则体系确实重构。
- 保留禁止编造、缺失标记、技术闭环、权利要求支持、实用新型结构边界等核心原则。
- 对明显错别字、文件名引用错误或模板残留，可以做小修正，并在提交信息或变更说明中列出。

## 修改后应检查哪些文件

修改规则或模板后，至少检查：

- `SKILL.md`
- `LEGAL_BASIS.md`
- `README.md`
- `docs/USAGE.md`
- `docs/FAQ.md`
- `templates/technical_disclosure_form.md`
- `templates/patent_draft_output.md`
- `templates/self_checklist.md`
- `templates/term_table.md`
- `examples/minimal_input.md`
- `examples/example_output.md`
- `reference_summaries/99_integrated_rule_map.md`

如果新增或重命名参考资料，还要检查 `reference_summaries/00_file_inventory.md` 和 `references/` 文件名。

## 如何运行人工自检

没有自动测试时，可以按人工自检执行：

1. 用 `examples/minimal_input.md` 作为输入，检查输出是否仍按八个固定章节组织。
2. 检查是否出现虚构附图、实验数据、主体信息或现有技术文献。
3. 检查实用新型输出是否围绕产品结构，不把方法或流程写成核心保护对象。
4. 检查摘要是否为连续段落且不超过 300 字。
5. 检查说明书段落编号是否连续。
6. 检查术语统一表、权利要求、说明书和附图标记是否一致。
7. 对 AI/算法/软件/大数据示例，检查是否有技术问题、技术手段、技术效果和数据合规提示。
8. 检查输出是否保留必要的 `[待补充]`，而不是自行补全未知事实。

## Git 提交建议

建议提交粒度：

- 文档补充单独提交。
- 法规或参考资料更新单独提交。
- 规则修改单独提交。
- 模板调整单独提交。
- 示例更新单独提交。

提交信息建议清楚说明变更范围，例如：

```text
docs: add usage and maintenance guides
rules: update AI algorithm drafting checks
templates: refine disclosure form fields
references: add updated examination guideline materials
```

提交前建议运行：

```bash
git status
git diff --check
git diff --stat
```

不要提交临时文件、编辑器缓存或本地环境文件。
