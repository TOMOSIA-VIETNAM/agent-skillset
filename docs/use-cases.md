# generate-short-bio — Use cases

Tài liệu này mô tả **hành vi theo use case** và các quyết định đã chốt; quy tắc chi tiết nằm trong `references/` của skill — mục nào trùng thì trỏ tới file đó thay vì chép lại. Sửa flow thì sửa tài liệu này và file reference tương ứng cùng lúc.

Use case được xác định bởi 3 điều kiện đầu vào:
- **Nguồn thông tin:** form nhập tay · file / link CV (paste ở Câu 1, hoặc gõ kèm lệnh `/generate-short-bio [link CV | thông tin member]` — bỏ bước in form). Skill không nhận flag.
- **Mức độ chi tiết:** chi tiết · sơ sài
- **JD:** không có · có

Output luôn chỉ là file bio (vi mặc định; en / ja khi member yêu cầu) — không tạo file profile hay file trung gian.

---

## 1. Thứ tự xử lý chung

Mọi use case đi theo cùng một thứ tự. Use case chỉ khác nhau ở cách thực hiện từng bước.

```
1. Lấy thông tin        Câu 1 (gõ tay) · đọc CV → in tóm tắt, không chờ "ok"
2. Bổ sung / tự vấn      field bắt buộc còn thiếu · mức chi tiết · checklist role × cấp → 1 form
3. Kiểm tra role         role ↔ stack (có thể là câu cuối của form bước 2)
4. JD                    form riêng: không có JD / paste / link / file
5. Mức match             form riêng, có đề xuất (chỉ khi có JD)
6. Dự án                 chọn 1–2 dự án → rà mô tả / vai trò / stack → mỗi dự án 1 form (chỉ khi có dự án)
7. Sinh bio              JD adjustment (nếu có) → viết → humanize → tự kiểm tra
8. Rà checklist + lưu    in bio → lưu file (trùng tên → form) → khối nhắc → kết thúc
```

Cách hỏi (`SKILL.md` → *Cách hỏi*): ưu tiên form `AskUserQuestion`, 2–4 lựa chọn thật mỗi câu, tối đa 4 câu mỗi form, lựa chọn đề xuất đứng đầu kèm `(Đề xuất)`. Gom câu trong cùng một bước, không gom xuyên bước — câu JD và mức match luôn hỏi riêng; câu dự án hỏi sau mức match, mỗi dự án một form. Thông tin member đã đưa sẵn (VD JD gõ kèm lệnh) thì không hỏi lại.

---

## 2. Phân loại mức độ chi tiết

Đánh giá ở bước 2, sau khi có thông tin thô, áp dụng cho form và CV (`collect-info.md` §4).

| Mức độ | Tiêu chí | Ví dụ |
|---|---|---|
| **Chi tiết** | Có ít nhất 1 dự án kèm mô tả: sản phẩm làm gì, vai trò hoặc stack dùng. Kết quả, số liệu là điểm cộng, không bắt buộc. | "CloudBooks — hệ thống cloud cho công ty kế toán Nhật, ReactJS, team 6 người, làm basic design → implementation" |
| **Sơ sài** | Chỉ có 5 field bắt buộc (có thể kèm ngày sinh, domain), **hoặc** dự án chỉ có tên, không mô tả. | "Nguyễn Văn A, Frontend, 3 năm, React, Vue, a@example.com" |

---

## 3. Bảng use case

| Nguồn | Mức độ | Không kèm JD | Kèm JD |
|---|---|---|---|
| Form nhập tay | Chi tiết | **UC1** | **UC2** |
| Form nhập tay | Sơ sài | **UC3** | **UC4** |
| File / link CV | Chi tiết | **UC5** | **UC6** |
| File / link CV | Sơ sài | **UC7** | **UC8** |

---

## 4. Use case — Form nhập tay

### UC1 — Form chi tiết, không kèm JD

**Luồng:**
1. Câu 1: in form, member nhập (hoặc gõ kèm lệnh).
2. Validate 5 field bắt buộc; thiếu → hỏi đúng field thiếu **trong form tự vấn**: họ tên / email / tech stack gộp 1 câu gõ ở ô Other; role, số năm mỗi field 1 câu. Email thiếu mà đã có họ tên → câu riêng đề xuất `tên.họ@tomosia.com`.
3. Tự vấn: rà chỗ thiếu theo bảng ưu tiên (`collect-info.md` §5) — gồm checklist role × cấp — hỏi gộp 1 form.
4. Kiểm tra role → JD: chọn `Không có, viết bio chung`, không hỏi mức match.
5. Dự án: form dự án (mục 6).
6. Sinh bio → humanize → rà checklist → in → lưu file → khối nhắc.

**Output:**
- **Short Bio, 3 đoạn** theo cấu trúc của role (`write-bio.md` §1): định vị + domain → năng lực tổng hợp → cách làm việc. Không gọi tên dự án. Thể hiện các yêu cầu của role × cấp có bằng chứng.
- **Core Skills:** đúng skill member nhập, không thêm skill đi kèm. Skill chính (framework / platform, ngôn ngữ, database, cloud) luôn có số năm, skill phụ đi kèm chỉ ghi tên (Q2, Q17, `output.md` §2).
- **Số năm:** giữ nguyên thực tế.
- **Projects:** mục 6.

### UC2 — Form chi tiết, kèm JD

**Luồng:** như UC1 bước 1–3, sau đó:
1. JD: paste / link / file (`jd-match.md` §1).
2. Mức match: form có đề xuất, mỗi lựa chọn nêu hệ quả cụ thể với member (VD `Ghi 5 năm (JD 5+)`).
3. JD adjustment (`jd-match.md` §3):
   - Số năm chỉ nâng, không hạ: `max(thực tế, mốc theo mức match)`.
   - Thay stack cùng danh mục ở Core Skills và Short Bio.
   - JD ghi số năm cho một skill (VD "3 năm AWS") → skill đó được ghi số năm (Q12).
   - Nice to have member chưa có → chỉ Core Skills + khối nhắc, không vào bio (Q18).
   - Companion skills theo số năm đã chốt (`companions.md`).
   - Role JD khác role member → cross-role (`jd-match.md` §4, Q19).
4. Dự án: chọn dự án khớp JD, form dự án (mục 6).
5. Sinh bio → humanize → rà checklist theo cấp **đã chốt sau JD** → in → lưu → khối nhắc.

**Output:**
- **Short Bio, 3 đoạn:** câu mở kết nối nhu cầu JD; ưu tiên năng lực khớp JD.
- **Core Skills:** domain khớp JD lên trước. Phạm vi theo mức match:
  - **Hoàn toàn khớp:** chỉ skill / domain khớp JD (companion tính là khớp); Git / Docker / Jira cũng bỏ nếu JD không nhắc (Q20).
  - **Tương đối:** highlight skill khớp, giữ điểm mạnh khác.
  - **Tổng quát:** JD là gợi ý nhẹ.
- **Projects:** mục 6, ưu tiên dự án khớp JD.

**Stack khi có JD (áp dụng cho UC2/4/6/8):**

| Phần | Stack ghi |
|---|---|
| Core Skills | Theo JD (đã thay stack cùng loại) |
| Short Bio (năng lực tổng hợp) | Theo JD |
| Short Bio, câu gắn stack với loại sản phẩm / domain đã làm | Stack thật |
| Projects | Stack thật của dự án, cộng công nghệ member chọn ở form dự án (Q10) |

Lý do: dự án là thông tin cụ thể mà khách có thể hỏi lại. Phần điều chỉnh theo JD nằm ở năng lực tổng quát.

### UC3 — Form sơ sài, không kèm JD

**Luồng:**
1. Câu 1 → validate.
2. Tự vấn — câu bổ sung dự án nằm trong form: `Bạn có muốn thêm 1–2 dự án không? Có dự án thì bio đủ 3 đoạn và có phần Projects.` · `Có, nhập ở tin nhắn sau` · `Không cần, bio 2 đoạn là được`.
   - Chọn `Có` → in 1 dòng `Bạn nhập 1–2 dự án nhé: tên, thời gian, vị trí, mô tả, việc bạn làm và tech stack.` — lần bổ sung duy nhất. Đủ chi tiết → chuyển sang **UC1**.
   - Chọn `Bỏ qua` → tiếp tục UC3, không hỏi lại.
3. Kiểm tra role → JD: không có.
4. Có dự án → form dự án (mục 6).
5. Sinh bio sơ sài → humanize → rà checklist → in → lưu → khối nhắc.

**Output:**
- **Short Bio, 2 đoạn** (Q1). Không bịa dự án, kết quả hay cách làm việc. Việc member xác nhận ở checklist được viết vào bio.
- **Core Skills:** đúng skill member nhập. Skill chính không có số năm → hỏi ở tự vấn; vẫn không có thì framework chính ghi bằng tổng số năm, skill chính khác → `_… năm/tháng_`; skill phụ chỉ ghi tên (Q2, Q17).
- **Projects:** có ghi tên dự án → vẫn tạo, hỏi ở form dự án; field còn thiếu để placeholder. Không có dự án → bỏ section.

### UC4 — Form sơ sài, kèm JD

**Luồng:** như UC3 bước 1–3 (đủ chi tiết thì chuyển sang **UC2**), rồi JD → mức match → JD adjustment như UC2.

**Output:** Short Bio 2 đoạn — đoạn 1 kết nối JD, đoạn 2 năng lực theo skill khớp JD (kể cả skill bổ sung). Core Skills như UC2. Projects như UC3.

---

## 5. Use case — File / link CV

Cách đọc từng loại link / file, bảng lỗi, quy tắc trích xuất và mẫu tóm tắt: `collect-info.md` §2.

**Chung cho UC5–UC8:**
1. Đọc CV → trích theo các field của Câu 1; bỏ học vấn, lương, giới tính, SĐT, địa chỉ, ảnh, sở thích. Ngoại ngữ và chứng chỉ chuyên môn thì giữ (Q24, Q25).
2. In tóm tắt rồi đi tiếp ngay, không hỏi `ok`. Cùng lượt: hỏi field bắt buộc còn thiếu (nếu có) và form tự vấn. Member sửa tóm tắt qua ô "Other" hoặc nhắn kèm → merge, đánh giá lại mức chi tiết.
3. CV chỉ mô tả tính năng của sản phẩm, không rõ phần member làm → câu multiSelect `Ở dự án [Dự án], bạn trực tiếp làm những tính năng nào?` trong form tự vấn.
4. Kiểm tra role.

**Biến thể:** vừa đưa link CV vừa gõ thêm thông tin → đọc CV, phần gõ tay ưu tiên khi trùng field.

### UC5 — CV chi tiết, không kèm JD
Như **UC1** sau bước đọc CV. CV thường có nhiều dự án và skill hơn form, nên chọn lọc điểm mạnh nổi bật nhất.

### UC6 — CV chi tiết, kèm JD
Như **UC2** sau bước đọc CV. Dự án chọn theo mức khớp JD.

### UC7 — CV sơ sài, không kèm JD
Đọc CV → tự vấn có câu bổ sung dự án như UC3. Bổ sung đủ → như **UC5**; không → như **UC3**.

### UC8 — CV sơ sài, kèm JD
Như UC7, sau đó JD → mức match → JD adjustment → như **UC4**.

---

## 6. Projects

Quy tắc đầy đủ: `projects.md` (bước 6).

| Đầu vào | Có sinh section? |
|---|---|
| Form / CV có ít nhất 1 dự án có tên | Có |
| Không có dự án nào | **Không** — bỏ hẳn section (CV: nêu trong "Lưu ý" của tóm tắt) |

**Chọn dự án** (Q8): 1–2 dự án, chọn sau khi có JD. Không JD: ưu tiên gần đây, quy mô lớn, mô tả rõ. Có JD: ưu tiên dự án khớp JD. CV có > 2 dự án → form 1 câu cho member chọn, 2 dự án đề xuất đứng đầu.

**Form dự án** — mỗi dự án một form, tối đa 4 câu, chỉ hỏi field chưa đạt:
1. **Vai trò trong dự án** (multiSelect): lựa chọn lấy từ dòng mô tả công việc, tính năng, giai đoạn được tick trong CV.
2. **Mô tả**: chưa đủ sản phẩm / người dùng / chức năng chính → câu hỏi nêu ý còn thiếu kèm khung gợi ý; lựa chọn `Dùng mô tả viết từ CV (Đề xuất)` · `Để trống, mình điền sau`, bổ sung gõ ở Other.
3. **Tech Stack** (multiSelect): công nghệ nhắc trong mô tả nhưng chưa có trong stack (đề xuất), skill của member thường đi cùng stack này, `Không, stack như CV là đủ`.
4. **Thời gian / Vị trí**: mốc và thời lượng lệch nhau, hoặc thiếu vị trí.

Ví dụ (dự án giả định):

```
### Project 1 — Website thương mại điện tử đồ gia dụng tại Nhật
**Thời gian:** 10 tháng (02/2025 – 12/2025)
**Vị trí:** Frontend Developer
**Team size:** 5 người
**Mô tả:** Website thương mại điện tử bán đồ gia dụng cho khách hàng tại Nhật. Người dùng tìm kiếm sản phẩm, đặt hàng và theo dõi đơn hàng trên cùng một hệ thống.
**Vai trò trong dự án:**
- Dựng màn tìm kiếm và lọc sản phẩm
- Làm giỏ hàng và luồng thanh toán
- Tham gia basic design

**Tech Stack:** NuxtJS, Pinia, Tailwind CSS
```

- **Mô tả** rà theo checklist `projects.md` §6: đủ sản phẩm / người dùng / chức năng chính, 2–3 câu (~30–60 từ), không kể việc member làm, không lặp stack / thời gian / team size, không phóng đại.
- **Vai trò trong dự án** chỉ gồm việc member làm (Q16), 2–5 dòng mở đầu bằng động từ; không tự suy.
- **Vị trí** thiếu → hỏi ở form dự án; bỏ qua → placeholder, không tự lấy role tổng (Q9).
- **Team size** chỉ ghi khi input / CV có; không có thì bỏ dòng.
- **Tiêu đề:** tiêu đề mô tả `[Loại sản phẩm] [lĩnh vực / người dùng]`, không tên thật của dự án (ShopNow), sản phẩm hay khách; khối nhắc ghép tiêu đề với tên thật cho member. Mô tả và Vai trò trong dự án cũng không nhắc tên.
- **Ngôn ngữ:** nội dung theo ngôn ngữ output, giữ nguyên tên công nghệ. Nhãn theo Q11.

---

## 7. Lưu file khi đã tồn tại

Quy tắc đầy đủ: `output.md` §4.
1. Không trùng tên → lưu luôn, không hỏi.
2. Trùng tên → in bio trước, rồi form: `Tạo bản mới [tên]-v2.md (Đề xuất)` · `Ghi đè file cũ`. Hậu tố lấy số nhỏ nhất chưa dùng (file gốc là v1).
3. In `Đã lưu: [tên file]` / `Đã ghi đè: [tên file]`.

Bản en / ja member yêu cầu thêm: tên theo cùng hậu tố với bản đầu (`...-en-[ngày]-v2.md`); trùng → hỏi như bước 2.

---

## 8. Khối nhắc sau khi lưu

In 1 khối duy nhất (không phải câu hỏi) nếu có ít nhất một mục:

```
⚠ File short-bio-nguyen-van-a-2026-10-21.md cần kiểm tra trước khi gửi khách:
- Header: Ngày sinh
- Project 1 — LabPortal: Thời gian, Vai trò trong dự án
- Short Bio (suy luận): "quản lý kho y tế" suy từ tên dự án MediVault
- Thêm theo JD (chưa có trong profile): AWS (2 năm), Docker — chuẩn bị nếu khách hỏi
- Điều chỉnh theo JD: tổng số năm 4 → 5 năm; Vue → React
- Chưa thể hiện (yêu cầu Senior Backend): review code cho team — bổ sung nếu đã làm
Bổ sung trực tiếp vào file trước khi gửi khách hàng.
```

Không có gì để nhắc → không in. Xong là kết thúc — không hỏi tạo bản en / ja.

---

## 9. Quy tắc chung cho mọi use case

- Hỏi bằng form có lựa chọn đề xuất; mọi thông tin cần hỏi đều hiện trong form, kể cả field gõ tay (họ tên, email, tech stack). Chỉ hỏi bằng dòng chữ cho Câu 1, nội dung JD, mô tả dự án, hoặc field bắt buộc member chọn `Gửi ở tin nhắn sau`. Không có `AskUserQuestion` → in danh sách đánh số.
- Tự vấn **tối đa 1 form** mỗi lượt chạy; bổ sung dự án tối đa 1 lần. Mục bỏ qua → placeholder + khối nhắc, không hỏi lại.
- **Short Bio:** 2–3 câu mỗi đoạn, không bullet, ~110–160 từ (chi tiết) / ~80–120 từ (sơ sài); không đại từ, không tên member, không tên dự án, không câu bị động; luôn qua humanizer; không bịa (JD chỉ dùng để chọn và bổ sung skill, không tạo dự án).
- Toàn bộ output theo ngôn ngữ output, kể cả nội dung lấy từ CV ở ngôn ngữ khác.
- Không dùng học vấn, lương, bậc lương / level nội bộ. Ngoại ngữ, chứng chỉ chuyên môn có trong input / CV thì đưa vào header (Q24, Q25).

---

## 10. Xử lý ngoại lệ

| Tình huống | Áp dụng | Xử lý |
|---|---|---|
| Thiếu field bắt buộc | Tất cả | Hỏi field thiếu trong form tự vấn (field gõ tay gộp 1 câu, ưu tiên cao nhất), merge, validate lại; chưa đủ thì không đi tiếp |
| CV không đọc được (404 / private / file hỏng) | UC5–8 | Báo lý do theo bảng lỗi `collect-info.md` §2, gợi ý cách khác; không đoán |
| CV dạng ảnh / PDF scan | UC5–8 | Đọc bằng vision (Q5); vẫn in tóm tắt để member sửa |
| CV có thời gian dự án mâu thuẫn | UC5–8 | Dùng mốc tháng/năm, nêu trong "Lưu ý" |
| Role chung chung / CV không ghi chức danh | Tất cả | Suy từ stack; có thể xác nhận trong form tự vấn |
| Role lệch stack | Tất cả | Form: đổi role (đề xuất) hay giữ |
| Role member ngoài 5 role hỗ trợ | Tất cả | Báo không hỗ trợ; form chọn role gần nhất hoặc dừng |
| Role JD ngoài 5 role hỗ trợ | Có JD | Form: tạo bio không theo JD (đề xuất) hay dừng (Q7) |
| JD là đường dẫn file không tồn tại / link không đọc được | Có JD | Báo lỗi, gợi ý paste nội dung, hỏi lại câu JD (Q6) |
| Nội dung đưa vào câu JD giống CV hơn JD | Có JD | Form: `JD khách hàng` hay `CV của tôi` — chọn CV → quay lại bước lấy thông tin |
| Câu trả lời không hợp lệ | Tất cả | Nhắc lựa chọn hợp lệ, hỏi lại |

---

## 11. Quyết định đã chốt

| # | Vấn đề | Quyết định |
|---|---|---|
| Q1 | Bio sơ sài có giữ 3 đoạn không | **2 đoạn.** Không có dự án thì đoạn 3 dễ thành câu chung chung hoặc bịa |
| Q2 | Member chỉ ghi tổng số năm, không ghi năm từng skill | Suy từ thời gian dự án, không có thì hỏi ở tự vấn. Vẫn không có: framework chính của role ghi bằng tổng số năm; skill chính khác để `_… năm/tháng_` cho member điền |
| Q3 | Có JD thì có hỏi mức match không | Luôn hỏi (form có đề xuất), trừ khi member đã nói sẵn — mức match quyết định số năm ghi trong bio |
| Q4 | Có nhận flag (`--cv`, `--jd`...) không | **Không.** Nội dung gõ kèm lệnh = câu trả lời Câu 1; output chỉ có file bio |
| Q5 | CV dạng ảnh hoặc PDF scan | Đọc bằng vision; vẫn in tóm tắt để member sửa |
| Q6 | JD là link | Đọc giống link CV (cùng cách xử lý lỗi) |
| Q7 | Role JD nằm ngoài 5 role hỗ trợ | Báo không hỗ trợ, cho chạy tiếp không JD |
| Q8 | Số dự án tối đa trong phần Projects | **1 đến 2** |
| Q9 | Thiếu vị trí trong dự án | Hỏi ở form dự án (bước 6) với lựa chọn đề xuất; bỏ qua → placeholder |
| Q10 | Có JD: Tech Stack trong phần Projects có thay theo JD không | **Không thay.** Chỉ thêm công nghệ member chọn ở form dự án |
| Q11 | Nhãn phần Projects (heading `## Projects` ở mọi ngôn ngữ) | vi: Thời gian, Vị trí, Team size, Mô tả, Vai trò trong dự án, Tech Stack · en: Duration, Position, Team size, Description, Responsibilities, Tech Stack · ja: 期間, ポジション, チーム規模, 概要, 担当業務, 技術スタック |
| Q12 | JD ghi số năm cho một skill cụ thể (VD "3 năm AWS") | Mức 1 / 2: thêm hoặc nâng, số năm = N / 80% × N (≤ tổng số năm); mức 3: không thêm. Skill này được ghi số năm ở Core Skills dù không phải framework. Luôn liệt kê trong khối nhắc |
| Q13 | Suy role từ CV có cả FE lẫn BE | Fullstack chỉ khi cả hai phía là stack chính; không thì lấy phía chiếm ưu thế |
| Q14 | Domain Core Skills cho BE / FE / Fullstack | Có API Integration, Testing, UI/UX Design; chỉ in domain có skill |
| Q15 | Cách hỏi | **Form `AskUserQuestion` có lựa chọn đề xuất** thay cho hỏi tuần tự bằng text. Gom câu trong cùng bước; JD và mức match hỏi riêng |
| Q16 | Field "Tính năng chính" | Đổi thành **"Vai trò trong dự án"** (trước đó là "Tính năng đảm nhiệm") — việc cụ thể member làm, chọn nhiều từ lựa chọn gợi ý lấy từ CV; khách sẽ hỏi lại |
| Q17 | Core Skills | Nhãn domain in đậm; **skill chính luôn có số năm** (framework / platform, ngôn ngữ, database, cloud chính; skill JD ghi số năm), skill phụ đi kèm chỉ ghi tên; chỉ ghi tên công nghệ / công cụ cụ thể (không ghi "Caching", "Unit test") |
| Q18 | Skill nice to have trong JD mà member chưa có | Mức 1 / 2: chỉ Core Skills + khối nhắc, không viết vào bio; mức 3: không thêm |
| Q19 | Cross-role | Số năm framework mới = N / 80% × N / placeholder, không lấy số năm framework role cũ; dự án role cũ chỉ nhắc trong bio như kinh nghiệm nghiệp vụ / domain |
| Q20 | Hoàn toàn khớp có giữ Git / Docker / Jira không | **Không**, nếu JD không nhắc và không phải companion của mốc số năm |
| Q21 | Checklist nội dung | Theo role × cấp: Junior < 3, Middle 3–< 5, Senior ≥ 5 năm (tính từ số năm thực tế). Chỉ hỏi yêu cầu của đúng cấp, tối đa 3 mục trong 1 câu multiSelect; việc member xác nhận chỉ vào bio. JD nâng cấp → yêu cầu cấp mới chỉ ghi khối nhắc |
| Q22 | Checklist khi cross-role và JD đã biết ở bước 2 | Chỉ hỏi việc dùng chung giữa hai role; chọn 3 trong 5 theo thứ tự: thống nhất API → review code → mentor → viết test → requirement / estimate (bỏ mục đã có bằng chứng; JD nhấn mạnh mục nào thì đưa lên) |
| Q23 | Email | **Bắt buộc** (field thứ 5) — không bao giờ là placeholder |
| Q24 | Ngoại ngữ (JLPT, TOEIC, IELTS...) | **Đưa vào nếu input / CV có**: dòng `Ngoại ngữ` ở header, ghi đúng chứng chỉ / mức member ghi; không hỏi ở tự vấn, không để placeholder. JD yêu cầu ngoại ngữ: member có → nhắc trong bio; chưa có hoặc thấp hơn → khối nhắc. Không nâng theo JD |
| Q25 | Chứng chỉ chuyên môn (AWS Certified, PMP, ISTQB...) | Xử lý như ngoại ngữ (Q24): có trong input / CV → dòng `Chứng chỉ` ở header, ghi đúng tên và năm đạt; không hỏi, không thêm theo JD. Học vấn / bằng đại học vẫn bỏ qua |
| Q24 | Field bắt buộc chỉ gõ tay được (họ tên, email, tech stack) | Luôn hiện trong form tự vấn: gộp 1 câu, gõ ở ô Other, ưu tiên cao nhất; không đề xuất giá trị. Riêng email thiếu mà đã có họ tên → câu riêng đề xuất `tên.họ@tomosia.com` (VD `thien.tran@tomosia.com`), member chọn hoặc gõ email khác. Chỉ hỏi bằng dòng chữ khi member chọn `Gửi ở tin nhắn sau` |
| Q25 | Số năm framework / ngôn ngữ khi JD ghi mốc riêng (VD "6 năm PHP / Laravel") | `max(thực tế, mốc theo mức của skill đó)`, không nâng theo tổng; mốc gộp áp cho mọi skill trong nhóm. Chỉ framework chính JD không ghi mốc riêng mới nâng theo tổng mới. Tránh Vue 4 → 8 khi JD đòi 7, hay Laravel 7 nhưng PHP 6 |
