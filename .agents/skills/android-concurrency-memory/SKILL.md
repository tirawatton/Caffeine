---
name: android-concurrency-memory
description: Kotlin coroutines and memory management for Caffeine Android - structured concurrency in viewModelScope, injected dispatchers, suspend vs Flow, StateFlow with stateIn, one-shot effects via Channel, cooperative cancellation, Mutex, avoiding Context and Activity leaks, Compose stability, bitmap memory, caches, and profiling with LeakCanary and the Android Studio profilers. Loaded by android-developer.
---

# Android — Concurrency and Memory

## Coroutines
- **Scopes:** ViewModels use `viewModelScope`; app-wide work an injected `@ApplicationScope CoroutineScope`. Never `GlobalScope`, never `runBlocking` in app code.
- **Dispatchers are injected** (`@IoDispatcher`, `@DefaultDispatcher`) so tests can swap them; repositories switch with `withContext(io)`; CPU work (grouping thousands of rows) on Default; Compose/ViewModel state on Main.
- **API shape:** one-shot = `suspend fun`; observed data = cold `Flow` from Room; the ViewModel exposes `StateFlow<State>` via `stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), initial)`.
- **Effects** (navigate, toast, haptic) through a `Channel<Effect>(Channel.BUFFERED)` exposed as `receiveAsFlow()`, collected in a `LaunchedEffect` — never stored in State.
- **Latest wins:** search and filter use `flatMapLatest`/`collectLatest` or cancel the previous `Job`; debounce search with `debounce(300)`.
- **Cancellation is cooperative:** call `ensureActive()` in loops; always rethrow `CancellationException` (never swallow it in `catch (e: Exception)` — use `runCatching` carefully).
- **Shared mutable state:** `Mutex` / `MutableStateFlow.update {}`; no `synchronized` around suspend code.
- **Parallel reads:** `coroutineScope { val a = async { }; val b = async { } }`.

## Memory
- **No leaks across lifecycles:** ViewModels never hold `Activity`, `View` or composable references; use `@ApplicationContext` only when needed.
- **Compose:** keep State classes stable/immutable so unchanged items skip recomposition; check recomposition counts in Layout Inspector for list rows; `remember` objects you allocate in composition.
- **Bitmaps (slips, receipts, category photos):** decode at display size with `ImageDecoder` + `setTargetSize` (available on minSdk 28); store category photos as ~128dp thumbnails; never keep full-resolution bitmaps in State.
- **Caches:** `LruCache` sized from `maxMemory`, cleared in `onTrimMemory` (`android-app-lifecycle`).
- **Large lists:** paged repository queries (Paging 3 if the ledger can exceed a few thousand rows); don't map everything into UI models up front.

## Profiling (before claiming "fast")
LeakCanary in `debugImplementation` (list it in the lane file for backend-lead review, as any new library); Android Studio **Memory Profiler** (heap returns to baseline after opening/closing a screen 5×), **CPU Profiler** / system trace for main-thread work over 16 ms, JankStats or Macrobenchmark for scroll and startup when a task has a performance AC.
