# Feature Gap Analysis

**Date:** 2026-10-16  
**Project purpose used for prioritization:** Agricultural retail storefront and store operations for catalog/orders, inventory, customer credit, billing, and farming information. The project README and current implementation were available; no separate business requirements or acceptance criteria were present.

## 1. Essential Improvements

| Finding | Why it matters to this project | Status |
|---|---|---|
| Demo farmers with fixed sample passwords were created on a fresh database by default. | Predictable sample credentials should not be provisioned into a real store's customer database. | **Implemented:** demo data seeding is opt-in with `APP_BOOTSTRAP_DEMO_DATA=true`; the default is false. This only affects initialization and does not remove sample data already present in an existing database. |
| Fertilizer area was not validated by the service: null, zero, and negative values were silently changed to one acre, while the UI allowed 0.25–100 acres. | The calculator supports farm input decisions. A plausible result for a different area can lead to a materially wrong estimate. Enforce the UI's declared range at the shared service boundary for both page and API calls. | **Implemented:** accepts finite 0.25–100 acre values and returns a clear invalid-argument error otherwise. |
| “Basal Stage” appeared selectable although calculations always used the full-season schedule. | A farmer could reasonably expect a planting-time dose and receive a full-season estimate. Do not present an unsupported result as if it were stage-aware. | **Implemented:** removed the unsupported choice, disclosed full-season-only behavior, and reject unsupported stage values in the service/API. |
| Calculator and FAQ language implied exact or certified agronomic recommendations without evidence of validated data sources. | Farmers may use recommendations to make real purchasing/application decisions. The app should distinguish illustrative estimates from local, soil-test-based advice. | **Implemented:** UI, FAQ, and README describe estimates and direct users to labels/local advice. |
| No automated test source files existed. | Checkout, stock, payments, and credit balances are financially consequential. Without regression checks, changes can silently break store operations. | **Partially addressed:** added focused fertilizer-service tests for baseline calculations, area/soil adjustments, supported boundaries, and rejected inputs/stages. Other domain workflows still need a test suite. |
| Production readiness depends on recoverable data and controlled schema changes, but backup export is unavailable and Hibernate schema update is configured. | Orders, payments, and Udhari records are business records. A store needs a tested recovery path and predictable schema changes before relying on the system operationally. | **Not implemented:** requires owner decisions about backup destination, retention, encryption/access, restore process, and migration policy. Do not claim this is ready for production use. |

## 2. Recommended Improvements

| Finding | Why it matters to this project | Suggested implementation |
|---|---|---|
| Build out integration tests for account registration/login, product and category CRUD, checkout, stock concurrency, Udhari payments, order ownership, reports, and notifications. | These workflows connect Spring MVC, security, services, repositories, and PostgreSQL; service-only tests do not validate those boundaries. | Use disposable test data and an isolated database; assert response, persisted state, authorization, error and success messages. Include PostgreSQL-compatible tests before deployment. |
| Verify crop/soil/stage fertilizer values and bag-conversion formulas with a qualified local agronomist and cited sources. | Existing recommendations are hard-coded; their stage behavior is not modeled and their accuracy has not been independently established. | Version the source and effective date of reviewed recommendations; implement only reviewed schedules and keep estimates explicitly qualified. |
| Introduce versioned database migrations and a documented restore drill. | `ddl-auto=update` does not provide reviewable, repeatable production schema changes; a backup file is only useful if restore has been tested. | Select a migration framework and establish tested backup/retention/restore ownership before production rollout. |
| Normalize email identity and handle duplicate customer contact updates explicitly. | Registration and admin edits currently depend on database uniqueness and exact identifier lookup. Case variants may behave inconsistently, while duplicate admin edits can surface as database errors. | Decide account identity rules, migrate/resolve any existing conflicts, and enforce the same canonicalization on create, edit, and login. |
| Add administrator audit history for sensitive changes. | Stock adjustments, credit settlements, payment verification, and customer account edits affect financial and inventory records. | Persist actor, action, record, before/after values, timestamp, and reason; define retention and access permissions. |
| Add a real password-reset/recovery flow. | The current page only directs customers to contact the store, which is operationally manual. | Choose verified contact channel, token expiry, abuse controls, and support process before implementation. |

## 3. Optional Advanced Features

| Feature | Why it may fit | Dependency / design choice |
|---|---|---|
| Payment gateway and verified UPI reconciliation | Could reduce manual settlement handling for customer checkout. | Requires provider choice, sandbox/production credentials, webhook signature validation, idempotency, refund handling, and reconciliation rules. Never trust a transaction reference alone. |
| Live weather and localized alerts | Could make farming advisories timely for the local farming audience. | Requires a data provider, location policy, API credentials, attribution, stale-data behavior, and advisory review. |
| WhatsApp, SMS, or email reminders | Could improve Udhari collection workflows. | Requires provider/channel choices, consent and opt-out policy, delivery/error states, templates/languages, and credentials. In-app reminders are available today. |
| Offline/PWA or POS mode | May help shop-counter use during connectivity issues. | Requires conflict resolution, device security, and sync semantics for stock, prices, and payments. |
| Barcode-device integration and bulk catalog import | Could accelerate stock intake and catalog maintenance. | Depends on target scanner/import formats and validation rules; current manual product and barcode fields remain usable. |
| Multi-branch inventory and staff permissions | Could support business growth beyond a single shop/admin model. | Requires branch ownership, stock-transfer, role/permission, and reporting semantics. |

## Changes Made and Test Evidence

- `FarmingServiceImpl` now rejects invalid area inputs outside 0.25–100 acres and unsupported crop stages instead of silently returning a potentially misleading calculation.
- The calculator exposes only full-season estimates, requires an area value in the form, and explains the limits in English and Marathi. FAQ and README claims were corrected to describe estimates rather than exact/certified guidance.
- Added `FarmingServiceImplTest` and `DataInitializerTest`.
- Verification: `mvn test` passed: **6 tests, 0 failures, 0 errors, 0 skipped** (5 fertilizer-calculation tests and 1 demo-seed opt-out test). `git diff --check` passed.
- Browser/runtime verification remains **blocked**: the application did not start as a detected Java debug session in the previous runtime attempt and local app ports were unavailable. No full checkout, CRUD, API/database integration, or external-provider workflow is claimed as tested.
- Demo seeding is skipped on first initialization by default; existing demo records are retained, not deleted. Do not assume setting the flag off sanitizes a populated database.

## Deliberately Deferred Decisions

No payment gateway, backup storage, external notification service, live-weather provider, migration framework, or crop-stage agronomic schedule was selected or configured. Implementing these without the provider credentials, operational policy, or reviewed domain data would risk false payment status, unrecoverable backups, unwanted messages, misleading forecasts, unsafe schema changes, or incorrect application advice.
