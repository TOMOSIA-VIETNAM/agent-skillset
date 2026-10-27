"""Dựng 3 ảnh demo cho README: đầu vào, quy trình, đầu ra.

Nội dung lấy nguyên văn từ một lần chạy thật (2026-10-27, sau khi thêm quy tắc ngoại ngữ Q24) với dữ liệu giả lập ở
generate-short-bio/evals/cv-laravel-jd-full-match/files/ (cv-nguyen-van-d.md, jd-backend-senior.md;
khi chạy đặt tên file JD là jd-senior-backend.md như trong ảnh), mức Hoàn toàn khớp.
Chỗ rút gọn ghi "…"; chữ tím in nghiêng là chú thích thêm, không phải output.
Chạy lại khi skill đổi cách trình bày:  python3 docs/images/src/build.py
Dựng lại xong thì tăng số ?v=N ở 3 link ảnh demo trong README để trình xem không dùng bản cache cũ.
"""
import os
from svgterm import render, wrap

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
F = ("box", "cv")
J = ("box", "jd")
WN = ("box", "warn", "box-warn")


def line(*parts):
    return ("line", list(parts))


# ---------- 1. Đầu vào ----------
inp = [
    ("prompt", [("› ", "muted"), ("/generate-short-bio ./cv-nguyen-van-d.md JD: ./jd-senior-backend.md", "ink")]),
    ("gap", None),
    (F, [("cv-nguyen-van-d.md", "fileh")]),
    (F, [("# NGUYỄN VĂN D", "head")]),
    (F, [("Backend Developer", "ink")]),
    (F, [("Email: d.nguyen@example.com | DOB: 05/09/1997 | ", "ink"), ("Phone: 0905 123 456", "drop")]),
    (F, [("Education: Đại học Bách Khoa Đà Nẵng — Kỹ sư CNTT (2015–2019)", "drop"), ("  ← bỏ qua", "anno")]),
    (F, [("Japanese: JLPT N3", "hl"), ("  ← giữ, đưa vào header", "anno")]),
    (F, [("## Summary", "head")]),
    (F, [("4 years", "hl"), (" of experience in web backend development with PHP/Laravel.", "ink")]),
    (F, [("Worked on projects for Japanese clients.", "ink")]),
    (F, [("## Skills", "head")]),
    (F, [("PHP, ", "ink"), ("Laravel (4 years)", "hl"), (", MySQL, Redis, Docker, Git, RESTful API, PHPUnit,", "ink")]),
    (F, [("Vue.js (basic)", "ink")]),
    (F, [("## Projects", "head")]),
    (F, [("### HANAYOYAKU — Booking platform for beauty salons (Japan)", "sub")]),
    (F, [("Period: 03/2024 – now · Role: Backend Developer · Team size: 6", "ink")]),
    (F, [("Responsibilities: Built booking & cancellation API, staff shift scheduling,", "ink")]),
    (F, [("email/LINE notification via queue (Redis). Joined from basic design to …", "ink")]),
    (F, [("Tech: PHP 8, Laravel 10, MySQL, Redis, Docker", "ink")]),
    (F, [("### ZAIKO-NAVI — Inventory management for retail chain", "sub")]),
    (F, [("Period: 06/2021 – 02/2024 · Team size: 10", "ink"), ("   ← không ghi vai trò", "anno")]),
    (F, [("Description: Inventory management system for a retail chain with 40 stores …", "ink")]),
    (F, [("Responsibilities: Developed backend features.", "ink"), ("   ← chưa rõ phần đã làm", "anno")]),
    (F, [("Tech: PHP 7, Laravel 8, MySQL, Vue.js 2", "ink")]),
    ("gap", None),
    (J, [("jd-senior-backend.md", "fileh")]),
    (J, [("[JD] Senior Backend Engineer (Laravel) — client: Japanese HR-tech company", "head")]),
    (J, [("Requirements:", "label")]),
    (J, [("- ", "ink"), ("5+ years", "hl"), (" of backend development experience", "ink")]),
    (J, [("- Strong experience with Laravel", "ink")]),
    (J, [("- ", "ink"), ("3 years of experience with AWS", "hl"), (" (EC2, RDS, S3)", "ink"), ("   ← CV chưa có", "anno")]),
    (J, [("- Experience with MySQL, Redis, queue processing", "ink")]),
    (J, [("- Unit testing (PHPUnit)", "ink")]),
    (J, [("Nice to have: Docker, CI/CD (GitHub Actions)", "ink")]),
]
h1 = render(os.path.join(OUT, "demo-1-input.svg"), "Đầu vào · CV + JD", inp,
            "Đầu vào: lệnh gọi skill kèm file CV (Laravel 4 năm, có JLPT N3 được giữ, học vấn và số điện thoại bị bỏ qua, dự án ZAIKO-NAVI chưa rõ vai trò và phần đã làm) và file JD Senior Backend yêu cầu 5+ năm và 3 năm AWS")

# ---------- 2. Quy trình ----------
FM = ("box", "form1", "box-form")
FM2 = ("box", "form2", "box-form")
proc = [
    line(("Thông tin đọc từ CV:", "label")),
    line(("- Tên: Nguyễn Văn D · Email: d.nguyen@example.com · Role: Backend", "ink")),
    line(("- Số năm kinh nghiệm: 4 năm (theo Summary trong CV)", "ink")),
    line(("- Tech stack: PHP (7, 8), Laravel (8, 10; 4 năm), MySQL, Redis, Docker, Git, …", "ink")),
    line(("- Ngày sinh: 05/09/1997 · ", "ink"), ("Ngoại ngữ: JLPT N3", "hl")),
    line(("- Dự án: HANAYOYAKU (03/2024 – nay), ZAIKO-NAVI (06/2021 – 02/2024)", "ink")),
    line(("Lưu ý:", "label")),
    *wrap("- CV ghi 4 năm kinh nghiệm, nhưng các dự án kéo dài từ 06/2021 đến nay, tức khoảng 5 năm 4 tháng."),
    *wrap("- ZAIKO-NAVI chưa ghi vai trò. Phần trách nhiệm chỉ ghi \"Developed backend features\", chưa rõ bạn làm tính năng nào."),
    ("gap", None),
    (FM, [("Form tự vấn", "fileh"), ("   ← trong Claude Code là form chọn, ảnh ghi lại dạng danh sách", "anno")]),
    (FM, [("1. Yêu cầu cho vị trí Middle Backend: khách thường muốn biết bạn đã làm", "label")]),
    (FM, [("   những việc dưới đây chưa. Bạn đã làm việc nào? (chọn được nhiều)", "label")]),
    (FM, [("   a. Làm trọn feature từ yêu cầu tới deploy  b. Thiết kế DB / API cho feature", "ink")]),
    (FM, [("   c. Chưa làm việc nào trong số này", "ink")]),
    (FM, [("2. Ở dự án ZAIKO-NAVI, bạn trực tiếp làm những tính năng nào?", "label")]),
    (FM, [("   a. Nhập / xuất kho  b. Quét barcode  c. Báo cáo hàng tháng  d. Import CSV", "ink")]),
    (FM, [("3. Ở dự án ZAIKO-NAVI, bạn giữ vai trò gì?", "label")]),
    (FM, [("   a. ", "ink"), ("Backend Developer (Đề xuất)", "hl"), (". Phần trách nhiệm ghi \"backend features\" …", "ink")]),
    (FM, [("   b. Fullstack Developer, vì dự án có dùng Vue.js 2  c. Để trống, mình điền sau", "ink")]),
    (FM, [("4. CV ghi 4 năm kinh nghiệm, còn các dự án bắt đầu từ 06/2021, tức khoảng", "label")]),
    (FM, [("   5 năm. Bạn muốn lấy số nào?", "label")]),
    (FM, [("   a. ", "ink"), ("Giữ 4 năm như CV (Đề xuất)", "hl"), (". Đây là số CV ghi rõ  b. Ghi 5 năm, …", "ink")]),
    ("gap", None),
    ("prompt", [("› ", "muted"), ("1: a,b · 2: a,d · 3: a · 4: b", "you"), ("   ← member chỉ cần chọn", "anno")]),
    ("gap", None),
    *wrap("Đã cập nhật: tổng kinh nghiệm là 5 năm, nên giờ bạn được tính theo cấp Senior Backend. Bạn đã xác nhận làm trọn feature tới deploy và thiết kế DB / API. …"),
    *wrap("Mình đã so profile với JD Senior Backend Engineer (Laravel). Role giống nhau, và bạn đã có hầu hết skill bắt buộc … Bạn chỉ còn thiếu 3 năm AWS (EC2, RDS, S3), cộng GitHub Actions ở mục nice to have."),
    ("gap", None),
    (FM2, [("Form mức match", "fileh")]),
    (FM2, [("5. Bạn muốn bio bám sát JD tới mức nào?", "label")]),
    (FM2, [("   a. ", "ink"), ("Hoàn toàn khớp (Đề xuất)", "hl"), (": ghi 5 năm và Laravel 5 năm. Thêm AWS (EC2,", "ink")]),
    (FM2, [("      RDS, S3) 3 năm theo JD, GitHub Actions chỉ ghi tên. Chỉ nêu skill khớp JD, …", "ink")]),
    (FM2, [("   b. Tương đối khớp: vẫn ghi 5 năm. Thêm AWS 2 năm (80% mốc JD) …", "ink")]),
    (FM2, [("   c. Tổng quát: giữ đúng profile thật, không thêm AWS hay GitHub Actions. …", "ink")]),
    ("gap", None),
    ("prompt", [("› ", "muted"), ("a", "you")]),
    ("gap", None),
    line(("Xác nhận: ", "label"), ("Nguyễn Văn D · Role: Backend · Mức độ: chi tiết · JD: có · Match: hoàn toàn", "ink")),
    line(("          File: short-bio-nguyen-van-d-2026-10-27.md", "ink")),
]
h2 = render(os.path.join(OUT, "demo-2-process.svg"), "Quy trình · tự vấn → mức match → xác nhận", proc,
            "Quy trình: skill tóm tắt CV (có JLPT N3) và nêu chỗ mâu thuẫn, hỏi một form tự vấn 4 câu có đáp án đề xuất, member trả lời bằng cách chọn, skill so profile với JD và hỏi mức match, member chọn Hoàn toàn khớp, skill in dòng xác nhận")

# ---------- 3. Đầu ra ----------
B = ("box", "bio")
outp = [
    (B, [("short-bio-nguyen-van-d-2026-10-27.md", "fileh")]),
    (B, [("# Nguyễn Văn D", "head")]),
    (B, [("Vị trí: ", "label"), ("Backend Developer", "ink"), ("  ·  ", "muted"), ("Email: ", "label"), ("d.nguyen@example.com", "ink")]),
    (B, [("Ngày sinh: ", "label"), ("05/09/1997", "ink"), ("  ·  ", "muted"), ("Ngoại ngữ: ", "label"), ("JLPT N3", "hl"), ("   ← giữ đúng như CV", "anno")]),
    (B, [("## Short Bio", "head")]),
    *[(B, p) for _, p in wrap("Backend Developer với 5 năm phát triển web backend bằng PHP và Laravel, phần lớn cho khách hàng Nhật Bản. Các sản phẩm đã làm gồm nền tảng đặt lịch cho salon làm đẹp và hệ thống quản lý tồn kho cho chuỗi bán lẻ 40 cửa hàng.", width=82)],
    ("small", None),
    (B, [("Tự làm trọn feature từ thiết kế DB và API tới deploy", "hl"), (", như API đặt và hủy lịch, xếp ca", "ink")]),
    (B, [("nhân viên, nhập xuất kho hay import dữ liệu CSV.", "ink"), ("   ← việc member đã xác nhận ở form", "anno")]),
    *[(B, p) for _, p in wrap("Lưu dữ liệu nghiệp vụ trên MySQL và dùng Redis làm queue để gửi thông báo email, LINE bất đồng bộ. Đóng gói ứng dụng bằng Docker, triển khai trên AWS với EC2, RDS và S3.", width=82)],
    ("small", None),
    *[(B, p) for _, p in wrap("Tham gia dự án từ basic design, qua detailed design tới implementation, làm việc trong team từ 6 đến 10 người. Viết unit test bằng PHPUnit cho phần backend đảm nhận.", width=82)],
    (B, [("## Core Skills", "head")]),
    (B, [("Backend/Framework: ", "label"), ("Laravel (5 năm)", "hl"), (", PHP (5 năm), Eloquent ORM", "ink"), ("  ← 4 → 5 năm", "anno")]),
    (B, [("Cloud: ", "label"), ("AWS (3 năm)", "hl"), (", EC2, RDS, S3", "ink"), ("   ← thêm theo JD", "anno")]),
    (B, [("Database: ", "label"), ("MySQL (5 năm)", "ink"), ("   ← suy từ thời gian dự án", "anno")]),
    (B, [("Caching & Queue: ", "label"), ("Redis", "ink"), ("  ·  ", "muted"), ("Testing: ", "label"), ("PHPUnit", "ink")]),
    (B, [("DevOps/CI/CD: ", "label"), ("Docker, GitHub Actions", "ink"), ("  ·  ", "muted"), ("API Integration: ", "label"), ("RESTful API", "ink")]),
    (B, [("## Project Examples", "head")]),
    (B, [("### Project 1 — HANAYOYAKU", "sub")]),
    (B, [("Thời gian: ", "label"), ("2 năm 7 tháng (đang làm)", "ink"), ("  ·  ", "muted"), ("Vị trí: ", "label"), ("Backend Developer", "ink")]),
    (B, [("Tính năng đảm nhiệm: ", "label"), ("API đặt lịch và hủy lịch · Xếp ca làm việc cho nhân viên ·", "ink")]),
    (B, [("Gửi thông báo email / LINE qua queue (Redis)", "ink")]),
    (B, [("Tech Stack: ", "label"), ("PHP 8, Laravel 10, MySQL, Redis, Docker", "ink"), ("   ← giữ stack thật", "anno")]),
    (B, [("### Project 2 — ZAIKO-NAVI", "sub")]),
    (B, [("Thời gian: ", "label"), ("2 năm 8 tháng", "ink"), ("  ·  ", "muted"), ("Vị trí: ", "label"), ("Backend Developer", "ink"), ("   ← member chọn ở form", "anno")]),
    (B, [("Tính năng đảm nhiệm: ", "label"), ("Nhập / xuất kho · Import dữ liệu CSV", "ink"), ("   ← member chọn ở form", "anno")]),
    (B, [("Tech Stack: ", "label"), ("PHP 7, Laravel 8, MySQL, Vue.js 2", "ink")]),
    ("gap", None),
    line(("Đã lưu: ", "ok"), ("short-bio-nguyen-van-d-2026-10-27.md", "ink")),
    ("gap", None),
    (WN, [("⚠ File short-bio-nguyen-van-d-2026-10-27.md cần kiểm tra trước khi gửi khách:", "warnh")]),
    *[(WN, p) for _, p in wrap("- Thêm theo JD (chưa có trong profile): AWS (3 năm) với EC2, RDS, S3 (Short Bio có câu deploy lên AWS), GitHub Actions. Bạn nên chuẩn bị trước, vì khách thường hỏi sâu về AWS.", width=82)],
    (WN, [("- Companion skill thêm vào (CV chưa ghi): Eloquent ORM.", "ink")]),
    *[(WN, p) for _, p in wrap("- Điều chỉnh theo JD: Vue.js và Git bị bỏ khỏi Core Skills vì JD không yêu cầu (vẫn giữ ở Tech Stack của ZAIKO-NAVI).", width=82)],
    (WN, [("- Điều chỉnh theo câu trả lời của bạn: tổng kinh nghiệm 4 → 5 năm (CV ghi 4).", "ink")]),
    *[(WN, p) for _, p in wrap("- Suy luận: Laravel, PHP và MySQL 5 năm. CV ghi Laravel 4 năm, còn số 5 năm tính theo mốc 06/2021 vì cả hai dự án đều dùng các công nghệ này.", width=82)],
    *[(WN, p) for _, p in wrap("- Chưa thể hiện (yêu cầu Senior Backend): review code cho team, dẫn dắt / mentor thành viên, làm requirement / estimate với khách, xử lý sự cố / hiệu năng production. …", width=82)],
    (WN, [("Bổ sung trực tiếp vào file trước khi gửi khách hàng.", "ink")]),
]
h3 = render(os.path.join(OUT, "demo-3-output.svg"), "Đầu ra · file bio + khối nhắc", outp,
            "Đầu ra: file bio với header có dòng Ngoại ngữ JLPT N3, Short Bio 3 đoạn dùng việc member đã xác nhận, Core Skills (Laravel 5 năm, thêm AWS 3 năm theo JD, PHP và MySQL suy từ thời gian dự án), Project Examples giữ stack thật và dùng câu trả lời của member, dòng Đã lưu và khối nhắc liệt kê mọi điều chỉnh")

print("input", h1, "process", h2, "output", h3)
