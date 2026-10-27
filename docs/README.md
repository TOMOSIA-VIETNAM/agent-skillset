# Tài liệu

| File | Dành cho | Nội dung |
|---|---|---|
| [example.md](./example.md) | Người dùng | Một lần chạy mẫu: lệnh gọi, file bio sinh ra, khối nhắc |
| [use-cases.md](./use-cases.md) | Người sửa skill | Hành vi theo từng use case (UC1–UC8), xử lý ngoại lệ, các quyết định đã chốt (Q1–Q24) |
| [images/flow.svg](./images/flow.svg) | README | Sơ đồ flow 7 bước |
| [images/demo-*.svg](./images/) | README | 3 ảnh demo đầu vào → quy trình → đầu ra, dựng từ một lần chạy thật bằng [images/src/build.py](./images/src/build.py) |

Quy tắc chi tiết mà skill đọc khi chạy nằm ở `generate-short-bio/references/`, không nằm ở đây. Sửa hành vi của skill thì sửa file reference trước, rồi cập nhật `use-cases.md` cho khớp.

Kịch bản demo nội bộ, dữ liệu CV thật và output dự phòng nằm ở `demo/`, chỉ giữ trên máy người demo, không commit.
