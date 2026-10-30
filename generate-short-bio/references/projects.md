# Dự án (bước 6)

Mục lục: §1 Khi nào chạy · §2 Chọn dự án · §3 Rà từng dự án · §4 Form dự án · §5 Viết phần Projects · §6 Checklist Mô tả

Phần Projects là chỗ khách hỏi sâu nhất trong buổi phỏng vấn: "dự án này làm gì, anh/chị làm phần nào, dùng công nghệ gì?". CV skill sheet thường chỉ ghi giai đoạn (Basic design, Implementation) hoặc mô tả sản phẩm, nên nếu chép thẳng thì phần này mỏng và member khó nói tiếp. Bước này chọn 1–2 dự án, rà chỗ còn mỏng, rồi hỏi member bằng form có lựa chọn gợi ý sẵn.

---

## §1 — Khi nào chạy

- Input / CV có ít nhất 1 dự án có tên → chạy sau bước 5 (hoặc sau bước 4 khi không có JD), trước dòng `Xác nhận:`.
- Không có dự án → bỏ bước, file không có phần Projects.
- Dự án chỉ có tên (CV sơ sài, member không bổ sung) vẫn tính là có dự án: **vẫn có phần Projects**, field thiếu để placeholder. Form chỉ hỏi câu có lựa chọn suy được (VD Vị trí); không có gì để gợi ý thì không mở form.
- Thông tin dự án member đã gõ đủ ở Câu 1 hoặc ở tin nhắn bổ sung (bước 2) → không hỏi lại phần đã có; dự án đủ hết → không có form.

---

## §2 — Chọn dự án

Chọn tối đa 2 dự án:
- **Có JD:** ưu tiên dự án khớp JD nhất (stack, domain, loại việc JD yêu cầu). Cross-role: ưu tiên dự án gần role JD nhất; vẫn giữ stack và vị trí thật.
- **Không JD:** ưu tiên gần đây, quy mô lớn, có kết quả, mô tả rõ.
- Hai dự án nên bổ sung cho nhau (khác domain hoặc khác phía stack) thay vì giống nhau.

CV có ≤ 2 dự án → dùng hết, không hỏi. Có > 2 dự án → câu đầu của form dự án (§4, câu A).

---

## §3 — Rà từng dự án

Với mỗi dự án đã chọn, đối chiếu từng field với tiêu chí dưới. Field chưa đạt → đưa vào form (§4) theo thứ tự ưu tiên.

| Field | Đạt khi | Chưa đạt thường gặp |
|---|---|---|
| **Mô tả** | Đạt nhóm A của checklist §6: (1) sản phẩm là gì, (2) cho ai dùng / thị trường nào, (3) chức năng hoặc giá trị chính. Ý (4) quy mô / loại dự án là điểm cộng | CV chỉ ghi việc member làm ("Independent backend development..."), không nói sản phẩm là gì; hoặc 1 câu chung chung ("Website e-commerce") |
| **Vai trò trong dự án** | Liệt kê việc / tính năng cụ thể member làm, mở đầu bằng động từ | CV chỉ tick giai đoạn, hoặc chỉ mô tả tính năng của sản phẩm, không rõ phần nào member làm |
| **Tech Stack** | Đủ các lớp thật sự dùng: framework, database, hạ tầng / dịch vụ ngoài | CV chỉ ghi "PHP (Laravel)" trong khi mô tả nhắc Stripe, GraphQL, CSV; hoặc thiếu database |
| **Thời gian** | Mốc tháng/năm khớp thời lượng CV ghi (lệch ≤ 1 tháng) | Mốc và thời lượng lệch nhau |
| **Vị trí** | CV ghi chức danh trong dự án | Không ghi |
| **Team size** | CV ghi số người | Không ghi → bỏ dòng, không hỏi |

---

## §4 — Form dự án

**Mỗi dự án một form, tối đa 4 câu**, lần lượt dự án 1 rồi dự án 2 (tối đa 2 form, cộng câu A nếu cần). Không gom câu dự án vào form bước khác. `header` ghi tên dự án rút gọn (≤ 12 ký tự). Câu trong form theo thứ tự ưu tiên dưới; câu không cần (field đã đạt) thì bỏ.

**Câu A — chọn dự án** (chỉ khi > 2 dự án; form riêng 1 câu, trước các form dự án), multiSelect, header `Dự án`:
`Phần Projects sẽ giới thiệu 1–2 dự án. Bạn muốn đưa dự án nào vào?` — tối đa 4 lựa chọn: 2 dự án chọn theo §2 kèm `(Đề xuất)` và `description` nêu lý do (VD "khớp Laravel + thanh toán trong JD"), cộng 1–2 dự án kế tiếp. Member chọn quá 2 → lấy 2 dự án đầu theo thứ tự §2.

**Câu 1 — Vai trò trong dự án** (luôn hỏi khi field chưa đạt), **multiSelect**:
`Ở dự án [X], bạn đã làm những việc nào? Chọn hết phần bạn trực tiếp làm, việc khác gõ thêm ở Other.`
- Lựa chọn lấy từ CV, viết thành việc cụ thể mở đầu bằng động từ: dòng mô tả công việc của dự án, tính năng nêu trong mô tả, giai đoạn được tick (gộp giai đoạn vào 1 lựa chọn, VD `Basic design và thiết kế database`). Tối đa 4.
- Lựa chọn có căn cứ rõ là member làm (CV ghi "developed", "implemented", giai đoạn được tick) → `(Đề xuất)`. Tính năng chỉ là của sản phẩm → không `(Đề xuất)`.
- Không đề xuất việc CV không nhắc.

**Câu 2 — Mô tả** (khi thiếu ý A1–A3 của §6):
`Mô tả dự án [X] còn thiếu [các ý thiếu, VD "sản phẩm là gì và cho ai dùng"]. Bạn gõ bổ sung ở Other, VD: "[mẫu câu theo đúng ý thiếu]".`
- `Dùng mô tả viết từ CV (Đề xuất)` — `description` là bản mô tả skill viết từ CV (≤ 2 câu), hoặc dùng `preview` để hiện bản đó.
- `Để trống, mình điền sau`.
- Mẫu câu trong câu hỏi là khung gợi ý có chỗ trống (VD `"App ghi chép ___ cho ___, có ___"`), không điền sẵn chi tiết CV không có.

**Câu 3 — Tech Stack** (khi có ứng viên bổ sung), **multiSelect**:
`Tech stack của [X] trong CV là [stack]. Dự án có dùng thêm công nghệ nào dưới đây không?`
- Ứng viên, tối đa 3: công nghệ nhắc trong mô tả dự án nhưng chưa có trong stack → `(Đề xuất)`; skill của member thường đi cùng stack này (database, Docker, CI, framework FE...) → không `(Đề xuất)`, `description` ghi "có trong Core Skills của bạn".
- Lựa chọn cuối: `Không, stack như CV là đủ`.
- Chỉ thêm vào Tech Stack công nghệ member chọn hoặc gõ.

**Câu 4 — Thời gian / Vị trí** (một câu, ưu tiên thời gian):
- Thời gian lệch: `CV ghi dự án [X] kéo dài [Y], nhưng mốc [từ – đến] là [Z]. Thời gian đúng là bao lâu?` · `[Z], theo mốc (Đề xuất)` · `[Y], theo CV ghi`.
- Vị trí thiếu: `Ở dự án [X], bạn giữ vị trí gì?` · đề xuất suy từ stack dự án (VD chỉ Laravel → `Backend Developer`), role tổng, `Team Lead` nếu CV nhắc dẫn dắt.

Sau form:
- Không có câu nào cho dự án → không in form của dự án đó.
- Bỏ qua / không chọn → giữ dữ liệu CV; field còn thiếu → placeholder + khối nhắc.
- Việc member chọn ở Câu 1 được dùng làm bằng chứng cho Short Bio (năng lực, không tên dự án) và checklist role × cấp.

---

## §5 — Viết phần Projects

Heading section là `## Projects` ở mọi bản ngôn ngữ. Nhãn theo `output.md` §6.

```
## Projects

### Project 1 — [Tên dự án]
**Thời gian:** [X tháng | X năm Y tháng] ([MM/YYYY] – [MM/YYYY])
**Vị trí:** [Vị trí trong dự án]
**Team size:** [N người]   ← chỉ khi có
**Mô tả:** [2–3 câu]
**Vai trò trong dự án:**
- [Việc 1]
- [Việc 2]

**Tech Stack:** [Stack thật]
```

Luôn để 1 dòng trống giữa gạch đầu dòng cuối và `**Tech Stack:**`. Thiếu dòng trống, Markdown coi Tech Stack là phần tiếp của gạch đầu dòng cuối nên khi preview bị thụt vào trong.

| Field | Cách viết | Thiếu |
|---|---|---|
| Tên | Giữ tên gốc | Không có tên → không tính là dự án |
| Thời gian | Số tháng = (năm cuối − năm đầu) × 12 + (tháng cuối − tháng đầu), kèm mốc. Đang làm → tính tới ngày tạo file, thêm `(đang làm)` | Placeholder |
| Vị trí | Như CV hoặc member chọn; sửa lỗi chính tả rõ ràng (`Fulstack` → `Fullstack`) | Placeholder — không lấy role tổng |
| Team size | `N người` | Bỏ dòng |
| Mô tả | Viết theo khung và rà theo checklist §6 | Không có ý nào → placeholder; thiếu một phần → viết phần có, ý thiếu vào khối nhắc |
| Vai trò trong dự án | 2–5 gạch đầu dòng, mỗi dòng một việc cụ thể mở đầu bằng động từ, kèm kỹ thuật nếu input có (VD `Xử lý file CSV lớn bằng background job`). Giai đoạn gộp 1 dòng (`Tham gia basic design và thiết kế database`). Chỉ việc member làm | Placeholder — không tự suy |
| Tech Stack | Stack CV + công nghệ member chọn ở Câu 3. **Giữ stack thật kể cả khi có JD** | Placeholder |

Khách sẽ hỏi "phần này anh/chị làm thế nào?", nên dòng Vai trò trong dự án chỉ chứa việc member trả lời được.

---

## §6 — Checklist Mô tả

Mô tả trả lời câu khách hỏi đầu tiên về dự án: "đây là sản phẩm gì?". Quá sơ sài thì khách không hình dung được bối cảnh; quá dài thì lấn sang phần Vai trò và Tech Stack, khách đọc lướt sẽ bỏ qua. Viết xong mỗi Mô tả, rà đủ 4 nhóm dưới; mục nào chưa đạt thì sửa rồi mới lưu.

**Khung viết** (2–3 câu, chủ ngữ là sản phẩm):
1. `[Loại sản phẩm] [lĩnh vực] cho [người dùng / khách hàng, thị trường].`
2. `[1–3 chức năng chính của sản phẩm].`
3. Tùy chọn: `[quy mô / loại dự án / điểm đặc thù của sản phẩm].`

**A. Đủ ý bắt buộc** — thiếu ý nào → Câu 2 của form (§4); member bỏ qua → khối nhắc `Mô tả thiếu: [ý]`.
- [ ] A1. Sản phẩm là gì: loại hệ thống (web service, app mobile, SaaS B2B, hệ thống nội bộ...) và lĩnh vực.
- [ ] A2. Ai dùng: người dùng cuối hoặc loại doanh nghiệp, kèm thị trường nếu input có (VD "doanh nghiệp Nhật").
- [ ] A3. Chức năng / giá trị chính: 1–3 chức năng cốt lõi của **sản phẩm**, không phải việc member làm.

**B. Điểm cộng** — chỉ khi input có, không hỏi thêm:
- [ ] B1. Quy mô: số người dùng, số cửa hàng / chi nhánh, khối lượng dữ liệu.
- [ ] B2. Loại dự án: phát triển mới, renewal, migrate, vận hành / bảo trì.
- [ ] B3. Điểm đặc thù của sản phẩm (realtime, xử lý dữ liệu lớn, tích hợp AI, thanh toán) khi đó là bản chất sản phẩm.

**C. Độ dài** — không sơ sài, không dài dòng:
- [ ] C1. 2–3 câu; bản vi ~30–60 từ, en ~25–50 words, ja ~60–120 文字.
- [ ] C2. Mỗi câu một ý chính, ≤ ~25 từ; liệt kê tối đa 3 chức năng.
- [ ] C3. Không chỉ là một cụm danh từ (VD chỉ "Website e-commerce") — dấu hiệu sơ sài.

**D. Không lấn sang chỗ khác, không bịa**:
- [ ] D1. Không kể việc member làm (thuộc `Vai trò trong dự án`), không động từ ngôi member ("phát triển", "phụ trách").
- [ ] D2. Không lặp Tech Stack, Thời gian, Team size, Vị trí. Chỉ nhắc công nghệ khi nó là bản chất sản phẩm (VD "chatbot AI").
- [ ] D3. Không tên công ty khách hàng trừ khi CV ghi và đã công khai; mặc định gọi theo loại (VD "một công ty influencer marketing Nhật Bản").
- [ ] D4. Không từ phóng đại / quảng cáo ("hiện đại", "mạnh mẽ", "hàng đầu", "tối ưu").
- [ ] D5. Mỗi ý truy được về CV hoặc câu trả lời của member; ý suy luận (VD người dùng suy từ tên dự án) → khối nhắc.

Ví dụ (dự án giả định):
- Sơ sài: `Hệ thống quản lý kho.` (thiếu A2, A3, C3)
- Dài dòng: `Hệ thống quản lý kho hiện đại được xây dựng bằng Laravel 8 và Vue.js 2 trong 2 năm 8 tháng với team 10 người, nơi đã phát triển API nhập xuất kho...` (D1, D2, D4)
- Đạt: `Hệ thống quản lý tồn kho cho một chuỗi bán lẻ 40 cửa hàng. Nhân viên nhập / xuất kho, quét barcode và xem báo cáo tồn kho hằng tháng.`

