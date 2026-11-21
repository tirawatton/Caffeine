---
name: api-contract
description: The shared API contract rules for Caffeine - OpenAPI 3.1 as the single source owned by backend-lead, REST conventions, versioning, money as decimal strings with currency, RFC 3339 timestamps, RFC 9457 problem-details errors, idempotency keys, cursor pagination, ETag concurrency, offline sync with an outbox, and what each side may assume. Loaded by backend-lead, ios-developer and android-developer.
---

# API Contract

## Source of truth
- `docs/api/openapi.yaml` (OpenAPI 3.1), owned by **backend-lead**, written in Phase A next to the data contract. Feature notes in `docs/data-model/<feature>-model.md` §8 point to the operations.
- Developers never invent endpoints or fields. A missing or wrong operation → `CONTRACT_RETURNED`.
- External APIs (e.g. a bank slip verification API) are described in the same file under `x-external` with their auth, limits and error mapping.

## Conventions
| Topic | Rule |
|---|---|
| Base | `https://api.<domain>/v1`; breaking change → `/v2`, old version kept ≥ 6 months |
| Resources | plural nouns, UUID ids: `GET /transactions/{id}` |
| Money | `{"amount": "-320.00", "currency": "THB"}` — **string** decimal, never a JSON number |
| Time | RFC 3339 UTC instants (`2026-11-18T02:00:00Z`); local dates as `YYYY-MM-DD` with the zone documented |
| Errors | RFC 9457 `application/problem+json`: `type`, `title`, `status`, `detail`, `instance`, plus `code` (stable, machine-readable) — the app maps `code` to copy, never shows `detail` raw |
| Idempotency | every POST that creates/changes data takes `Idempotency-Key: <uuid>`; server stores the result 24 h |
| Pagination | cursor-based: `?limit=50&cursor=…` → `{"items": [], "nextCursor": "…"}` |
| Concurrency | `ETag` on reads, `If-Match` on updates; `412` → client refetches and merges |
| Sync | `GET /sync?since=<cursor>` returns changes + tombstones; client pushes its outbox in order with idempotency keys |
| Auth | `Authorization: Bearer <access token>`; `401` → refresh once, then sign-out |
| Rate limit | `429` + `Retry-After` |
| Security | all fields carry their classification (`x-classification: restricted|confidential|internal`); Restricted fields are `ciphertext` (base64 of AES-GCM combined) per `security-standard` |

## Offline-first rule (both apps)
The local store is the source of truth for the UI. Writes go to the local store **and** an outbox in one transaction; a sync worker sends the outbox when online. The UI never waits on the network to show a saved transaction. Conflicts: server version wins for shared (household) records, last-writer-wins by `updatedAt` for personal ones, unless the feature contract says otherwise.

## Contract tests
Backend validates requests/responses against `openapi.yaml` in CI. Each app has decoding tests from example payloads in the spec, so iOS and Android parse identical JSON identically.
