---
tags: [skill-creator]
max_turns: 30
timeout_seconds: 900
append_system_prompt: "Eval mode: no human is available to answer. Whenever the skill would ask the member a question (form or numbered list), first write the full question with all its options and the (Đề xuất) markers in your visible reply text, then answer it yourself by picking the option marked (Đề xuất) — or, if none, the option that skips / leaves the field blank — unless the member's message already answers it. State the chosen answer in one line and continue the flow to the end in the same turn without stopping."
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash, AskUserQuestion]
---

/generate-short-bio Trần Thị G, g.tran@example.com, Frontend, 4 năm, Vue.js (4 năm), Nuxt, TypeScript, Pinia. Dự án: EduNote — nền tảng học online cho trường Nhật, 06/2023 – 05/2025, Frontend Developer, mình làm màn bài giảng, quiz và dashboard giáo viên, stack Vue.js, Nuxt, Pinia.
JD: ./jd-vue-senior.md
