---
tags: [skill-creator]
max_turns: 30
timeout_seconds: 900
append_system_prompt: "Eval mode: no human is available to answer. Whenever the skill would ask the member a question (form or numbered list), first output the full question with all its options and the (Đề xuất) markers in your visible reply text (not only in thinking or a tool call; graders read only the visible text). Only print questions the skill would actually ask: skip any question the member's message already answers. Then answer it yourself by picking the option marked (Đề xuất) — or, if none, the option that skips / leaves the field blank — unless the member's message already answers it. State the chosen answer in one line and immediately continue the flow in the same turn. Never end your turn after printing a question; the run is complete only after the bio file is saved and the reminder block is printed."
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash, AskUserQuestion]
---

/generate-short-bio Nguyễn Văn B, b.nguyen@example.com, Backend, 6 năm, PHP, Laravel (6 năm), MySQL, Redis, Docker. Dự án: Kintai Cloud — hệ thống chấm công và tính lương cho doanh nghiệp Nhật, 04/2022 – 03/2025, Backend Developer, team 8 người, mình làm API chấm công, module tính lương theo ca và batch xuất báo cáo tháng, stack Laravel, MySQL, Redis. Không có JD.
