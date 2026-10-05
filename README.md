# 🌱 Krushi Seva Kendra Store Web Application (कृषी सेवा केंद्र)

> *"शेतकऱ्यांच्या सेवेसाठी, शेतीच्या प्रगतीसाठी." / "Serving Farmers, Supporting Better Farming."*

A full-stack, enterprise-grade, secure, and mobile-responsive e-commerce, credit ledger, and farming advisory platform tailored specifically for agricultural retail stores (**Krushi Seva Kendra**). 

Built using **Java & Spring Boot 3**, **Spring Data JPA / Hibernate**, **Spring Security**, **Thymeleaf**, **MySQL / H2 Database**, **Bootstrap 5**, **Chart.js**, and **Vanilla JavaScript**.

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
- **Automated & Manual Reminders**: Multi-channel reminder abstractions for **WhatsApp**, **SMS**, **Email**, and **In-App Notifications**.

### 3. 🧾 Automated GST Billing & Invoicing
- **Professional Printable Tax Invoices**: Standard compliant invoices including Shop Name, GSTIN, HSN/SAC codes, customer address, itemized rate, quantity, tax rate, CGST, SGST, grand total, and authorized signature box.
- **Official Payment Receipts**: Downloadable receipts for credit settlements and counter purchases.

### 4. 🌦️ Smart Farming Advisory Hub
- **Smart Fertilizer Requirement Calculator**: Implements state agricultural university (MPKV Rahuri / ICAR) agronomic recommendations. Farmers select Crop (Sugarcane, Cotton, Soybean, Wheat, Onion, Vegetables), Farm Area (Acres), and Soil Type to calculate exact pure N-P-K requirements (kg/acre) and recommended commercial bags (Urea, SSP, MOP vs Complex NPK 10:26:26 / 24:24:0 + Supplementary Urea).
- **Local Agri Weather Forecast**: Live temperature, humidity, wind velocity, precipitation probability, and weather-driven spraying/irrigation advisories.
- **Integrated Pest Management (IPM) Guide**: Symptoms, affected crops, chemical control measures, and biological/organic remedies for major agricultural pests.

### 5. 🔐 Role-Based Security & Farmer Registration
- **Role-Based Access Control**: `ROLE_ADMIN` (Store Owner / Staff) and `ROLE_CUSTOMER` (Farmers).
- **Dual-Login Support**: Farmers can authenticate using either their **10-digit mobile number** or **email address**.
- **BCrypt Password Hashing**, CSRF protection, and persistent Remember-Me authentication.

### 6. 📊 Admin Management Control Center
- **Analytics Dashboard**: Interactive Chart.js graphs for 30-day sales velocity, payment channel distribution, order status breakdown, and KPI summary tiles.
- **Product & Category CRUD**: Full lifecycle management with SKU, barcode auto-generator/hardware scanner, batch tracking, and minimum stock threshold alerts.
- **Inventory & Expiry Monitoring**: Audit logs for stock-in / stock-out transactions, low stock warnings, and expired product tracker with 30/60/90-day filters.
- **Customer Directory**: Complete farmer directory with purchase history and credit status.
- **Reports Center**: Date-range filtered sales, inventory valuation, Udhari ledger, and gross profit reports with **1-click CSV exports**.
- **Database Backup**: 1-click encrypted SQL database dump export and download.

### 7. 🌐 Bilingual & Modern UI/UX
- **Marathi (मराठी) & English Localization**: Seamless toggleable language selector with complete i18n dictionaries.
- **High-Contrast Dark Mode**: Eye-friendly dark theme with `localStorage` persistence.
- **Mobile-Responsive**: Optimized for mobile phones, tablets, POS terminals, and desktop displays.

---

## 🛠️ Technology Stack & Architecture

| Layer | Technology |
|---|---|
| **Backend Framework** | Java 17+, Spring Boot 3.2.5 |
| **Security & Auth** | Spring Security 6, BCrypt Password Encoder |
| **Persistence & ORM** | Spring Data JPA, Hibernate |
| **Databases** | MySQL 8.0+ (Production) / H2 In-Memory (Zero-Config Development) |
| **Server** | Embedded Apache Tomcat (or standalone WAR deployment) |
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
- *(Optional for Production)* **MySQL Server 8.0+**

---

### 2. Running the Application Out of the Box (H2 Development Mode)
The application is pre-configured to run out of the box with zero setup using an embedded in-memory database:

```bash
# Clone or navigate to the project directory
cd "krushi seva"

# Build and start the Spring Boot application
mvn spring-boot:run
```

Once started, open your web browser and navigate to:
👉 **`http://localhost:8080`**

H2 Database Console is accessible at:
👉 **`http://localhost:8080/h2-console`** *(JDBC URL: `jdbc:h2:mem:krushisevadb`, Username: `sa`, Password: empty)*

---

### 3. Production MySQL Database Setup

1. Open your MySQL client and execute the provided `schema.sql` and `data.sql`:
   ```bash
   mysql -u root -p < src/main/resources/schema.sql
   mysql -u root -p < src/main/resources/data.sql
   ```

2. Open `src/main/resources/application.properties`, uncomment the MySQL block, and configure your credentials:
   ```properties
   spring.datasource.url=jdbc:mysql://localhost:3306/krushiseva_db?createDatabaseIfNotExist=true&useSSL=false&serverTimezone=Asia/Kolkata&allowPublicKeyRetrieval=true
   spring.datasource.driverClassName=com.mysql.cj.jdbc.Driver
   spring.datasource.username=root
   spring.datasource.password=your_mysql_password
   spring.jpa.database-platform=org.hibernate.dialect.MySQLDialect
   ```

3. Build and launch:
   ```bash
   mvn clean package
   java -jar target/krushi-seva-kendra-1.0.0.jar
   ```

---

### 4. Deploying to External Apache Tomcat

1. In `pom.xml`, ensure packaging is set to `war` if deploying to external Tomcat:
   ```xml
   <packaging>war</packaging>
   ```
2. Build the WAR artifact:
   ```bash
   mvn clean package
   ```
3. Copy the generated file `target/krushi-seva-kendra-1.0.0.war` into your Tomcat `webapps/` directory (e.g. rename to `ROOT.war` for root deployment).
4. Start Apache Tomcat (`bin/startup.sh` or `bin/startup.bat`).

---

## 🔑 Default Seed Demo Credentials

| Role | Name | Email / Login ID | Mobile Number | Password |
|---|---|---|---|---|
| **Administrator** | Dattatray Kulkarni | `admin@krushiseva.com` | `9876543210` | `admin123` |
| **Customer / Farmer** | Ramesh Patil | `ramesh@patil.com` | `9822012345` | `farmer123` |
| **Customer / Farmer** | Suresh Deshmukh | `suresh@deshmukh.com` | `9822054321` | `farmer123` |

*Note: You can log in using either the Email Address or the 10-digit Mobile Number.*

---

## 📡 REST API Reference

| Endpoint | Method | Description | Access |
|---|---|---|---|
| `/api/products` | `GET` | Retrieve list of active products | Public |
| `/api/products/{id}` | `GET` | Retrieve product details by ID | Public |
| `/api/products/barcode/{barcode}` | `GET` | Scanned barcode lookup for POS & inventory | Public |
| `/api/products/search?q={query}` | `GET` | Live autocomplete search results | Public |
| `/api/categories` | `GET` | List all active agricultural categories | Public |
| `/api/farming/weather?city={city}` | `GET` | Get weather conditions and spraying advisory | Public |
| `/api/farming/fertilizer-calc` | `GET` | Calculate NPK dosage & commercial bag quantities | Public |
| `/api/admin/reminders/send` | `POST` | Dispatch WhatsApp/SMS payment reminder | Admin |

---

## 📋 Comprehensive Feature Walkthrough

1. **Farmer Experience**:
   - Visit `http://localhost:8080/`
   - Switch language to **मराठी** or toggle **Dark Mode** at the top right navbar.
   - Filter products by **Seeds** or **Fertilizers**, or search for "Cotton" or "Urea".
   - Click a product to review **Agronomic Usage & Spraying Guidelines** and submit a **Farmer Review**.
   - Add items to the cart, apply coupon `KHARIF10`, and proceed to checkout.
   - Select **UPI QR Scan** or **Udhari (Credit Ledger)** and place the order.
   - Navigate to **Farmer Dashboard** &rarr; **My Orders** to download the printable **GST Tax Invoice**.
   - Navigate to **My Udhari** to inspect current credit balance and payment receipts.

2. **Admin Operations**:
   - Login as `admin@krushiseva.com` / `admin123` &rarr; Redirected to `/admin/dashboard`.
   - Review live KPI tiles, revenue velocity chart, and low-stock alerts.
   - Navigate to **Products** to add new agricultural items or trigger quick stock adjustments.
   - Navigate to **Udhari Manager** to record customer payments or dispatch 1-click **WhatsApp / SMS payment reminders**.
   - Navigate to **Reports Center** to view date-range sales and download **CSV reports**.
   - Navigate to **Database Backup** to trigger on-demand SQL dump exports.
