# -*- coding: utf-8 -*-
import os

BASE_DIR = r"c:\Users\HP\OneDrive\Documents\krushi seva"
DIST_DIR = os.path.join(BASE_DIR, "dist")

from build_site import head_html, nav_html, foot_html

def render_admin_sidebar(active_tab="dashboard"):
    return f"""
<div class="admin-sidebar-wrap mb-4">
    <!-- Admin Brand Header -->
    <div class="admin-sidebar-brand">
        <div class="d-flex align-items-center gap-3">
            <div class="position-relative">
                <img src="images/saptashrungi_logo_round.jpg" class="admin-sidebar-logo shadow-sm" alt="Shop Logo" style="width:44px;height:44px;border-radius:50%;object-fit:cover;border:2px solid #22c55e;">
                <span class="position-absolute bottom-0 end-0 p-1 bg-success border border-light rounded-circle" style="width:10px;height:10px;"></span>
            </div>
            <div class="overflow-hidden">
                <div class="admin-sidebar-title text-truncate fw-bold text-white" style="font-size:0.95rem;">
                    <span class="lang-mr">ॲडमिन पोर्टल</span><span class="lang-en">Admin Portal</span>
                </div>
                <div class="admin-sidebar-sub text-truncate text-success small" style="font-size:0.75rem;">
                    Saptashrungi Agro Services
                </div>
            </div>
        </div>
    </div>

    <!-- Section: Operations -->
    <div class="admin-nav-section text-uppercase px-3 py-2 fw-bold" style="font-size:0.7rem;letter-spacing:0.5px;color:#22c55e;opacity:0.85;">
        <span class="lang-mr">कामकाज व व्यवस्थापन</span><span class="lang-en">OPERATIONS &amp; MANAGEMENT</span>
    </div>
    <nav class="nav flex-column gap-1">
        <a href="admin-dashboard.html" class="admin-nav-link {'active' if active_tab == 'dashboard' else ''}">
            <i class="bi bi-grid-1x2-fill"></i>
            <span><span class="lang-mr">डॅशबोर्ड</span><span class="lang-en">Dashboard</span></span>
        </a>
        <a href="admin-products.html" class="admin-nav-link {'active' if active_tab == 'products' else ''}">
            <i class="bi bi-box-seam-fill"></i>
            <span><span class="lang-mr">उत्पादने</span><span class="lang-en">Products</span></span>
        </a>
        <a href="admin-categories.html" class="admin-nav-link {'active' if active_tab == 'categories' else ''}">
            <i class="bi bi-tags-fill"></i>
            <span><span class="lang-mr">कॅटेगरी</span><span class="lang-en">Categories</span></span>
        </a>
        <a href="admin-inventory.html" class="admin-nav-link {'active' if active_tab == 'inventory' else ''}">
            <i class="bi bi-boxes"></i>
            <span><span class="lang-mr">साठा व्यवस्थापन</span><span class="lang-en">Inventory</span></span>
        </a>
        <a href="admin-inventory.html#expiry" class="admin-nav-link {'active' if active_tab == 'expiry' else ''}">
            <i class="bi bi-calendar-x-fill text-warning"></i>
            <span><span class="lang-mr">मुदत समाप्ती</span><span class="lang-en">Expiry Tracking</span></span>
            <span class="badge bg-warning text-dark ms-auto" style="font-size:0.65rem;">Alert</span>
        </a>
    </nav>

    <!-- Section: Sales & Customers -->
    <div class="admin-nav-section text-uppercase px-3 py-2 mt-3 fw-bold" style="font-size:0.7rem;letter-spacing:0.5px;color:#22c55e;opacity:0.85;">
        <span class="lang-mr">विक्री व शेतकरी</span><span class="lang-en">SALES &amp; CUSTOMERS</span>
    </div>
    <nav class="nav flex-column gap-1">
        <a href="admin-customers.html" class="admin-nav-link {'active' if active_tab == 'customers' else ''}">
            <i class="bi bi-people-fill"></i>
            <span><span class="lang-mr">शेतकरी ग्राहक</span><span class="lang-en">Customers</span></span>
        </a>
        <a href="admin-udhari.html" class="admin-nav-link {'active' if active_tab == 'udhari' else ''}">
            <i class="bi bi-wallet2 text-warning"></i>
            <span><span class="lang-mr">उधारी खाते</span><span class="lang-en">Credit Ledger</span></span>
        </a>
        <a href="admin-udhari.html" class="admin-nav-link {'active' if active_tab == 'payments' else ''}">
            <i class="bi bi-credit-card-fill text-info"></i>
            <span><span class="lang-mr">पेमेंट्स</span><span class="lang-en">Payments</span></span>
        </a>
        <a href="offers.html" class="admin-nav-link {'active' if active_tab == 'offers' else ''}">
            <i class="bi bi-percent text-danger"></i>
            <span><span class="lang-mr">ऑफर व कुपन्स</span><span class="lang-en">Offers &amp; Coupons</span></span>
        </a>
    </nav>

    <!-- Section: Analytics & Settings -->
    <div class="admin-nav-section text-uppercase px-3 py-2 mt-3 fw-bold" style="font-size:0.7rem;letter-spacing:0.5px;color:#22c55e;opacity:0.85;">
        <span class="lang-mr">अहवाल व सेटिंग्ज</span><span class="lang-en">REPORTS &amp; CONFIG</span>
    </div>
    <nav class="nav flex-column gap-1 mb-4">
        <a href="admin-dashboard.html" class="admin-nav-link {'active' if active_tab == 'reports' else ''}">
            <i class="bi bi-bar-chart-line-fill text-primary"></i>
            <span><span class="lang-mr">अहवाल केंद्र</span><span class="lang-en">Reports Center</span></span>
        </a>
        <a href="admin-dashboard.html" class="admin-nav-link {'active' if active_tab == 'backup' else ''}">
            <i class="bi bi-database-check text-secondary"></i>
            <span><span class="lang-mr">डेटाबेस बॅकअप</span><span class="lang-en">Database Backup</span></span>
        </a>
        <a href="admin-dashboard.html" class="admin-nav-link {'active' if active_tab == 'settings' else ''}">
            <i class="bi bi-gear-wide-connected"></i>
            <span><span class="lang-mr">दुकान सेटिंग्ज</span><span class="lang-en">Shop Settings</span></span>
        </a>
    </nav>

    <button onclick="handleLogout()" class="admin-logout-btn w-100 btn text-danger border-0 d-flex align-items-center justify-content-center gap-2 py-2 rounded-3" style="background:rgba(239,68,68,0.12);font-weight:600;">
        <i class="bi bi-box-arrow-right"></i>
        <span><span class="lang-mr">लॉगआउट करा</span><span class="lang-en">Logout Portal</span></span>
    </button>
</div>
"""

# ==============================================================================
# 1. AUTH LOGIN PAGE (Matching Screenshot 1 exactly)
# ==============================================================================
def save_admin_page(filename, content):
    p = os.path.join(DIST_DIR, filename)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    if filename.startswith('admin-'):
        admin_sub = filename.replace('admin-', '')
        admin_dir = os.path.join(DIST_DIR, 'admin')
        os.makedirs(admin_dir, exist_ok=True)
        with open(os.path.join(admin_dir, admin_sub), 'w', encoding='utf-8') as f:
            f.write(content)

def build_login_page():
    html = """<!DOCTYPE html>
<html lang="mr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login | Krushi Seva Kendra - Saptashrungi Agro Services</title>
    <link rel="icon" type="image/jpeg" href="images/saptashrungi_logo_round.jpg">
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css">
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Noto+Sans+Devanagari:wght@400;500;600;700&display=swap" rel="stylesheet">
    <!-- Theme CSS -->
    <link href="css/custom.css" rel="stylesheet">
    <link href="css/dark-mode.css" rel="stylesheet">
    <link href="css/login-page.css" rel="stylesheet">
</head>
<body class="auth-login-page">
<main class="login-shell">
    <div class="login-topbar">
        <a href="index.html" class="login-back-link">
            <i class="bi bi-arrow-left"></i>
            <span class="lang-mr">दुकानाकडे परत</span>
            <span class="lang-en">Back to shop</span>
        </a>

        <div class="login-language-switch" role="group" aria-label="Choose language">
            <button type="button" onclick="setLang('en')" class="btn-lang-en">EN</button>
            <button type="button" onclick="setLang('mr')" class="btn-lang-mr active">मराठी</button>
        </div>
    </div>

    <section class="login-card" aria-labelledby="loginTitle">
        <div class="login-brand">
            <img src="images/saptashrungi_logo_round.jpg" alt="Krushi Seva Kendra logo">
            <div>
                <div class="login-brand-name">Krushi Seva Kendra</div>
                <div class="login-brand-subtitle">Saptashrungi Agro Services</div>
            </div>
        </div>

        <header class="login-heading">
            <h1 id="loginTitle">
                <span class="lang-mr">पुन्हा स्वागत आहे</span>
                <span class="lang-en">Welcome back</span>
            </h1>
            <p>
                <span class="lang-mr">मोबाईल नंबर किंवा ईमेल वापरून लॉगिन करा.</span>
                <span class="lang-en">Sign in with your mobile number or email.</span>
            </p>
        </header>

        <!-- Dynamic Success / Logout Alert -->
        <div id="loginAlertBox" class="alert alert-success py-2 px-3 small rounded-3 mb-3 d-flex align-items-center" style="background:#e6f4ea; color:#137333; border: 1px solid #ceead6;">
            <i class="bi bi-check-circle-fill me-2 fs-6"></i>
            <div>
                <span class="lang-mr">आपण यशस्वीरित्या लॉग आउट झाला आहात.</span>
                <span class="lang-en">You have been logged out successfully / आपण यशस्वीरित्या लॉग आउट झाला आहात.</span>
            </div>
        </div>

        <form id="loginForm" onsubmit="handleStaticLogin(event)">
            <div class="login-field">
                <label for="loginUsername">
                    <span class="lang-mr">मोबाईल नंबर किंवा ईमेल</span>
                    <span class="lang-en">Mobile number or email</span>
                </label>
                <input type="text" name="username" id="loginUsername"
                       value="admin@krushiseva.com"
                       placeholder="Mobile number or email"
                       required autofocus autocomplete="username">
            </div>

            <div class="login-field">
                <label for="loginPassword">
                    <span class="lang-mr">पासवर्ड</span>
                    <span class="lang-en">Password</span>
                </label>
                <div class="login-password-wrap">
                    <input type="password" name="password" id="loginPassword"
                           value="admin123"
                           placeholder="••••••••" required autocomplete="current-password">
                    <button type="button" class="login-password-toggle" onclick="togglePass()" aria-label="Show or hide password">
                        <i class="bi bi-eye" id="eyeIcon"></i>
                    </button>
                </div>
            </div>

            <div class="login-options">
                <label class="login-remember" for="rememberMeCheck">
                    <input type="checkbox" name="remember-me" id="rememberMeCheck" checked>
                    <span class="lang-mr">लक्षात ठेवा</span>
                    <span class="lang-en">Remember me</span>
                </label>
                <a href="forgot-password.html">
                    <span class="lang-mr">पासवर्ड विसरलात?</span>
                    <span class="lang-en">Forgot password?</span>
                </a>
            </div>

            <button type="submit" class="login-submit">
                <span class="lang-mr">लॉगिन करा</span>
                <span class="lang-en">Log in</span>
            </button>
        </form>

        <footer class="login-footer">
            <span class="lang-mr">नवीन शेतकरी?</span>
            <span class="lang-en">New farmer?</span>
            <a href="register.html">
                <span class="lang-mr">नोंदणी करा</span>
                <span class="lang-en">Register</span>
            </a>
        </footer>
    </section>
</main>

<script>
function togglePass() {
    var pass = document.getElementById('loginPassword');
    var icon = document.getElementById('eyeIcon');
    if (pass.type === 'password') {
        pass.type = 'text';
        icon.className = 'bi bi-eye-slash';
    } else {
        pass.type = 'password';
        icon.className = 'bi bi-eye';
    }
}

function handleStaticLogin(e) {
    e.preventDefault();
    var username = document.getElementById('loginUsername').value.trim().toLowerCase();
    
    // Check if admin login
    if (username.indexOf('admin') !== -1 || username === 'admin@krushiseva.com') {
        localStorage.setItem('user_role', 'admin');
        localStorage.setItem('user_name', 'Admin');
        window.location.href = 'admin-dashboard.html';
    } else {
        localStorage.setItem('user_role', 'farmer');
        localStorage.setItem('user_name', username.split('@')[0] || 'Ramesh Patil');
        window.location.href = 'farmer-dashboard.html';
    }
}

function setLang(lang) {
    document.documentElement.setAttribute('lang', lang);
    localStorage.setItem('site_lang', lang);
    var isMr = (lang === 'mr');
    document.querySelectorAll('.btn-lang-mr').forEach(function(b){
        b.className = isMr ? 'btn-lang-mr active' : 'btn-lang-mr';
    });
    document.querySelectorAll('.btn-lang-en').forEach(function(b){
        b.className = !isMr ? 'btn-lang-en active' : 'btn-lang-en';
    });
}

document.addEventListener('DOMContentLoaded', function(){
    var savedLang = localStorage.getItem('site_lang') || 'mr';
    setLang(savedLang);
    
    // Check if logged out alert should show
    var urlParams = new URLSearchParams(window.location.search);
    var alertBox = document.getElementById('loginAlertBox');
    if (!urlParams.has('logout') && !document.referrer.includes('admin') && !document.referrer.includes('farmer')) {
        // If normal visit, still show the friendly prompt or keep it visible as per screenshot
    }
});
</script>
</body>
</html>
"""
    with open(os.path.join(DIST_DIR, "login.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Generated dist/login.html matching Screenshot 1")

# ==============================================================================
# 2. ADMIN DASHBOARD (Matching Screenshot 2, 3, 4)
# ==============================================================================
def build_admin_dashboard():
    sidebar = render_admin_sidebar("dashboard")
    content = head_html("ॲडमिन डॅशबोर्ड", "Admin Dashboard") + nav_html("dashboard") + f"""
<div class="container-fluid px-3 px-lg-4 my-4">
    <div class="row g-4">
        <!-- Left Sidebar (Screenshot 3) -->
        <div class="col-lg-3 col-xl-2">
            {sidebar}
        </div>

        <!-- Main Workspace Area -->
        <div class="col-lg-9 col-xl-10">
            <!-- Green Welcome Banner (Screenshot 4) -->
            <div class="admin-welcome-banner mb-4">
                <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-3">
                    <div>
                        <div class="d-inline-flex align-items-center gap-2 px-3 py-1 rounded-pill bg-white bg-opacity-25 small mb-2 fw-semibold">
                            <span>🌱</span>
                            <span class="lang-mr">सप्तशृंगी ॲग्रो सर्व्हिसेस, मिरखनगर</span>
                            <span class="lang-en">Saptashrungi Agro Services, Mirkhanagar</span>
                        </div>
                        <h2 class="h3 fw-bold mb-1 text-white">
                            <span class="lang-mr">व्यवस्थापन डॅशबोर्ड</span>
                            <span class="lang-en">Admin Dashboard</span>
                        </h2>
                        <p class="text-white-50 small mb-0">
                            <span class="lang-mr">विक्री, इन्व्हेंटरी, शेतकरी खाती आणि दुकानाच्या कामगिरीचा आढावा.</span>
                            <span class="lang-en">Overview of sales, inventory, farmer accounts, and store performance.</span>
                        </p>
                    </div>
                    <div class="d-flex align-items-center gap-2 flex-wrap">
                        <a href="admin-product-form.html" class="btn btn-light fw-bold text-success px-3 py-2 rounded-3 shadow-sm d-flex align-items-center gap-2">
                            <span>➕</span>
                            <span class="lang-mr">Add Product (नवीन उत्पादन)</span>
                            <span class="lang-en">Add Product</span>
                        </a>
                        <a href="admin-dashboard.html" class="btn btn-outline-light fw-semibold px-3 py-2 rounded-3 d-flex align-items-center gap-2">
                            <i class="bi bi-file-earmark-bar-graph"></i>
                            <span class="lang-mr">अहवाल</span>
                            <span class="lang-en">Reports</span>
                        </a>
                    </div>
                </div>
            </div>

            <!-- 4 Main Stats Cards (Screenshot 4) -->
            <div class="row g-3 mb-4">
                <!-- 1. Total Products -->
                <div class="col-sm-6 col-xl-3">
                    <a href="admin-products.html" class="admin-kpi-card text-decoration-none text-reset h-100 d-block">
                        <div class="d-flex justify-content-between align-items-start">
                            <span class="admin-kpi-label"><span class="lang-mr">एकूण उत्पादने (Total Products)</span><span class="lang-en">Total Products</span></span>
                            <div class="admin-kpi-icon-wrap" style="background: #dbeafe; color: #0284c7;">
                                <i class="bi bi-box-seam-fill"></i>
                            </div>
                        </div>
                        <div>
                            <div class="admin-kpi-val">14</div>
                            <span class="admin-kpi-badge" style="background: #eff6ff; color: #0284c7;">
                                <i class="bi bi-boxes"></i> <span class="lang-mr">कॅटलॉग यादी</span><span class="lang-en">In Catalog</span>
                            </span>
                        </div>
                    </a>
                </div>

                <!-- 2. Total Users -->
                <div class="col-sm-6 col-xl-3">
                    <a href="admin-customers.html" class="admin-kpi-card text-decoration-none text-reset h-100 d-block">
                        <div class="d-flex justify-content-between align-items-start">
                            <span class="admin-kpi-label"><span class="lang-mr">एकूण युझर्स (Total Users)</span><span class="lang-en">Total Users</span></span>
                            <div class="admin-kpi-icon-wrap" style="background: #f3e8ff; color: #7c3aed;">
                                <i class="bi bi-people-fill"></i>
                            </div>
                        </div>
                        <div>
                            <div class="admin-kpi-val">7</div>
                            <span class="admin-kpi-badge" style="background: #faf5ff; color: #7c3aed;">
                                <i class="bi bi-person-check-fill"></i> <span class="lang-mr">नोंदणीकृत शेतकरी</span><span class="lang-en">Registered Farmers</span>
                            </span>
                        </div>
                    </a>
                </div>

                <!-- 3. Udhari Outstanding -->
                <div class="col-sm-6 col-xl-3">
                    <a href="admin-udhari.html" class="admin-kpi-card text-decoration-none text-reset h-100 d-block">
                        <div class="d-flex justify-content-between align-items-start">
                            <span class="admin-kpi-label"><span class="lang-mr">बाकी उधारी (Udhari Outstanding)</span><span class="lang-en">Udhari Outstanding</span></span>
                            <div class="admin-kpi-icon-wrap" style="background: #fee2e2; color: #dc2626;">
                                <i class="bi bi-envelope-fill"></i>
                            </div>
                        </div>
                        <div>
                            <div class="admin-kpi-val" style="color: #dc2626;">₹8,000</div>
                            <span class="admin-kpi-badge" style="background: #fef2f2; color: #dc2626;">
                                <span class="lang-mr">1 मुदत संपलेली खाती</span><span class="lang-en">1 Overdue</span>
                            </span>
                        </div>
                    </a>
                </div>

                <!-- 4. Monthly Revenue -->
                <div class="col-sm-6 col-xl-3">
                    <a href="admin-dashboard.html" class="admin-kpi-card text-decoration-none text-reset h-100 d-block">
                        <div class="d-flex justify-content-between align-items-start">
                            <span class="admin-kpi-label"><span class="lang-mr">मासिक महसूल (Monthly Revenue)</span><span class="lang-en">Monthly Revenue</span></span>
                            <div class="admin-kpi-icon-wrap" style="background: #dcfce7; color: #16a34a;">
                                <i class="bi bi-cash-stack"></i>
                            </div>
                        </div>
                        <div>
                            <div class="admin-kpi-val text-success">₹0</div>
                            <span class="admin-kpi-badge" style="background: #f0fdf4; color: #16a34a;">
                                <i class="bi bi-graph-up-arrow"></i> <span class="lang-mr">चालू महिना विक्री</span><span class="lang-en">Current Month</span>
                            </span>
                        </div>
                    </a>
                </div>
            </div>

            <!-- Two Column Section: Recent Orders & Quick Actions (Screenshot 2) -->
            <div class="row g-4 mb-4">
                <!-- Left: Recent Orders -->
                <div class="col-lg-8">
                    <div class="card border-0 shadow-sm rounded-4 overflow-hidden h-100 bg-white">
                        <div class="card-header bg-white py-3 px-4 border-0 d-flex justify-content-between align-items-center">
                            <div class="d-flex align-items-center gap-2">
                                <i class="bi bi-receipt text-success fs-5"></i>
                                <h6 class="fw-bold text-dark mb-0"><span class="lang-mr">अलीकडील ऑर्डर्स</span><span class="lang-en">Recent Orders</span></h6>
                            </div>
                            <a href="admin-products.html" class="btn btn-sm btn-outline-success rounded-pill px-3 fw-semibold">
                                <span class="lang-mr">सर्व पाहा &rarr;</span><span class="lang-en">View All &rarr;</span>
                            </a>
                        </div>
                        <div class="table-responsive">
                            <table class="table table-hover align-middle mb-0">
                                <thead class="table-light text-muted small">
                                    <tr>
                                        <th class="ps-4">Order ID</th>
                                        <th>Customer Name</th>
                                        <th class="text-end">Amount</th>
                                        <th class="text-center">Status</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td class="ps-4">
                                            <span class="fw-bold text-success">KSK-2026-00001</span>
                                        </td>
                                        <td>
                                            <div class="fw-semibold text-dark">Ramesh Patil</div>
                                        </td>
                                        <td class="text-end fw-bold text-dark">₹4499.00</td>
                                        <td class="text-center">
                                            <span class="badge rounded-pill bg-success-subtle text-success border border-success-subtle px-3 py-1">Delivered</span>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td class="ps-4">
                                            <span class="fw-bold text-success">KSK-2026-00002</span>
                                        </td>
                                        <td>
                                            <div class="fw-semibold text-dark">Suresh Deshmukh</div>
                                        </td>
                                        <td class="text-end fw-bold text-dark">₹2850.00</td>
                                        <td class="text-center">
                                            <span class="badge rounded-pill bg-primary-subtle text-primary border border-primary-subtle px-3 py-1">Processing</span>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td class="ps-4">
                                            <span class="fw-bold text-success">KSK-2026-00003</span>
                                        </td>
                                        <td>
                                            <div class="fw-semibold text-dark">Dnyaneshwar Pawar</div>
                                        </td>
                                        <td class="text-end fw-bold text-dark">₹1350.00</td>
                                        <td class="text-center">
                                            <span class="badge rounded-pill bg-success-subtle text-success border border-success-subtle px-3 py-1">Delivered</span>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>

                <!-- Right: Quick Actions (Screenshot 2) -->
                <div class="col-lg-4">
                    <div class="card border-0 shadow-sm rounded-4 p-4 h-100 bg-white">
                        <div class="d-flex align-items-center gap-2 mb-3">
                            <i class="bi bi-lightning-charge-fill text-warning fs-5"></i>
                            <h6 class="fw-bold text-dark mb-0"><span class="lang-mr">जलद ॲक्शन्स</span><span class="lang-en">Quick Actions</span></h6>
                        </div>

                        <a href="admin-product-form.html" class="admin-tool-item">
                            <div class="admin-tool-icon-box" style="background: #dcfce7; color: #16a34a;">
                                <i class="bi bi-plus-lg"></i>
                            </div>
                            <div class="flex-grow-1"><span class="lang-mr">नवीन उत्पादन जोडा</span><span class="lang-en">Add New Product</span></div>
                            <i class="bi bi-chevron-right text-muted small"></i>
                        </a>

                        <a href="admin-inventory.html" class="admin-tool-item">
                            <div class="admin-tool-icon-box" style="background: #e0f2fe; color: #0284c7;">
                                <i class="bi bi-boxes"></i>
                            </div>
                            <div class="flex-grow-1"><span class="lang-mr">साठा व्यवस्थापन</span><span class="lang-en">Inventory Management</span></div>
                            <i class="bi bi-chevron-right text-muted small"></i>
                        </a>

                        <a href="admin-udhari.html" class="admin-tool-item">
                            <div class="admin-tool-icon-box" style="background: #fef3c7; color: #d97706;">
                                <i class="bi bi-wallet2"></i>
                            </div>
                            <div class="flex-grow-1"><span class="lang-mr">उधारी खाते</span><span class="lang-en">Credit Ledger</span></div>
                            <i class="bi bi-chevron-right text-muted small"></i>
                        </a>

                        <a href="admin-customers.html" class="admin-tool-item">
                            <div class="admin-tool-icon-box" style="background: #f3e8ff; color: #7c3aed;">
                                <i class="bi bi-people"></i>
                            </div>
                            <div class="flex-grow-1"><span class="lang-mr">शेतकरी ग्राहक यादी</span><span class="lang-en">Farmers Directory</span></div>
                            <i class="bi bi-chevron-right text-muted small"></i>
                        </a>

                        <a href="admin-dashboard.html" class="admin-tool-item mb-0">
                            <div class="admin-tool-icon-box" style="background: #f1f5f9; color: #475569;">
                                <i class="bi bi-graph-up"></i>
                            </div>
                            <div class="flex-grow-1"><span class="lang-mr">विक्री अहवाल</span><span class="lang-en">Sales Reports</span></div>
                            <i class="bi bi-chevron-right text-muted small"></i>
                        </a>

                        <!-- Shop Info Small Card (Screenshot 2) -->
                        <div class="mt-4 p-3 rounded-3" style="background: #f8fafc; border: 1px dashed #cbd5e1;">
                            <div class="d-flex align-items-center gap-2 mb-1">
                                <span class="badge bg-success"><span class="lang-mr">ऑनलाइन दुकान</span><span class="lang-en">Online Shop</span></span>
                                <small class="fw-bold text-dark">Saptashrungi Agro Services</small>
                            </div>
                            <small class="text-muted d-block" style="font-size: 0.75rem;">
                                📍 Mirkhanagar, Vaijapur, Chhatrapati Sambhajinagar<br>
                                📞 8600813827 | UPI Active
                            </small>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
""" + foot_html()
    save_admin_page("admin-dashboard.html", content)
    print("Generated dist/admin-dashboard.html matching Screenshot 2, 3, 4")

# ==============================================================================
# 3. ADMIN CATEGORIES PAGE (Matching Screenshot 5)
# ==============================================================================
def build_admin_categories():
    sidebar = render_admin_sidebar("categories")
    content = head_html("कॅटेगरी व्यवस्थापन", "Category Management") + nav_html("dashboard") + f"""
<div class="container-fluid px-3 px-lg-4 my-4">
    <div class="row g-4">
        <!-- Sidebar -->
        <div class="col-lg-3 col-xl-2">
            {sidebar}
        </div>

        <div class="col-lg-9 col-xl-10">
            <div class="row g-4">
                <!-- Add Category Card (Screenshot 5 left) -->
                <div class="col-lg-4">
                    <div class="card border-0 shadow-sm rounded-4 overflow-hidden bg-white">
                        <div class="card-header bg-success text-white py-3 px-4">
                            <h6 class="mb-0 fw-bold"><i class="bi bi-plus-circle me-2"></i><span class="lang-mr">नवीन कॅटेगरी जोडा</span><span class="lang-en">Add New Category</span></h6>
                        </div>
                        <div class="card-body p-4">
                            <form id="addCategoryForm" onsubmit="alert('Category saved successfully!'); return false;">
                                <div class="mb-3">
                                    <label class="form-label small fw-bold text-success">Category Name (English) *</label>
                                    <input type="text" class="form-control form-control-sm" placeholder="e.g. Bio-Pesticides" required>
                                </div>
                                <div class="mb-3">
                                    <label class="form-label small fw-bold text-success">Category Name (Marathi)</label>
                                    <input type="text" class="form-control form-control-sm" placeholder="उदा. सेंद्रिय कीटकनाशके">
                                </div>
                                <div class="mb-3">
                                    <label class="form-label small fw-bold text-success">Description</label>
                                    <textarea class="form-control form-control-sm" rows="3" placeholder="Short description"></textarea>
                                </div>
                                <div class="mb-4">
                                    <label class="form-label small fw-bold text-success">Image Name</label>
                                    <input type="text" class="form-control form-control-sm" placeholder="e.g. seeds.jpg">
                                </div>
                                <button type="submit" class="btn btn-success w-100 fw-bold py-2 rounded-3 shadow-sm" style="background:#16a34a;border:none;">
                                    Create Category
                                </button>
                            </form>
                        </div>
                    </div>
                </div>

                <!-- Categories List Table (Screenshot 5 right) -->
                <div class="col-lg-8">
                    <div class="card border-0 shadow-sm rounded-4 overflow-hidden bg-white">
                        <div class="card-header bg-white py-3 px-4 border-bottom d-flex justify-content-between align-items-center">
                            <h5 class="mb-0 fw-bold text-dark"><i class="bi bi-tags-fill text-success me-2"></i>Product Categories (8)</h5>
                        </div>
                        <div class="card-body p-0">
                            <div class="table-responsive">
                                <table class="table table-hover align-middle mb-0">
                                    <thead class="table-light text-muted small">
                                        <tr>
                                            <th class="ps-4">#</th>
                                            <th>CATEGORY NAME</th>
                                            <th>MARATHI NAME</th>
                                            <th>DESCRIPTION</th>
                                            <th>STATUS</th>
                                            <th class="text-end pe-4">ACTIONS</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td class="ps-4 fw-bold">1</td>
                                            <td><strong class="text-dark">Seeds</strong></td>
                                            <td>बियाणे</td>
                                            <td class="small text-muted text-truncate" style="max-width: 180px;">High yield certified hyb...</td>
                                            <td><span class="badge bg-success px-2 py-1">ACTIVE</span></td>
                                            <td class="text-end pe-4">
                                                <button class="btn btn-sm btn-outline-secondary py-1 px-2" style="font-size:0.75rem;">Disable</button>
                                                <button class="btn btn-sm btn-outline-danger py-1 px-2 ms-1" style="font-size:0.75rem;"><i class="bi bi-trash"></i></button>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="ps-4 fw-bold">2</td>
                                            <td><strong class="text-dark">Fertilizers</strong></td>
                                            <td>खते</td>
                                            <td class="small text-muted text-truncate" style="max-width: 180px;">Chemical, water-solub...</td>
                                            <td><span class="badge bg-success px-2 py-1">ACTIVE</span></td>
                                            <td class="text-end pe-4">
                                                <button class="btn btn-sm btn-outline-secondary py-1 px-2" style="font-size:0.75rem;">Disable</button>
                                                <button class="btn btn-sm btn-outline-danger py-1 px-2 ms-1" style="font-size:0.75rem;"><i class="bi bi-trash"></i></button>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="ps-4 fw-bold">3</td>
                                            <td><strong class="text-dark">Pesticides</strong></td>
                                            <td>कीटकनाशके</td>
                                            <td class="small text-muted text-truncate" style="max-width: 180px;">Broad-spectrum insec...</td>
                                            <td><span class="badge bg-success px-2 py-1">ACTIVE</span></td>
                                            <td class="text-end pe-4">
                                                <button class="btn btn-sm btn-outline-secondary py-1 px-2" style="font-size:0.75rem;">Disable</button>
                                                <button class="btn btn-sm btn-outline-danger py-1 px-2 ms-1" style="font-size:0.75rem;"><i class="bi bi-trash"></i></button>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="ps-4 fw-bold">4</td>
                                            <td><strong class="text-dark">Farming Tools</strong></td>
                                            <td>शेती अवजारे</td>
                                            <td class="small text-muted text-truncate" style="max-width: 180px;">Battery sprayers, pruni...</td>
                                            <td><span class="badge bg-success px-2 py-1">ACTIVE</span></td>
                                            <td class="text-end pe-4">
                                                <button class="btn btn-sm btn-outline-secondary py-1 px-2" style="font-size:0.75rem;">Disable</button>
                                                <button class="btn btn-sm btn-outline-danger py-1 px-2 ms-1" style="font-size:0.75rem;"><i class="bi bi-trash"></i></button>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="ps-4 fw-bold">5</td>
                                            <td><strong class="text-dark">Drip Irrigation</strong></td>
                                            <td>ठिबक सिंचन</td>
                                            <td class="small text-muted text-truncate" style="max-width: 180px;">Drip laterals, drippers, ...</td>
                                            <td><span class="badge bg-success px-2 py-1">ACTIVE</span></td>
                                            <td class="text-end pe-4">
                                                <button class="btn btn-sm btn-outline-secondary py-1 px-2" style="font-size:0.75rem;">Disable</button>
                                                <button class="btn btn-sm btn-outline-danger py-1 px-2 ms-1" style="font-size:0.75rem;"><i class="bi bi-trash"></i></button>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="ps-4 fw-bold">6</td>
                                            <td><strong class="text-dark">Animal Feed</strong></td>
                                            <td>पशूखाद्य</td>
                                            <td class="small text-muted text-truncate" style="max-width: 180px;">Cattle feed pellets, mi...</td>
                                            <td><span class="badge bg-success px-2 py-1">ACTIVE</span></td>
                                            <td class="text-end pe-4">
                                                <button class="btn btn-sm btn-outline-secondary py-1 px-2" style="font-size:0.75rem;">Disable</button>
                                                <button class="btn btn-sm btn-outline-danger py-1 px-2 ms-1" style="font-size:0.75rem;"><i class="bi bi-trash"></i></button>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="ps-4 fw-bold">7</td>
                                            <td><strong class="text-dark">Organic Products</strong></td>
                                            <td>सेंद्रिय उत्पादने</td>
                                            <td class="small text-muted text-truncate" style="max-width: 180px;">Neem cake, vermicom...</td>
                                            <td><span class="badge bg-success px-2 py-1">ACTIVE</span></td>
                                            <td class="text-end pe-4">
                                                <button class="btn btn-sm btn-outline-secondary py-1 px-2" style="font-size:0.75rem;">Disable</button>
                                                <button class="btn btn-sm btn-outline-danger py-1 px-2 ms-1" style="font-size:0.75rem;"><i class="bi bi-trash"></i></button>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="ps-4 fw-bold">8</td>
                                            <td><strong class="text-dark">Plant Growth Promoters</strong></td>
                                            <td>वाढ संप्रेरके</td>
                                            <td class="small text-muted text-truncate" style="max-width: 180px;">Humic acid, seaweed e...</td>
                                            <td><span class="badge bg-success px-2 py-1">ACTIVE</span></td>
                                            <td class="text-end pe-4">
                                                <button class="btn btn-sm btn-outline-secondary py-1 px-2" style="font-size:0.75rem;">Disable</button>
                                                <button class="btn btn-sm btn-outline-danger py-1 px-2 ms-1" style="font-size:0.75rem;"><i class="bi bi-trash"></i></button>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
""" + foot_html()
    save_admin_page("admin-categories.html", content)
    print("Generated dist/admin-categories.html matching Screenshot 5")

# ==============================================================================
# 4. ADMIN PRODUCTS LIST
# ==============================================================================
def build_admin_products():
    sidebar = render_admin_sidebar("products")
    content = head_html("उत्पादने व्यवस्थापन", "Product Management") + nav_html("dashboard") + f"""
<div class="container-fluid px-3 px-lg-4 my-4">
    <div class="row g-4">
        <!-- Sidebar -->
        <div class="col-lg-3 col-xl-2">
            {sidebar}
        </div>

        <div class="col-lg-9 col-xl-10">
            <div class="card border-0 shadow-sm rounded-4 overflow-hidden bg-white">
                <div class="card-header bg-white py-3 px-4 border-bottom d-flex justify-content-between align-items-center flex-wrap gap-2">
                    <h5 class="mb-0 fw-bold text-dark"><i class="bi bi-box-seam text-success me-2"></i><span class="lang-mr">उत्पादने यादी (Products)</span><span class="lang-en">Product Catalog</span></h5>
                    <a href="admin-product-form.html" class="btn btn-success fw-bold px-3 py-2 rounded-3 shadow-sm" style="background:#16a34a;border:none;">
                        ➕ <span class="lang-mr">Add Product</span><span class="lang-en">Add Product</span>
                    </a>
                </div>
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-hover align-middle mb-0">
                            <thead class="table-light text-muted small">
                                <tr>
                                    <th class="ps-4">Image</th>
                                    <th>Name</th>
                                    <th>Company</th>
                                    <th>Category</th>
                                    <th>Price</th>
                                    <th>Stock</th>
                                    <th>Status</th>
                                    <th class="text-end pe-4">Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="ps-4"><img src="images/wheat_seeds.jpg" class="rounded-3" style="width:40px;height:40px;object-fit:cover;"></td>
                                    <td><strong class="text-dark">Wheat Seeds (Lok-1)</strong></td>
                                    <td>MAHABEEJ</td>
                                    <td><span class="badge bg-light text-dark border">Seeds</span></td>
                                    <td><strong class="text-success">₹1,350</strong> <small class="text-muted text-decoration-line-through">₹1,450</small></td>
                                    <td><span class="badge bg-success">60 units</span></td>
                                    <td><span class="badge bg-success-subtle text-success border border-success-subtle">Active</span></td>
                                    <td class="text-end pe-4">
                                        <a href="admin-product-form.html" class="btn btn-sm btn-outline-primary py-1 px-2"><i class="bi bi-pencil-square"></i></a>
                                        <button class="btn btn-sm btn-outline-danger py-1 px-2 ms-1" onclick="alert('Product deleted')"><i class="bi bi-trash"></i></button>
                                    </td>
                                </tr>
                                <tr>
                                    <td class="ps-4"><img src="images/soybean_seeds.jpg" class="rounded-3" style="width:40px;height:40px;object-fit:cover;"></td>
                                    <td><strong class="text-dark">Soybean Seeds (JS-335)</strong></td>
                                    <td>MAHABEEJ</td>
                                    <td><span class="badge bg-light text-dark border">Seeds</span></td>
                                    <td><strong class="text-success">₹2,950</strong> <small class="text-muted text-decoration-line-through">₹3,200</small></td>
                                    <td><span class="badge bg-success">40 units</span></td>
                                    <td><span class="badge bg-success-subtle text-success border border-success-subtle">Active</span></td>
                                    <td class="text-end pe-4">
                                        <a href="admin-product-form.html" class="btn btn-sm btn-outline-primary py-1 px-2"><i class="bi bi-pencil-square"></i></a>
                                        <button class="btn btn-sm btn-outline-danger py-1 px-2 ms-1" onclick="alert('Product deleted')"><i class="bi bi-trash"></i></button>
                                    </td>
                                </tr>
                                <tr>
                                    <td class="ps-4"><img src="images/npk_191919.jpg" class="rounded-3" style="width:40px;height:40px;object-fit:cover;"></td>
                                    <td><strong class="text-dark">NPK 19:19:19</strong></td>
                                    <td>IFFCO</td>
                                    <td><span class="badge bg-light text-dark border">Fertilizers</span></td>
                                    <td><strong class="text-success">₹1,890</strong> <small class="text-muted text-decoration-line-through">₹2,350</small></td>
                                    <td><span class="badge bg-success">85 units</span></td>
                                    <td><span class="badge bg-success-subtle text-success border border-success-subtle">Active</span></td>
                                    <td class="text-end pe-4">
                                        <a href="admin-product-form.html" class="btn btn-sm btn-outline-primary py-1 px-2"><i class="bi bi-pencil-square"></i></a>
                                        <button class="btn btn-sm btn-outline-danger py-1 px-2 ms-1" onclick="alert('Product deleted')"><i class="bi bi-trash"></i></button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
""" + foot_html()
    save_admin_page("admin-products.html", content)
    print("Generated dist/admin-products.html")

# ==============================================================================
# 5. ADMIN PRODUCT FORM
# ==============================================================================
def build_admin_product_form():
    sidebar = render_admin_sidebar("products")
    content = head_html("उत्पादन फॉर्म", "Product Form") + nav_html("dashboard") + f"""
<div class="container-fluid px-3 px-lg-4 my-4">
    <div class="row g-4">
        <!-- Sidebar -->
        <div class="col-lg-3 col-xl-2">
            {sidebar}
        </div>

        <div class="col-lg-9 col-xl-10">
            <div class="card border-0 shadow-sm rounded-4 overflow-hidden bg-white">
                <div class="card-header bg-white py-3 px-4 border-bottom d-flex justify-content-between align-items-center">
                    <h5 class="mb-0 fw-bold text-dark"><i class="bi bi-plus-circle text-success me-2"></i><span class="lang-mr">उत्पादन जोडा / बदला</span><span class="lang-en">Add / Edit Product</span></h5>
                    <a href="admin-products.html" class="btn btn-sm btn-outline-secondary rounded-pill px-3">&larr; Back to Products</a>
                </div>
                <div class="card-body p-4">
                    <form onsubmit="alert('Product saved successfully!'); window.location.href='admin-products.html'; return false;">
                        <div class="row g-3">
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-success">Product Name (English) *</label>
                                <input type="text" class="form-control" placeholder="e.g. Wheat Seeds (Lok-1)" required>
                            </div>
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-success">Product Name (Marathi)</label>
                                <input type="text" class="form-control" placeholder="उदा. गहू बियाणे (लोक-१)">
                            </div>
                            <div class="col-md-4">
                                <label class="form-label small fw-bold text-success">Company / Brand</label>
                                <input type="text" class="form-control" placeholder="e.g. MAHABEEJ / IFFCO">
                            </div>
                            <div class="col-md-4">
                                <label class="form-label small fw-bold text-success">Category</label>
                                <select class="form-select">
                                    <option value="1">Seeds (बियाणे)</option>
                                    <option value="2">Fertilizers (खते)</option>
                                    <option value="3">Pesticides (कीटकनाशके)</option>
                                    <option value="4">Farming Tools (शेती अवजारे)</option>
                                    <option value="5">Drip Irrigation (ठिबक सिंचन)</option>
                                    <option value="6">Animal Feed (पशूखाद्य)</option>
                                    <option value="7">Organic Products (सेंद्रिय)</option>
                                    <option value="8">Plant Growth Promoters (वाढ संप्रेरके)</option>
                                </select>
                            </div>
                            <div class="col-md-4">
                                <label class="form-label small fw-bold text-success">GST Rate (%)</label>
                                <input type="number" step="0.01" class="form-control" placeholder="0.00 or 5.00" value="0.00">
                            </div>
                            <div class="col-md-4">
                                <label class="form-label small fw-bold text-success">Original Price (₹) *</label>
                                <input type="number" step="0.01" class="form-control" placeholder="1450" required>
                            </div>
                            <div class="col-md-4">
                                <label class="form-label small fw-bold text-success">Discount Price (₹)</label>
                                <input type="number" step="0.01" class="form-control" placeholder="1350">
                            </div>
                            <div class="col-md-2">
                                <label class="form-label small fw-bold text-success">Stock Quantity</label>
                                <input type="number" class="form-control" placeholder="60" value="50">
                            </div>
                            <div class="col-md-2">
                                <label class="form-label small fw-bold text-success">Minimum Stock Alert</label>
                                <input type="number" class="form-control" placeholder="10" value="10">
                            </div>
                            <div class="col-12">
                                <label class="form-label small fw-bold text-success">Description</label>
                                <textarea class="form-control" rows="3" placeholder="Enter product usage details, application dosage, etc."></textarea>
                            </div>
                            <div class="col-12 text-end pt-3">
                                <button type="submit" class="btn btn-success fw-bold px-4 py-2 rounded-3 shadow-sm" style="background:#16a34a;border:none;">
                                    💾 Save Product
                                </button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
""" + foot_html()
    save_admin_page("admin-product-form.html", content)
    print("Generated dist/admin-product-form.html")

# ==============================================================================
# 6. ADMIN UDHARI (Credit Ledger)
# ==============================================================================
def build_admin_udhari():
    sidebar = render_admin_sidebar("udhari")
    content = head_html("उधारी व्यवस्थापन", "Credit Ledger Management") + nav_html("dashboard") + f"""
<div class="container-fluid px-3 px-lg-4 my-4">
    <div class="row g-4">
        <!-- Sidebar -->
        <div class="col-lg-3 col-xl-2">
            {sidebar}
        </div>

        <div class="col-lg-9 col-xl-10">
            <div class="card border-0 shadow-sm rounded-4 overflow-hidden bg-white">
                <div class="card-header bg-white py-3 px-4 border-bottom d-flex justify-content-between align-items-center flex-wrap gap-2">
                    <h5 class="mb-0 fw-bold text-dark"><i class="bi bi-wallet2 text-warning me-2"></i><span class="lang-mr">शेतकरी उधारी खाते (Credit Ledger)</span><span class="lang-en">Credit Ledger Management</span></h5>
                    <div class="badge bg-danger-subtle text-danger border border-danger px-3 py-2 rounded-pill fw-bold">
                        Total Outstanding: ₹8,000
                    </div>
                </div>
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-hover align-middle mb-0">
                            <thead class="table-light text-muted small">
                                <tr>
                                    <th class="ps-4">Customer Name</th>
                                    <th>Contact</th>
                                    <th>Village</th>
                                    <th>Remaining Udhari</th>
                                    <th>Due Date</th>
                                    <th>Status</th>
                                    <th class="text-end pe-4">Action</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="ps-4 fw-bold text-dark">Ramesh Patil</td>
                                    <td>8600813827</td>
                                    <td>Vaijapur</td>
                                    <td><strong class="text-danger">₹3,500</strong></td>
                                    <td>15 Nov 2026</td>
                                    <td><span class="badge bg-warning text-dark">Pending</span></td>
                                    <td class="text-end pe-4">
                                        <button class="btn btn-sm btn-success rounded-pill px-3" onclick="alert('Marked as paid!'); this.disabled=true; this.innerText='Paid';">Mark as Paid</button>
                                    </td>
                                </tr>
                                <tr>
                                    <td class="ps-4 fw-bold text-dark">Suresh Deshmukh</td>
                                    <td>9822001122</td>
                                    <td>Shrirampur</td>
                                    <td><strong class="text-danger">₹4,500</strong></td>
                                    <td>28 Oct 2026</td>
                                    <td><span class="badge bg-danger text-white">Overdue</span></td>
                                    <td class="text-end pe-4">
                                        <button class="btn btn-sm btn-success rounded-pill px-3" onclick="alert('Marked as paid!'); this.disabled=true; this.innerText='Paid';">Mark as Paid</button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
""" + foot_html()
    save_admin_page("admin-udhari.html", content)
    print("Generated dist/admin-udhari.html")

# ==============================================================================
# 7. ADMIN INVENTORY
# ==============================================================================
def build_admin_inventory():
    sidebar = render_admin_sidebar("inventory")
    content = head_html("इन्व्हेंटरी व एक्सपायरी", "Inventory & Expiry") + nav_html("dashboard") + f"""
<div class="container-fluid px-3 px-lg-4 my-4">
    <div class="row g-4">
        <!-- Sidebar -->
        <div class="col-lg-3 col-xl-2">
            {sidebar}
        </div>

        <div class="col-lg-9 col-xl-10">
            <div class="card border-0 shadow-sm rounded-4 overflow-hidden bg-white">
                <div class="card-header bg-white py-3 px-4 border-bottom d-flex justify-content-between align-items-center flex-wrap gap-2">
                    <h5 class="mb-0 fw-bold text-dark"><i class="bi bi-boxes text-success me-2"></i><span class="lang-mr">इन्व्हेंटरी व एक्सपायरी ट्रॅकिंग</span><span class="lang-en">Inventory & Expiry Tracking</span></h5>
                    <div class="d-flex gap-2">
                        <span class="badge bg-success">Green = OK</span>
                        <span class="badge bg-warning text-dark">Yellow = Warning</span>
                        <span class="badge bg-danger">Red = Low</span>
                    </div>
                </div>
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-hover align-middle mb-0">
                            <thead class="table-light text-muted small">
                                <tr>
                                    <th class="ps-4">Product</th>
                                    <th>Category</th>
                                    <th>Current Stock</th>
                                    <th>Min Safe Stock</th>
                                    <th>Stock Level Status</th>
                                    <th>Expiry Date</th>
                                    <th class="text-end pe-4">Action</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="ps-4 fw-bold text-dark">Wheat Seeds (Lok-1)</td>
                                    <td>Seeds</td>
                                    <td>60 units</td>
                                    <td>15 units</td>
                                    <td><span class="badge bg-success px-3 py-1">OK (Safe)</span></td>
                                    <td>30 Apr 2027</td>
                                    <td class="text-end pe-4"><button class="btn btn-sm btn-outline-primary py-1 px-2">Update</button></td>
                                </tr>
                                <tr>
                                    <td class="ps-4 fw-bold text-dark">NPK 19:19:19</td>
                                    <td>Fertilizers</td>
                                    <td>85 units</td>
                                    <td>20 units</td>
                                    <td><span class="badge bg-success px-3 py-1">OK (Safe)</span></td>
                                    <td>15 Dec 2027</td>
                                    <td class="text-end pe-4"><button class="btn btn-sm btn-outline-primary py-1 px-2">Update</button></td>
                                </tr>
                                <tr>
                                    <td class="ps-4 fw-bold text-dark">Falcon Battery Sprayer (16L)</td>
                                    <td>Farming Tools</td>
                                    <td>3 units</td>
                                    <td>5 units</td>
                                    <td><span class="badge bg-danger px-3 py-1">Low Stock Alert</span></td>
                                    <td>N/A</td>
                                    <td class="text-end pe-4"><button class="btn btn-sm btn-outline-primary py-1 px-2">Reorder</button></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
""" + foot_html()
    save_admin_page("admin-inventory.html", content)
    print("Generated dist/admin-inventory.html")

# ==============================================================================
# 8. ADMIN CUSTOMERS
# ==============================================================================
def build_admin_customers():
    sidebar = render_admin_sidebar("customers")
    content = head_html("शेतकरी ग्राहक यादी", "Farmers Directory") + nav_html("dashboard") + f"""
<div class="container-fluid px-3 px-lg-4 my-4">
    <div class="row g-4">
        <!-- Sidebar -->
        <div class="col-lg-3 col-xl-2">
            {sidebar}
        </div>

        <div class="col-lg-9 col-xl-10">
            <div class="card border-0 shadow-sm rounded-4 overflow-hidden bg-white">
                <div class="card-header bg-white py-3 px-4 border-bottom d-flex justify-content-between align-items-center">
                    <h5 class="mb-0 fw-bold text-dark"><i class="bi bi-people-fill text-success me-2"></i><span class="lang-mr">शेतकरी ग्राहक यादी</span><span class="lang-en">Registered Farmers (7)</span></h5>
                </div>
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-hover align-middle mb-0">
                            <thead class="table-light text-muted small">
                                <tr>
                                    <th class="ps-4">Farmer Name</th>
                                    <th>Mobile Number</th>
                                    <th>Village</th>
                                    <th>Primary Crop</th>
                                    <th>Total Purchases</th>
                                    <th>Status</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="ps-4 fw-bold text-dark">Ramesh Patil</td>
                                    <td>8600813827</td>
                                    <td>Vaijapur</td>
                                    <td>Cotton, Maize</td>
                                    <td>₹14,500</td>
                                    <td><span class="badge bg-success">Active</span></td>
                                </tr>
                                <tr>
                                    <td class="ps-4 fw-bold text-dark">Suresh Deshmukh</td>
                                    <td>9822001122</td>
                                    <td>Shrirampur</td>
                                    <td>Sugarcane</td>
                                    <td>₹28,900</td>
                                    <td><span class="badge bg-success">Active</span></td>
                                </tr>
                                <tr>
                                    <td class="ps-4 fw-bold text-dark">Dnyaneshwar Pawar</td>
                                    <td>9421003344</td>
                                    <td>Gangapur</td>
                                    <td>Soybean, Gram</td>
                                    <td>₹8,200</td>
                                    <td><span class="badge bg-success">Active</span></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
""" + foot_html()
    save_admin_page("admin-customers.html", content)
    print("Generated dist/admin-customers.html")

if __name__ == "__main__":
    build_login_page()
    build_admin_dashboard()
    build_admin_categories()
    build_admin_products()
    build_admin_product_form()
    build_admin_udhari()
    build_admin_inventory()
    build_admin_customers()
    print("All Admin Panel and Login pages built successfully matching all screenshots!")
