# Xuất + lưu file (bước 7)

Mục lục: §1 Template · §2 Core Skills · §3 Project Examples · §4 Lưu file & khối nhắc · §5 Bản en / ja · §6 Nhãn theo ngôn ngữ

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

---

## Core Skills

**[Domain 1]:** [Framework A (X năm)], [Framework B (Y năm)], [Skill C], [Skill D]
**[Domain 2]:** [Skill E], [Skill F]

---

## Project Examples   ← chỉ khi đầu vào có dự án

### Project 1 — [Tên dự án]
**Thời gian:** [X tháng / X năm Y tháng]
**Vị trí:** [Vai trò trong dự án]
**Mô tả:** [2–3 câu: sản phẩm làm gì, cho ai, giá trị chính]
**Tính năng đảm nhiệm:**
- [Tính năng member làm 1]
- [Tính năng member làm 2]
**Tech Stack:** [Stack thật của dự án]

### Project 2 — [Tên dự án]
...
```

**Placeholder:** field thiếu ở header hoặc Project Examples → `_(chưa có — vui lòng bổ sung)_`, vẫn giữ dòng đó. Email là field bắt buộc nên không bao giờ là placeholder.

**Ngôn ngữ nội dung:** toàn bộ theo ngôn ngữ của bản đó, kể cả nội dung lấy từ CV viết bằng ngôn ngữ khác (CV tiếng Anh, bản vi → dịch Mô tả, Tính năng đảm nhiệm). Giữ nguyên tên dự án, tên công nghệ.

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

**Skill chính là gì:** thứ member dùng ở phần lớn dự án hoặc tự ghi là chính, thuộc 4 nhóm framework / platform, ngôn ngữ / runtime, database, cloud. Mỗi nhóm thường chỉ 1–2 skill chính; phần còn lại là skill phụ.

**Cách lấy số năm skill chính**, theo thứ tự: số member / CV ghi → suy từ thời gian các dự án dùng skill đó (ghi vào khối nhắc là ý suy luận) → hỏi ở form tự vấn (`collect-info.md` §5, ưu tiên 3) → vẫn không có: framework chính của role ghi bằng tổng số năm; skill chính khác để `(_… năm/tháng_)` và liệt kê trong khối nhắc. Không tự đoán.

**Domain:**
- BE / FE / Fullstack: Backend/Framework, Frontend, API Integration, Database, Caching & Queue, Testing, DevOps/CI/CD, Cloud, UI/UX Design, AI
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

## §3 — Project Examples

**Khi nào có section:** đầu vào (form hoặc CV) có ít nhất 1 dự án có tên → có. Không có dự án → bỏ hẳn section.

**Số dự án:** 1–2, chọn tiêu biểu. Không JD: ưu tiên gần đây, có kết quả, quy mô lớn. Có JD: ưu tiên dự án khớp JD.

| Field | Lấy từ | Thiếu |
|---|---|---|
| Tên | Input / CV, giữ tên gốc | Không có tên → không tính là dự án |
| Thời gian | Tính từ mốc (VD `02/2025 – 12/2025` → `10 tháng`). Đang làm → tính tới ngày tạo file, kèm `(đang làm)` | Placeholder |
| Vị trí | Vai trò trong dự án ghi ở input / CV hoặc member chọn ở tự vấn | Placeholder — không tự lấy role tổng của member |
| Mô tả | Mô tả trong input / CV, viết gọn lại, không thêm chi tiết | Placeholder |
| Tính năng đảm nhiệm | **Chỉ tính năng member làm / phụ trách** theo input, CV, hoặc member chọn ở tự vấn. Tối đa 5 mục; input ít hơn thì giữ đúng số đó | Placeholder — không tự suy |
| Tech Stack | Stack thật của dự án — **kể cả khi có JD, không thay theo JD** | Placeholder |

Tính năng đảm nhiệm khác tính năng của sản phẩm: khách hỏi "phần này anh/chị làm thế nào?" thì member phải trả lời được, nên chỉ ghi phần member thực sự làm.

---

## §4 — Lưu file & khối nhắc

**Tên file:** `short-bio-[ten-kebab]-[YYYY-MM-DD].md` (bản đầu luôn là vi). `[ten-kebab]`: bỏ dấu, `đ`/`Đ` → `d`, chữ thường, khoảng trắng → `-`, bỏ ký tự khác chữ / số. VD `Đặng Thị B` → `dang-thi-b`. Lưu ở thư mục làm việc hiện tại.

**Lưu ngay sau khi in:**
1. Chưa có file trùng tên → lưu luôn, không hỏi.
2. Trùng tên → form (header `File`): `File [tên] đã có rồi. Bạn muốn làm gì?` · `Tạo bản mới [tên-v2].md (Đề xuất)` — description `giữ bản cũ` · `Ghi đè file cũ`. Hậu tố `-v2`, `-v3`... đặt trước `.md`, lấy số nhỏ nhất chưa dùng (file gốc tính là v1).
3. In đúng 1 dòng riêng `Đã lưu: [tên file]` hoặc `Đã ghi đè: [tên file]` — mọi trường hợp, kể cả bản `-vN`; không diễn đạt lại thành câu văn ("đã lưu thành...") vì member dò dòng này để biết file nào là bản mới. Lời nhắn ngoài file xưng "mình", gọi member là "bạn", không "tôi".

**Khối nhắc** — in sau khi lưu nếu file còn placeholder, bio có ý suy luận, có điều chỉnh theo JD (`jd-match.md` §5), hoặc có yêu cầu role × cấp chưa có bằng chứng (`checklist.md` §1). Không phải câu hỏi, gom mọi thứ một chỗ:
```
⚠ File [tên file] cần kiểm tra trước khi gửi khách:
- Header: Ngày sinh
- Core Skills: số năm của Vue
- Project 1 — LabPortal: Thời gian, Tính năng đảm nhiệm
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

Heading `Short Bio` / `Core Skills` / `Project Examples` giữ nguyên ở mọi bản.

| vi | en | ja |
|---|---|---|
| Vị trí | Position | ポジション |
| Email | Email | メール |
| Ngày sinh | Date of birth | 生年月日 |
| Ngoại ngữ | Languages | 語学 |
| Chứng chỉ | Certifications | 資格 |
| Thời gian | Duration | 期間 |
| Mô tả | Description | 概要 |
| Tính năng đảm nhiệm | Features Delivered | 担当機能 |
| Tech Stack | Tech Stack | 技術スタック |
| X năm / X tháng | X years / X months | X年 / Xヶ月 |
| _(chưa có — vui lòng bổ sung)_ | _(not provided — please fill in)_ | _（未記入 — ご記入ください）_ |
| _… năm/tháng_ | _… years/months_ | _…年/ヶ月_ |
| (đang làm) | (ongoing) | （継続中） |
