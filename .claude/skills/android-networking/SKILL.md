---
name: android-networking
description: Networking and API integration for Caffeine Android - Retrofit and OkHttp with kotlinx.serialization in the data layer, decimal-string money and Instant serializers, problem-details error mapping, auth interceptor and Authenticator with single-flight refresh, idempotency keys, retry with backoff and jitter, timeouts and cancellation, ConnectivityManager callbacks, the outbox with WorkManager sync, and MockWebServer tests. Loaded by android-developer.
---

# Android — Networking and API Integration

Follows `api-contract` and `android-security` §5 (Network Security Config, pinning).

## Where it lives
`network/` package — Retrofit service interfaces, DTOs, interceptors. Only **repositories** call the API; ViewModels and composables never do (`mvi-android`). DTOs map to domain models in the repository.

## Stack
- Retrofit + OkHttp + kotlinx.serialization converter (versions in `libs.versions.toml`). `Json { ignoreUnknownKeys = false; explicitNulls = false }` — unknown fields are a contract bug to surface in debug.
- OkHttp: `callTimeout(15, SECONDS)`, no response cache for API routes, logging interceptor **only in debug** at `HEADERS` level (never `BODY`), redacting `Authorization`.
- Interceptors: `AuthInterceptor` (Bearer token from the Tink-encrypted token store), `IdempotencyInterceptor` (key from the outbox item tag). `Authenticator` handles 401: refresh under a `Mutex` (single flight), retry once, second 401 → sign-out.
- Retry: only IOException, 408, 429 (honour `Retry-After`) and 5xx on idempotent or keyed calls; exponential backoff with full jitter, max 3. Never retry 4xx.
- Suspend service functions; cancellation of the calling coroutine cancels the call; `CancellationException` is rethrown, not mapped to an error.

## Serialization
- `@Serializable data class MoneyDto(val amount: String, val currency: String)` → `BigDecimal(amount)`; invalid → error, never zero.
- `Instant` via a custom `KSerializer` (RFC 3339). Problem details (`application/problem+json`) → `ApiError(code, status)`; the app maps `code` to string resources.
- Restricted fields arrive as base64 ciphertext and are opened with the E2E key in the repository (`android-security` §2).

## Connectivity and sync
- `ConnectivityManager.registerDefaultNetworkCallback` exposed as `Flow<Boolean>` (`callbackFlow`) for the Offline state.
- Outbox: a Room `OutboxEntity` written in the same transaction as the change. `SyncWorker` (WorkManager, `NetworkType.CONNECTED`, unique work, exponential backoff) drains it in order, then pulls `GET /sync?since=`; also triggered on app foreground.
- Conflicts per `api-contract`; `412` → refetch, merge, retry.

## Testing
- `MockWebServer` for service + interceptor tests; no real network in unit tests.
- Decode every example payload in `docs/api/openapi.yaml`; test 401-refresh-retry, 429 backoff, problem-details mapping, cancellation, outbox ordering, and WorkManager with `WorkManagerTestInitHelper`.
