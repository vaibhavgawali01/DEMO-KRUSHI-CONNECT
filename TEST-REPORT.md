# Application Test Report

**Date:** 2026-10-17  
**Scope:** Existing application pages, navigation, forms, APIs, authentication, CRUD, persistence, and user workflows.  
**Test environment:** An isolated H2 in-memory launch was attempted to avoid modifying the configured external PostgreSQL database.

## Summary

| Status | Result |
|---|---|
| Passed | `mvn test`: 9 tests, 0 failures, 0 errors, 0 skipped. `mvn package`: `BUILD SUCCESS` and executable JAR produced. `node --check` passed for `admin.js`, `app.js`, and `premium.js`; `git diff --check` passed. |
| Failed | No application workflow failure was confirmed. |
| Blocked | Runtime launch and all browser/HTTP/database workflow execution. A fresh isolated H2 launch attempt for final QA did not yield a detected debug session within 120 seconds; one subsequent session check found none, and opening `http://localhost:18082/` returned `ERR_CONNECTION_REFUSED`. No automatic retry was made. |
| Not Tested | Behavior requiring an active application, persisted test data, valid user sessions, database assertions, or external service credentials. |

The launch attempt used an in-memory H2 database and a disposable bootstrap password. It did not intentionally connect to or mutate the configured external database. The launch result is **unconfirmed**, not evidence of a specific application defect. No automatic relaunch was attempted.

## Workflow Coverage

“Blocked” means a runtime test was intended but could not be executed because the application was not available. “Not Tested” means the behavior was not attempted in this environment, including cases dependent on runtime access or an external provider.

| Area / workflow | Status | Verification needed |
|---|---|---|
| Public home page and featured content | Blocked | Render, links, data, responsive behavior, and empty/error states |
| Catalog, category/brand/price/stock filters, sorting, pagination | Blocked | Valid, invalid, combined, and empty-result searches |
| Product detail, related products, review form | Blocked | Review submission, invalid rating/text, anonymous-user handling, persisted rating/count |
| Offers and coupon discovery | Blocked | Active/expired offers and links to applicable products |
| Farming tips and pest guidance | Blocked | Page rendering and navigation |
| Weather advisory | Blocked | City input and rendered sample data; live-weather integration is not configured |
| Fertilizer calculator | Blocked | Crop, area, soil, stage, boundary/invalid values, and calculated results |
| About, contact, FAQ | Blocked | Page render, contact/map links, and navigation |
| Login, invalid credentials, logout, remember-me | Blocked | Email/mobile login, error/success feedback, session expiry and cookie behavior |
| Registration | Blocked | Valid registration, invalid fields, mismatched passwords, duplicate email/mobile, persisted account |
| Forgot-password page | Blocked | Page and contact guidance; automated password reset is not implemented |
| Cart add/update/remove | Blocked | Valid quantity, zero/negative/excess stock, missing product, success/error feedback |
| Coupon application | Blocked | Valid, invalid, expired, below-minimum, repeated/replaced coupon, discount total |
| Checkout and order creation | Blocked | Valid/invalid form, stock race, totals/tax/discount, delivery snapshot, cart clearing |
| Payment states and order status | Blocked | Cash, UPI/bank pending state, admin verification, invalid transitions, persisted payment |
| Customer dashboard, orders, details, invoices | Blocked | Ownership enforcement, empty states, delivery details, invoice totals |
| Customer Udhari, payment, receipts | Blocked | Balance, partial/full/overpayment, receipt download, ownership |
| Customer notifications | Blocked | Read-one/read-all, unread counts, cross-account access denial |
| Customer profile | Blocked | Valid/invalid edits, persistence, authorization |
| Admin dashboard and navigation | Blocked | Dashboard data, menu targets, role restriction |
| Admin product CRUD and stock adjustments | Blocked | Create/edit/delete, invalid inputs, stock boundaries, persistence |
| Admin category CRUD/status | Blocked | Create/edit/toggle/delete and dependent-product behavior |
| Admin inventory and expiry pages | Blocked | Filtering, quantity adjustments, empty states |
| Admin customer list/details/edit | Blocked | Search, pagination, edits, access control |
| Admin order list/details/status/payment status | Blocked | Search/filter, invalid transitions, audit/payment effects |
| Admin Udhari create/edit/payment/reminder | Blocked | Valid/invalid balances, due dates, notifications and persistence |
| Admin payments and reports/CSV export | Blocked | Search, date filters, totals, valid CSV/download |
| Admin offers CRUD/toggle | Blocked | Valid/invalid coupon rules and persisted status |
| Admin backup page/trigger/download | Blocked | UI can render; export provider is not configured, so successful backup is not available |
| Public product/category/search/barcode APIs | Blocked | HTTP status/body, missing records, serialization, search bounds |
| Weather/fertilizer APIs | Blocked | HTTP status/body, valid and invalid query parameters |
| Admin reminder API | Blocked | Authorization and response; external reminder delivery is unsupported |
| Localization, theme toggle, responsive layout, menus | Blocked | Browser interaction and persistence across pages |
| External database/provider integrations | Not Tested | Requires explicitly configured credentials/services; no external system was contacted |

## Final QA Checks Completed

- **Automated tests:** `mvn test` passed: 9 tests, 0 failures, 0 errors, 0 skipped. This includes unit tests for demo-data opt-out, fertilizer inputs, active product lookup, and public product DTO field exposure.
- **Production packaging:** `mvn package` completed with `BUILD SUCCESS` and created `target/krushi-seva-kendra-1.0.0.jar`.
- **Frontend JavaScript syntax:** `node --check` succeeded for `admin.js`, `app.js`, and `premium.js`.
- **Patch formatting:** `git diff --check` succeeded.
- **Responsive/browser QA:** Not run at mobile, tablet, laptop, or desktop viewports because the isolated test application was unavailable. No visual checks, navigation/form interactions, browser-console inspection, network-failure inspection, or browser accessibility checks are claimed as passed.
- **Runtime availability:** The final H2-based launch timed out without a detected debug session. A single status check found no active debug session, and the browser received `ERR_CONNECTION_REFUSED` on port 18082.

## Fixes and Reproduction

No new application behavior was changed for this test request. Since the application could not be run, no functional issue could be reproduced safely and verified before/after a fix. This report does not count static source inspection as a passed workflow test.

## Unavailable Integrations

- Database backups require a configured database dump provider.
- WhatsApp, SMS, and email reminders require an external delivery provider; in-app notifications are the supported path.
- Weather output is sample/static data, not a live forecast.
- A payment gateway is not configured; UPI references must not be treated as payment verification.
- Automated password reset is not configured.

## Next Steps to Complete Runtime Coverage

1. Resolve the Java launch/session startup issue and make the app available on an isolated test database.
2. Add automated integration tests for authentication, cart/checkout, payment state transitions, Udhari accounting, ownership checks, and CRUD.
3. Replay the blocked browser/API workflows with valid seeded test accounts and assert persisted results.
4. Configure sandbox credentials for any external providers before testing their delivery behavior.
