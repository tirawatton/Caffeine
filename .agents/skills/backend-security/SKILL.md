---
name: backend-security
description: How the Caffeine backend (Phase 2 sync and API, built by backend-lead) implements the security standard - identity token verification and short-lived rotating tokens, per-user authorization against OWASP API Top 10, end-to-end encrypted Restricted data, KMS envelope encryption for Confidential data, TLS 1.3 and mTLS, secrets management, privacy-safe audit logging, encrypted backups, PDPA deletion and breach response, and the security gates before production. Loaded by backend-lead.
---

# Backend — Security and Data Protection

Implements `security-standard` on the server. Stack-independent; when Ton picks a stack, map each rule to it in `docs/security/backend-stack.md` before writing code.

## 1. Identity and sessions (ISO 8.5, API2)
- Accept Sign in with Apple / Google identity tokens; verify signature (provider JWKS), `iss`, `aud`, `exp`, `nonce` server-side.
- Issue a short-lived access token (≤ 15 min, signed with a KMS-held key, ES256/EdDSA) and an opaque refresh token (stored hashed, SHA-256), bound to a device id, **rotated on every use with reuse detection** (reuse → revoke the whole family).
- Revocation on sign-out, account deletion and suspicious reuse.

## 2. Authorization (API1 BOLA, API3, API5)
- Every query is scoped by the authenticated `userId` (or household membership checked per request) in the data layer, not only the controller. Object ids are UUIDs, never sequential.
- Responses return only fields the client needs (no mass assignment in, no over-exposure out). Admin functions don't exist on the public API.

## 3. Data protection
| Class | Server storage |
|---|---|
| Restricted | **Client-encrypted ciphertext only** (E2E, AES-256-GCM per `security-standard` §3). The server never holds the user content key and cannot decrypt. |
| Confidential | Application-level envelope encryption: per-tenant DEK (AES-256-GCM) wrapped by a KMS KEK, on top of database encryption at rest |
| Internal | database encryption at rest (KMS) |
- Object storage (slip images, exports, backups): server-side encryption with KMS keys; Restricted blobs arrive already client-encrypted.
- Keys in cloud KMS/HSM; services reach them by workload identity, never static credentials. Rotation per `security-standard` §4.

## 4. Transport and perimeter (ISO 8.20/8.21, API4)
- TLS 1.3 at the edge (1.2 AEAD only as fallback), HSTS `max-age=31536000; includeSubDomains`; mTLS or private networking between services.
- Rate limiting per user and per IP, request body size limits, pagination caps, timeouts on every outbound call (API4, API7 SSRF: no user-supplied URLs fetched).
- Strict input validation against the OpenAPI schema (`api-contract`); reject unknown fields.

## 5. Secrets and supply chain (ISO 8.8, 8.28)
- Secrets in a secrets manager; nothing in the repo, images or env files committed. Secret scanner in CI.
- Dependency and container scanning in CI; high/critical fixed within 30 days. SAST on every PR; DAST against staging before each production release.

## 6. Logging and audit (ISO 8.15)
- Structured logs with request id, user id (pseudonymous), route, status, latency — **no amounts, notes, tokens or ciphertext**.
- Separate append-only audit log for security events (sign-in, token reuse, deletion, key use), retained per policy and access-controlled.

## 7. Backup, deletion, incidents (ISO 8.13, 8.10, PDPA)
- Encrypted backups, restore tested quarterly, retention documented.
- Account deletion: revoke tokens, delete user rows and objects, destroy the user's DEKs (crypto-shredding), purge from backups by expiry; complete within 30 days.
- Incident response runbook in `docs/security/incident.md`; PDPA breach notification to the regulator within 72 hours and to affected users without undue delay when risk is high.

## 8. Gates before production (Ton approves)
Threat model updated; OWASP API Top 10 checklist passed; DAST clean of high/critical; penetration test by an independent party before first public release; data residency decided (Ton).
