---
tags: [skill-creator]
max_turns: 30
timeout_seconds: 900
append_system_prompt: "Eval mode: no human is available to answer. Whenever the skill would ask the member a question (form or numbered list), first write the full question with all its options and the (Đề xuất) markers in your visible reply text, then answer it yourself by picking the option marked (Đề xuất) — or, if none, the option that skips / leaves the field blank — unless the member's message already answers it. State the chosen answer in one line and continue the flow to the end in the same turn without stopping. Simulated member answers for this case: email is k.tran@example.com (typed via Other); skip adding projects; no JD."
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash, AskUserQuestion]
---

/generate-short-bio Trần Thị K, Frontend, 3 năm, React, TypeScript, Tailwind, Redux
