# Thu thập thông tin (bước 1–3)

Mục lục: §1 Câu 1 · §2 Đọc CV · §3 Field bắt buộc · §4 Mức độ chi tiết · §5 Tự vấn · §6 Kiểm tra role

---

## §1 — Câu 1: thông tin member

**Lệnh gọi kèm nội dung** (VD `/generate-short-bio https://docs.google.com/...` hoặc `/generate-short-bio Nguyễn Văn A, Frontend, 3 năm, React`) → coi đó là câu trả lời Câu 1, không in form. Skill không nhận flag (`--cv`, `--jd`...).

**Không kèm nội dung** → in (đây là câu gõ tay duy nhất bắt buộc, vì không thể đoán trước nội dung):
```
Bạn gửi link hoặc đường dẫn file CV, hoặc nhập thông tin theo danh sách dưới đây:

Bắt buộc:
- Họ tên
- Email
- Role (Backend, Frontend, Fullstack, Mobile, QA)
- Số năm kinh nghiệm
- Tech stack (kèm số năm của các skill chính nếu có: framework, ngôn ngữ, database, cloud)

Tùy chọn:
- Ngày sinh
- Ngoại ngữ (chứng chỉ hoặc trình độ, VD JLPT N3, TOEIC 750, IELTS 6.5)
- Chứng chỉ chuyên môn (VD AWS Certified Solutions Architect – Associate, PMP, ISTQB)
- Domain đã làm (EC, logistics, HR, fintech...)
- Dự án nổi bật: tên, thời gian, vai trò, mô tả, tính năng đã đảm nhiệm, tech stack, kết quả
```

Câu trả lời là link (`http...`) hoặc đường dẫn file tồn tại → §2. Có cả link lẫn thông tin gõ tay → đọc CV, thông tin gõ tay ưu tiên khi trùng field. Chỉ gõ tay → §3.

---

## §2 — Đọc CV

### Lấy nội dung
- **Google Docs** (`docs.google.com/document/d/[ID]/...`) → WebFetch `https://docs.google.com/document/d/[ID]/export?format=txt`.
- **Google Sheets** (`docs.google.com/spreadsheets/d/[ID]/...`, kể cả Excel tải lên có `rtpof=true`) → `curl -fsSL` tải `https://docs.google.com/spreadsheets/d/[ID]/export?format=xlsx` vào thư mục tạm, đọc như XLSX.
- **Google Drive file** (`drive.google.com/file/d/[ID]/...` hoặc `open?id=[ID]`) → `curl -fsSL` tải `https://drive.google.com/uc?export=download&id=[ID]`.
- **URL PDF / DOCX / trang web khác** → WebFetch; trả về nhị phân hoặc trống → `curl -fsSL` vào thư mục tạm rồi đọc như file trên máy.
- **File trên máy:** PDF / txt / md → Read. DOCX → `pandoc -t plain`; không có pandoc → macOS `textutil -convert txt -stdout`, Linux/WSL `unzip -p [file] word/document.xml | sed -e 's/<\/w:p>/\n/g' -e 's/<[^>]*>//g'`.
- **XLSX** (skill sheet): đọc mọi sheet. Có `openpyxl` thì dùng; không có → `python3` + `zipfile` đọc `xl/sharedStrings.xml` và `xl/worksheets/*.xml` (cell `t="s"` là index vào sharedStrings). Ngày dạng số (VD `36358`) là Excel serial date → `1899-12-30 + N ngày`.
- **Ảnh / PDF scan** → Read (xem ảnh). Thông tin vẫn hiện trong tóm tắt để member sửa nếu đọc sai.
- Text PDF bị ngắt giữa từ (VD `A / WS`) → nối lại trước khi trích.

### Không đọc được — báo lỗi, không đoán
| Dấu hiệu | Lý do in ra | Gợi ý |
|---|---|---|
| 404 / "Page not found" | `không tìm thấy tài liệu` | `Vui lòng kiểm tra lại link` |
| 401 / 403 / redirect tới trang đăng nhập (`accounts.google.com`, LinkedIn...) / Google export trả HTML thay vì text/XLSX | `cần đăng nhập hoặc chưa chia sẻ` | `Vui lòng bật chia sẻ "Anyone with the link"` |
| File hỏng, không trích được kể cả khi xem như ảnh | `không đọc được nội dung file` | — |

```
Không đọc được CV từ: [link member đưa] ([lý do])
[gợi ý]. Hoặc gửi file CV trên máy, hoặc nhập thông tin trực tiếp:
```
kèm danh sách field Câu 1 (từ `Bắt buộc:`). Câu trả lời tiếp theo xử lý như câu trả lời Câu 1.

### Trích xuất
Chỉ lấy các field của Câu 1; bỏ qua phần *Ngoài phạm vi* (học vấn, bằng đại học, lương...) và giới tính, địa chỉ, SĐT, ảnh, sở thích.
- **Số năm kinh nghiệm:** lấy số CV ghi rõ; chỉ có năm bắt đầu hoặc không ghi → tính từ công việc IT đầu tiên tới hiện tại, làm tròn xuống, không cộng chồng giai đoạn trùng.
- **Ngoại ngữ:** ghi đúng chứng chỉ / mức CV ghi (JLPT N2, TOEIC 800, IELTS 6.5, "tiếng Nhật giao tiếp"), kèm năm đạt nếu có. Không suy, không quy đổi giữa các thang.
- **Chứng chỉ chuyên môn:** ghi đúng tên chứng chỉ CV ghi, kèm năm đạt nếu có (VD `AWS Certified Developer – Associate (2024)`). Không suy từ skill, không gộp hay đổi tên.
- **Role:** chức danh member tự ghi ở đầu CV → chức danh công việc gần nhất → suy từ stack (ghi chú trong tóm tắt).
- **Tech stack:** gộp mục Skills với stack các dự án, bỏ trùng.
- **Số năm skill chính** (framework, ngôn ngữ, database, cloud chính — `output.md` §2): số CV ghi; không có → suy từ khoảng thời gian các dự án dùng skill đó.
- **Dự án:** tên, thời gian, vai trò, mô tả, tính năng member đảm nhiệm, tech stack. Thời gian ưu tiên mốc tháng/năm; số tháng = (năm cuối − năm đầu) × 12 + (tháng cuối − tháng đầu), VD `02/2025 – 12/2025` = 10 tháng. Lệch quá 1 tháng so với thời lượng CV ghi riêng → dùng mốc tháng/năm, nêu trong Lưu ý.
- **Vai trò trong dự án:** chỉ khi CV ghi rõ chức danh trong dự án (VD "Frontend Developer", "Team Lead"). Số người trong team hay các giai đoạn tham gia không phải vai trò.
- **Tính năng đảm nhiệm:** tính năng CV ghi là member làm / phụ trách. CV chỉ mô tả tính năng của sản phẩm, không rõ phần nào member làm → đưa vào tự vấn (§5).

### Tóm tắt — in rồi đi tiếp ngay
```
Thông tin đọc từ CV:
- Tên: [...]
- Email: [... | chưa có]
- Role: [...]  [(CV không ghi chức danh — suy từ stack) nếu suy ra]
- Số năm kinh nghiệm: [...]
- Tech stack: [...]
- Ngày sinh: [... | chưa có]
- Ngoại ngữ: [... | chưa có]
- Chứng chỉ: [... | chưa có]
- Domain: [... | chưa có]
- Dự án: [tên 1] ([thời gian]), [tên 2] ([thời gian])... | chưa có

Lưu ý:
- [chỉ hiện khi có vấn đề: thời gian mâu thuẫn, dự án thiếu mô tả / vai trò, CV không có dự án...]
```
Không hỏi `ok`. Ngay trong cùng lượt: §3 (nếu thiếu field bắt buộc) → §5 tự vấn (form). Member có thể sửa tóm tắt qua ô "Other" của form hoặc nhắn kèm — merge rồi đánh giá lại §4.

---

## §3 — Field bắt buộc (5 field)

| Field | Nhận diện | Cách hỏi khi thiếu |
|---|---|---|
| Họ tên | Tên riêng đầy đủ | Câu gõ ở ô Other (dưới) |
| Email | Có `@` | Câu gõ ở ô Other (dưới) |
| Role | Backend / Frontend / Fullstack / Mobile / QA | Form — đề xuất role suy từ stack (bảng §6) |
| Số năm kinh nghiệm | Số hoặc khoảng ("3 năm", "3-4 năm") | Form — đề xuất số suy từ CV / dự án nếu có; không có dữ liệu → các mốc `1-2 năm`, `3-4 năm`, `5-6 năm`, `7+ năm`, member chọn hoặc gõ số chính xác |
| Tech stack | Ít nhất 1 ngôn ngữ hoặc framework | Câu gõ ở ô Other (dưới) |

**Mọi field bắt buộc còn thiếu đều nằm trong form tự vấn §5**, kể cả field chỉ gõ tay được — không hỏi bằng dòng chữ riêng trước hay sau form. Member nhìn một form là thấy hết những gì còn thiếu; hỏi rải rác khiến form trông như bỏ sót, và member dễ trả lời xong form rồi bỏ đi.
- **Field gõ tay gộp vào 1 câu** để giữ suất cho các câu khác: câu hỏi liệt kê đúng các field thiếu, VD `Bạn cho biết họ tên và email nhé. Gõ vào ô Other theo dạng "Họ tên, email".` (header `Bắt buộc`). Lựa chọn: `Gõ vào ô Other` · `Gửi ở tin nhắn sau` (description: bio chỉ được tạo sau khi có đủ). Không đề xuất giá trị (VD email đoán theo tên) — đó là bịa.
- Field có lựa chọn (role, số năm) → mỗi field một câu như bảng trên.
- Các câu bắt buộc chiếm suất trước mọi câu không bắt buộc.
- Member chọn `Gửi ở tin nhắn sau` hoặc chọn `Gõ vào ô Other` mà để trống → sau form in đúng 1 dòng `Bạn gửi giúp [các field còn thiếu] nhé:`. Đây là trường hợp duy nhất hỏi field bắt buộc ngoài form.

Không in lại form Câu 1, không nhắc lại thông tin đã có. Merge, validate lại; thiếu field bắt buộc thì không đi tiếp.

Khoảng ("3-4 năm") → tính bằng cận trên.

---

## §4 — Mức độ chi tiết

| Mức | Tiêu chí |
|---|---|
| **Chi tiết** | Có ≥ 1 dự án kèm mô tả (sản phẩm làm gì, vai trò hoặc stack dùng). Kết quả, số liệu là điểm cộng. |
| **Sơ sài** | Chỉ có field bắt buộc (± ngày sinh, domain), hoặc mọi dự án chỉ có tên. |

Quyết định số đoạn bio (`write-bio.md`) và việc có Project Examples (`output.md`). Đánh giá lại sau mỗi lần member bổ sung.

---

## §5 — Tự vấn: rà chỗ thiếu rồi hỏi bằng form

Sau khi có đủ thông tin thô, tự rà xem file bio sẽ còn chỗ nào trống, mơ hồ, hoặc đang phải đoán. Mục tiêu: member chỉ cần **chọn** để lấp, thay vì phát hiện placeholder sau khi file đã lưu.

**Danh sách rà, theo thứ tự ưu tiên** (lấy từ trên xuống, tối đa 4 câu mỗi form):

| # | Chỗ thiếu / mơ hồ | Câu hỏi gợi ý | Lựa chọn đề xuất lấy từ đâu |
|---|---|---|---|
| 1 | Field bắt buộc còn thiếu: 1 câu gộp các field gõ tay (họ tên, email, tech stack) + mỗi field chọn (role, số năm) 1 câu | xem §3 | stack, mốc thời gian CV; field gõ tay không đề xuất giá trị |
| 2 | Thông tin sơ sài: không có dự án / dự án chỉ có tên | `Bạn có muốn thêm 1–2 dự án không? Có dự án thì bio đủ 3 đoạn và có phần Project Examples.` | `Có, nhập ở tin nhắn sau` · `Không cần, bio 2 đoạn là được` |
| 2b | Yêu cầu nội dung của role × cấp chưa có bằng chứng (VD Senior Backend chưa thấy review code, thiết kế) | 1 câu **multiSelect** theo `checklist.md` §1 | tối đa 3 yêu cầu còn thiếu + `Chưa làm việc nào trong số này` |
| 3 | Số năm skill chính chưa rõ, không suy được từ dự án | Framework chính: `Bạn đã dùng [Laravel] được bao lâu?` · Skill chính khác: 1 câu gộp `Bạn đã dùng [PHP, MySQL] được bao lâu? Gõ theo dạng "PHP 5, MySQL 4".` | Framework: `[X] năm, bằng tổng kinh nghiệm` · thời gian các dự án dùng nó · `Chưa chắc, để trống`. Câu gộp: `Gõ vào ô Other` · `Để trống, mình điền sau` |
| 4 | Tính năng member đảm nhiệm chưa rõ (CV chỉ mô tả sản phẩm) | `Ở dự án [Dự án], bạn trực tiếp làm những tính năng nào?` — **multiSelect** | các tính năng CV liệt kê (tối đa 4) |
| 5 | Vai trò trong dự án thiếu | `Ở dự án [Dự án], bạn giữ vai trò gì?` | suy từ stack dự án (VD chỉ Laravel → `Backend Developer`), role tổng của member, `Team Lead` nếu CV nhắc dẫn dắt |
| 6 | Domain chưa có nhưng suy được | `Các dự án của bạn chủ yếu thuộc lĩnh vực nào?` | suy từ tên / mô tả dự án (VD "BillCheck — kế toán" → `Kế toán / fintech`) |
| 7 | Ý đang phải suy luận (role suy từ stack, số năm tính từ mốc) | `Có phải [ý suy luận] không?` | `Đúng vậy (Đề xuất)` · lựa chọn khác hợp lý |
| 8 | Ngày sinh thiếu | `Bạn có muốn ghi ngày sinh vào hồ sơ không?` | `Để trống, mình điền sau` · `Gõ vào ô Other` (DD/MM/YYYY) |

Cách làm:
- **Một form, tối đa 4 câu**, gom các mục ưu tiên cao nhất. Mục còn lại → placeholder + khối nhắc. Không mở form thứ hai cho phần không bắt buộc — hỏi dồn nhiều lượt làm member mệt và bỏ ngang.
- Mỗi câu có lựa chọn `Bỏ qua` khi field không bắt buộc. Có đáp án suy ra đáng tin → đặt đầu, nhãn kèm `(Đề xuất)`, `description` nêu căn cứ.
- **Chỉ đề xuất điều suy được từ dữ liệu.** Không tạo lựa chọn chứa tính năng, domain hay kết quả mà input không gợi ra — lựa chọn đề xuất cũng là một dạng bịa nếu không có căn cứ.
- Member chọn `Có, nhập ở tin nhắn sau` (bổ sung dự án) → in 1 dòng: `Bạn nhập 1–2 dự án nhé: tên, thời gian, vai trò, mô tả, tính năng bạn làm và tech stack.` — đây là lần hỏi bổ sung duy nhất; xong đánh giá lại §4, không hỏi thêm dù vẫn sơ sài.
- Không còn chỗ thiếu → bỏ qua §5, đi tiếp.
- Kiểm tra role (§6) phát hiện được ngay từ dữ liệu → có thể đặt làm câu cuối của cùng form nếu còn suất, để giảm một lượt hỏi.
- **Không đưa câu JD hay mức match vào form này** — chúng thuộc bước 4–5 (`jd-match.md`), hỏi sau khi profile đã chốt.

---

## §6 — Kiểm tra role

Role member nhập là nguồn chính; stack chỉ để kiểm tra chéo. Chỉ hỏi khi rơi vào các trường hợp dưới; khớp thì không hỏi.

**Nhận diện role từ stack:**
- **Backend** — Ruby on Rails, PHP, Java, Python, Node.js, Go, Spring Boot, Laravel...
- **Frontend** — Vue.js, React.js, Angular, Next.js (không có BE rõ ràng)
- **Mobile** — iOS, Android, Flutter, React Native, Swift, Kotlin, Dart...
- **QA** — QA, Tester, QC, Selenium, Appium, Manual, Automation, JMeter...
- **Fullstack** — cả BE lẫn FE/Mobile đều là stack chính (mỗi phía ≥ nửa tổng số năm, hoặc có ở phần lớn dự án). Một phía chỉ xuất hiện ở 1 dự án / ít năm → role theo phía chiếm ưu thế, skill phía phụ vẫn ghi ở Core Skills.

**Các trường hợp:**
- Role chung chung ("Software Engineer", "Web Developer") hoặc CV không ghi chức danh → suy từ stack, không hỏi riêng (đã hiện trong tóm tắt; có thể xác nhận ở mục 7 của §5).
- **Role lệch stack** (VD ghi "Fullstack" nhưng chỉ có Laravel) → form: `Bạn ghi role là [X], nhưng stack chủ yếu là [Y]. Bạn muốn ghi role nào?` · `Đổi thành [Z] (Đề xuất)` — description nêu căn cứ · `Giữ [X], gõ thêm stack còn thiếu ở Other`. Không tự đổi.
- **Role ngoài 5 loại** (DevOps, BrSE, PM, Data/AI, Designer...) → báo skill hỗ trợ Backend / Frontend / Fullstack / Mobile / QA; form gồm tối đa 3 role gần nhất với stack (role gần nhất ghi `(Đề xuất)`) + `Dừng`. Không map ngầm.
