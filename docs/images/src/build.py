"""Dựng 3 ảnh demo cho README: đầu vào, quy trình, đầu ra.

Nội dung lấy nguyên văn từ một lần chạy thật (2026-10-31, flow 8 bước, có câu AI và tiêu đề dự án không dùng tên thật)
với dữ liệu giả lập ở evals/generate-short-bio/cv-laravel-jd-full-match/files/ (cv-nguyen-van-d.md, jd-backend-senior.md;
khi chạy đặt tên file JD là jd-senior-backend.md như trong ảnh), mức Hoàn toàn khớp. Chạy bằng `claude -p` với câu trả lời
giả lập: 5 năm, đã làm trọn feature tới deploy và thiết kế DB / API, có dùng AI, ZAIKO-NAVI làm nhập / xuất kho và import CSV.
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
FM3 = ("box", "form3", "box-form")
FM4 = ("box", "form4", "box-form")
proc = [
    line(("Thông tin đọc từ CV:", "label")),
    line(("- Tên: Nguyễn Văn D · Email: d.nguyen@example.com · Role: Backend", "ink")),
    line(("- Số năm kinh nghiệm: 4 năm (theo CV ghi)", "ink")),
    line(("- Tech stack: PHP, Laravel (4 năm), MySQL, Redis, Docker, Git, RESTful API, …", "ink")),
    line(("- Ngày sinh: 05/09/1997 · ", "ink"), ("Ngoại ngữ: JLPT N3", "hl")),
    line(("- Dự án: HANAYOYAKU (03/2024 – nay), ZAIKO-NAVI (06/2021 – 02/2024)", "ink")),
    line(("Lưu ý:", "label")),
    *wrap("- CV ghi 4 năm kinh nghiệm, nhưng dự án sớm nhất bắt đầu từ 06/2021 (tính tới nay là 5 năm 4 tháng)"),
    *wrap("- ZAIKO-NAVI chưa ghi vị trí, phần việc chỉ ghi \"Developed backend features\""),
    ("gap", None),
    (FM, [("Form tự vấn", "fileh"), ("   ← trong Claude Code là form chọn, ảnh ghi lại dạng danh sách", "anno")]),
    (FM, [("1. Bạn có dùng AI trong lúc phát triển không? Có thì mình thêm 2 dòng AI vào", "label")]),
    (FM, [("   Core Skills và 1 đoạn về cách dùng AI ở cuối bio.", "label")]),
    (FM, [("   a. ", "ink"), ("Có, thêm đủ 2 dòng AI (Đề xuất)", "hl"), ("  b. Chỉ ghi công cụ mình gõ  c. Không thêm", "ink")]),
    (FM, [("2. Yêu cầu cho vị trí Middle Backend: bạn đã làm việc nào? (chọn được nhiều)", "label")]),
    (FM, [("   a. Làm trọn feature từ yêu cầu tới deploy  b. Thiết kế DB / API cho feature", "ink")]),
    (FM, [("   c. Chưa làm việc nào trong số này", "ink")]),
    (FM, [("3. Các dự án của bạn chủ yếu thuộc lĩnh vực nào?", "label")]),
    (FM, [("   a. ", "ink"), ("Đặt lịch dịch vụ làm đẹp và quản lý tồn kho bán lẻ (Đề xuất)", "hl"), ("  b. …", "ink")]),
    (FM, [("4. CV ghi 4 năm, nhưng dự án đầu tiên bắt đầu từ 06/2021. Tổng kinh nghiệm", "label")]),
    (FM, [("   đúng của bạn là bao nhiêu?", "label")]),
    (FM, [("   a. ", "ink"), ("5 năm, tính từ 06/2021 (Đề xuất)", "hl"), ("  b. 4 năm, theo CV ghi", "ink")]),
    ("gap", None),
    ("prompt", [("› ", "muted"), ("1: a · 2: a,b · 3: a · 4: a", "you"), ("   ← member chỉ cần chọn", "anno")]),
    ("gap", None),
    (FM2, [("Form mức match", "fileh"), ("   ← JD đã gửi kèm lệnh nên không hỏi lại", "anno")]),
    (FM2, [("5. Bạn muốn bio bám sát JD tới mức nào?", "label")]),
    (FM2, [("   a. ", "ink"), ("Hoàn toàn khớp (Đề xuất)", "hl"), (": ghi 5 năm (JD 5+), thêm AWS (3 năm), chỉ nêu", "ink")]),
    (FM2, [("      skill khớp JD; bạn đã có Laravel, MySQL, Redis/queue, PHPUnit, Docker", "ink")]),
    (FM2, [("   b. Tương đối khớp: giữ 5 năm, thêm AWS (2 năm), giữ bức tranh toàn diện", "ink")]),
    (FM2, [("   c. Tổng quát: giữ 5 năm, không thêm AWS, nêu toàn bộ điểm mạnh", "ink")]),
    ("gap", None),
    ("prompt", [("› ", "muted"), ("a", "you")]),
    ("gap", None),
    (FM3, [("Form dự án · HANAYOYAKU", "fileh"), ("   ← đã đủ mô tả và vai trò, chỉ hỏi stack", "anno")]),
    (FM3, [("6. Tech stack trong CV là PHP 8, Laravel 10, MySQL, Redis, Docker. Dự án có dùng", "label")]),
    (FM3, [("   thêm công nghệ nào dưới đây không? (chọn được nhiều)", "label")]),
    (FM3, [("   a. ", "ink"), ("LINE Messaging API (Đề xuất)", "hl"), (": mô tả có nhắc thông báo LINE  b. PHPUnit …", "ink")]),
    ("gap", None),
    ("prompt", [("› ", "muted"), ("a", "you")]),
    ("gap", None),
    (FM4, [("Form dự án · ZAIKO-NAVI", "fileh")]),
    (FM4, [("7. Ở dự án ZAIKO-NAVI, bạn đã làm những việc nào? (chọn được nhiều)", "label")]),
    (FM4, [("   a. Xây chức năng nhập / xuất kho  b. Quét barcode  c. Báo cáo tồn kho hằng tháng", "ink")]),
    (FM4, [("   d. Xây chức năng import CSV", "ink"), ("   ← lấy từ mô tả trong CV", "anno")]),
    (FM4, [("8. Tech stack trong CV là PHP 7, Laravel 8, MySQL, Vue.js 2. Có dùng thêm …?", "label")]),
    (FM4, [("   a. Redis  b. Docker  c. PHPUnit", "ink"), ("   ← có trong Core Skills", "anno"), ("  d. ", "ink"), ("Không (Đề xuất)", "hl")]),
    (FM4, [("9. Ở dự án ZAIKO-NAVI, bạn giữ vị trí gì?", "label")]),
    (FM4, [("   a. ", "ink"), ("Backend Developer (Đề xuất)", "hl"), ("  b. Fullstack Developer  c. Team Lead", "ink")]),
    ("gap", None),
    ("prompt", [("› ", "muted"), ("7: a,d · 8: d · 9: a", "you")]),
    ("gap", None),
    line(("Xác nhận: ", "label"), ("Nguyễn Văn D · Role: Backend · Mức độ: chi tiết · JD: có · Match: hoàn toàn", "ink")),
    line(("          File: short-bio-nguyen-van-d-2026-10-31.md", "ink")),
]
h2 = render(os.path.join(OUT, "demo-2-process.svg"), "Quy trình · tự vấn → mức match → dự án → xác nhận", proc,
            "Quy trình: skill tóm tắt CV (có JLPT N3) và nêu chỗ chưa khớp về số năm, hỏi một form tự vấn có câu AI và đáp án đề xuất, member chọn, skill hỏi mức match, member chọn Hoàn toàn khớp, skill hỏi form dự án cho HANAYOYAKU (stack) và ZAIKO-NAVI (việc đã làm, stack, vị trí), rồi in dòng xác nhận")

# ---------- 3. Đầu ra ----------
B = ("box", "bio")
outp = [
    (B, [("short-bio-nguyen-van-d-2026-10-31.md", "fileh")]),
    (B, [("# Nguyễn Văn D", "head")]),
    (B, [("Vị trí: ", "label"), ("Backend Developer", "ink"), ("  ·  ", "muted"), ("Email: ", "label"), ("d.nguyen@example.com", "ink")]),
    (B, [("Ngày sinh: ", "label"), ("05/09/1997", "ink"), ("  ·  ", "muted"), ("Ngoại ngữ: ", "label"), ("JLPT N3", "hl"), ("   ← giữ đúng như CV", "anno")]),
    (B, [("## Short Bio", "head")]),
    *[(B, p) for _, p in wrap("Backend Developer với 5 năm phát triển web bằng PHP và Laravel, phần lớn cho khách hàng Nhật Bản. Đã làm nền tảng đặt lịch cho salon làm đẹp và hệ thống quản lý tồn kho cho chuỗi bán lẻ 40 cửa hàng, nên nắm rõ nghiệp vụ lịch hẹn, ca làm việc và nhập xuất kho.", width=82)],
    ("small", None),
    (B, [("Thường nhận trọn một feature, từ phân tích yêu cầu, thiết kế database và API cho tới", "hl")]),
    (B, [("deploy.", "hl"), ("   ← việc member đã xác nhận ở form", "anno")]),
    *[(B, p) for _, p in wrap("Đã xây API đặt và hủy lịch, xếp ca nhân viên, nhập xuất kho và import CSV trên MySQL, đồng thời đưa thông báo email và LINE sang xử lý nền qua queue Redis. Đóng gói ứng dụng bằng Docker và triển khai lên AWS với EC2, RDS và S3.", width=82)],
    ("small", None),
    *[(B, p) for _, p in wrap("Làm việc trong team 6 đến 10 người, tham gia từ basic design, detailed design tới implementation và phối hợp với frontend ở khâu tích hợp. Viết unit test bằng PHPUnit cho phần logic nghiệp vụ.", width=82)],
    ("small", None),
    (B, [("Có kinh nghiệm ứng dụng AI vào quy trình phát triển phần mềm, sử dụng Claude, Cursor và", "ink")]),
    (B, [("MCP để hỗ trợ phân tích yêu cầu, … code review và testing. …", "ink"), ("   ← đoạn AI", "anno")]),
    (B, [("## Core Skills", "head")]),
    (B, [("Backend/Framework: ", "label"), ("Laravel (5 năm)", "hl"), (", PHP (5 năm), Eloquent ORM", "ink"), ("  ← 4 → 5 năm", "anno")]),
    (B, [("Cloud: ", "label"), ("AWS (3 năm)", "hl"), (", EC2, RDS, S3", "ink"), ("   ← thêm theo JD", "anno")]),
    (B, [("Database: ", "label"), ("MySQL (5 năm)", "ink"), ("  ·  ", "muted"), ("Caching & Queue: ", "label"), ("Redis, Laravel Queue", "ink")]),
    (B, [("Testing: ", "label"), ("PHPUnit", "ink"), ("  ·  ", "muted"), ("DevOps/CI/CD: ", "label"), ("Docker, GitHub Actions", "ink"), ("  ·  ", "muted"), ("API Integration: ", "label"), ("RESTful API", "ink")]),
    (B, [("AI / AI-assisted Development: ", "label"), ("Claude, Cursor, MCP, Prompt Engineering, …", "ink"), ("  ← member chọn", "anno")]),
    (B, [("AI-driven Software Development: ", "label"), ("AI-assisted Requirement Analysis, Code Review, …", "ink")]),
    (B, [("## Projects", "head")]),
    (B, [("### Project 1 — Nền tảng đặt lịch cho salon làm đẹp tại Nhật Bản", "sub"), ("  ← không dùng tên thật", "anno")]),
    (B, [("Thời gian: ", "label"), ("2 năm 7 tháng (03/2024 – 10/2026) (đang làm)", "ink"), ("  ·  ", "muted"), ("Team size: ", "label"), ("6 người", "ink")]),
    (B, [("Mô tả: ", "label"), ("Nền tảng web đặt lịch hẹn tại các salon làm đẹp ở Nhật Bản. Khách hàng đặt", "ink")]),
    (B, [("lịch trực tuyến, còn salon quản lý lịch làm việc của nhân viên và menu dịch vụ.", "ink")]),
    (B, [("Vai trò trong dự án: ", "label"), ("Xây API đặt lịch và hủy lịch · Xếp ca làm việc cho nhân viên ·", "ink")]),
    (B, [("Gửi thông báo email / LINE qua queue Redis · Tham gia từ basic design tới implementation", "ink")]),
    (B, [("Tech Stack: ", "label"), ("PHP 8, Laravel 10, MySQL, Redis, Docker, LINE Messaging API", "ink"), ("  ← stack thật", "anno")]),
    (B, [("### Project 2 — Hệ thống quản lý tồn kho cho chuỗi bán lẻ", "sub")]),
    (B, [("Thời gian: ", "label"), ("2 năm 8 tháng (06/2021 – 02/2024)", "ink"), ("  ·  ", "muted"), ("Vị trí: ", "label"), ("Backend Developer", "ink"), ("  ← form dự án", "anno")]),
    (B, [("Mô tả: ", "label"), ("Hệ thống quản lý tồn kho cho một chuỗi bán lẻ 40 cửa hàng. …", "ink")]),
    (B, [("Vai trò trong dự án: ", "label"), ("Phát triển backend cho chức năng nhập / xuất kho ·", "ink")]),
    (B, [("Phát triển chức năng import dữ liệu CSV", "ink"), ("   ← member chọn ở form", "anno")]),
    (B, [("Tech Stack: ", "label"), ("PHP 7, Laravel 8, MySQL, Vue.js 2", "ink")]),
    ("gap", None),
    line(("Đã lưu: ", "ok"), ("short-bio-nguyen-van-d-2026-10-31.md", "ink")),
    ("gap", None),
    (WN, [("⚠ File short-bio-nguyen-van-d-2026-10-31.md cần kiểm tra trước khi gửi khách:", "warnh")]),
    (WN, [("- Projects (tiêu đề đã thay tên thật): Project 1 = HANAYOYAKU, Project 2 = ZAIKO-NAVI", "ink")]),
    *[(WN, p) for _, p in wrap("- Thêm theo JD (chưa có trong profile): AWS (3 năm), EC2, RDS, S3; GitHub Actions (nice to have, chỉ có ở Core Skills); Eloquent ORM; Laravel Queue. Bạn chuẩn bị câu trả lời nếu khách hỏi", width=82)],
    *[(WN, p) for _, p in wrap("- Điều chỉnh theo JD / mốc dự án: tổng số năm 4 → 5 năm (CV ghi 4, bạn xác nhận 5 năm tính từ 06/2021); Laravel 4 → 5 năm", width=82)],
    (WN, [("- Core Skills (suy luận): PHP 5 năm, MySQL 5 năm, tính từ thời gian hai dự án", "ink")]),
    *[(WN, p) for _, p in wrap("- Chưa thể hiện (yêu cầu Senior Backend): thiết kế kiến trúc / chọn công nghệ, review code cho team, dẫn dắt / mentor thành viên, … Bổ sung nếu bạn đã làm", width=82)],
    (WN, [("Bổ sung trực tiếp vào file trước khi gửi khách hàng.", "ink")]),
]
h3 = render(os.path.join(OUT, "demo-3-output.svg"), "Đầu ra · file bio + khối nhắc", outp,
            "Đầu ra: file bio với header có dòng Ngoại ngữ JLPT N3, Short Bio 3 đoạn dùng việc member đã xác nhận cộng đoạn AI, Core Skills (Laravel 5 năm, thêm AWS 3 năm theo JD, 2 dòng AI), Projects dùng tiêu đề mô tả thay tên thật, có Mô tả, Vai trò trong dự án và stack thật, dòng Đã lưu và khối nhắc ghép tiêu đề với tên thật cùng mọi điều chỉnh")

print("input", h1, "process", h2, "output", h3)
