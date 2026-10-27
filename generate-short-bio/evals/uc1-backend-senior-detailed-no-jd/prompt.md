---
tags: [skill-creator]
max_turns: 30
timeout_seconds: 900
append_system_prompt: "Eval mode: no human is available to answer. Whenever the skill would ask the member a question (form or numbered list), first write the full question with all its options and the (Đề xuất) markers in your visible reply text, then answer it yourself by picking the option marked (Đề xuất) — or, if none, the option that skips / leaves the field blank — unless the member's message already answers it. State the chosen answer in one line and continue the flow to the end in the same turn without stopping."
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash, AskUserQuestion]
---

/generate-short-bio Nguyễn Văn B, b.nguyen@example.com, Backend, 6 năm, PHP, Laravel (6 năm), MySQL, Redis, Docker. Dự án: Kintai Cloud — hệ thống chấm công và tính lương cho doanh nghiệp Nhật, 04/2022 – 03/2025, Backend Developer, team 8 người, mình làm API chấm công, module tính lương theo ca và batch xuất báo cáo tháng, stack Laravel, MySQL, Redis. Không có JD.
