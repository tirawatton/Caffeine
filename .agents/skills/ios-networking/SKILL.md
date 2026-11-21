---
name: ios-networking
description: Networking and API integration for Caffeine iOS - an APIClient actor on URLSession async/await inside the data layer, Codable with decimal-string money and RFC 3339 dates, problem-details error mapping, auth token injection with single-flight refresh, idempotency keys, retry with backoff and jitter, timeouts and cancellation, NWPathMonitor connectivity, the outbox sync worker, and URLProtocol-based tests. Loaded by ios-developer.
---

# iOS — Networking and API Integration

Follows `api-contract` (endpoints, formats) and `ios-security` §5 (ATS, pinning). No third-party HTTP library.

## Where it lives
`Sources/Networking/` — `APIClient`, endpoints, DTOs. Only **repositories** call the API client; Stores and Views never do (`mvi-ios`). DTOs are mapped to domain structs in the repository; DTOs never reach the UI.

## APIClient
```swift
actor APIClient {
    private let session: URLSession          // ephemeral config, pinned via NSPinnedDomains, timeouts set
    private let baseURL: URL
    private let tokens: TokenStore           // Keychain-backed actor (ios-security §4)
    private var refreshTask: Task<Void, Error>?   // single-flight refresh

    func send<Response: Decodable & Sendable>(_ endpoint: Endpoint<Response>) async throws -> Response
}
```
- `URLSessionConfiguration.ephemeral` (no disk cache of financial responses), `timeoutIntervalForRequest = 15`, `waitsForConnectivity = false` (the outbox handles offline).
- `try await session.data(for: request)`; check `HTTPURLResponse.statusCode`; decode `application/problem+json` into `APIError(code:status:)`.
- **401:** start (or join) one `refreshTask`, retry the request once; second 401 → sign-out flow.
- **Idempotency:** every mutating request carries the outbox item's `Idempotency-Key`.
- **Retry:** only for network errors, 408, 429 (honour `Retry-After`) and 5xx on idempotent or keyed requests; exponential backoff with full jitter, max 3 attempts. Never retry 4xx.
- **Cancellation:** the caller's task cancellation cancels the request; `URLError.cancelled` is not an error state.

## Codable
- One shared `JSONDecoder`/`JSONEncoder`: `.iso8601` with fractional seconds handled, `keyDecodingStrategy` explicit per DTO (`CodingKeys`) — no `convertFromSnakeCase` surprises.
- Money DTO: `struct MoneyDTO: Codable { let amount: String; let currency: String }` → `Decimal(string:locale: Locale(identifier: "en_US_POSIX"))`; invalid → decoding error, never 0.
- Restricted fields arrive as base64 ciphertext and are opened with the E2E key in the repository (`ios-security` §2).

## Connectivity and sync
- `NWPathMonitor` wrapped in an `AsyncStream<Bool>`; the UI shows the Offline state from it (Space pill / 1G).
- Outbox: a SwiftData `OutboxItem` (operation, payload ciphertext, idempotency key, attempts) written in the same save as the change. A `SyncWorker` actor drains it when online and on `.active`, in order, then pulls `GET /sync?since=`. Background drain via the backup/refresh task (`ios-app-lifecycle`).
- Conflicts per `api-contract`; `412` → refetch, merge, retry.

## Testing
- `URLProtocol` stub registered on a test `URLSessionConfiguration`; no real network in unit tests.
- Decode every example payload in `docs/api/openapi.yaml`; test 401-refresh-retry, 429 backoff, problem-details mapping, cancellation, and outbox ordering.
