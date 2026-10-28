# Viết Short Bio (bước 6)

Mục lục: §1 Số đoạn & cấu trúc · §2 Ý cần có · §3 Viết thế nào · §4 Humanize · §5 Kiểm tra trước khi xuất · §6 Văn phong vi / en / ja

Short Bio là phần khách đọc đầu tiên và thường đọc lướt giữa nhiều hồ sơ. Nó phải cho thấy **toàn bộ năng lực** của member trong vài câu, đọc như người viết, và không có câu nào member không thể bảo vệ khi bị hỏi.

---

## §1 — Số đoạn & cấu trúc

| Mức (`collect-info.md` §4) | Số đoạn | Độ dài (bản vi, cả Short Bio) |
|---|---|---|
| Chi tiết | 3 | ~110–160 từ |
| Sơ sài | 2 | ~80–120 từ |

Mỗi đoạn 2–3 câu. en / ja độ dài tương đương.

**Sơ sài — 2 đoạn, mọi role.** Không có dự án thì đoạn thứ 3 chỉ có thể là câu chung chung hoặc bịa, nên bỏ.
- Đoạn 1: role, số năm, stack chính, domain (nếu có). Có JD: nối vào nhu cầu JD.
- Đoạn 2: năng lực theo nhóm Core Skills, viết tự nhiên. Không JD: chỉ skill member đã nhập. Có JD: ưu tiên skill khớp JD, kể cả skill bổ sung.

**Chi tiết — 3 đoạn theo role:**

*Backend / Frontend / Fullstack*
1. Role, tổng năm, stack chính, mảng sản phẩm / domain cốt lõi.
2. Năng lực tổng hợp qua các dự án: loại sản phẩm đã làm, nhóm năng lực kỹ thuật, quy mô team, phạm vi đảm nhận, kết quả (nếu input có).
3. Cách làm việc: quy trình tham gia, review code, viết test, phối hợp FE / BE / QA, đề xuất cải tiến.

*Mobile*
1. Role, số năm, platform chính, loại app. Có JD: nối nhu cầu platform của khách.
2. Các loại app đã làm, nhóm tính năng nổi bật, kinh nghiệm phát hành store.
3. Tư duy UX / performance, phối hợp designer và backend.

*QA*
1. Role, số năm QA, loại testing chính, domain. Có JD: nối yêu cầu testing.
2. Loại sản phẩm / domain đã test, coverage, công cụ nổi bật, vị trí trong dev cycle. **Không nhắc CI/CD setup.**
3. Tư duy chất lượng, phối hợp dev, phát hiện bug sớm, cải tiến quy trình.

**Toàn bộ bio nói về năng lực tổng hợp, không về một dự án.** Không gọi tên dự án, không kể riêng từng dự án. Gom theo loại sản phẩm / domain / quy mô (VD "đã làm hệ thống cloud cho kế toán, web app chat AI và nền tảng quản lý công việc"). Chi tiết từng dự án nằm ở Project Examples.

---

## §2 — Ý cần có

Ý nào input không có dữ liệu → bỏ, không viết cho đủ.

| # | Ý | Khi nào có | Vị trí |
|---|---|---|---|
| 1 | **Định vị:** role, số năm, stack chính | Luôn | Câu đầu |
| 2 | **Mảng sản phẩm / domain** (gom lại, không tên dự án) | Có dự án hoặc domain | Đoạn 1 |
| 3 | **Năng lực kỹ thuật theo nhóm** — phủ các nhóm chính của Core Skills (UI, state, API, DB, DevOps...), nói skill dùng để làm gì | Luôn | Đoạn 2 |
| 4 | **Phạm vi & quy trình:** requirement definition / basic design / detailed design / implementation / deploy (ja: 要件定義 / 基本設計 / 詳細設計 / 実装 / デプロイ), quy mô team | Input / CV có | Đoạn 2 hoặc 3 |
| 5 | **Cách phối hợp:** với BE / FE / QA / designer, review, test | Rút ra được từ input | Đoạn 3 |
| 6 | **Kết quả, số liệu** | Chỉ khi input có — không bao giờ tự tạo | Đoạn 2 |
| 7 | **Kết nối JD** | Có JD | Câu đầu |
| 8 | **Ngoại ngữ / chứng chỉ** (VD "giao tiếp tiếng Nhật, JLPT N3", "có chứng chỉ AWS Developer") | JD yêu cầu ngoại ngữ / chứng chỉ đó và member có | Đoạn 1 hoặc 3 |

Sơ sài: ý 1, 2, 7 ở đoạn 1; ý 3 ở đoạn 2; ý 4–6 thường không có → bỏ.

Ngoài bảng trên, bio phải thể hiện các yêu cầu nội dung theo role × cấp có bằng chứng (`checklist.md`) — đó là thứ làm bio Senior khác bio Junior cùng stack.

---

## §3 — Viết thế nào

**Diễn giải skill thành năng lực.** Nói skill dùng để làm gì, gom skill cùng nhóm, phủ nhiều nhóm năng lực thay vì nhắc 1–2 skill:
- Tránh: "Dùng React, Redux, Tailwind, Jest."
- Viết: "Dựng giao diện responsive bằng React và Tailwind CSS, tổ chức state bằng Redux và kết nối dữ liệu qua RESTful API."

**Đoạn 3 viết bằng hành động có bối cảnh, không câu mindset.**
- Tránh: "Luôn đặt chất lượng lên hàng đầu và có tinh thần trách nhiệm cao."
- Viết: "Thống nhất API contract với frontend ngay đầu sprint, giảm rework khi tích hợp."
- Profile không có chi tiết cách làm việc → rút từ các dự án (giai đoạn tham gia, test đã viết, team phối hợp), không bịa.

**Padding — tránh:**
| Tránh | Vì sao |
|---|---|
| "qua nhiều dự án thực tế" | không cụ thể |
| "tích lũy kinh nghiệm" | hiển nhiên |
| "có yêu cầu cao về hiệu năng và độ ổn định" | quá chung |
| "phục vụ nghiệp vụ phức tạp" | không cụ thể |
| "có kỹ năng làm việc nhóm tốt" | thay bằng hành động cụ thể |
| "điều này giúp..." | giải thích thừa |

Mỗi câu gói 1–2 ý liên quan. Không câu cụt, không liệt kê trơn. Có transition giữa các đoạn để bio đọc như một mạch.

**Stack trong bio khi có JD:** năng lực tổng hợp dùng stack đã thay theo JD; câu gắn stack với một loại sản phẩm đã làm thật thì giữ stack thật (`jd-match.md` §3 bước 3).

---

## §4 — Humanize (luôn chạy, mọi ngôn ngữ)

Bản nháp đầu thường còn dấu hiệu văn AI (mở đầu giống nhau, liệt kê 3 điểm, câu kết chung chung). Khách đọc nhiều hồ sơ nên nhận ra ngay, và độ tin cậy giảm theo.

1. Viết nháp Short Bio theo §1–§3.
2. Gọi skill `humanizer` ở **embedded mode** cho riêng các đoạn Short Bio — chỉ lấy văn bản cuối, không in bản nháp hay danh sách pattern cho member.
3. **Ràng buộc của skill này ưu tiên hơn humanizer.** Sau humanize kiểm tra lại: số liệu, số năm, stack giữ nguyên; không thêm chi tiết mới, không tên dự án; không đại từ, không gọi tên, không câu bị động; đúng số đoạn, số câu, độ dài.
4. Core Skills, Project Examples, heading, nhãn: không humanize.

**Không có skill `humanizer`** → tự áp dụng:
- Đa dạng mở đầu ("Trong X năm...", "Với nền tảng...", "Đã xây dựng..."), không phải lúc nào cũng "Sở hữu X năm...".
- Transition tự nhiên giữa đoạn.
- Đặt skill vào bối cảnh có sẵn trong input (VD có dự án EC dùng React → "xây giao diện EC bằng React").
- Tránh: "không chỉ X mà còn Y", liệt kê 3 điểm đối xứng, dash liên tục, từ phóng đại ("xuất sắc", "mạnh mẽ"), câu kết một dòng.

---

## §5 — Kiểm tra trước khi xuất (sau humanize, sửa tới khi đạt hết)

1. **Truy được nguồn:** mỗi ý chỉ ra được dòng tương ứng trong input / CV / JD / quy tắc JD adjustment. Không truy được → bỏ hoặc viết lại.
2. **Khớp Core Skills:** skill và số năm trong bio có ở Core Skills, không mâu thuẫn.
3. **Ý suy luận được báo:** ý suy ra thay vì có sẵn (VD domain suy từ tên dự án) → ghi vào khối nhắc.
4. **Đủ ý:** các ý có dữ liệu ở §2 đều xuất hiện.
5. **Văn phong:** không đại từ, không tên member, không tên dự án, không câu bị động; đúng số đoạn / câu / độ dài; không padding.
6. **Có JD:** skill nice to have member chưa có không xuất hiện trong bio như kinh nghiệm; cross-role thì dự án role cũ chỉ được nhắc dưới dạng nghiệp vụ / domain (`jd-match.md` §3 bước 4, §4 bước 5). Rà từng câu có tính năng / luồng của dự án role cũ: khách đọc có hiểu member đã làm phần đó ở role mới không? Có → viết lại thành "am hiểu nghiệp vụ..." hoặc bỏ.
7. **Đúng tầm cấp:** mọi yêu cầu của role × cấp (`checklist.md`) có bằng chứng đều được thể hiện ở đúng đoạn; yêu cầu không có bằng chứng thì không viết.

---

## §6 — Văn phong theo ngôn ngữ

Không dùng đại từ vì bio có thể do member tự gửi hoặc BD chuyển cho khách — câu không chủ ngữ đúng trong cả hai trường hợp.

### vi
Chủ động, chuyên nghiệp, không bullet trong bio. Câu không chủ ngữ, mở bằng động từ / cụm danh từ ("Đã xây dựng...", "Backend Developer với..."). Không "tôi" / "bạn" / "anh" / "chị", không gọi tên member. Không chuyển sang bị động ("được xử lý bởi...") để né đại từ.
Cụm mở đầu: "Sở hữu...", "Thành thạo...", "Có kinh nghiệm...", "Chuyên về...", "Đã xây dựng...", "[Role] với X năm..."
QA: "Có kinh nghiệm...", "Đảm bảo chất lượng...", "Phát hiện và xử lý..." — không dùng ngôn ngữ developer (kiến trúc hệ thống, tích hợp CI/CD).

### en
Active voice, professional, no bullets in bio paragraphs. Implied first person, resume style: start with an action verb or noun phrase ("Built...", "Led...", "Backend Developer with..."). Never "I" / "my" / "you" / "he" / "she", never the member's name. Do not fall back to passive voice ("Releases were handled...") or abstract subjects ("Close work with designers keeps...") — write "Handled releases...", "Work closely with designers...".
Openers: "Experienced in...", "Proficient in...", "Skilled at...", "With X years of...", "Built...", "Led..."
QA: "Experienced in building...", "Skilled at detecting..." — avoid developer language (architecture, CI/CD setup).

### ja
能動的・丁寧・自然。BioにBulletは使わない。主語を省略した文で書く（「〜を専門としています」「〜を担当しました」）。「私」「あなた」、氏名（〜氏は）は使わない。代名詞を避けるために受動態にしない。
フレーズ例: 「〜に精通し...」「〜の経験を持ち...」「〜を専門とし...」
QA: 「〜のテスト経験を持ち...」「〜を用いた品質保証...」 — developer表現（アーキテクチャ、CI/CD構築）は使わない。
