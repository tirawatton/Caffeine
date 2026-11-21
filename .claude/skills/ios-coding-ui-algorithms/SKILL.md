---
name: ios-coding-ui-algorithms
description: Everyday SwiftUI coding and algorithm rules for Caffeine iOS - composing small views, state ownership, list identity and performance, custom layout, Decimal money maths, date and calendar maths in Asia/Bangkok, grouping and searching ledgers, formatting, and complexity budgets. Loaded by ios-developer.
---

# iOS — Coding, UI and Algorithms

Pairs with `swift-style` (safety rules), `ios-swiftui-design` (design → native components) and `mvi-ios` (where logic lives).

## SwiftUI views
- **Small views.** A `body` over ~40 lines gets split into subviews (structs, not computed `some View` properties, so SwiftUI can diff them separately).
- **Views are a function of State.** Read `store.state`, send `store.send(_:)`. UI-only state (focus, scroll position, sheet drag) may use `@State`/`@FocusState`.
- **Identity:** `ForEach` over `Identifiable` models with stable `id: UUID`. Never `id: \.self` on values that change, never indices for mutable lists.
- **No `AnyView`.** Use `@ViewBuilder`, `Group`, or an enum switch. Avoid `if` that swaps whole subtrees when a modifier (`opacity`, `disabled`) would keep identity.
- **Lists:** `List` or `LazyVStack` for anything that can exceed one screen; page large fetches through the repository (`fetchLimit`/`fetchOffset`).
- **Layout:** stacks + `Spacer` + spacing tokens first; `ViewThatFits` for "wide vs narrow" (e.g. large amounts); a custom `Layout` only when stacks can't express it. No hard-coded frames except design-specified sizes (tokens).
- **Dynamic Type:** text uses token fonts (`CaffeineFont.*`); hero amounts use `.minimumScaleFactor` + `.lineLimit(1)` as the spec says; test at AX sizes in previews.
- **Previews:** one `#Preview` per state (loading, empty, error, privacy, over budget) in Dark and Light, fed by a fake repository.

## Algorithms and data
- **Money:** `Decimal` only. Round with `NSDecimalRound` (scale 2, mode from `caffeine-domain`); never via `Double`. Sum with `reduce(Decimal.zero, +)`.
- **Formatting:** `Decimal.FormatStyle.Currency(code: "THB")` with an injected `Locale`; always signed per the amount colour rule (`+฿`, `−฿`). Never build strings by hand.
- **Dates:** inject `Calendar` with `timeZone = Asia/Bangkok`; month and cycle boundaries via `calendar.dateInterval(of:for:)` / `date(byAdding:)`, never `86400 * n`. Store instants (UTC `Date`), compute local days at the edge.
- **Grouping:** `Dictionary(grouping:by:)` keyed by `calendar.startOfDay(for:)`, then sort keys once — O(n log n). Do it in the Store/repository, not in `body`.
- **Search / filter:** precompute a lowercase, diacritic-folded search key per row (`folding(options: [.caseInsensitive, .diacriticInsensitive], locale:)`); for date ranges on sorted arrays use binary search (`partitioningIndex`) instead of linear scans.
- **Budgets:** anything per row on the main actor stays O(1); per screen load ≤ O(n log n) on n transactions; heavier work goes to the repository actor (`ios-concurrency-memory`).
- **Pure functions** for every calculation in `caffeine-domain` (budget, pace, cycle, split), in `Sources/Shared/` or the feature's `Domain/` folder, so they are unit-tested with the cases table.
