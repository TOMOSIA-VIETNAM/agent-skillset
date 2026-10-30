# Checklist nội dung theo role × cấp

Mục lục: §1 Cách dùng · §2 Xác định cấp · §3 Backend · §4 Frontend · §5 Fullstack · §6 Mobile · §7 QA · §8 Checklist chung

Khách đọc bio để trả lời một câu: "người này có làm được việc của một [Senior Backend] không?". Mỗi cấp có những việc khách mặc định phải thấy — Senior mà bio chỉ nói "viết API" thì trông như Junior lâu năm. Checklist này liệt kê những việc đó để skill **chủ động hỏi** member khi input chưa có, thay vì để bio thiếu hoặc tự bịa cho đủ.

---

## §1 — Cách dùng

Checklist dùng ở hai chỗ trong flow:

**Bước 2 — tự vấn (`collect-info.md` §5, mục 2b):**
1. Xác định role + cấp (§2) từ số năm **thực tế**.
2. Lấy các yêu cầu của đúng role × cấp đó. Với mỗi yêu cầu, tìm bằng chứng trong input / CV (cột *Tín hiệu*).
3. Yêu cầu chưa có bằng chứng → gom vào **một câu multiSelect** trong form tự vấn:
   - Header: `Chuẩn [cấp]` (`Chuẩn Junior` / `Chuẩn Middle` / `Chuẩn Senior`). Câu hỏi: `Yêu cầu cho vị trí [Senior Backend]: khách thường muốn biết bạn đã làm những việc dưới đây chưa. Bạn đã làm việc nào?`
   - Lựa chọn: tối đa 3 yêu cầu còn thiếu (ưu tiên theo thứ tự trong bảng), nhãn ngắn theo cột *Lựa chọn khi hỏi*, cộng `Chưa làm việc nào trong số này`.
   - Member chọn → coi là bằng chứng do member xác nhận, được viết vào **bio** (không thêm vào Core Skills — đây là việc đã làm, không phải công cụ; chỉ khi member gõ tên công cụ cụ thể ở ô Other, VD "Jest", thì công cụ đó mới vào Core Skills). Không chọn / chọn `Chưa làm` → không viết, ghi vào khối nhắc.
4. Không hỏi về yêu cầu đã có bằng chứng. Đủ hết → không có câu này.
5. **Chỉ dùng yêu cầu của đúng cấp hiện tại**, không hỏi yêu cầu của cấp dưới (VD Middle không hỏi Scrum / Git của Junior). Việc cơ bản thường đã lộ ra từ CV, còn form chỉ có 4 câu nên dành chỗ cho việc thể hiện đúng tầm cấp.
6. **JD đã biết từ lúc này** (member đưa kèm lệnh) **và role JD khác role member** → chỉ hỏi các yêu cầu **dùng chung giữa hai role**: review code / convention, dẫn dắt / mentor, làm requirement / estimate với khách, phối hợp / thống nhất API, viết test. Có 5 mục nhưng form chỉ chứa 3: bỏ trước mục đã có bằng chứng trong CV, rồi chọn theo đúng thứ tự vừa liệt kê, trừ khi JD nhấn mạnh một mục (VD JD ghi "mentor junior") thì đưa mục đó lên. Bỏ yêu cầu riêng của role cũ (VD `Thiết kế kiến trúc FE` khi sang Mobile) — cross-role sẽ xóa chúng nên hỏi là phí một lượt của member. JD chưa biết → hỏi theo role hiện tại như bình thường.

**Bước 7–8 — trước khi lưu:**
- Rà output theo bảng của role × cấp **đã chốt sau JD** và §8. Yêu cầu có bằng chứng mà output chưa thể hiện → sửa output. Yêu cầu không có bằng chứng → ghi khối nhắc (`output.md` §4), **không viết vào bio**.
- JD nâng số năm làm cấp tăng (VD 4 → 5 năm: Middle → Senior) → yêu cầu của cấp mới chưa có bằng chứng chỉ ghi khối nhắc, không mở thêm lượt hỏi (flow đã qua bước 2).

Checklist chạy ngầm, không in cho member. Mỗi yêu cầu chỉ cần thể hiện **một lần, ngắn gọn** — bio vẫn giữ độ dài và số đoạn của `write-bio.md` §1, nên gộp nhiều yêu cầu vào cùng một câu khi tự nhiên.

---

## §2 — Xác định cấp

| Cấp | Số năm |
|---|---|
| **Junior** | < 3 năm |
| **Middle** | 3 – dưới 5 năm |
| **Senior** | ≥ 5 năm |

Số năm là khoảng ("3-4 năm") → lấy cận trên như `collect-info.md` §3. Role Fullstack dùng bảng §5, không cộng hai bảng BE + FE.

Cột *Thể hiện ở*: **B1/B2/B3** = đoạn 1/2/3 của Short Bio · **CS** = Core Skills · **PJ** = Projects. Bio sơ sài (2 đoạn) → yêu cầu ghi B3 chuyển lên B2 nếu có bằng chứng.

---

## §3 — Backend

| Cấp | Yêu cầu nội dung | Thể hiện ở | Tín hiệu trong input | Lựa chọn khi hỏi |
|---|---|---|---|---|
| Junior | Xây API / tính năng theo spec bằng framework chính, nêu loại tính năng | B1, B2 | dự án có mô tả tính năng, stack | — (luôn có từ input) |
| Junior | Làm việc với DB: query, migration, quan hệ dữ liệu | B2, CS | MySQL/PostgreSQL, ORM | `Thiết kế bảng / migration` |
| Junior | Viết test hoặc debug, sửa bug | B3 | PHPUnit/JUnit, "fix bug" | `Viết unit test` |
| Junior | Làm việc trong quy trình team: Git, task, Scrum | B3 | Git, Jira, Agile/Scrum | `Làm theo Scrum / sprint` |
| Middle | Tự làm trọn feature từ phân tích yêu cầu tới deploy | B2 | "end-to-end", phụ trách module | `Làm trọn feature từ yêu cầu tới deploy` |
| Middle | Thiết kế DB / API cho feature | B2 | "design DB", "API design", detailed design | `Thiết kế DB / API cho feature` |
| Middle | Tối ưu: query, cache, queue, xử lý dữ liệu lớn | B2 | Redis, queue, index, "optimize" | `Tối ưu query / cache / queue` |
| Middle | Phối hợp FE / QA, tham gia detailed design | B3 | team size, "phối hợp", 詳細設計 | `Tham gia detailed design` |
| Senior | Thiết kế hệ thống / kiến trúc, chọn công nghệ | B1, B2 | basic design, architecture, microservices | `Thiết kế kiến trúc / chọn công nghệ` |
| Senior | Review code, đặt convention cho team | B3 | "review", "convention" | `Review code cho team` |
| Senior | Dẫn dắt / mentor thành viên | B3 | Team Lead, "lead", "mentor" | `Dẫn dắt / mentor thành viên` |
| Senior | Làm việc với khách ở giai đoạn yêu cầu, estimate | B3 | requirement definition, 要件定義, "estimate" | `Làm requirement / estimate với khách` |
| Senior | Xử lý vấn đề production: scale, bảo mật, sự cố | B2 | monitoring, security, "incident" | `Xử lý sự cố / hiệu năng production` |

---

## §4 — Frontend

| Cấp | Yêu cầu nội dung | Thể hiện ở | Tín hiệu trong input | Lựa chọn khi hỏi |
|---|---|---|---|---|
| Junior | Dựng UI từ design (Figma) bằng framework chính, responsive | B1, B2 | React/Vue, Figma, CSS | `Dựng UI từ Figma` |
| Junior | Kết nối API, xử lý dữ liệu hiển thị | B2 | REST, axios, "integrate API" | — (thường có từ stack) |
| Junior | Quản lý state cơ bản trong component | B2, CS | hooks, Redux/Pinia | — |
| Junior | Làm việc trong quy trình team: Git, task, review | B3 | Git, Jira, Scrum | `Làm theo Scrum / sprint` |
| Middle | Thiết kế component tái sử dụng, cấu trúc state phức tạp | B2 | design system, Redux Toolkit, Zustand | `Xây component dùng chung` |
| Middle | Tối ưu hiệu năng: render, bundle, Core Web Vitals | B2 | "performance", lazy load, SSR | `Tối ưu hiệu năng trang` |
| Middle | Viết test (unit / E2E) | B3, CS | Jest, Vitest, Cypress, Playwright | `Viết unit / E2E test` |
| Middle | Thống nhất API contract với BE, phối hợp designer | B3 | "phối hợp BE", API spec | `Thống nhất API với backend` |
| Senior | Kiến trúc FE: cấu trúc dự án, design system, SSR / monorepo | B1, B2 | Next.js/Nuxt, monorepo, Storybook | `Thiết kế kiến trúc FE` |
| Senior | Chọn công nghệ, đặt convention, review code | B3 | "review", "convention", ESLint rules | `Review code / đặt convention` |
| Senior | Dẫn dắt / mentor thành viên FE | B3 | Team Lead, "mentor" | `Dẫn dắt / mentor thành viên` |
| Senior | Chất lượng sản phẩm: accessibility, i18n, đa trình duyệt | B2 | a11y, i18n | `Accessibility / đa ngôn ngữ` |

---

## §5 — Fullstack

| Cấp | Yêu cầu nội dung | Thể hiện ở | Tín hiệu trong input | Lựa chọn khi hỏi |
|---|---|---|---|---|
| Junior | Làm tính năng cả FE lẫn BE theo spec, nêu stack hai phía | B1, B2 | stack BE + FE | — |
| Junior | Kết nối UI với API do mình viết, DB cơ bản | B2 | REST, ORM | — |
| Junior | Làm việc trong quy trình team | B3 | Git, Scrum | `Làm theo Scrum / sprint` |
| Middle | Tự làm trọn feature end-to-end cả hai phía | B2 | phụ trách module, "end-to-end" | `Làm trọn feature cả FE và BE` |
| Middle | Thiết kế DB / API, tối ưu cả hai phía | B2 | design DB, cache, SSR | `Thiết kế DB / API` |
| Middle | Đóng gói và deploy: Docker, cloud | B2, CS | Docker, AWS/GCP | `Deploy bằng Docker / cloud` |
| Middle | Viết test hai phía | B3 | PHPUnit, Jest | `Viết test cả FE và BE` |
| Senior | Kiến trúc end-to-end, chọn công nghệ | B1, B2 | architecture, basic design | `Thiết kế kiến trúc hệ thống` |
| Senior | CI/CD, monitoring | B2, CS | GitHub Actions, Datadog | `Dựng CI/CD / monitoring` |
| Senior | Review code, dẫn dắt team | B3 | Team Lead, "review" | `Review code / dẫn dắt team` |
| Senior | Làm requirement / estimate với khách | B3 | 要件定義, "estimate" | `Làm requirement / estimate với khách` |

---

## §6 — Mobile

| Cấp | Yêu cầu nội dung | Thể hiện ở | Tín hiệu trong input | Lựa chọn khi hỏi |
|---|---|---|---|---|
| Junior | Làm màn hình / tính năng theo design trên platform chính, nêu loại app | B1, B2 | Flutter/RN/Swift/Kotlin, loại app | — |
| Junior | Gọi API, hiển thị dữ liệu | B2 | Retrofit, dio, Alamofire | — |
| Junior | Debug trên thiết bị thật / simulator | B3 | "debug", device testing | `Debug trên thiết bị thật` |
| Junior | Làm việc trong quy trình team | B3 | Git, Scrum | `Làm theo Scrum / sprint` |
| Middle | Tổ chức kiến trúc app (MVVM, Bloc...), quản lý state | B2, CS | MVVM, Bloc, Redux | `Tổ chức kiến trúc app (MVVM...)` |
| Middle | Tính năng thiết bị: push, offline / local storage, camera, map | B2 | FCM, Room, CoreData | `Push / offline / tính năng thiết bị` |
| Middle | Phát hành lên App Store / Google Play | B2 | TestFlight, store release | `Phát hành lên store` |
| Middle | Phối hợp designer và backend | B3 | "phối hợp", Figma | `Thống nhất API với backend` |
| Senior | Kiến trúc app tổng thể (Clean Architecture), chọn công nghệ | B1, B2 | Clean Architecture, modular | `Thiết kế kiến trúc app` |
| Senior | CI/CD mobile, tự động build / phát hành | B2, CS | Fastlane, Codemagic, GH Actions | `Dựng CI/CD build app` |
| Senior | Xử lý crash / hiệu năng production | B2 | Crashlytics, "performance" | `Xử lý crash / hiệu năng` |
| Senior | Review code, dẫn dắt team mobile | B3 | Team Lead, "review" | `Review code / dẫn dắt team` |

---

## §7 — QA

Không có CI/CD setup ở mọi cấp — QA chạy test trong pipeline, không sở hữu infrastructure.

| Cấp | Yêu cầu nội dung | Thể hiện ở | Tín hiệu trong input | Lựa chọn khi hỏi |
|---|---|---|---|---|
| Junior | Viết và chạy test case theo spec, nêu loại testing chính | B1, B2 | test case, manual/automation | — |
| Junior | Báo bug và theo dõi tới khi đóng | B2 | Jira, Redmine, Backlog | `Quản lý bug trên Jira / Backlog` |
| Junior | Chạy regression / smoke trước release | B2 | regression, smoke | `Chạy regression / smoke test` |
| Junior | Test đa trình duyệt / thiết bị | B2 | cross-browser, device | `Test đa trình duyệt / thiết bị` |
| Middle | Lập test plan, thiết kế test case theo kỹ thuật (boundary, decision table) | B2 | test plan, test design | `Lập test plan` |
| Middle | API testing | B2, CS | Postman, RestAssured | `Test API bằng Postman` |
| Middle | Viết automation script (nếu automation) | B2, CS | Selenium, Playwright, Appium | `Viết automation script` |
| Middle | Tham gia từ giai đoạn review yêu cầu, phối hợp dev | B3 | "review spec", team size | `Review yêu cầu / spec cùng dev` |
| Senior | Xây test strategy, quy trình QA | B1, B2 | test strategy, QA process | `Xây test strategy / quy trình QA` |
| Senior | Thiết kế framework automation | B2, CS | framework design, POM, BDD | `Thiết kế framework automation` |
| Senior | Quyết định chất lượng release, theo dõi metrics | B2 | release, defect metrics | `Đánh giá chất lượng release` |
| Senior | Dẫn dắt / mentor team QA | B3 | QA Lead, "mentor" | `Dẫn dắt / mentor team QA` |

---

## §8 — Checklist chung (mọi role, mọi cấp)

Rà trước khi lưu, sai thì sửa rồi mới lưu:

- **Header:** đủ Vị trí (role dạng đầy đủ), Email, Ngày sinh hoặc placeholder; dòng Ngoại ngữ, Chứng chỉ khi input / CV có.
- **Short Bio:** đạt `write-bio.md` §5.
- **Core Skills:** nhãn domain in đậm; skill chính (framework / platform, ngôn ngữ, database, cloud) có số năm hoặc `(_… năm/tháng_)`, skill phụ chỉ ghi tên, skill JD yêu cầu số năm ghi theo JD (`output.md` §2); có JD thì domain khớp JD đứng trước; số năm không vượt tổng.
- **Projects:** chỉ có khi input có dự án; 1–2 dự án; Mô tả đạt checklist `projects.md` §6 (ý thiếu nằm trong khối nhắc); `Vai trò trong dự án` chỉ chứa việc member làm; Tech Stack là stack thật (`projects.md` §5).
- **File:** đúng mẫu tên `short-bio-[ten-kebab]-[YYYY-MM-DD].md`, không tạo file nào khác.
- **Khối nhắc:** đủ placeholder, ý suy luận, điều chỉnh theo JD và yêu cầu checklist chưa có bằng chứng.
