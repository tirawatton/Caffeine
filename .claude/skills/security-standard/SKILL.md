---
name: security-standard
description: The Caffeine security and data-protection standard every agent follows on iOS, Android and the backend - ISO/IEC 27001:2022 and 27002:2022 control mapping, OWASP MASVS v2 level L2, Thailand PDPA, data classification, the cryptography policy (AES-256-GCM, TLS 1.3, approved and banned algorithms), key management, encryption at rest and in transit and end to end, logging, deletion and the per-feature security definition of done. Loaded by ba, backend-lead, ios-developer, android-developer and qa-engineer.
---

# Caffeine Security Standard

Caffeine holds personal financial data. **Every piece of user data is encrypted at rest, in transit and in backups, on every platform, with the algorithms below — no exceptions without Ton's written approval in `docs/security/exceptions.md`.**

## 1. Standards we follow
| Standard | What it gives us |
|---|---|
| **ISO/IEC 27001:2022** | The management system: risk-based, documented, reviewed controls |
| **ISO/IEC 27002:2022** | The controls (mapping in §8) |
| **ISO/IEC 27701** | Privacy extension (PII controller/processor duties) |
| **ISO/IEC 18033-3 / 19772 / 11770** | Block cipher (AES), authenticated encryption (GCM), key management — matched by NIST FIPS 197, SP 800-38D, SP 800-57 |
| **OWASP MASVS v2, level L2** + MASTG tests | Mobile app requirements: STORAGE, CRYPTO, AUTH, NETWORK, PLATFORM, CODE, RESILIENCE, PRIVACY |
| **OWASP API Security Top 10 (2023)** | Backend API risks |
| **Thailand PDPA (B.E. 2562)** | Consent, purpose limitation, data-subject rights (access, deletion, portability), breach notification within 72 h |
These guide engineering; Caffeine is not certified. Certification would be a business decision for Ton.

## 2. Data classification (ISO 27002 5.12) — every field in a data contract gets one
| Class | Examples | Rule |
|---|---|---|
| **Restricted** | account/card numbers (even masked source), slip images and QR payloads, notes/memos, merchant + location, auth tokens, encryption keys, biometric results | Encrypted at rest **twice** (store-level + field-level AES-256-GCM), end-to-end encrypted before sync, never logged, never in analytics, never in notifications/widgets in clear |
| **Confidential** | amounts, balances, budgets, categories, dates, goals, trips, profile name, income baseline | Store-level encryption at rest, TLS in transit, server-side encryption at rest, masked in Privacy Mode, never logged |
| **Internal** | settings, theme, feature flags, non-identifying counters | Store-level encryption (same store), may appear in diagnostics without user identity |
| **Public** | app version, static copy | no restriction |

## 3. Cryptography policy (ISO 27002 8.24)
| Purpose | Approved | Banned |
|---|---|---|
| Symmetric encryption | **AES-256-GCM**, 96-bit random nonce per message, 128-bit tag, AAD = record id + field name + schema version | ECB, CBC without MAC, DES/3DES, RC4, custom ciphers |
| Hashing / integrity | SHA-256, SHA-384, HMAC-SHA-256 | MD5, SHA-1 for security |
| Key derivation | HKDF-SHA-256 (from a key); Argon2id or PBKDF2-HMAC-SHA-256 ≥ 600,000 iterations (from a passcode) | plain hash of a password |
| Asymmetric / signatures | P-256 ECDH/ECDSA, Ed25519/X25519 | RSA < 3072, hand-rolled curves |
| Transport | **TLS 1.3** (TLS 1.2 with AEAD suites only as server fallback), HSTS, certificate/public-key pinning in apps | TLS ≤ 1.1, cleartext HTTP, disabled certificate checks |
| Randomness | OS CSPRNG (`SecRandomCopyBytes`/CryptoKit, `SecureRandom`, `crypto.randomBytes`/KMS) | `Random`, `Math.random`, timestamps as nonces |
Use platform libraries only (CryptoKit, Android Keystore/Tink, cloud KMS). **Never write crypto primitives yourself.**

## 4. Key management (ISO 27002 8.24, ISO/IEC 11770)
- **Envelope encryption everywhere:** a data-encryption key (DEK) encrypts data; a key-encryption key (KEK) protected by hardware wraps the DEK.
- **Device KEK:** iOS Keychain (Secure Enclave–backed where possible), Android Keystore (StrongBox when available), non-exportable, `ThisDeviceOnly`.
- **Server KEK:** cloud KMS/HSM (FIPS 140-2/3 level 3 HSM where offered), access by service identity only.
- **End-to-end sync key:** a per-user content key, generated on device, never sent to the server in clear; recovery = re-wrap with a key derived from a user recovery secret or a second device (Ton decides the recovery UX before Phase 2).
- **Rotation:** server KEKs yearly or on suspicion; DEKs re-wrapped, not re-encrypted bulk. Rotation steps recorded in `docs/security/keys.md`. **No key, secret or certificate private key in source code, logs, crash reports or the repo.**

## 5. Encryption layers (all must be present)
| Layer | iOS | Android | Backend |
|---|---|---|---|
| Whole local store at rest | SwiftData file under Data Protection `complete` (OS AES-256, passcode-bound) | Room on **SQLCipher** (AES-256), key wrapped by Keystore | Database + disk encryption at rest with KMS keys |
| Restricted fields | CryptoKit AES-GCM field encryption | Tink/JCA AES-GCM field encryption | Stores only client-encrypted ciphertext (E2E) |
| Files (slips, receipts, photos, exports) | encrypted blobs, `complete` protection | encrypted blobs in app-private storage | object storage with SSE-KMS; Restricted blobs are client-encrypted |
| In transit | TLS 1.3 + pinning (ATS on) | TLS 1.3 + pinning (Network Security Config) | TLS 1.3, HSTS, mTLS between services |
| Backups | iCloud/CloudKit: client-encrypted payloads (`encryptedValues` minimum) | Auto Backup excluded for the DB/keys; app backup only client-encrypted | encrypted, access-logged, restore-tested |

## 6. Logging, privacy, deletion
- **Logging (8.15):** no Confidential/Restricted values in logs, crash reports, analytics, notifications or widgets. Log event ids and error codes only. Release builds strip debug logs.
- **Masking (8.11):** Privacy Mode masks every amount; app switcher / recents show a cover when Privacy Mode or App Lock is on.
- **Deletion (8.10, PDPA):** "Delete my data" wipes the local store, files and keys (crypto-shredding: destroying the DEK makes ciphertext unrecoverable) and requests server deletion within 30 days.
- **Consent:** analytics off until consent; purpose stated in the privacy policy.

## 7. Security definition of done (every feature, checked by QA and the lead)
1. Every new field has a classification in the data contract; Restricted fields are field-encrypted.
2. No secret, key or token in code or repo (`grep` and a secret scanner pass).
3. No Confidential/Restricted data in logs, analytics, notifications, widgets or screenshots in recents.
4. All network calls use the API client (TLS 1.3, pinning); no cleartext, no disabled trust checks.
5. Auth tokens only in Keychain / Keystore-encrypted storage, never in UserDefaults / SharedPreferences plain.
6. Feature threat model (STRIDE, 5–10 lines) in `docs/security/<feature>-threats.md`, written by backend-lead with the contract.
7. Security tests for the feature pass (`qa-verification` step 6).

## 8. ISO/IEC 27002:2022 control map for Caffeine
| Control | Where it is implemented |
|---|---|
| 5.12 Classification of information | §2, data contract column |
| 5.34 Privacy and protection of PII | §6, PDPA flows |
| 8.5 Secure authentication | Sign in with Apple / Google, App Lock, token handling (platform skills) |
| 8.10 Information deletion | crypto-shredding, delete-my-data |
| 8.11 Data masking | Privacy Mode, app-switcher cover |
| 8.12 Data leakage prevention | no PII in logs/analytics/widgets, FLAG_SECURE, pasteboard rules |
| 8.13 Information backup | encrypted backups, restore tests |
| 8.15 Logging | §6 |
| 8.20 / 8.21 Network security | TLS 1.3, pinning, mTLS |
| 8.24 Use of cryptography | §3, §4, §5 |
| 8.25 / 8.26 Secure development life cycle, app security requirements | this skill in every stage; threat model per feature |
| 8.28 Secure coding | platform security skills, `code-review` security section |
| 8.29 Security testing | `qa-verification` step 6 (MASTG) |
| 8.8 Technical vulnerabilities | dependency scanning in CI, update within 30 days for high/critical |
