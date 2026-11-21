---
name: mvi-android
description: The Android MVI pattern for Caffeine (immutable State data class, sealed Intent, ViewModel as Store with StateFlow, one-shot Effects channel, Repository interface). Same shape as mvi-ios. Read by android-developer and backend-lead (review).
---

# MVI on Android (Kotlin, Compose)

Same concept as `mvi-ios`, so a reader fluent in one can read the other.

```kotlin
data class HomeState(
    val hero: BudgetHero = BudgetHero.Loading,
    val recent: List<TransactionRow> = emptyList(),
    val alert: HomeAlert? = null,
)

sealed interface HomeIntent {
    data object Appeared : HomeIntent
    data object SeeAllTapped : HomeIntent
    data class TransactionTapped(val id: String) : HomeIntent
}

sealed interface HomeEffect { data object OpenHistory : HomeEffect }

class HomeViewModel(
    private val transactions: TransactionRepository,
    private val clock: Clock,
) : ViewModel() {
    private val _state = MutableStateFlow(HomeState())
    val state: StateFlow<HomeState> = _state.asStateFlow()
    private val _effects = Channel<HomeEffect>(Channel.BUFFERED)
    val effects = _effects.receiveAsFlow()

    fun onIntent(intent: HomeIntent) {
        when (intent) {
            HomeIntent.Appeared -> load()
            HomeIntent.SeeAllTapped -> viewModelScope.launch { _effects.send(HomeEffect.OpenHistory) }
            is HomeIntent.TransactionTapped -> Unit
        }
    }
    private fun load() = viewModelScope.launch { /* repository, then _state.update { ... } */ }
}

@Composable
fun HomeRoute(viewModel: HomeViewModel, onOpenHistory: () -> Unit) {
    val state by viewModel.state.collectAsStateWithLifecycle()
    HomeScreen(state = state, onIntent = viewModel::onIntent)
}
```

## Rules
- Stateless `XxxScreen(state, onIntent)` composables; `XxxRoute` wires the ViewModel. Previews use the stateless screen.
- One-shot events (navigation, snackbar) go through the Effects channel, never in State.
- No `launch` inside composables to call the ViewModel. No Room/DAO imports in ViewModels or composables.
- Inject `Clock`, `ZoneId` and dispatchers (Hilt) so maths and coroutines are testable.
- Name mapping with iOS: Store ↔ ViewModel, `send` ↔ `onIntent`, `Decimal` ↔ `BigDecimal`, `#Preview` ↔ `@Preview`.
