---
name: kotlin-style
description: Kotlin style and safety rules for Caffeine Android - no !!, BigDecimal money, coroutines and dispatchers, Detekt/ktlint, package layout, minSdk 28. Read by every Android agent.
---

# Kotlin Style

- Kotlin current stable (check kotlinlang.org releases at the start of each feature and update `gradle/libs.versions.toml`). **minSdk 28**, targetSdk/compileSdk = latest stable API.
- No `!!` and no `lateinit` for nullable state in production code.
- Money is `BigDecimal` (scale 2, `RoundingMode.HALF_UP`). No `Double`/`Float` money.
- Coroutines: `viewModelScope` / injected scopes only; never `GlobalScope`; dispatchers injected (Hilt `@IoDispatcher`).
- DI: Hilt. Navigation: Navigation Compose with type-safe routes.
- Strings in `res/values/strings.xml` and `values-th/`. No hard-coded user-facing text.
- Package `com.tonapps.caffeine`: `features/<feature>/{ui,vm}`, `model`, `repository`, `data/room`, `shared/{theme,components,format}`.
- Lint: `./gradlew detekt ktlintCheck lint`; zero errors.
