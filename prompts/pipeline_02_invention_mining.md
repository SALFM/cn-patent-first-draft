# Pipeline 02：Invention Mining

## 目标

基于 Intake Handoff，构建发明画像和“现有技术缺陷 -> 技术问题 -> 技术手段 -> 技术效果”闭环。

## 输入

- Intake 阶段 handoff。
- 用户技术交底和缺失事实列表。
- `prompts/01_invention_mining.md`。
- `templates/invention_profile.md`。

## 输出

- 发明画像。
- 技术问题、核心技术手段、技术效果和必要技术特征候选。
- 需用户确认的发明事实。
- `templates/phase_scorecard.md`。
- `templates/phase_handoff.md`。

## 质量门

- 每个主要技术问题至少对应一个技术手段和一个技术效果。
- 技术效果必须能由已披露技术特征合理推出，不能编造实验或测试结论。
- 若无法形成技术闭环，应输出 `NEEDS_USER_FACTS` 或 `REVISE`，不得强行进入下一阶段。

## 交接要求

下一阶段建议通常为 Feature Matrix。若核心技术方案不清，返回 Intake 或停止等待用户事实。
