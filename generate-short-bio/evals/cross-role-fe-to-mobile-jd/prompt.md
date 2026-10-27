---
tags: [skill-creator]
max_turns: 30
timeout_seconds: 900
append_system_prompt: "Eval mode: no human is available to answer. Whenever the skill would ask the member a question (form or numbered list), first write the full question with all its options and the (Đề xuất) markers in your visible reply text, then answer it yourself by picking the option marked (Đề xuất) — or, if none, the option that skips / leaves the field blank — unless the member's message already answers it. State the chosen answer in one line and continue the flow to the end in the same turn without stopping."
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash, AskUserQuestion]
---

/generate-short-bio Nguyễn Văn C, c.nguyen@example.com, Frontend, 5 năm, React (5 năm), Next.js, TypeScript, Redux Toolkit, Tailwind. Dự án: MediBook — web đặt lịch khám cho chuỗi phòng khám, 01/2023 – 12/2024, Frontend Developer, mình làm màn đặt lịch, lịch sử khám và thanh toán online, stack React, Next.js, Redux Toolkit, Tailwind.
JD: ./jd-react-native.md — mức tương đối khớp

Input files: jd-react-native.md
