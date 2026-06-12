# Pipeline 03：Feature Matrix

## 目标

把发明画像拆成可追溯的技术特征矩阵，标明必要性、支持依据、风险和下游用途。

## 输入

- Invention Mining handoff。
- 发明画像。
- `prompts/02_feature_matrix.md`。
- `templates/feature_matrix.md`。

## 输出

- 技术特征矩阵。
- 必要技术特征、可选技术特征、fallback 特征和需用户确认特征。
- `templates/phase_scorecard.md`。
- `templates/phase_handoff.md`。

## 质量门

- 每个核心技术特征必须对应技术问题、技术效果和用户依据。
- 进入独权的候选特征必须标明必要性。
- 缺失事实不能被写成确定特征。

## 交接要求

下一阶段建议通常为 Claim Architecture。若必要技术特征不清，应返回 Invention Mining 或进入 NEEDS_USER_FACTS。
