# Pipeline 01：Intake & Boundary

## 目标

由一个阶段 Codex 独立完成输入解析、事实/推断/缺失项分离和边界风险判断。

## 输入

- 用户技术交底。
- 用户指定的专利类型、保护目标、已有附图/草图、现有技术和与技术方案有关的公开/合规边界。
- `prompts/00_intake_and_boundary.md`。

## 输出

- 输入解析与缺失信息分级。
- 不授权客体、违法/社会公德/公共利益、涉密、遗传资源、AI/数据合规等边界风险。
- 初步 Case ID。
- `templates/phase_scorecard.md`。
- `templates/phase_handoff.md`。

## 质量门

- 技术方案至少能识别为可处理、需用户事实或不可处理之一。
- 事实、推断、缺失事实必须分开。
- 不得编造现有技术、公开日期、产品结构、参数或已经存在的正式附图。
- 申请人、发明人、代理机构、优先权等主体/程序信息默认不作为本阶段缺失项；用户明确要求正式申请字段时，只能照录用户提供内容。

## 交接要求

阶段 Codex 不得开启下一对话。必须在 handoff 中给 controller 一个下一阶段建议：Invention Mining、NEEDS_USER_FACTS 或 STOP_LIMIT。
