---
name: ios-concurrency-memory
description: Swift 6 concurrency and memory management for Caffeine iOS - async/await, actor isolation, MainActor Stores, @ModelActor repositories, Sendable, structured concurrency and cancellation, AsyncStream, continuations, ARC and retain cycles, image memory, caches, and how to profile with Instruments. Loaded by ios-developer.
---

# iOS — Concurrency and Memory

## Concurrency (Swift 6, strict concurrency complete)
- **Isolation map:** Views and Stores are `@MainActor`. Persistence runs in a `@ModelActor` repository. Pure domain functions are `nonisolated` and `Sendable`. Shared mutable state outside these lives in an `actor`.
- **Only `Sendable` crosses actors:** domain structs and enums, never `@Model` objects or `ModelContext`.
- **Structured first:** `async let` for a fixed set of parallel reads, `withThrowingTaskGroup` for a dynamic set. No `Task.detached`, no `DispatchQueue`, no semaphores or locks around async code.
- **Ownership:** prefer `.task { }` in the View (auto-cancelled). A Store that starts its own `Task` keeps the handle and cancels it when the work is replaced (e.g. new search text) — last request wins.
- **Cancellation is cooperative:** `try Task.checkCancellation()` in loops, treat `CancellationError` as "stop quietly", never as an error state.
- **Streams:** observe data with `AsyncStream`/`AsyncThrowingStream`; finish the continuation and set `onTermination` to release resources.
- **Bridging callbacks:** `withCheckedThrowingContinuation`, resumed exactly once on every path.
- **Debounce search** with `try await Task.sleep(for: .milliseconds(300))` inside a cancellable task — the only acceptable sleep.
- **`@unchecked Sendable`** only with a comment proving safety (rule in `swift-style`).

## Memory
- **Value types by default** (State, domain models). Classes only for Stores, repositories, caches.
- **Retain cycles:** a closure stored by an object that it captures needs `[weak self]` (timers, NotificationCenter tokens, stored callbacks). A `Task` stored on a Store that captures `self` keeps the Store alive until it ends — cancel it, or capture weakly in long loops.
- **Images (slips, receipts, category photos):** downsample with ImageIO (`CGImageSourceCreateThumbnailAtIndex`, `kCGImageSourceThumbnailMaxPixelSize`) to display size; never decode full-resolution photos into `UIImage` for thumbnails. Category photo icons store a ~128pt thumbnail.
- **Caches:** `NSCache` (auto-purges under pressure), keyed by id; no unbounded dictionaries.
- **Large lists:** lazy containers + paged fetches; don't map thousands of rows into view models up front.

## Profiling (before claiming "fast")
Instruments: **Leaks** and **Allocations** (memory graph after opening/closing a screen 5× must return to baseline), **Time Profiler** for main-thread work over 16 ms, **SwiftUI** instrument for excessive body updates, **Hangs** for > 250 ms blocks. Record numbers in the lane file when a task has a performance AC.
