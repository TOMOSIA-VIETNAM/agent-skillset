# Companion skills theo role × số năm

**Chỉ dùng khi có JD** (`jd-match.md` §3 bước 5). Không có JD → không thêm skill nào ngoài profile.

Chọn mốc theo số năm đã chốt sau JD adjustment, lấy skill của mốc đó và các mốc dưới. Chỉ lấy skill liên quan JD — không đổ cả danh sách. Mốc phải khớp số năm: member 1 năm mà có microservices sẽ khiến khách nghi ngờ cả hồ sơ.

Ở Core Skills, companion skill chỉ ghi tên (`output.md` §2). Mọi companion skill member chưa có → khối nhắc.

## Backend
- 1-2y: framework core, công cụ cơ bản.
- 3-4y: + ORM, testing framework, basic DevOps.
- 5-6y: + design patterns, message queue, caching, security.
- 7+y: + microservices, distributed systems, CI/CD nâng cao, monitoring.
- VD: PHP 4y → Eloquent ORM, PHPUnit. Java 7y → Spring Cloud, Kafka, JUnit, JWT/OAuth2.

## Frontend
Thay framework nếu JD yêu cầu (React ↔ Vue ↔ Angular; Next.js đi với React, Nuxt đi với Vue).
- 1-2y: HTML/CSS, JavaScript/TypeScript, framework core, Git.
- 3-4y: + state management (Redux/Zustand/Pinia), REST API integration, Tailwind/SCSS, Jest/Vitest.
- 5-6y: + Next.js/Nuxt (SSR/SSG), performance (Core Web Vitals), E2E (Cypress/Playwright), design system/Storybook.
- 7+y: + micro-frontend, monorepo (Nx/Turborepo), FE CI/CD, accessibility/i18n, FE architecture.

## Fullstack
Kết hợp BE + FE cùng mốc nhưng chọn lọc theo JD, không cộng dồn hai danh sách.
- 1-2y: framework BE core + framework FE core, REST API, SQL cơ bản.
- 3-4y: + ORM, state management, Docker cơ bản, unit test cả hai phía.
- 5-6y: + caching, SSR, cloud deploy (AWS/GCP), CI/CD pipeline.
- 7+y: + system design/microservices, monitoring, kiến trúc end-to-end.

## Mobile
Thay platform nếu JD yêu cầu; iOS ↔ Android chỉ thay khi JD rõ ràng; Flutter / RN cross-platform giữ cả hai nếu hợp lý.
- *iOS/Swift:* 1-2y UIKit, Xcode, CocoaPods · 3-4y + CoreData, Alamofire, Push Notification, TestFlight · 5-6y + Combine/RxSwift, MVVM, XCTest, App Store · 7+y + Clean Architecture, Fastlane, SPM.
- *Android/Kotlin:* 1-2y Android SDK, Gradle · 3-4y + Retrofit, Room, Coroutines, LiveData · 5-6y + Jetpack Compose, MVVM/MVI, Firebase, Espresso · 7+y + Clean Architecture, Fastlane/GH Actions, Google Play.
- *Flutter/Dart:* 1-2y Flutter SDK, Dart, Widget tree · 3-4y + Bloc/Provider, Firebase, dio · 5-6y + Clean Architecture, Platform Channels, dual-store · 7+y + CI/CD, custom plugins.
- *React Native:* 1-2y React Native, Expo, JS/TS · 3-4y + Redux/Zustand, Native Modules, React Navigation · 5-6y + Performance, CI/CD, dual-store · 7+y + custom native modules, Clean Architecture.

## QA
Nhận diện loại testing (Manual / Automation / Performance / Mobile / API); thay framework nếu JD yêu cầu. Không có CI/CD setup.
- *Automation:* 1-2y Selenium/Appium, Java/Python, JUnit/TestNG · 3-4y + POM, Allure, chạy test trong CI pipeline (không set up) · 5-6y + framework design, BDD/Cucumber, JMeter, Postman/RestAssured · 7+y + test architecture, multi-framework, QA process design, mentoring.
- *Manual:* 1-2y test case design, Jira, TestRail, cross-browser/device · 3-4y + Postman, test planning, regression/smoke/sanity · 5-6y + risk-based testing, test strategy, JMeter cơ bản · 7+y + QA process design, team lead, release optimization.
