---
name: swift-style
description: Swift 6 style and safety rules for Caffeine - strict concurrency, no force unwraps, Decimal money, SwiftLint config, file layout. Read by every iOS agent.
---

# Swift Style

- Swift 6 language mode, `SWIFT_STRICT_CONCURRENCY = complete`, zero warnings. Deployment target **iOS 18.0**.
- No `!`, `try!`, `as!` or implicitly unwrapped optionals in production code.
- Money is `Decimal`. No `Double`/`Float` for amounts, prices, balances, fees, totals.
- Structured concurrency only; no `Task.detached`, no `DispatchQueue.global` for app work. `@unchecked Sendable` needs a comment explaining why it is safe.
- Liquid Glass: `.glassEffect()` behind `if #available(iOS 26, *)`, `Material` fallback on iOS 18–25.
- Strings in `Localizable.xcstrings` (en source, th). No hard-coded user-facing text in Views.
- Every interactive element: `.accessibilityLabel` and `.accessibilityIdentifier("<screen>.<element>")` (same id as Android).
- Layout: `Sources/App`, `Sources/Features/<Feature>/{Views,Store}`, `Sources/Models`, `Sources/Repositories`, `Sources/Shared/{DesignSystem,Components,Formatting}`.
- Functions <= 40 lines, files <= 300 lines (SwiftLint warns, errors at 60/500).
- Lint: `swiftlint lint --strict --config ios-app/.swiftlint.yml`.
- Simulator: set `SIM_ID` to an available iPhone simulator id (`xcrun simctl list devices available`, prefer the newest iOS and one iOS 18 device for the minimum target). Simulator names are duplicated on this Mac, so destinations use `id=`, not `name=`.
