# Ví dụ output

Một lần chạy với **nhân vật giả lập**: Backend 6 năm, nhập tay, có 1 dự án, không có JD.

## Lệnh gọi

```text
/generate-short-bio Nguyễn Văn B, b.nguyen@example.com, Backend, 6 năm, PHP (6 năm), Laravel (6 năm), MySQL (5 năm), Redis, Docker.
Dự án: Kintai Cloud — hệ thống chấm công và tính lương cho doanh nghiệp Nhật, 04/2022 – 03/2025, Backend Developer,
team 8 người, mình làm API chấm công, module tính lương theo ca và batch xuất báo cáo tháng, stack Laravel, MySQL, Redis.
Không có JD.
```

Skill hỏi thêm một form tự vấn (các việc của Level Senior Backend, ngày sinh), bỏ qua câu JD vì đã có câu trả lời. Ở bước Dự án, Kintai Cloud đã đủ mô tả, vị trí và việc member làm, nên form dự án chỉ có 1 câu: dự án có dùng thêm Docker (có trong Core Skills) không. Member chọn `Không, stack như CV là đủ`, rồi skill sinh bio.

## File `short-bio-nguyen-van-b-2026-10-27.md`

```markdown
# Nguyễn Văn B

**Vị trí:** Backend Developer
**Email:** b.nguyen@example.com
**Ngày sinh:** _(chưa có — vui lòng bổ sung)_

---

## Short Bio

Backend Developer với 6 năm làm PHP và Laravel, chuyên về hệ thống nghiệp vụ nhân sự cho doanh nghiệp Nhật Bản, đặc biệt là chấm công và tính lương. Làm việc hằng ngày với MySQL, Redis và môi trường Docker.

Trong mảng này, đã xây dựng API chấm công, module tính lương theo từng loại ca làm việc và các batch tổng hợp dữ liệu để xuất báo cáo tháng trên nền Laravel. Dữ liệu chấm công được lưu và truy vấn trên MySQL, kết hợp Redis ở tầng ứng dụng, còn các dịch vụ chạy trong Docker.

Gắn bó gần 3 năm với một hệ thống chấm công – tính lương trong team 8 người, phụ trách phía backend từ API tới batch xử lý cuối tháng. Nhờ vậy nắm chắc nghiệp vụ ca làm việc và kỳ lương của doanh nghiệp Nhật, nơi số liệu chấm công và báo cáo lương phải khớp nhau ở mọi kỳ.

---

## Core Skills

**Backend/Framework:** Laravel (6 năm), PHP (6 năm)
**Database:** MySQL (5 năm)
**Caching & Queue:** Redis
**DevOps/CI/CD:** Docker

---

## Projects

### Project 1 — Hệ thống chấm công và tính lương cho doanh nghiệp Nhật
**Thời gian:** 2 năm 11 tháng (04/2022 – 03/2025)
**Vị trí:** Backend Developer
**Team size:** 8 người
**Mô tả:** Hệ thống chấm công và tính lương dành cho doanh nghiệp Nhật Bản.
**Vai trò trong dự án:**
- Xây API chấm công
- Làm module tính lương theo ca
- Viết batch xuất báo cáo tháng

**Tech Stack:** Laravel, MySQL, Redis
```

## Khối nhắc in sau khi lưu

```text
⚠ File short-bio-nguyen-van-b-2026-10-27.md cần kiểm tra trước khi gửi khách:
- Header: Ngày sinh
- Projects (tiêu đề đã thay tên thật): Project 1 = Kintai Cloud
- Short Bio (suy luận): "Redis ở tầng ứng dụng", "dịch vụ chạy trong Docker" — diễn giải từ stack, input không nói dùng vào việc gì
- Chưa thể hiện (yêu cầu Senior Backend): thiết kế kiến trúc / chọn công nghệ, review code cho team, dẫn dắt / mentor
  thành viên, làm requirement / estimate với khách — bổ sung nếu đã làm
Bổ sung trực tiếp vào file trước khi gửi khách hàng.
```

Vài điểm đáng chú ý:

- **Số năm** ghi ở các skill chính: Laravel (framework), PHP (ngôn ngữ), MySQL (database). Redis và Docker là skill phụ đi kèm nên chỉ ghi tên.
- **Thời gian dự án** `04/2022 – 03/2025` được tính thành `2 năm 11 tháng`.
- **Tên thật của dự án** (Kintai Cloud) không xuất hiện ở đâu trong file: phần Projects dùng tiêu đề mô tả, còn khối nhắc cho member biết Project 1 là dự án nào.
- Member không xác nhận việc nào của Level Senior, nên bio **không tự viết** về kiến trúc hay mentor; các việc đó nằm ở khối nhắc.
