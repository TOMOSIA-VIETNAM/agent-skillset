# Xuất + lưu file (bước 8)

Mục lục: §1 Template · §2 Core Skills · §3 Projects · §4 Lưu file & khối nhắc · §5 Bản en / ja · §6 Nhãn theo ngôn ngữ

---

## §1 — Template

In nội dung file ra màn hình rồi lưu (§4). Giữ đúng thứ tự:

```
# [Tên member]

**Vị trí:** [Role đầy đủ — "Frontend" → "Frontend Developer", "QA" → "QA Engineer"]
**Email:** [email]
**Ngày sinh:** [DD/MM/YYYY hoặc MM/YYYY như member nhập | _(chưa có — vui lòng bổ sung)_]
**Ngoại ngữ:** [chứng chỉ / trình độ đúng như member ghi, VD JLPT N3 · TOEIC 750]   ← chỉ khi có; không có thì bỏ dòng
**Chứng chỉ:** [chứng chỉ chuyên môn đúng như member ghi, VD AWS Certified Developer – Associate (2024)]   ← chỉ khi có; không có thì bỏ dòng

---

## Short Bio

[Đoạn 1]

[Đoạn 2]

[Đoạn 3]   ← chỉ khi mức chi tiết

[Đoạn AI]   ← chỉ role develop có dòng AI (`write-bio.md` §1)

---

## Core Skills

**[Domain 1]:** [Framework A (X năm)], [Framework B (Y năm)], [Skill C], [Skill D]
**[Domain 2]:** [Skill E], [Skill F]

---

## Projects   ← chỉ khi đầu vào có dự án; mẫu và cách viết: `projects.md` §5

### Project 1 — [Tiêu đề mô tả, không tên thật — `projects.md` §5]
...

### Project 2 — [Tiêu đề mô tả]
...
```

**Placeholder:** field thiếu ở header hoặc Projects → `_(chưa có — vui lòng bổ sung)_`, vẫn giữ dòng đó. Email là field bắt buộc nên không bao giờ là placeholder.

**Ngôn ngữ nội dung:** toàn bộ theo ngôn ngữ của bản đó, kể cả nội dung lấy từ CV viết bằng ngôn ngữ khác (CV tiếng Anh, bản vi → dịch Mô tả, Vai trò trong dự án). Giữ nguyên tên công nghệ; tiêu đề dự án viết theo ngôn ngữ của bản đó.

---

## §2 — Core Skills

**Format:** mỗi domain một dòng, **nhãn domain in đậm**, skill liệt kê inline, không dùng bảng. Trong mỗi dòng, skill chính đứng trước.

**Skill chính luôn ghi số năm, skill phụ đi kèm chỉ ghi tên.** Ở phần skill, điều khách quan tâm là các công nghệ chính đã dùng bao lâu; số năm ở mọi thư viện, công cụ làm dòng rối, khách khó tập trung vào thế mạnh chính.

| Nhóm | Ghi số năm? | VD |
|---|---|---|
| **Framework / platform chính** của role | Luôn ghi (cách lấy số năm: dưới) | BE: Laravel, Rails, Spring Boot, Django, FastAPI, NestJS, Express, Fastify... · FE: React, Vue, Angular, Next.js, Nuxt... · Mobile: Flutter, React Native, iOS (Swift), Android (Kotlin) · QA: framework automation chính (Selenium, Appium, Playwright, Cypress); QA manual → loại testing chính (`Manual Testing (4 năm)`) |
| **Skill chính khác**: ngôn ngữ / runtime chính, database chính, cloud chính | Luôn ghi (cách lấy số năm: dưới) | `PHP (5 năm)`, `TypeScript (6 năm)`, `Node.js (3 năm)`, `MySQL (4 năm)`, `AWS (2 năm)` |
| **Skill JD ghi rõ số năm** (VD "3 năm AWS") | Ghi theo `jd-match.md` §3 | `AWS (4 năm)` |
| **Skill phụ đi kèm**: thư viện, ORM, UI library, CSS tooling, công cụ test, CI/CD tool, cache / queue, Git / Docker / Jira, companion skills, database / ngôn ngữ chỉ dùng ở ít dự án | Chỉ ghi tên | Redux, Eloquent ORM, Tailwind CSS, Jest, Redis, GitHub Actions |

Skill chính dưới 1 năm (VD MongoDB 6 tháng) → chỉ ghi tên: con số nhỏ kéo hồ sơ xuống thay vì làm nổi bật. Số năm skill chính khác **không nâng theo tổng khi có JD** — chỉ nâng khi JD ghi số năm cho chính skill đó. Mọi số năm ≤ tổng số năm trong bio.

**Chỉ ghi tên công nghệ / công cụ cụ thể** (Redis, Jest, RabbitMQ), không ghi tên hoạt động hay khái niệm (`Unit test`, `Queue processing`, `Caching`, `Code review`). Hoạt động member đã làm, kể cả việc xác nhận ở checklist, thuộc về bio. Domain như `Caching & Queue` vẫn dùng làm nhãn, nhưng skill trong dòng phải là tên công cụ.

**Dòng AI — luôn đề xuất.** Khách ngày càng hỏi member dùng AI thế nào trong phát triển, nên mọi bio đều đề xuất 2 dòng này, đặt cuối Core Skills:
```
**AI / AI-assisted Development:** Claude, Cursor, MCP, Prompt Engineering, AI-driven Development Workflow
**AI-driven Software Development:** AI-assisted Requirement Analysis, Specification & Planning, Code Generation, Code Review, Test Case Generation, Refactoring
```
- Input đã có → dùng đúng nội dung member ghi. Chưa có → hỏi ở form tự vấn (`collect-info.md` §5, mục 1b); không tự thêm khi member chưa chọn.
- Member chọn thêm đủ → 2 dòng như trên. Chỉ gõ công cụ ở Other → dòng 1 chỉ gồm công cụ đó, bỏ dòng 2. `Không thêm` → bỏ cả hai, không nhắc AI trong bio.
- Hai dòng này là ngoại lệ của quy tắc chỉ ghi tên công cụ (mục dòng 2 là hoạt động) và không ghi số năm.
- Có JD: giữ ở mọi mức match, kể cả Hoàn toàn khớp; vẫn đứng sau các domain khớp JD.
- Có dòng AI và role develop → Short Bio có đoạn AI cuối cùng (`write-bio.md` §1). QA chỉ có dòng AI ở Core Skills.

**Skill chính là gì:** thứ member dùng ở phần lớn dự án hoặc tự ghi là chính, thuộc 4 nhóm framework / platform, ngôn ngữ / runtime, database, cloud. Mỗi nhóm thường chỉ 1–2 skill chính; phần còn lại là skill phụ.

**Cách lấy số năm skill chính**, theo thứ tự: số member / CV ghi → suy từ thời gian các dự án dùng skill đó (ghi vào khối nhắc là ý suy luận) → hỏi ở form tự vấn (`collect-info.md` §5, ưu tiên 3) → vẫn không có: framework chính của role ghi bằng tổng số năm; skill chính khác để `(_… năm/tháng_)` và liệt kê trong khối nhắc. Không tự đoán.

**Domain:**
- BE / FE / Fullstack: Backend/Framework, Frontend, API Integration, Database, Caching & Queue, Testing, DevOps/CI/CD, Cloud, UI/UX Design, rồi 2 dòng AI (trên). Mobile, QA cũng thêm 2 dòng AI ở cuối
- Mobile: Mobile Platform, UI Framework, State Management, Networking, Testing, CI/CD & Deployment
- QA: Testing Type, Automation Framework, Test Management, API Testing, Performance Testing — **không có CI/CD**

Chỉ in domain có skill. Có JD: domain khớp JD lên trước.

VD:
```
**Backend/Framework:** Laravel (7 năm), Fastify (3 năm), PHP (7 năm), Node.js (3 năm), Eloquent ORM
**API Integration:** RESTful API, GraphQL
**Database:** MySQL (5 năm), PostgreSQL
**Cloud:** AWS (2 năm), ECS, RDS
```

---

## §3 — Projects

Chọn dự án, form hỏi member và cách viết từng field: `projects.md` (bước 6). Ở bước này chỉ rà lại: có dự án thì có section `## Projects` (1–2 dự án), không có thì bỏ hẳn; dòng Vai trò trong dự án chỉ chứa việc member làm; Tech Stack là stack thật.

---

## §4 — Lưu file & khối nhắc

**Tên file:** `short-bio-[ten-kebab]-[YYYY-MM-DD].md` (bản đầu luôn là vi). `[ten-kebab]`: bỏ dấu, `đ`/`Đ` → `d`, chữ thường, khoảng trắng → `-`, bỏ ký tự khác chữ / số. VD `Đặng Thị B` → `dang-thi-b`. Lưu ở thư mục làm việc hiện tại.

**Lưu ngay sau khi in:**
1. Chưa có file trùng tên → lưu luôn, không hỏi.
2. Trùng tên → form (header `File`): `File [tên] đã có rồi. Bạn muốn làm gì?` · `Tạo bản mới [tên-v2].md (Đề xuất)` — description `giữ bản cũ` · `Ghi đè file cũ`. Hậu tố `-v2`, `-v3`... đặt trước `.md`, lấy số nhỏ nhất chưa dùng (file gốc tính là v1).
3. In đúng 1 dòng riêng `Đã lưu: [tên file]` hoặc `Đã ghi đè: [tên file]` — mọi trường hợp, kể cả bản `-vN`; không diễn đạt lại thành câu văn ("đã lưu thành...") vì member dò dòng này để biết file nào là bản mới. Lời nhắn ngoài file xưng "mình", gọi member là "bạn", không "tôi".

**Khối nhắc** — in sau khi lưu nếu file còn placeholder, bio có ý suy luận, có điều chỉnh theo JD (`jd-match.md` §5), hoặc có yêu cầu role × cấp chưa có bằng chứng (`checklist.md` §1). Có phần Projects thì luôn có dòng ghép tiêu đề với tên thật của dự án — khối nhắc chỉ in ra màn hình, không nằm trong file. Không phải câu hỏi, gom mọi thứ một chỗ:
```
⚠ File [tên file] cần kiểm tra trước khi gửi khách:
- Header: Ngày sinh
- Core Skills: số năm của Vue
- Projects (tiêu đề đã thay tên thật): Project 1 = LabPortal, Project 2 = MediVault
- Project 1 — LabPortal: Thời gian, Vai trò trong dự án
- Short Bio (suy luận): "quản lý kho y tế" suy từ tên dự án MediVault
- Thêm theo JD (chưa có trong profile): AWS (2 năm), Docker — chuẩn bị nếu khách hỏi
- Điều chỉnh theo JD: tổng số năm 4 → 5 năm; Vue → React
- Chưa thể hiện (yêu cầu Senior Backend): review code cho team, dẫn dắt thành viên — bổ sung nếu đã làm
Bổ sung trực tiếp vào file trước khi gửi khách hàng.
```
Không có gì để nhắc → không in. Xong là **kết thúc skill**.

---

## §5 — Bản en / ja (chỉ khi member tự yêu cầu)

Không hỏi tạo thêm bản. Member yêu cầu sau đó ("tạo bản en", "thêm bản tiếng Nhật") → sinh từ cùng thông tin, có humanize, văn phong theo `write-bio.md` §6, nhãn theo §6 dưới.
Tên file chèn `-en` / `-ja` trước ngày, theo cùng hậu tố với bản đầu (bản đầu `-v2` → `short-bio-[ten]-en-[ngày]-v2.md`). Trùng → hỏi như §4 bước 2. In khối nhắc nếu có.

---

## §6 — Nhãn theo ngôn ngữ

Heading `Short Bio` / `Core Skills` / `Projects` giữ nguyên ở mọi bản.

| vi | en | ja |
|---|---|---|
| Vị trí | Position | ポジション |
| Email | Email | メール |
| Ngày sinh | Date of birth | 生年月日 |
| Ngoại ngữ | Languages | 語学 |
| Chứng chỉ | Certifications | 資格 |
| Thời gian | Duration | 期間 |
| Mô tả | Description | 概要 |
| Team size | Team size | チーム規模 |
| Vai trò trong dự án | Responsibilities | 担当業務 |
| N người | N members | N名 |
| Tech Stack | Tech Stack | 技術スタック |
| X năm / X tháng | X years / X months | X年 / Xヶ月 |
| _(chưa có — vui lòng bổ sung)_ | _(not provided — please fill in)_ | _（未記入 — ご記入ください）_ |
| _… năm/tháng_ | _… years/months_ | _…年/ヶ月_ |
| (đang làm) | (ongoing) | （継続中） |
