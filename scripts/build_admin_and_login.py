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
        <a href="admin-reviews.html" class="admin-nav-link {'active' if active_tab == 'reviews' else ''}">
            <i class="bi bi-star-fill text-warning"></i>
            <span><span class="lang-mr">शेतकरी रिव्ह्यू व्यवस्थापन</span><span class="lang-en">Manage Reviews</span></span>
            <span class="badge bg-success ms-auto" style="font-size:0.65rem;">New</span>
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

        <!-- Bilingual Switcher in Login Header -->
        <div class="login-language-switch" role="group" aria-label="Choose language">
            <button type="button" id="loginBtnEn" onclick="setLang('en')" class="btn-lang-en">EN</button>
            <button type="button" id="loginBtnMr" onclick="setLang('mr')" class="btn-lang-mr active">मराठी</button>
        </div>
    </div>

    <section class="login-card" aria-labelledby="loginTitle">
        <div class="login-brand">
            <img src="images/saptashrungi_logo_round.jpg" alt="Krushi Seva Kendra logo">
            <div>
                <div class="login-brand-name">Krushi Seva Kendra</div>
                <div class="login-brand-subtitle">
                    <span class="lang-mr">सप्तशृंगी ॲग्रो सर्व्हिसेस</span>
                    <span class="lang-en">Saptashrungi Agro Services</span>
                </div>
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

        <!-- Dynamic Success / Logout Alert Banner -->
        <div id="loginAlertBox" class="alert py-2 px-3 small rounded-3 mb-3 d-none align-items-center" style="background:#e6f4ea; color:#137333; border: 1px solid #ceead6;">
            <i id="loginAlertIcon" class="bi bi-check-circle-fill me-2 fs-6"></i>
            <div id="loginAlertContent">
                <span id="alertMsgMr" class="lang-mr">आपण यशस्वीरित्या लॉग आउट झाला आहात.</span>
                <span id="alertMsgEn" class="lang-en">You have been logged out successfully.</span>
            </div>
        </div>

        <form id="loginForm" action="login.html" onsubmit="handleStaticLogin(event)">
            <div class="login-field">
                <label for="loginUsername">
                    <span class="lang-mr">मोबाईल नंबर किंवा ईमेल *</span>
                    <span class="lang-en">Mobile number or email *</span>
                </label>
                <input type="text" name="username" id="loginUsername"
                       data-placeholder-mr="मोबाईल नंबर किंवा ईमेल"
                       data-placeholder-en="Mobile number or email"
                       placeholder="मोबाईल नंबर किंवा ईमेल"
                       required autofocus autocomplete="username">
            </div>

            <div class="login-field">
                <label for="loginPassword">
                    <span class="lang-mr">पासवर्ड *</span>
                    <span class="lang-en">Password *</span>
                </label>
                <div class="login-password-wrap">
                    <input type="password" name="password" id="loginPassword"
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

            <button type="submit" class="login-submit" id="btnSubmit">
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
    var uInput = document.getElementById('loginUsername');
    var username = (uInput ? uInput.value : '').trim().toLowerCase();
    
    // Check if admin login
    if (username.indexOf('admin') !== -1 || username === 'admin@krushiseva.com' || username === 'staff') {
        localStorage.setItem('user_role', 'admin');
        localStorage.setItem('user_name', 'Admin');
        window.location.href = 'admin-dashboard.html';
    } else {
        localStorage.setItem('user_role', 'farmer');
        var registeredName = localStorage.getItem('last_registered_name');
        var displayName = registeredName || username.split('@')[0] || 'VSGAWALI';
        localStorage.setItem('user_name', displayName);
        window.location.href = 'farmer-dashboard.html';
    }
}

function setLang(lang) {
    document.documentElement.setAttribute('lang', lang);
    localStorage.setItem('site_lang', lang);
    var isMr = (lang === 'mr');
    
    // Update active state on language toggle buttons
    var btnEn = document.getElementById('loginBtnEn');
    var btnMr = document.getElementById('loginBtnMr');
    if (btnEn) btnEn.className = (!isMr) ? 'btn-lang-en active' : 'btn-lang-en';
    if (btnMr) btnMr.className = isMr ? 'btn-lang-mr active' : 'btn-lang-mr';

    // Update input placeholders
    document.querySelectorAll('[data-placeholder-mr]').forEach(function(el){
        el.placeholder = isMr ? el.getAttribute('data-placeholder-mr') : el.getAttribute('data-placeholder-en');
    });

    window.dispatchEvent(new CustomEvent('languagechange', { detail: { lang: lang } }));
}

document.addEventListener('DOMContentLoaded', function(){
    var savedLang = localStorage.getItem('site_lang') || 'mr';
    setLang(savedLang);
    
    var urlParams = new URLSearchParams(window.location.search);
    var alertBox = document.getElementById('loginAlertBox');
    var alertIcon = document.getElementById('loginAlertIcon');
    var msgMr = document.getElementById('alertMsgMr');
    var msgEn = document.getElementById('alertMsgEn');
    var uInput = document.getElementById('loginUsername');
    var pInput = document.getElementById('loginPassword');

    // Case 1: Just registered
    if (urlParams.has('registered')) {
        var phone = urlParams.get('phone') || localStorage.getItem('last_registered_phone') || '';
        if (uInput && phone) {
            uInput.value = phone;
        }
        if (pInput) {
            pInput.value = '';
            pInput.focus();
        }
        if (alertBox) {
            alertBox.style.background = '#e6f4ea';
            alertBox.style.color = '#137333';
            alertBox.style.borderColor = '#ceead6';
            if (alertIcon) alertIcon.className = 'bi bi-check-circle-fill me-2 fs-6 text-success';
            if (msgMr) msgMr.textContent = '🎉 आपली शेतकरी नोंदणी यशस्वी झाली आहे! कृपया पासवर्ड टाकून लॉगिन करा.';
            if (msgEn) msgEn.textContent = '🎉 Farmer registration successful! Please enter your password to log in.';
            alertBox.classList.remove('d-none');
            alertBox.classList.add('d-flex');
        }
    }
    // Case 2: Just logged out
    else if (urlParams.has('logout')) {
        if (alertBox) {
            alertBox.style.background = '#f1f5f9';
            alertBox.style.color = '#334155';
            alertBox.style.borderColor = '#cbd5e1';
            if (alertIcon) alertIcon.className = 'bi bi-info-circle-fill me-2 fs-6 text-secondary';
            if (msgMr) msgMr.textContent = 'आपण यशस्वीरित्या लॉग आउट झाला आहात.';
            if (msgEn) msgEn.textContent = 'You have been logged out successfully.';
            alertBox.classList.remove('d-none');
            alertBox.classList.add('d-flex');
        }
        if (uInput) {
            var lastPhone = localStorage.getItem('last_registered_phone');
            if (lastPhone) uInput.value = lastPhone;
            else uInput.value = '';
        }
        if (pInput) pInput.value = '';
    }
    // Case 3: Default visit
    else {
        var lastPhone = localStorage.getItem('last_registered_phone');
        if (lastPhone && uInput && !uInput.value) {
            uInput.value = lastPhone;
        }
    }
});
</script>
</body>
</html>
"""
    with open(os.path.join(DIST_DIR, "login.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Generated dist/login.html with full bilingual support and registration alert handler")


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
                <!-- Add Category Card (Screenshot 1 left) -->
                <div class="col-lg-4">
                    <div class="card border-0 shadow-sm rounded-4 overflow-hidden bg-white">
                        <div class="card-header bg-success text-white py-3 px-4" style="background:#15803d !important;">
                            <h6 class="mb-0 fw-bold d-flex align-items-center gap-2">
                                <i class="bi bi-plus-circle"></i>
                                <span class="lang-mr">नवीन कॅटेगरी जोडा</span>
                                <span class="lang-en">Add New Category</span>
                            </h6>
                        </div>
                        <div class="card-body p-4">
                            <div id="catSuccessAlert" class="alert alert-success d-none py-2 mb-3 small">
                                <i class="bi bi-check-circle-fill me-1"></i>
                                <span class="lang-mr">कॅटेगरी फोटोसह यशस्वीरित्या जोडली!</span>
                                <span class="lang-en">Category added successfully with image!</span>
                            </div>

                            <form id="addCategoryForm" onsubmit="return handleCreateCategory(event)">
                                <div class="mb-3">
                                    <label class="form-label small fw-bold text-success">Category Name (English) *</label>
                                    <input type="text" id="catNameEn" class="form-control" placeholder="e.g. Bio-Pesticides" required>
                                </div>
                                <div class="mb-3">
                                    <label class="form-label small fw-bold text-success">Category Name (Marathi)</label>
                                    <input type="text" id="catNameMr" class="form-control" placeholder="उदा. सेंद्रिय कीटकनाशके">
                                </div>
                                <div class="mb-3">
                                    <label class="form-label small fw-bold text-success">Description</label>
                                    <textarea id="catDesc" class="form-control" rows="3" placeholder="Short description"></textarea>
                                </div>

                                <!-- Image Upload Option (Requested) -->
                                <div class="mb-4">
                                    <label class="form-label small fw-bold text-success d-flex align-items-center gap-1">
                                        <i class="bi bi-image"></i>
                                        <span class="lang-mr">कॅटेगरीचा फोटो (Category Image)</span>
                                        <span class="lang-en">Category Image</span>
                                    </label>
                                    
                                    <div class="p-3 rounded-3 text-center border-dashed"
                                         id="catDropzone"
                                         onclick="triggerCatFileInput()"
                                         style="border: 2px dashed #16a34a; background: #f0fdf4; cursor: pointer; transition: all 0.2s;">
                                        
                                        <input type="file" id="catImageInput" accept="image/jpeg,image/png,image/webp,image/jpg,image/gif" class="d-none" onchange="previewCatImage(event)">
                                        
                                        <!-- Prompt -->
                                        <div id="catUploadPrompt" class="py-2">
                                            <i class="bi bi-cloud-arrow-up text-success fs-2 d-block mb-1"></i>
                                            <span class="small fw-bold text-dark d-block">
                                                <span class="lang-mr">फोटो निवडण्यासाठी येथे क्लिक करा</span>
                                                <span class="lang-en">Click here to upload category image</span>
                                            </span>
                                            <small class="text-muted d-block" style="font-size:11px;">JPG, PNG, WebP (Max 5MB)</small>
                                            <button type="button" class="btn btn-sm btn-outline-success rounded-pill px-3 py-1 mt-2 fw-semibold" style="font-size:12px;">
                                                <i class="bi bi-folder2-open me-1"></i> Choose Image
                                            </button>
                                        </div>

                                        <!-- Live Preview -->
                                        <div id="catImagePreviewWrap" class="d-none text-center py-1">
                                            <div class="position-relative d-inline-block shadow-sm rounded-3 overflow-hidden border bg-white p-1">
                                                <img id="catImagePreview" src="" alt="Category Image" style="max-height: 120px; max-width: 100%; object-fit: cover; border-radius: 6px;">
                                                <button type="button" onclick="removeCatImage(event)" class="btn btn-danger btn-sm position-absolute top-0 end-0 m-1 rounded-circle d-flex align-items-center justify-content-center" style="width: 26px; height: 26px; padding:0;" title="Remove image">
                                                    <i class="bi bi-x-lg" style="font-size: 11px;"></i>
                                                </button>
                                            </div>
                                            <div class="mt-2 d-flex align-items-center justify-content-center gap-2">
                                                <span id="catFileName" class="badge bg-success-subtle text-success border border-success-subtle small" style="font-size:11px;"></span>
                                                <button type="button" onclick="triggerCatFileInput(); event.stopPropagation();" class="btn btn-sm btn-link text-success text-decoration-none p-0 fw-bold" style="font-size:12px;">Change</button>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <button type="submit" class="btn btn-success w-100 fw-bold py-2 rounded-3 shadow-sm" style="background:#16a34a;border:none;">
                                    <span class="lang-mr">कॅटेगरी तयार करा</span>
                                    <span class="lang-en">Create Category</span>
                                </button>
                            </form>
                        </div>
                    </div>
                </div>

                <!-- Categories List Table (Screenshot 1 right) -->
                <div class="col-lg-8">
                    <div class="card border-0 shadow-sm rounded-4 overflow-hidden bg-white">
                        <div class="card-header bg-white py-3 px-4 border-bottom d-flex justify-content-between align-items-center">
                            <h5 class="mb-0 fw-bold text-dark d-flex align-items-center gap-2">
                                <i class="bi bi-tags-fill text-success"></i>
                                <span>Product Categories (<span id="catCountSpan">8</span>)</span>
                            </h5>
                        </div>
                        <div class="card-body p-0">
                            <div class="table-responsive">
                                <table class="table table-hover align-middle mb-0">
                                    <thead class="table-light text-muted small">
                                        <tr>
                                            <th class="ps-4">#</th>
                                            <th>IMAGE</th>
                                            <th>CATEGORY NAME</th>
                                            <th>MARATHI NAME</th>
                                            <th>DESCRIPTION</th>
                                            <th>STATUS</th>
                                            <th class="text-end pe-4">ACTIONS</th>
                                        </tr>
                                    </thead>
                                    <tbody id="categoryTableBody">
                                        <tr>
                                            <td class="ps-4 fw-bold">1</td>
                                            <td><img src="images/wheat_seeds.jpg" class="rounded-3 border" style="width:36px;height:36px;object-fit:cover;"></td>
                                            <td><strong class="text-dark">Seeds</strong></td>
                                            <td>बियाणे</td>
                                            <td class="small text-muted text-truncate" style="max-width: 160px;">High yield certified hyb...</td>
                                            <td><span class="badge bg-success px-2 py-1">ACTIVE</span></td>
                                            <td class="text-end pe-4">
                                                <button class="btn btn-sm btn-outline-secondary py-1 px-2" style="font-size:0.75rem;">Disable</button>
                                                <button class="btn btn-sm btn-outline-danger py-1 px-2 ms-1" style="font-size:0.75rem;"><i class="bi bi-trash"></i></button>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="ps-4 fw-bold">2</td>
                                            <td><img src="images/fertilizer_npk.jpg" class="rounded-3 border" style="width:36px;height:36px;object-fit:cover;"></td>
                                            <td><strong class="text-dark">Fertilizers</strong></td>
                                            <td>खते</td>
                                            <td class="small text-muted text-truncate" style="max-width: 160px;">Chemical, water-solub...</td>
                                            <td><span class="badge bg-success px-2 py-1">ACTIVE</span></td>
                                            <td class="text-end pe-4">
                                                <button class="btn btn-sm btn-outline-secondary py-1 px-2" style="font-size:0.75rem;">Disable</button>
                                                <button class="btn btn-sm btn-outline-danger py-1 px-2 ms-1" style="font-size:0.75rem;"><i class="bi bi-trash"></i></button>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="ps-4 fw-bold">3</td>
                                            <td><img src="images/urea_bag.jpg" class="rounded-3 border" style="width:36px;height:36px;object-fit:cover;"></td>
                                            <td><strong class="text-dark">Pesticides</strong></td>
                                            <td>कीटकनाशके</td>
                                            <td class="small text-muted text-truncate" style="max-width: 160px;">Broad-spectrum insec...</td>
                                            <td><span class="badge bg-success px-2 py-1">ACTIVE</span></td>
                                            <td class="text-end pe-4">
                                                <button class="btn btn-sm btn-outline-secondary py-1 px-2" style="font-size:0.75rem;">Disable</button>
                                                <button class="btn btn-sm btn-outline-danger py-1 px-2 ms-1" style="font-size:0.75rem;"><i class="bi bi-trash"></i></button>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="ps-4 fw-bold">4</td>
                                            <td><img src="images/battery_sprayer.jpg" class="rounded-3 border" style="width:36px;height:36px;object-fit:cover;"></td>
                                            <td><strong class="text-dark">Farming Tools</strong></td>
                                            <td>शेती अवजारे</td>
                                            <td class="small text-muted text-truncate" style="max-width: 160px;">Battery sprayers, pruni...</td>
                                            <td><span class="badge bg-success px-2 py-1">ACTIVE</span></td>
                                            <td class="text-end pe-4">
                                                <button class="btn btn-sm btn-outline-secondary py-1 px-2" style="font-size:0.75rem;">Disable</button>
                                                <button class="btn btn-sm btn-outline-danger py-1 px-2 ms-1" style="font-size:0.75rem;"><i class="bi bi-trash"></i></button>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="ps-4 fw-bold">5</td>
                                            <td><img src="images/saptashrungi_shop.jpg" class="rounded-3 border" style="width:36px;height:36px;object-fit:cover;"></td>
                                            <td><strong class="text-dark">Drip Irrigation</strong></td>
                                            <td>ठिबक सिंचन</td>
                                            <td class="small text-muted text-truncate" style="max-width: 160px;">Drip laterals, drippers, ...</td>
                                            <td><span class="badge bg-success px-2 py-1">ACTIVE</span></td>
                                            <td class="text-end pe-4">
                                                <button class="btn btn-sm btn-outline-secondary py-1 px-2" style="font-size:0.75rem;">Disable</button>
                                                <button class="btn btn-sm btn-outline-danger py-1 px-2 ms-1" style="font-size:0.75rem;"><i class="bi bi-trash"></i></button>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="ps-4 fw-bold">6</td>
                                            <td><img src="images/cotton_seeds.jpg" class="rounded-3 border" style="width:36px;height:36px;object-fit:cover;"></td>
                                            <td><strong class="text-dark">Animal Feed</strong></td>
                                            <td>पशूखाद्य</td>
                                            <td class="small text-muted text-truncate" style="max-width: 160px;">Cattle feed pellets, mi...</td>
                                            <td><span class="badge bg-success px-2 py-1">ACTIVE</span></td>
                                            <td class="text-end pe-4">
                                                <button class="btn btn-sm btn-outline-secondary py-1 px-2" style="font-size:0.75rem;">Disable</button>
                                                <button class="btn btn-sm btn-outline-danger py-1 px-2 ms-1" style="font-size:0.75rem;"><i class="bi bi-trash"></i></button>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="ps-4 fw-bold">7</td>
                                            <td><img src="images/soybean_seeds.jpg" class="rounded-3 border" style="width:36px;height:36px;object-fit:cover;"></td>
                                            <td><strong class="text-dark">Organic Products</strong></td>
                                            <td>सेंद्रिय उत्पादने</td>
                                            <td class="small text-muted text-truncate" style="max-width: 160px;">Neem cake, vermicom...</td>
                                            <td><span class="badge bg-success px-2 py-1">ACTIVE</span></td>
                                            <td class="text-end pe-4">
                                                <button class="btn btn-sm btn-outline-secondary py-1 px-2" style="font-size:0.75rem;">Disable</button>
                                                <button class="btn btn-sm btn-outline-danger py-1 px-2 ms-1" style="font-size:0.75rem;"><i class="bi bi-trash"></i></button>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="ps-4 fw-bold">8</td>
                                            <td><img src="images/saptashrungi_logo_round.jpg" class="rounded-3 border" style="width:36px;height:36px;object-fit:cover;"></td>
                                            <td><strong class="text-dark">Plant Growth Promoters</strong></td>
                                            <td>वाढ संप्रेरके</td>
                                            <td class="small text-muted text-truncate" style="max-width: 160px;">Humic acid, seaweed e...</td>
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

<script>
let selectedCatImageDataUrl = '';

function triggerCatFileInput() {{
    const input = document.getElementById('catImageInput');
    if (input) input.click();
}}

function previewCatImage(event) {{
    const file = event.target.files && event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function(e) {{
        selectedCatImageDataUrl = e.target.result;
        const img = document.getElementById('catImagePreview');
        const promptBox = document.getElementById('catUploadPrompt');
        const previewWrap = document.getElementById('catImagePreviewWrap');
        const fileNameBadge = document.getElementById('catFileName');

        if (img) img.src = selectedCatImageDataUrl;
        if (fileNameBadge) fileNameBadge.textContent = file.name + ' (' + Math.round(file.size / 1024) + ' KB)';
        if (promptBox) promptBox.classList.add('d-none');
        if (previewWrap) previewWrap.classList.remove('d-none');
    }};
    reader.readAsDataURL(file);
}}

function removeCatImage(event) {{
    if (event) event.stopPropagation();
    selectedCatImageDataUrl = '';
    const input = document.getElementById('catImageInput');
    if (input) input.value = '';
    const promptBox = document.getElementById('catUploadPrompt');
    const previewWrap = document.getElementById('catImagePreviewWrap');
    if (promptBox) promptBox.classList.remove('d-none');
    if (previewWrap) previewWrap.classList.add('d-none');
}}

function handleCreateCategory(e) {{
    if (e && e.preventDefault) e.preventDefault();

    const nameEn = document.getElementById('catNameEn').value.trim();
    const nameMr = document.getElementById('catNameMr').value.trim() || nameEn;
    const desc = document.getElementById('catDesc').value.trim();
    const image = selectedCatImageDataUrl || 'images/saptashrungi_logo_round.jpg';

    const newCat = {{
        id: Date.now(),
        nameEn: nameEn,
        nameMr: nameMr,
        desc: desc,
        image: image
    }};

    // Save to localStorage
    const saved = JSON.parse(localStorage.getItem('ksk_custom_categories') || '[]');
    saved.unshift(newCat);
    localStorage.setItem('ksk_custom_categories', JSON.stringify(saved));

    const alertBox = document.getElementById('catSuccessAlert');
    if (alertBox) alertBox.classList.remove('d-none');

    // Prepend to table
    const tbody = document.getElementById('categoryTableBody');
    if (tbody) {{
        const tr = document.createElement('tr');
        tr.className = 'table-success-subtle';
        tr.innerHTML = `
            <td class="ps-4 fw-bold">NEW</td>
            <td><img src="${{image}}" class="rounded-3 border shadow-sm" style="width:36px;height:36px;object-fit:cover;"></td>
            <td><strong class="text-dark">${{nameEn}}</strong></td>
            <td>${{nameMr}}</td>
            <td class="small text-muted text-truncate" style="max-width: 160px;">${{desc}}</td>
            <td><span class="badge bg-success px-2 py-1">ACTIVE</span></td>
            <td class="text-end pe-4">
                <button class="btn btn-sm btn-outline-secondary py-1 px-2" style="font-size:0.75rem;">Disable</button>
            </td>
        `;
        tbody.insertBefore(tr, tbody.firstChild);
    }}

    // Reset form
    document.getElementById('addCategoryForm').reset();
    removeCatImage();

    setTimeout(() => {{
        if (alertBox) alertBox.classList.add('d-none');
    }}, 3000);

    return false;
}}

document.addEventListener('DOMContentLoaded', function(){{
    const saved = JSON.parse(localStorage.getItem('ksk_custom_categories') || '[]');
    const tbody = document.getElementById('categoryTableBody');
    const countSpan = document.getElementById('catCountSpan');
    if (countSpan) countSpan.textContent = 8 + saved.length;

    if (tbody && saved.length > 0) {{
        saved.forEach((c, idx) => {{
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td class="ps-4 fw-bold">+${{idx+1}}</td>
                <td><img src="${{c.image}}" class="rounded-3 border shadow-sm" style="width:36px;height:36px;object-fit:cover;"></td>
                <td><strong class="text-dark">${{c.nameEn}}</strong></td>
                <td>${{c.nameMr}}</td>
                <td class="small text-muted text-truncate" style="max-width: 160px;">${{c.desc}}</td>
                <td><span class="badge bg-success px-2 py-1">ACTIVE</span></td>
                <td class="text-end pe-4">
                    <button class="btn btn-sm btn-outline-danger py-1 px-2" style="font-size:0.75rem;" onclick="deleteCustomCategory(${{c.id}})">Delete</button>
                </td>
            `;
            tbody.insertBefore(tr, tbody.firstChild);
        }});
    }}
}});

function deleteCustomCategory(id) {{
    let saved = JSON.parse(localStorage.getItem('ksk_custom_categories') || '[]');
    saved = saved.filter(c => c.id !== id);
    localStorage.setItem('ksk_custom_categories', JSON.stringify(saved));
    window.location.reload();
}}
</script>
""" + foot_html()
    save_admin_page("admin-categories.html", content)
    print("Generated dist/admin-categories.html matching Screenshot 1 with Image Upload!")


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
                            <tbody id="adminProductsTableBody">
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

<script>
document.addEventListener('DOMContentLoaded', function(){{
    const tbody = document.getElementById('adminProductsTableBody');
    const customProds = JSON.parse(localStorage.getItem('ksk_custom_products') || '[]');
    if (tbody && customProds.length > 0) {{
        customProds.forEach(p => {{
            const tr = document.createElement('tr');
            tr.className = 'table-success-subtle';
            tr.innerHTML = `
                <td class="ps-4">
                    <img src="${{p.image}}" class="rounded-3 shadow-sm border" style="width:44px;height:44px;object-fit:cover;" onerror="this.src='images/cotton_seeds.jpg'">
                </td>
                <td>
                    <strong class="text-dark d-block">${{p.nameEn}}</strong>
                    <small class="text-muted">${{p.nameMr}}</small>
                </td>
                <td>${{p.company}}</td>
                <td><span class="badge bg-light text-dark border">${{p.category}}</span></td>
                <td><strong class="text-success">₹${{p.discountPrice || p.price}}</strong></td>
                <td><span class="badge bg-success">${{p.stock}}</span></td>
                <td><span class="badge bg-success-subtle text-success">Active</span></td>
                <td class="text-end pe-4">
                    <a href="admin-product-form.html" class="btn btn-sm btn-outline-primary py-1 px-2"><i class="bi bi-pencil-square"></i></a>
                    <button class="btn btn-sm btn-outline-danger py-1 px-2 ms-1" onclick="deleteCustomProduct(${{p.id}})"><i class="bi bi-trash"></i></button>
                </td>
            `;
            tbody.insertBefore(tr, tbody.firstChild);
        }});
    }}
}});

function deleteCustomProduct(id) {{
    if (confirm('या उत्पादनाला काढून टाकायचे आहे का? (Delete this product?)')) {{
        let prods = JSON.parse(localStorage.getItem('ksk_custom_products') || '[]');
        prods = prods.filter(p => p.id !== id);
        localStorage.setItem('ksk_custom_products', JSON.stringify(prods));
        window.location.reload();
    }}
}}
</script>
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
                <div class="card-header bg-white py-3 px-4 border-bottom d-flex justify-content-between align-items-center flex-wrap gap-2">
                    <h5 class="mb-0 fw-bold text-dark d-flex align-items-center gap-2">
                        <i class="bi bi-plus-circle text-success fs-5"></i>
                        <span class="lang-mr">उत्पादन जोडा / बदला</span>
                        <span class="lang-en">Add / Edit Product</span>
                    </h5>
                    <a href="admin-products.html" class="btn btn-sm btn-outline-secondary rounded-pill px-3">&larr; <span class="lang-mr">उत्पादनांकडे परत जा</span><span class="lang-en">Back to Products</span></a>
                </div>
                <div class="card-body p-4">
                    <div id="saveAlert" class="alert alert-success d-none py-2 mb-3">
                        <i class="bi bi-check-circle-fill me-2"></i>
                        <span class="lang-mr">उत्पादन फोटोसह यशस्वीरित्या सेव्ह केले!</span>
                        <span class="lang-en">Product saved successfully with image!</span>
                    </div>

                    <form id="productForm" onsubmit="return handleSaveProduct(event)">
                        <div class="row g-3">
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-success">
                                    <span class="lang-mr">उत्पादनाचे नाव (इंग्रजी) *</span>
                                    <span class="lang-en">Product Name (English) *</span>
                                </label>
                                <input type="text" id="pNameEn" class="form-control" placeholder="e.g. Wheat Seeds (Lok-1)" required>
                            </div>
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-success">
                                    <span class="lang-mr">उत्पादनाचे नाव (मराठी)</span>
                                    <span class="lang-en">Product Name (Marathi)</span>
                                </label>
                                <input type="text" id="pNameMr" class="form-control" placeholder="उदा. गहू बियाणे (लोक-१)">
                            </div>
                            <div class="col-md-4">
                                <label class="form-label small fw-bold text-success">
                                    <span class="lang-mr">कंपनी / ब्रँड</span>
                                    <span class="lang-en">Company / Brand</span>
                                </label>
                                <input type="text" id="pCompany" class="form-control" placeholder="e.g. MAHABEEJ / IFFCO">
                            </div>
                            <div class="col-md-4">
                                <label class="form-label small fw-bold text-success">
                                    <span class="lang-mr">वर्गवारी (Category)</span>
                                    <span class="lang-en">Category</span>
                                </label>
                                <select id="pCategory" class="form-select">
                                    <option value="Seeds">Seeds (बियाणे)</option>
                                    <option value="Fertilizers">Fertilizers (खते)</option>
                                    <option value="Pesticides">Pesticides (कीटकनाशके)</option>
                                    <option value="Farming Tools">Farming Tools (शेती अवजारे)</option>
                                    <option value="Drip Irrigation">Drip Irrigation (ठिबक सिंचन)</option>
                                    <option value="Animal Feed">Animal Feed (पशूखाद्य)</option>
                                    <option value="Organic Products">Organic Products (सेंद्रिय)</option>
                                    <option value="Plant Growth Promoters">Plant Growth Promoters (वाढ संप्रेरके)</option>
                                </select>
                            </div>
                            <div class="col-md-4">
                                <label class="form-label small fw-bold text-success">
                                    <span class="lang-mr">जीएसटी दर (%)</span>
                                    <span class="lang-en">GST Rate (%)</span>
                                </label>
                                <input type="number" step="0.01" id="pGst" class="form-control" placeholder="0.00 or 5.00" value="0.00">
                            </div>

                            <div class="col-md-3">
                                <label class="form-label small fw-bold text-success">
                                    <span class="lang-mr">मूळ किंमत (₹) *</span>
                                    <span class="lang-en">Original Price (₹) *</span>
                                </label>
                                <input type="number" step="0.01" id="pPrice" class="form-control" placeholder="1450" required>
                            </div>
                            <div class="col-md-3">
                                <label class="form-label small fw-bold text-success">
                                    <span class="lang-mr">सवलत किंमत (₹)</span>
                                    <span class="lang-en">Discount Price (₹)</span>
                                </label>
                                <input type="number" step="0.01" id="pDiscount" class="form-control" placeholder="1350">
                            </div>
                            <div class="col-md-3">
                                <label class="form-label small fw-bold text-success">
                                    <span class="lang-mr">उपलब्ध साठा (Stock)</span>
                                    <span class="lang-en">Stock Quantity</span>
                                </label>
                                <input type="number" id="pStock" class="form-control" placeholder="50" value="50">
                            </div>
                            <div class="col-md-3">
                                <label class="form-label small fw-bold text-success">
                                    <span class="lang-mr">किमान साठा अलर्ट</span>
                                    <span class="lang-en">Minimum Stock Alert</span>
                                </label>
                                <input type="number" id="pMinStock" class="form-control" placeholder="10" value="10">
                            </div>

                            <!-- Product Image Upload Box (Requested Feature) -->
                            <div class="col-12">
                                <label class="form-label small fw-bold text-success d-flex align-items-center gap-1">
                                    <i class="bi bi-image-fill"></i>
                                    <span class="lang-mr">उत्पादनाचा फोटो (Product Image) *</span>
                                    <span class="lang-en">Product Image *</span>
                                </label>

                                <div class="product-image-upload-box p-4 rounded-4 text-center border-dashed"
                                     id="productDropzone"
                                     onclick="triggerFileInput()"
                                     style="border: 2px dashed #16a34a; background: #f0fdf4; cursor: pointer; transition: all 0.2s;">
                                    
                                    <input type="file" id="productImageInput" accept="image/jpeg,image/png,image/webp,image/jpg,image/gif" class="d-none" onchange="previewProductImage(event)">
                                    
                                    <!-- Upload Prompt (Click or Drag) -->
                                    <div id="uploadPrompt" class="py-2">
                                        <div class="mb-2">
                                            <i class="bi bi-cloud-arrow-up-fill text-success" style="font-size: 2.75rem;"></i>
                                        </div>
                                        <h6 class="fw-bold text-dark mb-1">
                                            <span class="lang-mr">फोटो निवडण्यासाठी येथे क्लिक करा</span>
                                            <span class="lang-en">Click here to upload product image</span>
                                        </h6>
                                        <p class="small text-muted mb-2">
                                            <span class="lang-mr">किंवा तुमच्या डिव्हाइसवरून इमेज फाइल येथे ड्रॅग आणि ड्रॉप करा (JPG, PNG, WebP)</span>
                                            <span class="lang-en">or drag and drop your image file here (JPG, PNG, WebP, max 10MB)</span>
                                        </p>
                                        <button type="button" class="btn btn-sm btn-outline-success rounded-pill px-3 py-1 fw-bold">
                                            <i class="bi bi-folder2-open me-1"></i>
                                            <span class="lang-mr">फाइल निवडा (Choose File)</span>
                                            <span class="lang-en">Choose File</span>
                                        </button>
                                    </div>

                                    <!-- Live Selected Image Preview -->
                                    <div id="imagePreviewWrap" class="d-none text-center py-2">
                                        <div class="d-inline-block position-relative shadow-sm rounded-4 overflow-hidden border p-2 bg-white">
                                            <img id="productImagePreview" src="" alt="Selected Product Image" style="max-height: 200px; max-width: 100%; object-fit: contain; border-radius: 10px;">
                                            <button type="button" onclick="removeProductImage(event)" class="btn btn-danger btn-sm position-absolute top-0 end-0 m-2 rounded-circle d-flex align-items-center justify-content-center" style="width: 32px; height: 32px;" title="Remove image">
                                                <i class="bi bi-trash-fill fs-6"></i>
                                            </button>
                                        </div>
                                        <div class="mt-2 d-flex align-items-center justify-content-center gap-2">
                                            <span id="imageFileName" class="badge bg-success-subtle text-success border border-success-subtle px-3 py-1 rounded-pill small fw-semibold"></span>
                                            <button type="button" onclick="triggerFileInput(); event.stopPropagation();" class="btn btn-sm btn-link text-success text-decoration-none fw-bold">
                                                <i class="bi bi-arrow-repeat me-1"></i>
                                                <span class="lang-mr">फोटो बदला (Change Image)</span>
                                                <span class="lang-en">Change Image</span>
                                            </button>
                                        </div>
                                    </div>
                                </div>
                                <div class="form-text small text-muted">
                                    <span class="lang-mr">दुकानात व वेबसाइटवर दाखवण्यासाठी उत्पादनाचा स्पष्ट फोटो निवडा.</span>
                                    <span class="lang-en">Select a clear product image to display in store catalog.</span>
                                </div>
                            </div>

                            <div class="col-12">
                                <label class="form-label small fw-bold text-success">
                                    <span class="lang-mr">उत्पादनाची माहिती / वापर (Description)</span>
                                    <span class="lang-en">Description</span>
                                </label>
                                <textarea id="pDesc" class="form-control" rows="3" placeholder="Enter product usage details, application dosage, etc."></textarea>
                            </div>

                            <div class="col-12 text-end pt-3">
                                <button type="submit" id="btnSaveProd" class="btn btn-success fw-bold px-4 py-2 rounded-3 shadow-sm" style="background:#16a34a;border:none;">
                                    💾 <span class="lang-mr">उत्पादन सेव्ह करा</span><span class="lang-en">Save Product</span>
                                </button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
let selectedProductImageDataUrl = '';

function triggerFileInput() {{
    var input = document.getElementById('productImageInput');
    if (input) input.click();
}}

function previewProductImage(event) {{
    const file = event.target.files && event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function(e) {{
        selectedProductImageDataUrl = e.target.result;
        const img = document.getElementById('productImagePreview');
        const promptBox = document.getElementById('uploadPrompt');
        const previewWrap = document.getElementById('imagePreviewWrap');
        const fileNameBadge = document.getElementById('imageFileName');

        if (img) img.src = selectedProductImageDataUrl;
        if (fileNameBadge) fileNameBadge.textContent = file.name + ' (' + Math.round(file.size / 1024) + ' KB)';
        if (promptBox) promptBox.classList.add('d-none');
        if (previewWrap) previewWrap.classList.remove('d-none');
    }};
    reader.readAsDataURL(file);
}}

function removeProductImage(event) {{
    if (event) event.stopPropagation();
    selectedProductImageDataUrl = '';
    const input = document.getElementById('productImageInput');
    if (input) input.value = '';
    const promptBox = document.getElementById('uploadPrompt');
    const previewWrap = document.getElementById('imagePreviewWrap');
    if (promptBox) promptBox.classList.remove('d-none');
    if (previewWrap) previewWrap.classList.add('d-none');
}}

// Drag & Drop event bindings
document.addEventListener('DOMContentLoaded', function(){{
    const dropzone = document.getElementById('productDropzone');
    if (dropzone) {{
        ['dragenter', 'dragover'].forEach(eventName => {{
            dropzone.addEventListener(eventName, (e) => {{
                e.preventDefault();
                e.stopPropagation();
                dropzone.style.background = '#dcfce7';
                dropzone.style.borderColor = '#15803d';
            }}, false);
        }});
        ['dragleave', 'drop'].forEach(eventName => {{
            dropzone.addEventListener(eventName, (e) => {{
                e.preventDefault();
                e.stopPropagation();
                dropzone.style.background = '#f0fdf4';
                dropzone.style.borderColor = '#16a34a';
            }}, false);
        }});
        dropzone.addEventListener('drop', (e) => {{
            const dt = e.dataTransfer;
            const files = dt.files;
            if (files && files[0]) {{
                const input = document.getElementById('productImageInput');
                input.files = files;
                previewProductImage({{ target: {{ files: files }} }});
            }}
        }}, false);
    }}
}});

function handleSaveProduct(e) {{
    if (e && e.preventDefault) e.preventDefault();
    
    const nameEn = document.getElementById('pNameEn').value.trim();
    const nameMr = document.getElementById('pNameMr').value.trim() || nameEn;
    const company = document.getElementById('pCompany').value.trim() || 'Saptashrungi Agro';
    const category = document.getElementById('pCategory').value;
    const price = parseFloat(document.getElementById('pPrice').value) || 0;
    const discountPrice = parseFloat(document.getElementById('pDiscount').value) || price;
    const stock = parseInt(document.getElementById('pStock').value) || 50;
    const desc = document.getElementById('pDesc').value.trim();
    const image = selectedProductImageDataUrl || 'images/cotton_seeds.jpg';

    const newProd = {{
        id: Date.now(),
        nameEn: nameEn,
        nameMr: nameMr,
        company: company,
        category: category,
        price: price,
        discountPrice: discountPrice,
        stock: stock,
        desc: desc,
        image: image,
        createdAt: new Date().toISOString()
    }};

    // Save to localStorage
    const saved = JSON.parse(localStorage.getItem('ksk_custom_products') || '[]');
    saved.unshift(newProd);
    localStorage.setItem('ksk_custom_products', JSON.stringify(saved));

    const alertBox = document.getElementById('saveAlert');
    if (alertBox) {{
        alertBox.classList.remove('d-none');
    }}

    setTimeout(() => {{
        window.location.href = 'admin-products.html';
    }}, 1200);

    return false;
}}
</script>
""" + foot_html()
    save_admin_page("admin-product-form.html", content)
    print("Generated dist/admin-product-form.html with Image Upload and Live Preview!")


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


# ==============================================================================
# 9. ADMIN REVIEWS MANAGEMENT (Manage & Delete Farmer Reviews)
# ==============================================================================
def build_admin_reviews():
    sidebar = render_admin_sidebar("reviews")
    content = head_html("शेतकरी रिव्ह्यू व्यवस्थापन", "Manage Farmer Reviews") + nav_html("dashboard") + f"""
<div class="container-fluid px-3 px-lg-4 my-4">
    <div class="row g-4">
        <!-- Sidebar -->
        <div class="col-lg-3 col-xl-2">
            {sidebar}
        </div>

        <div class="col-lg-9 col-xl-10">
            <!-- Header Banner -->
            <div class="card border-0 shadow-sm rounded-4 bg-white p-4 mb-4">
                <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-3">
                    <div>
                        <h4 class="fw-bold text-dark mb-1 d-flex align-items-center gap-2">
                            <i class="bi bi-star-fill text-warning"></i>
                            <span class="lang-mr">शेतकरी अभिप्राय व रेटिंग्ज व्यवस्थापन</span>
                            <span class="lang-en">Manage Farmer Reviews & Ratings</span>
                        </h4>
                        <p class="text-muted small mb-0">
                            <span class="lang-mr">शेतकऱ्यांनी दिलेले अभिप्राय तपासा, रेटिंग्स पाहा आणि अवांछित रिव्ह्यू हटवा (Delete Reviews).</span>
                            <span class="lang-en">Review customer feedback, monitor ratings, and delete inappropriate entries.</span>
                        </p>
                    </div>
                    <div class="d-flex gap-2">
                        <button class="btn btn-outline-success btn-sm rounded-pill px-3" onclick="resetDefaultReviews()">
                            <i class="bi bi-arrow-clockwise me-1"></i>
                            <span class="lang-mr">डिफॉल्ट रिव्ह्यू रीसेट करा</span>
                            <span class="lang-en">Reset Defaults</span>
                        </button>
                    </div>
                </div>
            </div>

            <!-- Stats Row -->
            <div class="row g-3 mb-4">
                <div class="col-sm-6 col-xl-3">
                    <div class="card border-0 shadow-sm rounded-4 p-3 bg-white border-start border-4 border-warning h-100">
                        <div class="d-flex justify-content-between align-items-center mb-1">
                            <small class="text-muted fw-bold text-uppercase" style="font-size:11px;">Average Rating</small>
                            <i class="bi bi-star-fill text-warning fs-5"></i>
                        </div>
                        <h3 class="fw-bold text-warning mb-0" id="adminAvgRating">4.9 / 5.0</h3>
                        <small class="text-muted" style="font-size:11px;">Overall Customer Score</small>
                    </div>
                </div>
                <div class="col-sm-6 col-xl-3">
                    <div class="card border-0 shadow-sm rounded-4 p-3 bg-white border-start border-4 border-success h-100">
                        <div class="d-flex justify-content-between align-items-center mb-1">
                            <small class="text-muted fw-bold text-uppercase" style="font-size:11px;">Total Reviews</small>
                            <i class="bi bi-chat-heart-fill text-success fs-5"></i>
                        </div>
                        <h3 class="fw-bold text-success mb-0" id="adminTotalReviews">5</h3>
                        <small class="text-muted" style="font-size:11px;">Active Published Reviews</small>
                    </div>
                </div>
                <div class="col-sm-6 col-xl-3">
                    <div class="card border-0 shadow-sm rounded-4 p-3 bg-white border-start border-4 border-primary h-100">
                        <div class="d-flex justify-content-between align-items-center mb-1">
                            <small class="text-muted fw-bold text-uppercase" style="font-size:11px;">5-Star Ratings</small>
                            <i class="bi bi-hand-thumbs-up-fill text-primary fs-5"></i>
                        </div>
                        <h3 class="fw-bold text-primary mb-0" id="adminFiveStarCount">96%</h3>
                        <small class="text-muted" style="font-size:11px;">Satisfied Farmers</small>
                    </div>
                </div>
                <div class="col-sm-6 col-xl-3">
                    <div class="card border-0 shadow-sm rounded-4 p-3 bg-white border-start border-4 border-info h-100">
                        <div class="d-flex justify-content-between align-items-center mb-1">
                            <small class="text-muted fw-bold text-uppercase" style="font-size:11px;">Verified Buyers</small>
                            <i class="bi bi-patch-check-fill text-info fs-5"></i>
                        </div>
                        <h3 class="fw-bold text-info mb-0">100%</h3>
                        <small class="text-muted" style="font-size:11px;">Registered Customers</small>
                    </div>
                </div>
            </div>

            <!-- Alert Box -->
            <div id="adminReviewAlert" class="alert alert-success d-none py-2 mb-3">
                <i class="bi bi-check-circle-fill me-2"></i>
                <span id="adminReviewAlertText">रिव्ह्यू यशस्वीरित्या हटवण्यात आला आहे.</span>
            </div>

            <!-- Reviews Table Card -->
            <div class="card border-0 shadow-sm rounded-4 bg-white overflow-hidden">
                <div class="card-header bg-white py-3 px-4 border-bottom d-flex justify-content-between align-items-center flex-wrap gap-2">
                    <h5 class="mb-0 fw-bold text-dark d-flex align-items-center gap-2">
                        <i class="bi bi-chat-quote-fill text-success"></i>
                        <span>Farmer Reviews List (<span id="tableReviewCount">5</span>)</span>
                    </h5>
                    <div class="d-flex gap-2">
                        <input type="text" id="reviewSearchInput" class="form-control form-control-sm rounded-pill px-3" placeholder="Search farmer or product..." oninput="filterReviewsTable()">
                    </div>
                </div>
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-hover align-middle mb-0">
                            <thead class="table-light text-muted small">
                                <tr>
                                    <th class="ps-4">#</th>
                                    <th>FARMER NAME & LOCATION</th>
                                    <th>RATING</th>
                                    <th>PRODUCT / CONTEXT</th>
                                    <th style="min-width:250px;">FEEDBACK COMMENT</th>
                                    <th>DATE</th>
                                    <th class="text-end pe-4">ACTION</th>
                                </tr>
                            </thead>
                            <tbody id="adminReviewsTableBody">
                                <!-- Populated dynamically -->
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
const DEFAULT_REVIEWS = [
    {{
        id: 1,
        name: "रामेश्वर पाटील",
        village: "वैजापूर, छत्रपती संभाजीनगर",
        product: "महाबीज गहू बियाणे (लोक-१)",
        rating: 5,
        date: "26 Oct 2026",
        comment: "सप्तशृंगी ॲग्रो कडून घेतलेले गहू बियाणे १००% उगवून आले. दर्जेदार बियाणे आणि रास्त भाव. दुकानदार योग्य सल्ला देतात.",
        verified: true
    }},
    {{
        id: 2,
        name: "सचिन गायकवाड",
        village: "कोपरगाव, अहिल्यानगर",
        product: "IFFCO NPK 19:19:19 खत",
        rating: 5,
        date: "20 Oct 2026",
        comment: "विद्राव्य खताचा रिझल्ट अतिशय चांगला आला. कांद्याची पात हिरवीगार झाली. वेळेवर माल मिळाला.",
        verified: true
    }},
    {{
        id: 3,
        name: "बाळासाहेब थोरात",
        village: "येवला, नाशिक",
        product: "ठिबक सिंचन फिल्टर व लॅटरल",
        rating: 5,
        date: "15 Oct 2026",
        comment: "ठिबकचे साहित्य योग्य किमतीत मिळाले. फिटिंगसाठी योग्य मार्गदर्शन केले. अतिशय प्रामाणिक सेवा.",
        verified: true
    }},
    {{
        id: 4,
        name: "ज्ञानेश्वर शिंदे",
        village: "धोंदलगाव, वैजापूर",
        product: "बॅटरी स्प्रेअर पंप (१६ लिटर)",
        rating: 4,
        date: "10 Oct 2026",
        comment: "बॅटरी पंप चांगला चालतो. एकदा चार्ज केल्यावर १५-२० टाक्या फवारणी होते. वॉरंटी पण दिली.",
        verified: true
    }},
    {{
        id: 5,
        name: "संजय कदम",
        village: "मिरखनगर, वैजापूर",
        product: "सेंद्रिय निंबोळी पेंड व खत",
        rating: 5,
        date: "04 Oct 2026",
        comment: "सेंद्रिय उत्पादने अस्सल आहेत. रासायनिक खतांचा खर्च कमी झाला. आमचे हक्काचे कृषी सेवा केंद्र!",
        verified: true
    }}
];

function getStoredReviews() {{
    const raw = localStorage.getItem('ksk_farmer_reviews');
    if (!raw) {{
        localStorage.setItem('ksk_farmer_reviews', JSON.stringify(DEFAULT_REVIEWS));
        return DEFAULT_REVIEWS;
    }}
    try {{
        return JSON.parse(raw);
    }} catch(e) {{
        return DEFAULT_REVIEWS;
    }}
}}

function renderAdminReviews() {{
    const reviews = getStoredReviews();
    const tbody = document.getElementById('adminReviewsTableBody');
    const countEl = document.getElementById('tableReviewCount');
    const totalEl = document.getElementById('adminTotalReviews');
    const avgEl = document.getElementById('adminAvgRating');

    if (countEl) countEl.textContent = reviews.length;
    if (totalEl) totalEl.textContent = reviews.length;

    if (reviews.length > 0 && avgEl) {{
        const sum = reviews.reduce((acc, r) => acc + (Number(r.rating) || 5), 0);
        avgEl.textContent = (sum / reviews.length).toFixed(1) + ' / 5.0';
    }}

    if (!tbody) return;

    if (reviews.length === 0) {{
        tbody.innerHTML = `
            <tr>
                <td colspan="7" class="text-center py-5 text-muted">
                    <i class="bi bi-chat-square-text fs-1 d-block mb-2 text-secondary opacity-50"></i>
                    <p class="mb-0 fw-bold">कोणतेही रिव्ह्यू उपलब्ध नाहीत / No reviews found</p>
                    <small>शेतकऱ्यांनी सबमिट केलेले रिव्ह्यू येथे दिसतील.</small>
                </td>
            </tr>
        `;
        return;
    }}

    tbody.innerHTML = reviews.map((r, idx) => {{
        let starsHtml = '';
        for (let i = 1; i <= 5; i++) {{
            if (i <= r.rating) {{
                starsHtml += '<i class="bi bi-star-fill text-warning"></i>';
            }} else {{
                starsHtml += '<i class="bi bi-star text-muted"></i>';
            }}
        }}

        return `
            <tr id="reviewRow_${{r.id}}">
                <td class="ps-4 fw-bold text-muted">${{idx + 1}}</td>
                <td>
                    <strong class="text-dark d-block">${{r.name}}</strong>
                    <small class="text-muted"><i class="bi bi-geo-alt me-1"></i>${{r.village || 'मिरखनगर'}}</small>
                </td>
                <td>
                    <div class="d-flex align-items-center gap-1">${{starsHtml}}</div>
                    <small class="fw-bold text-warning">${{r.rating}}.0</small>
                </td>
                <td>
                    <span class="badge bg-success-subtle text-success border border-success-subtle px-2 py-1">${{r.product || 'कृषी सेवा'}}</span>
                </td>
                <td>
                    <p class="small text-dark mb-0" style="max-width:320px; line-height:1.45;">"${{r.comment}}"</p>
                </td>
                <td class="small text-muted">${{r.date || 'Recent'}}</td>
                <td class="text-end pe-4">
                    <button type="button" class="btn btn-sm btn-outline-danger px-2 py-1 d-inline-flex align-items-center gap-1" onclick="deleteReview(${{r.id}}, '${{r.name.replace(/'/g, "\\\'")}}')" title="Delete this review">
                        <i class="bi bi-trash"></i>
                        <span>Delete</span>
                    </button>
                </td>
            </tr>
        `;
    }}).join('');
}}

function deleteReview(id, farmerName) {{
    if (!confirm('आपण ' + farmerName + ' यांचा रिव्ह्यू नक्की हटवू इच्छिता का?\n(Are you sure you want to delete this review?)')) {{
        return;
    }}

    let reviews = getStoredReviews();
    reviews = reviews.filter(r => r.id !== id);
    localStorage.setItem('ksk_farmer_reviews', JSON.stringify(reviews));

    const alertBox = document.getElementById('adminReviewAlert');
    const alertText = document.getElementById('adminReviewAlertText');
    if (alertBox && alertText) {{
        alertText.textContent = farmerName + ' यांचा रिव्ह्यू यशस्वीरित्या हटवण्यात आला आहे. (Review deleted successfully)';
        alertBox.classList.remove('d-none');
        setTimeout(() => {{ alertBox.classList.add('d-none'); }}, 3500);
    }}

    renderAdminReviews();
}}

function resetDefaultReviews() {{
    if (confirm('सर्व रिव्ह्यू मूळ डिफॉल्ट स्थितीत रीसेट करायचे का?')) {{
        localStorage.setItem('ksk_farmer_reviews', JSON.stringify(DEFAULT_REVIEWS));
        renderAdminReviews();
    }}
}}

function filterReviewsTable() {{
    const query = (document.getElementById('reviewSearchInput').value || '').toLowerCase().trim();
    const rows = document.querySelectorAll('#adminReviewsTableBody tr');
    rows.forEach(tr => {{
        const text = tr.innerText.toLowerCase();
        tr.style.display = text.includes(query) ? '' : 'none';
    }});
}}

document.addEventListener('DOMContentLoaded', function(){{
    renderAdminReviews();
}});
</script>
""" + foot_html()
    save_admin_page("admin-reviews.html", content)
    print("Generated dist/admin-reviews.html with Review Management & Delete!")


if __name__ == "__main__":
    build_login_page()
    build_admin_dashboard()
    build_admin_categories()
    build_admin_products()
    build_admin_product_form()
    build_admin_udhari()
    build_admin_inventory()
    build_admin_customers()
    build_admin_reviews()
    print("All Admin Panel and Login pages built successfully matching all screenshots!")
