---
name: android-coding-ui-algorithms
description: Everyday Jetpack Compose coding and algorithm rules for Caffeine Android - stateless composables and state hoisting, recomposition-friendly code (remember, derivedStateOf, stable types, lazy list keys), modifier order, BigDecimal money maths, java.time date maths in Asia/Bangkok, grouping and searching ledgers, formatting, and complexity budgets. Loaded by android-developer.
---

# Android — Coding, UI and Algorithms

Pairs with `kotlin-style` (safety rules), `compose-craft` (design → Compose) and `mvi-android` (where logic lives).

## Compose
- **Stateless by default:** a screen composable takes `state: XState` and `onIntent: (XIntent) -> Unit`; only the route composable touches the ViewModel (`collectAsStateWithLifecycle()`).
- **Small composables:** over ~40 lines → extract. Shared pieces take plain parameters, not feature State.
- **Recomposition:** State classes are `@Immutable` data classes with `ImmutableList`/`List` read-only; derived values via `remember(key) { }` or `derivedStateOf` (e.g. "show scroll-to-top"), not recomputed in composition; lambdas that capture changing values use `rememberUpdatedState` in effects.
- **Lazy lists:** `LazyColumn` with `key = { it.id }` and `contentType`; sticky day headers via `stickyHeader`. Never `Column` + `verticalScroll` for unbounded data.
- **Modifier order matters:** size → padding → background/clip → clickable for correct hit areas; touch target ≥ 48dp (`minimumInteractiveComponentSize`).
- **Font scale:** sizes in `sp` from `CaffeineType`; hero amounts use `maxLines = 1` + auto-size (`BasicText` `autoSize` where available, else a measured fallback) as the spec says.
- **Previews:** `@Preview` per state (loading, empty, error, privacy, over budget) × Dark/Light (`uiMode`), plus a large-font preview (`fontScale = 2f`), fed by fake state.

## Algorithms and data
- **Money:** `BigDecimal`, scale 2, rounding mode from `caffeine-domain`; sum with `fold(BigDecimal.ZERO, BigDecimal::add)`; compare with `compareTo`, never `==` (scale-sensitive).
- **Formatting:** `NumberFormat.getCurrencyInstance(locale)` with `Currency.getInstance("THB")`, always signed per the amount colour rule. Never concatenate strings by hand.
- **Dates:** `java.time` (API 26+, fine on minSdk 28). Store `Instant`/epoch millis; compute local days with an injected `Clock` and `ZoneId.of("Asia/Bangkok")`; months and cycles with `YearMonth`, `TemporalAdjusters.lastDayOfMonth()`, never millis arithmetic.
- **Grouping:** `groupBy { it.date.atZone(zone).toLocalDate() }` then sort keys once — O(n log n), in the ViewModel/repository, never in a composable.
- **Search / filter:** precomputed normalized key per row (`Normalizer.normalize(..., NFD)` minus marks, lowercase with `Locale.ROOT`); binary search (`binarySearchBy`) for date ranges on sorted lists.
- **Budgets:** O(1) per row in composition; ≤ O(n log n) per screen load; heavy work on the IO/Default dispatcher (`android-concurrency-memory`).
- **Pure functions** for every `caffeine-domain` calculation, in `shared/` or the feature's `domain/` package, unit-tested with the cases table.
