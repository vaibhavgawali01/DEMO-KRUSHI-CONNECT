# 🌱 Krushi Seva Kendra Store Web Application (कृषी सेवा केंद्र)

> *"शेतकऱ्यांच्या सेवेसाठी, शेतीच्या प्रगतीसाठी." / "Serving Farmers, Supporting Better Farming."*

A full-stack, enterprise-grade, secure, and mobile-responsive e-commerce, credit ledger, and farming advisory platform tailored specifically for agricultural retail stores (**Krushi Seva Kendra**). 

Built using **Java & Spring Boot 3**, **Spring Data JPA / Hibernate**, **Spring Security**, **Thymeleaf**, **PostgreSQL (MySQL and H2 drivers are also available)**, **Bootstrap 5**, **Chart.js**, and **Vanilla JavaScript**.

---

## 🌟 Key Highlights & Modules

### 1. 🌾 Customer & Farmer Storefront
- **Agricultural Product Catalog**: Certified seeds, chemical and water-soluble fertilizers, insecticides, fungicides, weedicides, battery sprayers, drip irrigation kits, cattle feed, and organic bio-stimulants.
- **Dynamic Search & Filtering**: Live search autocomplete with instant product lookup, filter by category, company/brand, price range, and stock availability.
- **Detailed Product Specifications**: Technical dosage instructions, application timings, batch numbers, expiry dates, GST rates, verified farmer reviews, and 5-star rating submissions.
- **Shopping Cart & 1-Click Checkout**: Live quantity adjustments, promo coupon code engine, automated GST calculation (CGST + SGST split), and flexible payment selection.
- **Payment Options**: Cash on Delivery / Counter Pickup, Dynamic UPI QR Code generator (Google Pay, PhonePe, Paytm, BHIM), and Udhari (Credit Ledger).

### 2. 📒 Comprehensive Udhari (Credit) Management System
- **Real-Time Customer Credit Ledger**: Complete audit trail of total credit issued, paid amount, and remaining due balance.
- **Payment Term & Overdue Tracking**: Configurable due dates (e.g. 30 days) with automatic overdue detection and alert flags.
- **Partial & Full Payment Recording**: Record payments via Cash, UPI, or Bank Transfer with instant printable payment receipts.
- **In-App Reminders**: In-app reminders are supported. External WhatsApp, SMS, and email delivery require a provider integration and are currently unavailable.

### 3. 🧾 Automated GST Billing & Invoicing
- **Professional Printable Tax Invoices**: Standard compliant invoices including Shop Name, GSTIN, HSN/SAC codes, customer address, itemized rate, quantity, tax rate, CGST, SGST, grand total, and authorized signature box.
- **Official Payment Receipts**: Downloadable receipts for credit settlements and counter purchases.

### 4. 🌦️ Smart Farming Advisory Hub
- **Fertilizer Calculator**: Provides indicative N-P₂O₅-K₂O and fertilizer-bag estimates from simplified crop and soil assumptions. It is not a soil-test-based or certified agronomic recommendation; farmers should follow product labels and local agricultural advice.
- **Weather Advisory**: Sample weather information; this is not a live forecast or weather-provider integration.
- **Integrated Pest Management (IPM) Guide**: Symptoms, affected crops, chemical control measures, and biological/organic remedies for major agricultural pests.

### 5. 🔐 Role-Based Security & Farmer Registration
- **Role-Based Access Control**: `ROLE_ADMIN` (Store Owner / Staff) and `ROLE_CUSTOMER` (Farmers).
- **Dual-Login Support**: Farmers can authenticate using either their **10-digit mobile number** or **email address**.
- **BCrypt Password Hashing**, CSRF protection, and persistent Remember-Me authentication.

### 6. 📊 Admin Management Control Center
- **Admin Dashboard**: KPI summary tiles and low-stock alerts, with sales and payment reports available through the reports center.
- **Product & Category CRUD**: Full lifecycle management with SKU, barcode auto-generator/hardware scanner, batch tracking, and minimum stock threshold alerts.
- **Inventory & Expiry Monitoring**: Audit logs for stock-in / stock-out transactions, low stock warnings, and expired product tracker with 30/60/90-day filters.
- **Customer Directory**: Complete farmer directory with purchase history and credit status.
- **Reports Center**: Date-range filtered sales, inventory valuation, Udhari ledger, and gross profit reports with **1-click CSV exports**.
- **Database Backup**: Backup export is currently unavailable because no database dump provider is configured.

### 7. 🌐 Bilingual & Modern UI/UX
- **Marathi (मराठी) & English Localization**: Seamless toggleable language selector with complete i18n dictionaries.
- **High-Contrast Dark Mode**: Eye-friendly dark theme with `localStorage` persistence.
- **Mobile-Responsive**: Optimized for mobile phones, tablets, POS terminals, and desktop displays.

---

## 🛠️ Technology Stack & Architecture

| Layer | Technology |
|---|---|
| **Backend Framework** | Java 17+, Spring Boot 3.5.16 |
| **Security & Auth** | Spring Security 6, BCrypt Password Encoder |
| **Persistence & ORM** | Spring Data JPA, Hibernate |
| **Databases** | PostgreSQL (active configuration); MySQL and H2 drivers are included but not enabled by default |
| **Server** | Embedded Apache Tomcat in the executable JAR |
| **Frontend Templates** | Thymeleaf 3 + Thymeleaf Extras Spring Security |
| **UI Framework** | Bootstrap 5.3, Bootstrap Icons 1.11, Custom Agri Theme |
| **Data Visuals** | Chart.js 4.4 |
| **Build Tool** | Apache Maven 3.8+ |

### Layered Architecture
```
com.krushisevakendra
├── KrushiSevaApplication.java      [Main Spring Boot Entry Point]
├── config/                         [Security, WebMvc i18n, DataInitializer]
├── controller/                     [Home, Auth, Cart, Customer, Admin, REST API]
├── dto/                            [Registration, Checkout, Cart, Udhari, Fertilizer]
├── entity/                         [User, Role, Category, Product, Order, Udhari, etc.]
├── enums/                          [OrderStatus, PaymentMethod, UdhariStatus, etc.]
├── exception/                      [GlobalExceptionHandler, ResourceNotFoundException]
├── repository/                     [Spring Data JPA Repositories]
├── security/                       [CustomUserDetailsService, CustomUserDetails, SecurityUtil]
└── service/                        [Service Interfaces & Implementations]
```

---

## 🚀 Getting Started & Execution

### 1. Prerequisites
- **Java Development Kit (JDK 17 or higher)** installed (`java -version`)
- **Apache Maven 3.8+** installed (`mvn -version`)
- *(Optional, if switching the database configuration)* **MySQL Server 8.0+**

---

### 2. Running the Application
The checked-in configuration connects to the configured PostgreSQL database and listens on port 8082. Supply its password using `DB_PASSWORD`. If your Supabase project uses a different database user, set `DB_USERNAME` to the user shown in the Supabase connection settings (for the session pooler, this is commonly `postgres.<project-ref>`). `SPRING_DATASOURCE_URL` can override the JDBC URL when you use a different Supabase endpoint. The database must be reachable from the host. For a new/empty database, configure `APP_BOOTSTRAP_ADMIN_PASSWORD` so the initial administrator can be created. Never commit credentials or paste production credentials into logs or support requests.

PowerShell:
```powershell
$env:DB_PASSWORD = "your-database-password"
$env:DB_USERNAME = "postgres.your-project-ref" # only if different from the configured default
# Set this only if using a different Supabase JDBC endpoint:
# $env:SPRING_DATASOURCE_URL = "jdbc:postgresql://<host>:5432/postgres?sslmode=require"
$env:APP_BOOTSTRAP_ADMIN_PASSWORD = "a-unique-strong-initial-admin-password"
# Configure this only when creating the first admin in an empty database.
# Optional but recommended: set a long, random stable key for remember-me cookies.
$env:APP_REMEMBER_ME_KEY = "a-long-random-private-value"
# Disable template caching only during local development.
$env:SPRING_THYMELEAF_CACHE = "false"
$env:APP_BOOTSTRAP_DEMO_DATA = "false"
mvn spring-boot:run
```

POSIX shell:
```bash
export DB_PASSWORD='your-database-password'
export DB_USERNAME='postgres.your-project-ref' # only if different from the configured default
# Set this only if using a different Supabase JDBC endpoint:
# export SPRING_DATASOURCE_URL='jdbc:postgresql://<host>:5432/postgres?sslmode=require'
export APP_BOOTSTRAP_ADMIN_PASSWORD='a-unique-strong-initial-admin-password'
# Configure this only when creating the first admin in an empty database.
# Optional but recommended: set a long, random stable key for remember-me cookies.
export APP_REMEMBER_ME_KEY='a-long-random-private-value'
# Disable template caching only during local development.
export SPRING_THYMELEAF_CACHE=false
export APP_BOOTSTRAP_DEMO_DATA=false
mvn spring-boot:run
```

Open **`http://localhost:8082`** after startup. If `APP_REMEMBER_ME_KEY` is unset, remember-me cookies are invalidated when the application restarts. Configure the key from a secret manager or deployment environment; do not use the example placeholder.

### Local development with disposable H2

To run without the configured PostgreSQL service, activate the `local` profile. It uses an in-memory H2 database; all local database records are erased when the process stops. This does not change the default PostgreSQL profile or relax login/role permissions.

PowerShell:
```powershell
$env:SPRING_PROFILES_ACTIVE = "local"
$env:APP_BOOTSTRAP_ADMIN_PASSWORD = "choose-a-strong-local-admin-password"
mvn spring-boot:run
```

POSIX shell:
```bash
export SPRING_PROFILES_ACTIVE=local
export APP_BOOTSTRAP_ADMIN_PASSWORD='choose-a-strong-local-admin-password'
mvn spring-boot:run
```

After the `Started KrushiSevaApplication` message appears, open **`http://localhost:8082`**. Use the configured admin password to sign in. The local profile does not include demo accounts or products; add data through the authenticated admin interface. Clear `SPRING_PROFILES_ACTIVE` to return to the default PostgreSQL configuration.

### Database setup and schema changes

- The default configuration uses PostgreSQL. Ensure the database exists and the configured database user has the required schema privileges before starting the application.
- Hibernate is configured with `spring.jpa.hibernate.ddl-auto=update`; Spring SQL initialization is disabled (`spring.sql.init.mode=never`). `src/main/resources/schema.sql` is not automatically executed by this configuration.
- Before deploying schema-affecting changes, take and verify a database backup. Review the generated schema changes in a staging copy first; Hibernate `update` is not a substitute for versioned, reviewed migrations and it does not provide rollback.
- For production, use an explicit migration process and set `SPRING_JPA_HIBERNATE_DDL_AUTO=validate` after the schema has been migrated. The application does not currently include Flyway or Liquibase.
- `APP_BOOTSTRAP_DEMO_DATA` defaults to `false`. Only turn it on for a disposable demonstration database; turning it off later does not remove seeded records.

---
### 3. Building the Executable JAR

The current Maven configuration packages an executable JAR; external Tomcat/WAR deployment is not configured.

```bash
mvn clean package
```

PowerShell (set the same required database/admin variables described above):
```powershell
$env:DB_PASSWORD = "your-database-password"
$env:APP_BOOTSTRAP_ADMIN_PASSWORD = "a-unique-strong-initial-admin-password"
java -jar target/krushi-seva-kendra-1.0.0.jar
```

POSIX shell:
```bash
export DB_PASSWORD='your-database-password'
export APP_BOOTSTRAP_ADMIN_PASSWORD='a-unique-strong-initial-admin-password'
java -jar target/krushi-seva-kendra-1.0.0.jar
```

---

## Administrator Bootstrap

The first administrator account (`admin@krushiseva.com`) is created only when `APP_BOOTSTRAP_ADMIN_PASSWORD` is configured. Subsequent application starts preserve the existing password. There is no default administrator password; log in using the configured password and the account's email address or mobile number.

Sample farmer accounts, catalog products, offers, and transactions are **not** seeded by default. To populate a disposable demonstration database with sample data, set `APP_BOOTSTRAP_DEMO_DATA=true` before first startup. Demo records are not automatically removed if the setting is later turned off; do not enable demo seeding on a production database.

---
## 📡 REST API Reference

| Endpoint | Method | Description | Access |
|---|---|---|---|
| `/api/products` | `GET` | Retrieve list of active products | Public |
| `/api/products/{id}` | `GET` | Retrieve product details by ID | Public |
| `/api/products/barcode/{barcode}` | `GET` | Scanned barcode lookup for POS & inventory | Admin |
| `/api/products/search?q={query}` | `GET` | Live autocomplete search results | Public |
| `/api/categories` | `GET` | List all active agricultural categories | Public |
| `/api/farming/weather?city={city}` | `GET` | Get sample weather data and a non-live advisory | Public |
| `/api/farming/fertilizer-calc` | `GET` | Calculate NPK dosage & commercial bag quantities | Public |
| `/api/admin/reminders/send` | `POST` | Create an in-app reminder; external delivery is unavailable until a provider is configured | Admin |

---

## 📋 Comprehensive Feature Walkthrough

1. **Farmer Experience**:
   - Visit `http://localhost:8082/`
   - Switch language to **मराठी** or toggle **Dark Mode** at the top right navbar.
   - Filter products by **Seeds** or **Fertilizers**, or search for "Cotton" or "Urea".
   - Click a product to review **Agronomic Usage & Spraying Guidelines** and submit a **Farmer Review**.
   - Add items to the cart, apply coupon `KHARIF10`, and proceed to checkout.
   - Select **UPI QR Scan** or **Udhari (Credit Ledger)** and place the order.
   - Navigate to **Farmer Dashboard** &rarr; **My Orders** to download the printable **GST Tax Invoice**.
   - Navigate to **My Udhari** to inspect current credit balance and payment receipts.

2. **Admin Operations**:
   - Login using the administrator password configured with `APP_BOOTSTRAP_ADMIN_PASSWORD` &rarr; Redirected to `/admin/dashboard`.
   - Review KPI tiles and low-stock alerts.
   - Navigate to **Products** to add new agricultural items or trigger quick stock adjustments.
   - Navigate to **Udhari Manager** to record customer payments or create an in-app reminder. External WhatsApp/SMS delivery is not configured.
   - Navigate to **Reports Center** to view date-range sales and download **CSV reports**.
   - Navigate to **Database Backup** to review backup availability. Export is unavailable until a dump provider is configured.
