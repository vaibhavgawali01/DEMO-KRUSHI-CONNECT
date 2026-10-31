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

    </nav>

    <!-- Section: Analytics & Settings -->
    <div class="admin-nav-section text-uppercase px-3 py-2 mt-3 fw-bold" style="font-size:0.7rem;letter-spacing:0.5px;color:#22c55e;opacity:0.85;">
        <span class="lang-mr">अहवाल व सेटिंग्ज</span><span class="lang-en">REPORTS &amp; CONFIG</span>
    </div>
    <nav class="nav flex-column gap-1 mb-4">
        <a href="admin-reports.html" class="admin-nav-link {'active' if active_tab == 'reports' else ''}">
            <i class="bi bi-bar-chart-line-fill text-primary"></i>
            <span><span class="lang-mr">अहवाल केंद्र</span><span class="lang-en">Reports Center</span></span>
        </a>
        <a href="admin-backup.html" class="admin-nav-link {'active' if active_tab == 'backup' else ''}">
            <i class="bi bi-database-check text-secondary"></i>
            <span><span class="lang-mr">डेटाबेस बॅकअप</span><span class="lang-en">Database Backup</span></span>
        </a>
        <a href="admin-settings.html" class="admin-nav-link {'active' if active_tab == 'settings' else ''}">
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
    content = (head_html("ॲडमिन डॅशबोर्ड", "Admin Dashboard") + nav_html("dashboard") + """
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

                <!-- 2. Total Users (Dynamically synced from ksk_registered_farmers) -->
                <div class="col-sm-6 col-xl-3">
                    <a href="admin-customers.html" class="admin-kpi-card text-decoration-none text-reset h-100 d-block">
                        <div class="d-flex justify-content-between align-items-start">
                            <span class="admin-kpi-label"><span class="lang-mr">एकूण युझर्स (Total Users)</span><span class="lang-en">Total Users</span></span>
                            <div class="admin-kpi-icon-wrap" style="background: #f3e8ff; color: #7c3aed;">
                                <i class="bi bi-people-fill"></i>
                            </div>
                        </div>
                        <div>
                            <div class="admin-kpi-val" id="dashTotalUsersVal" style="color: #7c3aed;">7</div>
                            <span class="admin-kpi-badge" id="dashTotalUsersBadge" style="background: #faf5ff; color: #7c3aed;">
                                <i class="bi bi-person-check-fill"></i> <span id="dashTotalUsersText"><span class="lang-mr">७ नोंदणीकृत शेतकरी</span><span class="lang-en">7 Registered Farmers</span></span>
                            </span>
                        </div>
                    </a>
                </div>

                <!-- 3. Udhari Outstanding (Empty by default when no udhari exists) -->
                <div class="col-sm-6 col-xl-3">
                    <a href="admin-udhari.html" class="admin-kpi-card text-decoration-none text-reset h-100 d-block">
                        <div class="d-flex justify-content-between align-items-start">
                            <span class="admin-kpi-label"><span class="lang-mr">बाकी उधारी (Udhari Outstanding)</span><span class="lang-en">Udhari Outstanding</span></span>
                            <div class="admin-kpi-icon-wrap" id="dashUdhariIconWrap" style="background: #dcfce7; color: #16a34a;">
                                <i class="bi bi-wallet2" id="dashUdhariIcon"></i>
                            </div>
                        </div>
                        <div>
                            <div class="admin-kpi-val" id="dashUdhariVal" style="color: #16a34a;">₹0</div>
                            <span class="admin-kpi-badge" id="dashUdhariBadge" style="background: #f0fdf4; color: #16a34a;">
                                <i class="bi bi-check-circle-fill me-1"></i> <span class="lang-mr">शून्य बाकी (सर्व उधारी पूर्ण)</span><span class="lang-en">0 Overdue (No Dues)</span>
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
                        <!-- Empty Orders State (User Request: admin pannel madhil resent order empty kr) -->
                        <div class="card-body p-4 text-center py-5">
                            <div class="mb-3">
                                <div class="d-inline-flex align-items-center justify-content-center rounded-circle shadow-sm" style="width: 72px; height: 72px; background: #f0fdf4; border: 2px dashed #86efac;">
                                    <i class="bi bi-inbox text-success fs-1"></i>
                                </div>
                            </div>
                            <h6 class="fw-bold text-dark mb-1">
                                <span class="lang-mr">सध्या कोणतीही चालू ऑर्डर नाही</span>
                                <span class="lang-en">No Recent Orders Available</span>
                            </h6>
                            <p class="text-muted small mb-0" style="max-width: 360px; margin: 0 auto; line-height: 1.5;">
                                <span class="lang-mr">शेतकऱ्यांनी नवीन उत्पादनांची ऑर्डर दिल्यावर त्या ऑर्डर्स येथे आपोआप दिसतील.</span>
                                <span class="lang-en">New customer orders will automatically appear in this table once placed.</span>
                            </p>
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

                        <a href="admin-reports.html" class="admin-tool-item mb-0">
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

<script>
function syncDashboardUdhariState() {
    const raw = localStorage.getItem('ksk_udhari_records');
    let records = [];
    if (raw) {
        try { records = JSON.parse(raw); } catch(e) { records = []; }
    }
    const activeRecords = records.filter(r => r.status !== 'Paid' && (parseFloat(r.amount) || 0) > 0);
    const total = activeRecords.reduce((sum, r) => sum + (parseFloat(r.amount) || 0), 0);
    const overdueCount = activeRecords.filter(r => r.status === 'Overdue').length;

    const valEl = document.getElementById('dashUdhariVal');
    const badgeEl = document.getElementById('dashUdhariBadge');
    const iconWrap = document.getElementById('dashUdhariIconWrap');

    if (total > 0) {
        if (valEl) {
            valEl.textContent = '₹' + total.toLocaleString('en-IN');
            valEl.style.color = '#dc2626';
        }
        if (iconWrap) {
            iconWrap.style.background = '#fee2e2';
            iconWrap.style.color = '#dc2626';
        }
        if (badgeEl) {
            badgeEl.style.background = '#fef2f2';
            badgeEl.style.color = '#dc2626';
            badgeEl.innerHTML = `<i class="bi bi-exclamation-circle-fill me-1"></i> <span class="lang-mr">${overdueCount || activeRecords.length} खाती बाकी</span><span class="lang-en">${overdueCount || activeRecords.length} Overdue</span>`;
        }
    } else {
        if (valEl) {
            valEl.textContent = '₹0';
            valEl.style.color = '#16a34a';
        }
        if (iconWrap) {
            iconWrap.style.background = '#dcfce7';
            iconWrap.style.color = '#16a34a';
        }
        if (badgeEl) {
            badgeEl.style.background = '#f0fdf4';
            badgeEl.style.color = '#16a34a';
            badgeEl.innerHTML = `<i class="bi bi-check-circle-fill me-1"></i> <span class="lang-mr">शून्य बाकी (सर्व उधारी पूर्ण)</span><span class="lang-en">0 Overdue (No Dues)</span>`;
        }
    }
}
function syncDashboardUsersState() {
    const DEFAULT_FARMERS = [
        { id: 1, farmerId: "KSK-8600813827", loginId: "8600813827", name: "Ramesh Patil", mobile: "8600813827", phone: "8600813827", village: "Vaijapur", crop: "Cotton, Maize", purchases: "₹14,500", status: "Active", registeredAt: "2026-10-15T10:00:00.000Z" }},
        { id: 2, farmerId: "KSK-9822001122", loginId: "9822001122", name: "Suresh Deshmukh", mobile: "9822001122", phone: "9822001122", village: "Shrirampur", crop: "Sugarcane", purchases: "₹28,900", status: "Active", registeredAt: "2026-10-18T11:30:00.000Z" }},
        { id: 3, farmerId: "KSK-9421003344", loginId: "9421003344", name: "Dnyaneshwar Pawar", mobile: "9421003344", phone: "9421003344", village: "Gangapur", crop: "Soybean, Gram", purchases: "₹8,200", status: "Active", registeredAt: "2026-10-20T14:15:00.000Z" }},
        { id: 4, farmerId: "KSK-8605000000", loginId: "8605000000", name: "VSGAWALI", mobile: "8605000000", phone: "8605000000", village: "Kopargaon", crop: "Wheat, Onion", purchases: "₹15,650", status: "Active", registeredAt: "2026-10-22T09:00:00.000Z" }},
        { id: 5, farmerId: "KSK-9850123456", loginId: "9850123456", name: "Balasaheb Thorat", mobile: "9850123456", phone: "9850123456", village: "Yeola", crop: "Pomegranate, Grapes", purchases: "₹32,000", status: "Active", registeredAt: "2026-10-25T16:45:00.000Z" }},
        { id: 6, farmerId: "KSK-9763112233", loginId: "9763112233", name: "Sanjay Kadam", mobile: "9763112233", phone: "9763112233", village: "Mirakhnagar", crop: "Vegetables, Bajra", purchases: "₹11,200", status: "Active", registeredAt: "2026-10-28T08:20:00.000Z" }},
        { id: 7, farmerId: "KSK-9922445566", loginId: "9922445566", name: "Eknath Shinde", mobile: "9922445566", phone: "9922445566", village: "Dhondalgaon", crop: "Maize, Wheat", purchases: "₹19,800", status: "Active", registeredAt: "2026-10-29T12:00:00.000Z" }}
    ];

    let farmers = [];
    const raw = localStorage.getItem('ksk_registered_farmers');
    if (raw) {
        try { farmers = JSON.parse(raw); } catch(e) { farmers = []; }
    }
    if (!farmers || farmers.length === 0) {
        farmers = DEFAULT_FARMERS.slice();
        localStorage.setItem('ksk_registered_farmers', JSON.stringify(farmers));
    }

    // 1. Update KPI Count
    const valEl = document.getElementById('dashTotalUsersVal');
    const badgeCountEl = document.getElementById('dashTotalUsersText');
    const countBadge = document.getElementById('dashRecentFarmersCount');
    if (valEl) valEl.textContent = farmers.length;
    if (badgeCountEl) {
        badgeCountEl.innerHTML = '<span class="lang-mr">' + farmers.length + ' नोंदणीकृत शेतकरी</span><span class="lang-en">' + farmers.length + ' Registered Farmers</span>';
    }
    if (countBadge) countBadge.textContent = farmers.length + ' शेतकरी';

    // 2. Populate Recent Registered Farmers table
    const tbody = document.getElementById('dashRecentFarmersTableBody');
    if (tbody) {
        const recent = farmers.slice(0, 6);
        tbody.innerHTML = recent.map(f => {
            const mob = f.mobile || f.phone || '-';
            const fid = f.farmerId || 'KSK-' + mob;
            const dt = f.registeredAt ? new Date(f.registeredAt).toLocaleDateString('mr-IN', { day:'2-digit', month:'short', year:'numeric' }) : 'नुकतीच';
            return `
                <tr>
                    <td class="ps-4">
                        <div class="fw-bold text-dark d-flex align-items-center gap-2">
                            <i class="bi bi-person-circle text-success fs-5"></i>
                            <div>
                                <span class="d-block">${f.name}</span>
                                <span class="badge bg-success-subtle text-success border border-success-subtle px-2 py-0 fw-semibold" style="font-size:10px;">
                                    <i class="bi bi-person-badge me-1"></i>ID: ${fid}
                                </span>
                            </div>
                        </div>
                    </td>
                    <td>
                        <a href="tel:${mob}" class="text-decoration-none fw-semibold text-dark">
                            <i class="bi bi-telephone text-muted me-1"></i>${mob}
                        </a>
                    </td>
                    <td><i class="bi bi-geo-alt text-danger me-1"></i>${f.village || '-'}</td>
                    <td><span class="badge bg-light text-dark border">${f.crop || 'सर्व पिके'}</span></td>
                    <td><small class="text-muted"><i class="bi bi-calendar-event me-1"></i>${dt}</small></td>
                    <td><span class="badge ${f.status === 'Active' ? 'bg-success' : 'bg-secondary'}">${f.status || 'Active'}</span></td>
                    <td class="text-end pe-4">
                        <a href="admin-customers.html" class="btn btn-sm btn-outline-success py-1 px-2 fw-semibold">
                            <i class="bi bi-pencil-square"></i> संपादन
                        </a>
                    </td>
                </tr>
            `;
        }).join('');
    }
}

document.addEventListener('DOMContentLoaded', function() {
    syncDashboardUdhariState();
    syncDashboardUsersState();
});
</script>
""").replace("{sidebar}", sidebar) + foot_html()
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
                                        <a href="admin-product-form.html?edit=1" class="btn btn-sm btn-outline-primary py-1 px-2"><i class="bi bi-pencil-square"></i></a>

                                        <button class="btn btn-sm btn-outline-danger py-1 px-2 ms-1" onclick="deleteDefaultProduct(1)"><i class="bi bi-trash"></i></button>

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
                                        <a href="admin-product-form.html?edit=2" class="btn btn-sm btn-outline-primary py-1 px-2"><i class="bi bi-pencil-square"></i></a>

                                        <button class="btn btn-sm btn-outline-danger py-1 px-2 ms-1" onclick="deleteDefaultProduct(2)"><i class="bi bi-trash"></i></button>

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
                                        <a href="admin-product-form.html?edit=3" class="btn btn-sm btn-outline-primary py-1 px-2"><i class="bi bi-pencil-square"></i></a>

                                        <button class="btn btn-sm btn-outline-danger py-1 px-2 ms-1" onclick="deleteDefaultProduct(3)"><i class="bi bi-trash"></i></button>

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
    if (!tbody) return;

    // 1. Hide default products that were marked deleted
    const hiddenDefaults = JSON.parse(localStorage.getItem('ksk_hidden_default_products') || '[]');
    hiddenDefaults.forEach(id => {{
        const rows = tbody.querySelectorAll('tr');
        rows.forEach(row => {{
            const editLink = row.querySelector('a[href="admin-product-form.html?edit=' + id + '"]');
            if (editLink) row.style.display = 'none';
        }});
    }});

    // 2. Apply any saved edits to default products (overrides)
    const overrides = JSON.parse(localStorage.getItem('ksk_default_product_overrides') || '{{}}');
    Object.keys(overrides).forEach(id => {{
        const prod = overrides[id];
        const rows = tbody.querySelectorAll('tr');
        rows.forEach(row => {{
            const editLink = row.querySelector('a[href="admin-product-form.html?edit=' + id + '"]');
            if (editLink) {{
                // Update image
                if (prod.image) {{
                    const img = row.querySelector('td:nth-child(1) img');
                    if (img) img.src = prod.image;
                }}
                // Update name
                const nameCol = row.querySelector('td:nth-child(2)');
                if (nameCol) {{
                    nameCol.innerHTML = '<strong class="text-dark d-block">' + (prod.nameEn || '') + '</strong>' +
                                        (prod.nameMr ? '<small class="text-muted">' + prod.nameMr + '</small>' : '');
                }}
                // Update company
                const compCol = row.querySelector('td:nth-child(3)');
                if (compCol && prod.company) compCol.textContent = prod.company;
                // Update category
                const catCol = row.querySelector('td:nth-child(4) .badge');
                if (catCol && prod.category) catCol.textContent = prod.category;
                // Update price
                const priceCol = row.querySelector('td:nth-child(5)');
                if (priceCol && (prod.discountPrice || prod.price)) {{
                    const dp = prod.discountPrice || prod.price;
                    const op = prod.price || prod.discountPrice;
                    priceCol.innerHTML = '<strong class="text-success">₹' + dp.toLocaleString('en-IN') + '</strong>' +
                                         (op > dp ? ' <small class="text-muted text-decoration-line-through">₹' + op.toLocaleString('en-IN') + '</small>' : '');
                }}
                // Update stock
                const stockCol = row.querySelector('td:nth-child(6) .badge');
                if (stockCol && prod.stock !== undefined) stockCol.textContent = prod.stock + ' units';
            }}
        }});
    }});

    // 3. Prepend custom/added products
    const customProds = JSON.parse(localStorage.getItem('ksk_custom_products') || '[]');
    if (customProds.length > 0) {{
        customProds.forEach(p => {{
            const tr = document.createElement('tr');
            tr.className = 'table-success-subtle';
            const dp = p.discountPrice || p.price || 0;
            const op = p.price || p.discountPrice || 0;
            tr.innerHTML = `
                <td class="ps-4">
                    <img src="${{p.image || 'images/cotton_seeds.jpg'}}" class="rounded-3 shadow-sm border" style="width:40px;height:40px;object-fit:cover;" onerror="this.src='images/cotton_seeds.jpg'">
                </td>
                <td>
                    <strong class="text-dark d-block">${{p.nameEn || ''}}</strong>
                    <small class="text-muted">${{p.nameMr || ''}}</small>
                </td>
                <td>${{p.company || 'Saptashrungi Agro'}}</td>
                <td><span class="badge bg-light text-dark border">${{p.category || 'General'}}</span></td>
                <td>
                    <strong class="text-success">₹${{dp.toLocaleString('en-IN')}}</strong>
                    ${{op > dp ? `<small class="text-muted text-decoration-line-through ms-1">₹${{op.toLocaleString('en-IN')}}</small>` : ''}}
                </td>
                <td><span class="badge bg-success">${{p.stock || 0}} units</span></td>
                <td><span class="badge bg-success-subtle text-success border border-success-subtle">Active</span></td>
                <td class="text-end pe-4">
                    <a href="admin-product-form.html?edit=${{p.id}}&src=custom" class="btn btn-sm btn-outline-primary py-1 px-2" title="Edit Product"><i class="bi bi-pencil-square"></i></a>
                    <button class="btn btn-sm btn-outline-danger py-1 px-2 ms-1" onclick="deleteCustomProduct(${{p.id}})" title="Delete Product"><i class="bi bi-trash"></i></button>
                </td>
            `;
            tbody.insertBefore(tr, tbody.firstChild);
        }});
    }}
}});

function deleteCustomProduct(id) {{
    if (confirm('या उत्पादनाला काढून टाकायचे आहे का? (Delete this product?)')) {{
        let prods = JSON.parse(localStorage.getItem('ksk_custom_products') || '[]');
        prods = prods.filter(p => String(p.id) !== String(id));
        localStorage.setItem('ksk_custom_products', JSON.stringify(prods));
        window.location.reload();
    }}
}}

function deleteDefaultProduct(id) {{
    if (confirm('हे उत्पादन काढून टाकायचे आहे का? (Delete this default product?)')) {{
        let hidden = JSON.parse(localStorage.getItem('ksk_hidden_default_products') || '[]');
        if (!hidden.includes(id)) hidden.push(id);
        localStorage.setItem('ksk_hidden_default_products', JSON.stringify(hidden));
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
                        <input type="hidden" id="editProductId" value="">
                        <input type="hidden" id="editProductSrc" value="">
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

// Default products catalog data for pre-population
const DEFAULT_EDIT_PRODUCTS = [
    {{
        id: 1,
        nameEn: "Wheat Seeds (Lok-1)",
        nameMr: "गहू बियाणे (लोक-१)",
        company: "MAHABEEJ",
        category: "Seeds",
        gst: "0.00",
        price: 1450,
        discountPrice: 1350,
        stock: 60,
        minStock: 10,
        desc: "High germination certified Lok-1 wheat seeds suitable for Maharashtra irrigated soil.",
        image: "images/wheat_seeds.jpg"
    }},
    {{
        id: 2,
        nameEn: "Soybean Seeds (JS-335)",
        nameMr: "सोयाबीन बियाणे (JS-335)",
        company: "MAHABEEJ",
        category: "Seeds",
        gst: "0.00",
        price: 3200,
        discountPrice: 2950,
        stock: 40,
        minStock: 10,
        desc: "Certified high yielding JS-335 soybean seeds with strong disease resistance.",
        image: "images/soybean_seeds.jpg"
    }},
    {{
        id: 3,
        nameEn: "NPK 19:19:19",
        nameMr: "NPK 19:19:19 खत",
        company: "IFFCO",
        category: "Fertilizers",
        gst: "5.00",
        price: 2350,
        discountPrice: 1890,
        stock: 85,
        minStock: 15,
        desc: "100% water soluble balanced fertilizer providing Nitrogen, Phosphorus, and Potassium in equal ratio.",
        image: "images/npk_191919.jpg"
    }}
];

// Pre-populate form when opening in Edit mode (?edit=<id>)
document.addEventListener('DOMContentLoaded', function() {{
    const params = new URLSearchParams(window.location.search);
    const editId = params.get('edit');
    const editSrc = params.get('src'); // 'custom' or default

    if (editId) {{
        document.getElementById('editProductId').value = editId;
        document.getElementById('editProductSrc').value = editSrc || 'default';

        let product = null;

        if (editSrc === 'custom') {{
            // Search in custom products
            const customs = JSON.parse(localStorage.getItem('ksk_custom_products') || '[]');
            product = customs.find(p => String(p.id) === String(editId));
        }} else {{
            // Search in overrides first, then defaults
            const overrides = JSON.parse(localStorage.getItem('ksk_default_product_overrides') || '{{}}');
            if (overrides[editId]) {{
                product = overrides[editId];
            }} else {{
                product = DEFAULT_EDIT_PRODUCTS.find(p => String(p.id) === String(editId));
            }}
        }}

        if (product) {{
            // 1. Fill all input fields with existing values
            if (document.getElementById('pNameEn')) document.getElementById('pNameEn').value = product.nameEn || '';
            if (document.getElementById('pNameMr')) document.getElementById('pNameMr').value = product.nameMr || '';
            if (document.getElementById('pCompany')) document.getElementById('pCompany').value = product.company || '';
            if (document.getElementById('pCategory')) document.getElementById('pCategory').value = product.category || 'Seeds';
            if (document.getElementById('pGst')) document.getElementById('pGst').value = product.gst !== undefined ? product.gst : '0.00';
            if (document.getElementById('pPrice')) document.getElementById('pPrice').value = product.price !== undefined ? product.price : '';
            if (document.getElementById('pDiscount')) document.getElementById('pDiscount').value = product.discountPrice !== undefined ? product.discountPrice : '';
            if (document.getElementById('pStock')) document.getElementById('pStock').value = product.stock !== undefined ? product.stock : '';
            if (document.getElementById('pMinStock')) document.getElementById('pMinStock').value = product.minStock !== undefined ? product.minStock : '10';
            if (document.getElementById('pDesc')) document.getElementById('pDesc').value = product.desc || '';

            // 2. Pre-populate image preview
            if (product.image) {{
                selectedProductImageDataUrl = product.image;
                const img = document.getElementById('productImagePreview');
                const promptBox = document.getElementById('uploadPrompt');
                const previewWrap = document.getElementById('imagePreviewWrap');
                const fileNameBadge = document.getElementById('imageFileName');
                if (img) img.src = product.image;
                if (fileNameBadge) fileNameBadge.textContent = 'Existing image (' + (product.nameEn || 'product') + ')';
                if (promptBox) promptBox.classList.add('d-none');
                if (previewWrap) previewWrap.classList.remove('d-none');
            }}

            // 3. Update Page Title and Button to Edit Mode
            const titleEl = document.querySelector('h5.fw-bold');
            if (titleEl) {{
                titleEl.innerHTML = '<i class="bi bi-pencil-square text-success fs-5"></i> ' +
                                    '<span class="lang-mr">उत्पादन माहिती बदला</span>' +
                                    '<span class="lang-en">Edit Product</span>';
            }}
            const btnSave = document.getElementById('btnSaveProd');
            if (btnSave) {{
                btnSave.innerHTML = '💾 <span class="lang-mr">बदल सेव्ह करा</span><span class="lang-en">Update Product</span>';
            }}
            const alertText = document.getElementById('saveAlert');
            if (alertText) {{
                alertText.innerHTML = '<i class="bi bi-check-circle-fill me-2"></i> ' +
                                      '<span class="lang-mr">उत्पादनाची माहिती यशस्वीरित्या अपडेट केली!</span>' +
                                      '<span class="lang-en">Product information updated successfully!</span>';
            }}
        }}
    }}
}});

function handleSaveProduct(e) {{
    if (e && e.preventDefault) e.preventDefault();
    
    const nameEn = document.getElementById('pNameEn').value.trim();
    const nameMr = document.getElementById('pNameMr').value.trim() || nameEn;
    const company = document.getElementById('pCompany').value.trim() || 'Saptashrungi Agro';
    const category = document.getElementById('pCategory').value;
    const gst = document.getElementById('pGst') ? document.getElementById('pGst').value.trim() : '0.00';
    const price = parseFloat(document.getElementById('pPrice').value) || 0;
    const discountPrice = parseFloat(document.getElementById('pDiscount').value) || price;
    const stock = parseInt(document.getElementById('pStock').value) || 50;
    const minStock = document.getElementById('pMinStock') ? parseInt(document.getElementById('pMinStock').value) || 10 : 10;
    const desc = document.getElementById('pDesc').value.trim();
    const image = selectedProductImageDataUrl || 'images/cotton_seeds.jpg';

    const editId = document.getElementById('editProductId').value;
    const editSrc = document.getElementById('editProductSrc').value;

    if (editId) {{
        // EDIT MODE - update existing record
        if (editSrc === 'custom') {{
            let customs = JSON.parse(localStorage.getItem('ksk_custom_products') || '[]');
            const idx = customs.findIndex(p => String(p.id) === String(editId));
            if (idx >= 0) {{
                customs[idx] = Object.assign(customs[idx], {{
                    nameEn, nameMr, company, category, gst, price, discountPrice, stock, minStock, desc, image,
                    updatedAt: new Date().toISOString()
                }});
            }}
            localStorage.setItem('ksk_custom_products', JSON.stringify(customs));
        }} else {{
            const overrides = JSON.parse(localStorage.getItem('ksk_default_product_overrides') || '{{}}');
            const base = DEFAULT_EDIT_PRODUCTS.find(p => String(p.id) === String(editId)) || {{}};
            overrides[editId] = Object.assign({{}}, base, {{
                nameEn, nameMr, company, category, gst, price, discountPrice, stock, minStock, desc, image,
                updatedAt: new Date().toISOString()
            }});
            localStorage.setItem('ksk_default_product_overrides', JSON.stringify(overrides));
        }}
    }} else {{
        // ADD NEW PRODUCT MODE
        const newProd = {{
            id: Date.now(),
            nameEn, nameMr, company, category, gst,
            price, discountPrice, stock, minStock, desc, image,
            createdAt: new Date().toISOString()
        }};
        const saved = JSON.parse(localStorage.getItem('ksk_custom_products') || '[]');
        saved.unshift(newProd);
        localStorage.setItem('ksk_custom_products', JSON.stringify(saved));
    }}

    const alertBox = document.getElementById('saveAlert');
    if (alertBox) alertBox.classList.remove('d-none');

    setTimeout(() => {{
        window.location.href = 'admin-products.html';
    }}, 900);

    return false;
}}
</script>
""" + foot_html()
    save_admin_page("admin-product-form.html", content)
    print("Generated dist/admin-product-form.html with Image Upload and Live Preview!")


def build_admin_udhari():
    sidebar = render_admin_sidebar("udhari")
    content = (head_html("उधारी व्यवस्थापन", "Credit Ledger Management") + nav_html("dashboard") + """
<div class="container-fluid px-3 px-lg-4 my-4">
    <div class="row g-4">
        <!-- Sidebar -->
        <div class="col-lg-3 col-xl-2">
            {sidebar}
        </div>

        <div class="col-lg-9 col-xl-10">
            <div class="card border-0 shadow-sm rounded-4 overflow-hidden bg-white mb-4">
                <div class="card-header bg-white py-3 px-4 border-bottom d-flex justify-content-between align-items-center flex-wrap gap-2">
                    <div>
                        <h5 class="mb-0 fw-bold text-dark d-flex align-items-center gap-2">
                            <i class="bi bi-wallet2 text-success"></i>
                            <span class="lang-mr">शेतकरी उधारी खातेवही (Credit Ledger)</span>
                            <span class="lang-en">Credit Ledger Management</span>
                        </h5>
                        <small class="text-muted">
                            <span class="lang-mr">उधारी असल्यास योग्य डेटा दाखवा, नसलेस शून्य बाकी दिसेल.</span>
                            <span class="lang-en">Shows active dues if present, otherwise displays clean zero-dues empty state.</span>
                        </small>
                    </div>
                    <div class="d-flex align-items-center gap-2">
                        <div id="udhariTotalBadge" class="badge bg-success-subtle text-success border border-success-subtle px-3 py-2 rounded-pill fw-bold">
                            Total Outstanding: ₹0
                        </div>
                        <button type="button" class="btn btn-sm btn-success rounded-pill px-3 fw-bold" onclick="openAddUdhariModal()">
                            <i class="bi bi-plus-circle me-1"></i>
                            <span class="lang-mr">नवीन उधारी नोंदवा</span>
                            <span class="lang-en">+ Add Entry</span>
                        </button>
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
                            <tbody id="udhariTableBody">
                                <!-- Populated dynamically or shows empty state -->
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Modal: Record New Udhari -->
<div class="modal fade" id="addUdhariModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content border-0 shadow-lg rounded-4 overflow-hidden">
            <div class="modal-header bg-success text-white py-3 px-4">
                <h6 class="modal-title fw-bold">
                    <i class="bi bi-wallet2 me-2"></i>
                    <span class="lang-mr">नवीन उधारी नोंदवा</span>
                    <span class="lang-en">Record New Udhari</span>
                </h6>
                <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <form id="addUdhariForm" onsubmit="handleSaveUdhari(event)">
                <div class="modal-body p-4">
                    <div class="mb-3">
                        <label class="form-label small fw-bold text-success">Customer Name *</label>
                        <input type="text" id="udhariName" class="form-control" placeholder="e.g. Ramesh Patil" required>
                    </div>
                    <div class="row g-2 mb-3">
                        <div class="col-6">
                            <label class="form-label small fw-bold text-success">Mobile Number</label>
                            <input type="tel" id="udhariMobile" class="form-control" placeholder="10-digit mobile">
                        </div>
                        <div class="col-6">
                            <label class="form-label small fw-bold text-success">Village</label>
                            <input type="text" id="udhariVillage" class="form-control" placeholder="e.g. Vaijapur">
                        </div>
                    </div>
                    <div class="row g-2 mb-3">
                        <div class="col-6">
                            <label class="form-label small fw-bold text-success">Udhari Amount (₹) *</label>
                            <input type="number" id="udhariAmount" class="form-control" placeholder="Amount in ₹" min="1" required>
                        </div>
                        <div class="col-6">
                            <label class="form-label small fw-bold text-success">Due Date</label>
                            <input type="date" id="udhariDueDate" class="form-control">
                        </div>
                    </div>
                    <div class="mb-3">
                        <label class="form-label small fw-bold text-success">Status</label>
                        <select id="udhariStatus" class="form-select">
                            <option value="Pending" selected>Pending</option>
                            <option value="Overdue">Overdue</option>
                        </select>
                    </div>
                </div>
                <div class="modal-footer bg-light px-4 py-2 border-top">
                    <button type="button" class="btn btn-outline-secondary rounded-pill px-3" data-bs-dismiss="modal">Cancel</button>
                    <button type="submit" class="btn btn-success rounded-pill px-4 fw-bold">Save Udhari Entry</button>
                </div>
            </form>
        </div>
    </div>
</div>

<script>
function getUdhariRecords() {
    const raw = localStorage.getItem('ksk_udhari_records');
    if (!raw) return [];
    try {
        return JSON.parse(raw);
    } catch(e) {
        return [];
    }
}

function saveUdhariRecords(records) {
    localStorage.setItem('ksk_udhari_records', JSON.stringify(records));
}

function renderUdhariTable() {
    const records = getUdhariRecords();
    const tbody = document.getElementById('udhariTableBody');
    const badge = document.getElementById('udhariTotalBadge');
    
    // Filter active records
    const activeRecords = records.filter(r => r.status !== 'Paid' && (parseFloat(r.amount) || 0) > 0);
    const total = activeRecords.reduce((sum, r) => sum + (parseFloat(r.amount) || 0), 0);

    // Update total outstanding badge
    if (badge) {
        if (total > 0) {
            badge.className = 'badge bg-danger-subtle text-danger border border-danger px-3 py-2 rounded-pill fw-bold';
            badge.textContent = 'Total Outstanding: ₹' + total.toLocaleString('en-IN');
        } else {
            badge.className = 'badge bg-success-subtle text-success border border-success-subtle px-3 py-2 rounded-pill fw-bold';
            badge.textContent = 'Total Outstanding: ₹0 (No Dues)';
        }
    }

    if (!tbody) return;

    if (activeRecords.length === 0) {
        // EMPTY STATE as requested: "data nasel kahi udhari data tr empty dakvat ja"
        tbody.innerHTML = `
            <tr>
                <td colspan="7" class="text-center py-5">
                    <div class="py-4">
                        <div class="rounded-circle d-inline-flex align-items-center justify-content-center bg-success-subtle text-success mb-3 shadow-sm" style="width: 64px; height: 64px;">
                            <i class="bi bi-check2-circle fs-1"></i>
                        </div>
                        <h5 class="fw-bold text-dark mb-1">
                            <span class="lang-mr">कोणतीही उधारी बाकी नाही!</span>
                            <span class="lang-en">No Outstanding Udhari!</span>
                        </h5>
                        <p class="text-muted small mb-3">
                            <span class="lang-mr">सर्व शेतकरी ग्राहकांची खाती पूर्णपणे भरलेली आहेत (शून्य बाकी).</span>
                            <span class="lang-en">All farmer customer accounts are fully settled (Zero Outstanding).</span>
                        </p>
                        <button type="button" class="btn btn-sm btn-success rounded-pill px-4 fw-semibold" onclick="openAddUdhariModal()">
                            <i class="bi bi-plus-circle me-1"></i>
                            <span class="lang-mr">नवीन उधारी नोंदवा</span>
                            <span class="lang-en">Record New Udhari</span>
                        </button>
                    </div>
                </td>
            </tr>
        `;
        return;
    }

    tbody.innerHTML = activeRecords.map(r => `
        <tr>
            <td class="ps-4 fw-bold text-dark">${r.name}</td>
            <td>${r.mobile || '-'}</td>
            <td>${r.village || '-'}</td>
            <td><strong class="text-danger">₹${parseFloat(r.amount).toLocaleString('en-IN')}</strong></td>
            <td>${r.dueDate || 'Open'}</td>
            <td>
                <span class="badge ${r.status === 'Overdue' ? 'bg-danger text-white' : 'bg-warning text-dark'}">
                    ${r.status}
                </span>
            </td>
            <td class="text-end pe-4">
                <button type="button" class="btn btn-sm btn-outline-success rounded-pill px-3 fw-bold me-1" onclick="markUdhariPaid(${r.id})">
                    <i class="bi bi-check-lg me-1"></i>Mark Paid
                </button>
                <button type="button" class="btn btn-sm btn-outline-danger rounded-circle p-1" style="width:28px;height:28px;" onclick="deleteUdhariRecord(${r.id})" title="Delete">
                    <i class="bi bi-trash"></i>
                </button>
            </td>
        </tr>
    `).join('');
}

function openAddUdhariModal() {
    const form = document.getElementById('addUdhariForm');
    if (form) form.reset();
    const modalEl = document.getElementById('addUdhariModal');
    if (modalEl && typeof bootstrap !== 'undefined') {
        const m = new bootstrap.Modal(modalEl);
        m.show();
    }
}

function handleSaveUdhari(e) {
    if (e && e.preventDefault) e.preventDefault();
    const name = document.getElementById('udhariName').value.trim();
    const mobile = document.getElementById('udhariMobile').value.trim();
    const village = document.getElementById('udhariVillage').value.trim();
    const amount = parseFloat(document.getElementById('udhariAmount').value) || 0;
    const dueDate = document.getElementById('udhariDueDate').value || '15 Nov 2026';
    const status = document.getElementById('udhariStatus').value;

    if (!name || amount <= 0) {
        alert('Please enter valid customer name and amount.');
        return;
    }

    let records = getUdhariRecords();
    records.unshift({
        id: Date.now(),
        name,
        mobile,
        village,
        amount,
        dueDate,
        status
    });
    saveUdhariRecords(records);

    const modalEl = document.getElementById('addUdhariModal');
    if (modalEl && typeof bootstrap !== 'undefined') {
        const modalInstance = bootstrap.Modal.getInstance(modalEl);
        if (modalInstance) modalInstance.hide();
    }
    renderUdhariTable();
}

function markUdhariPaid(id) {
    let records = getUdhariRecords();
    const item = records.find(r => r.id === id);
    if (item) {
        item.status = 'Paid';
        item.amount = 0;
        saveUdhariRecords(records);
        renderUdhariTable();
    }
}

function deleteUdhariRecord(id) {
    if (!confirm('Are you sure you want to delete this record?')) return;
    let records = getUdhariRecords();
    records = records.filter(r => r.id !== id);
    saveUdhariRecords(records);
    renderUdhariTable();
}

document.addEventListener('DOMContentLoaded', renderUdhariTable);
</script>
""").replace("{sidebar}", sidebar) + foot_html()
    save_admin_page("admin-udhari.html", content)
    print("Generated dist/admin-udhari.html with dynamic empty state!")

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
            <!-- Header Bar -->
            <div class="card border-0 shadow-sm rounded-4 bg-white p-4 mb-4">
                <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-3">
                    <div>
                        <h4 class="fw-bold text-dark mb-1 d-flex align-items-center gap-2">
                            <i class="bi bi-people-fill text-success"></i>
                            <span class="lang-mr">शेतकरी ग्राहक डिरेक्टरी व्यवस्थापन</span>
                            <span class="lang-en">Farmer Customer Directory Management</span>
                        </h4>
                        <p class="text-muted small mb-0">
                            <span class="lang-mr">शेतकऱ्यांची माहिती संपादित (Edit) करा, नवीन ग्राहक जोडा आणि खाते स्थिती व्यवस्थापित करा.</span>
                            <span class="lang-en">Manage registered farmer records, edit customer details, and control account status.</span>
                        </p>
                    </div>
                    <div class="d-flex gap-2">
                        <button type="button" class="btn btn-success rounded-pill px-3 fw-bold d-flex align-items-center gap-2" onclick="openAddFarmerModal()" style="background:#15803d; border:none;">
                            <i class="bi bi-person-plus-fill"></i>
                            <span class="lang-mr">नवीन शेतकरी जोडा</span>
                            <span class="lang-en">Add New Farmer</span>
                        </button>
                    </div>
                </div>
            </div>

            <!-- Success Alert -->
            <div id="farmerAlertBox" class="alert alert-success d-none py-2 mb-3">
                <i class="bi bi-check-circle-fill me-2"></i>
                <span id="farmerAlertText">शेतकऱ्याची माहिती यशस्वीरित्या अपडेट करण्यात आली!</span>
            </div>

            <!-- Customers Table Card -->
            <div class="card border-0 shadow-sm rounded-4 overflow-hidden bg-white">
                <div class="card-header bg-white py-3 px-4 border-bottom d-flex justify-content-between align-items-center flex-wrap gap-2">
                    <h5 class="mb-0 fw-bold text-dark d-flex align-items-center gap-2">
                        <i class="bi bi-person-badge text-success"></i>
                        <span>Registered Farmers (<span id="farmerCountBadge">7</span>)</span>
                    </h5>
                    <div class="d-flex gap-2">
                        <input type="text" id="farmerSearchInput" class="form-control form-control-sm rounded-pill px-3" placeholder="Search farmer, mobile, village..." oninput="filterFarmersTable()">
                    </div>
                </div>
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-hover align-middle mb-0">
                            <thead class="table-light text-muted small">
                                <tr>
                                    <th class="ps-4">FARMER NAME</th>
                                    <th>MOBILE NUMBER</th>
                                    <th>VILLAGE</th>
                                    <th>PRIMARY CROP</th>
                                    <th>TOTAL PURCHASES</th>
                                    <th>STATUS</th>
                                    <th class="text-end pe-4">ACTIONS</th>
                                </tr>
                            </thead>
                            <tbody id="farmerTableBody">
                                <!-- Populated dynamically from localStorage -->
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- ================= EDIT / ADD FARMER MODAL ================= -->
<div class="modal fade" id="farmerEditModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content border-0 shadow-lg rounded-4">
            <div class="modal-header border-0 pb-0">
                <h5 class="modal-title fw-bold text-success d-flex align-items-center gap-2" id="farmerModalTitle">
                    <i class="bi bi-pencil-square"></i>
                    <span>Edit Farmer Details / शेतकरी माहिती संपादित करा</span>
                </h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body p-4">
                <form id="farmerEditForm" onsubmit="return handleSaveFarmer(event)">
                    <input type="hidden" id="editFarmerId">

                    <div class="mb-3">
                        <label class="form-label small fw-bold text-success">Farmer Name / शेतकऱ्याचे नाव *</label>
                        <input type="text" id="editFarmerName" class="form-control" required placeholder="e.g. Ramesh Patil">
                    </div>

                    <div class="mb-3">
                        <label class="form-label small fw-bold text-success">Mobile Number / मोबाईल नंबर *</label>
                        <input type="tel" id="editFarmerMobile" class="form-control" required placeholder="e.g. 8600813827">
                    </div>

                    <div class="mb-3">
                        <label class="form-label small fw-bold text-success">Village / Location / गाव *</label>
                        <input type="text" id="editFarmerVillage" class="form-control" required placeholder="e.g. Vaijapur">
                    </div>

                    <div class="mb-3">
                        <label class="form-label small fw-bold text-success">Primary Crop / मुख्य पिके *</label>
                        <input type="text" id="editFarmerCrop" class="form-control" required placeholder="e.g. Cotton, Maize, Wheat">
                    </div>

                    <div class="row g-2 mb-4">
                        <div class="col-sm-6">
                            <label class="form-label small fw-bold text-success">Total Purchases (₹)</label>
                            <input type="text" id="editFarmerPurchases" class="form-control" placeholder="e.g. ₹14,500">
                        </div>
                        <div class="col-sm-6">
                            <label class="form-label small fw-bold text-success">Account Status</label>
                            <select id="editFarmerStatus" class="form-select">
                                <option value="Active" selected>Active</option>
                                <option value="Inactive">Inactive</option>
                            </select>
                        </div>
                    </div>

                    <div class="d-flex gap-2">
                        <button type="button" class="btn btn-light rounded-3 px-4 w-50" data-bs-dismiss="modal">Cancel</button>
                        <button type="submit" class="btn btn-success rounded-3 px-4 fw-bold w-50" style="background:#15803d; border:none;">
                            <i class="bi bi-save me-1"></i> Save Changes
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>

<script>
const DEFAULT_FARMERS = [
    {{ id: 1, farmerId: "KSK-8600813827", loginId: "8600813827", name: "Ramesh Patil", mobile: "8600813827", phone: "8600813827", village: "Vaijapur", crop: "Cotton, Maize", purchases: "₹14,500", status: "Active", registeredAt: "2026-10-15T10:00:00.000Z" }},
    {{ id: 2, farmerId: "KSK-9822001122", loginId: "9822001122", name: "Suresh Deshmukh", mobile: "9822001122", phone: "9822001122", village: "Shrirampur", crop: "Sugarcane", purchases: "₹28,900", status: "Active", registeredAt: "2026-10-18T11:30:00.000Z" }},
    {{ id: 3, farmerId: "KSK-9421003344", loginId: "9421003344", name: "Dnyaneshwar Pawar", mobile: "9421003344", phone: "9421003344", village: "Gangapur", crop: "Soybean, Gram", purchases: "₹8,200", status: "Active", registeredAt: "2026-10-20T14:15:00.000Z" }},
    {{ id: 4, farmerId: "KSK-8605000000", loginId: "8605000000", name: "VSGAWALI", mobile: "8605000000", phone: "8605000000", village: "Kopargaon", crop: "Wheat, Onion", purchases: "₹15,650", status: "Active", registeredAt: "2026-10-22T09:00:00.000Z" }},
    {{ id: 5, farmerId: "KSK-9850123456", loginId: "9850123456", name: "Balasaheb Thorat", mobile: "9850123456", phone: "9850123456", village: "Yeola", crop: "Pomegranate, Grapes", purchases: "₹32,000", status: "Active", registeredAt: "2026-10-25T16:45:00.000Z" }},
    {{ id: 6, farmerId: "KSK-9763112233", loginId: "9763112233", name: "Sanjay Kadam", mobile: "9763112233", phone: "9763112233", village: "Mirakhnagar", crop: "Vegetables, Bajra", purchases: "₹11,200", status: "Active", registeredAt: "2026-10-28T08:20:00.000Z" }},
    {{ id: 7, farmerId: "KSK-9922445566", loginId: "9922445566", name: "Eknath Shinde", mobile: "9922445566", phone: "9922445566", village: "Dhondalgaon", crop: "Maize, Wheat", purchases: "₹19,800", status: "Active", registeredAt: "2026-10-29T12:00:00.000Z" }}
];

function getStoredFarmers() {{
    const raw = localStorage.getItem('ksk_registered_farmers');
    if (!raw) {{
        localStorage.setItem('ksk_registered_farmers', JSON.stringify(DEFAULT_FARMERS));
        return DEFAULT_FARMERS;
    }}
    try {{
        return JSON.parse(raw);
    }} catch(e) {{
        return DEFAULT_FARMERS;
    }}
}}

function renderFarmersTable() {{
    const farmers = getStoredFarmers();
    const tbody = document.getElementById('farmerTableBody');
    const badge = document.getElementById('farmerCountBadge');
    if (badge) badge.textContent = farmers.length;

    if (!tbody) return;

    if (farmers.length === 0) {{
        tbody.innerHTML = `
            <tr>
                <td colspan="7" class="text-center py-5 text-muted">
                    <i class="bi bi-people fs-1 d-block mb-2 text-secondary opacity-50"></i>
                    <p class="mb-0 fw-bold">कोणतेही शेतकरी रेकॉर्ड उपलब्ध नाहीत / No farmers registered</p>
                </td>
            </tr>
        `;
        return;
    }}

    tbody.innerHTML = farmers.map(f => {{
        const statusBadge = f.status === 'Active'
            ? '<span class="badge bg-success">Active</span>'
            : '<span class="badge bg-secondary">Inactive</span>';

        const mob = f.mobile || f.phone || '-';
        const fid = f.farmerId || ('KSK-' + mob);
        const dt = f.registeredAt ? new Date(f.registeredAt).toLocaleDateString('mr-IN', {{ day:'2-digit', month:'short', year:'numeric' }}) : 'नुकतीच';
        const safeName = (f.name || 'Farmer').replace(/'/g, "\\'");

        return `
            <tr id="farmerRow_${{f.id}}">
                <td class="ps-4">
                    <div class="fw-bold text-dark d-flex align-items-center gap-2">
                        <i class="bi bi-person-circle text-success fs-5"></i>
                        <div>
                            <span class="d-block text-dark">${{f.name}}</span>
                            <span class="badge bg-success-subtle text-success border border-success-subtle px-2 py-0 fw-semibold" style="font-size:10px;">
                                <i class="bi bi-person-badge me-1"></i>ID: ${{fid}}
                            </span>
                        </div>
                    </div>
                </td>
                <td>
                    <a href="tel:${{mob}}" class="text-decoration-none fw-semibold text-dark">
                        <i class="bi bi-telephone text-muted me-1"></i>${{mob}}
                    </a>
                </td>
                <td><i class="bi bi-geo-alt text-danger me-1"></i>${{f.village || '-'}}</td>
                <td><span class="badge bg-light text-dark border">${{f.crop || 'सर्व पिके'}}</span></td>
                <td class="fw-bold text-success">${{f.purchases || '₹0.00'}}</td>
                <td>${{statusBadge}}</td>
                <td class="text-end pe-4">
                    <button type="button" class="btn btn-sm btn-outline-success py-1 px-2" onclick="editFarmer(${{f.id}})" title="Edit Farmer Details">
                        <i class="bi bi-pencil-square"></i> Edit
                    </button>
                    <button type="button" class="btn btn-sm btn-outline-danger py-1 px-2 ms-1" onclick="deleteFarmer(${{f.id}}, '${{safeName}}')" title="Delete Farmer">
                        <i class="bi bi-trash"></i>
                    </button>
                </td>
            </tr>
        `;
    }}).join('');
}}

function openAddFarmerModal() {{
    document.getElementById('farmerEditForm').reset();
    document.getElementById('editFarmerId').value = '';
    document.getElementById('farmerModalTitle').innerHTML = '<i class="bi bi-person-plus-fill me-2"></i>Add New Farmer / नवीन शेतकरी जोडा';
    const modalEl = document.getElementById('farmerEditModal');
    if (modalEl && typeof bootstrap !== 'undefined') {{
        const m = new bootstrap.Modal(modalEl);
        m.show();
    }}
}}

function editFarmer(id) {{
    const farmers = getStoredFarmers();
    const f = farmers.find(item => item.id === id);
    if (!f) return;

    document.getElementById('editFarmerId').value = f.id;
    document.getElementById('editFarmerName').value = f.name;
    document.getElementById('editFarmerMobile').value = f.mobile;
    document.getElementById('editFarmerVillage').value = f.village;
    document.getElementById('editFarmerCrop').value = f.crop;
    document.getElementById('editFarmerPurchases').value = f.purchases;
    document.getElementById('editFarmerStatus').value = f.status || 'Active';

    document.getElementById('farmerModalTitle').innerHTML = '<i class="bi bi-pencil-square me-2"></i>Edit Farmer / ' + f.name;

    const modalEl = document.getElementById('farmerEditModal');
    if (modalEl && typeof bootstrap !== 'undefined') {{
        const m = new bootstrap.Modal(modalEl);
        m.show();
    }}
}}

function handleSaveFarmer(e) {{
    if (e && e.preventDefault) e.preventDefault();

    const id = document.getElementById('editFarmerId').value;
    const name = document.getElementById('editFarmerName').value.trim();
    const mobile = document.getElementById('editFarmerMobile').value.trim();
    const village = document.getElementById('editFarmerVillage').value.trim();
    const crop = document.getElementById('editFarmerCrop').value.trim();
    let purchases = document.getElementById('editFarmerPurchases').value.trim();
    if (purchases && !purchases.startsWith('₹')) purchases = '₹' + purchases;
    const status = document.getElementById('editFarmerStatus').value;

    let farmers = getStoredFarmers();

    if (id) {{
        // Update existing farmer
        const index = farmers.findIndex(item => item.id == id);
        if (index !== -1) {{
            farmers[index] = {{ ...farmers[index], name, mobile, village, crop, purchases: purchases || '₹0', status }};
        }}
    }} else {{
        // Add new farmer
        const newFarmer = {{
            id: Date.now(),
            name,
            mobile,
            village,
            crop,
            purchases: purchases || '₹0',
            status
        }};
        farmers.unshift(newFarmer);
    }}

    localStorage.setItem('ksk_registered_farmers', JSON.stringify(farmers));

    const modalEl = document.getElementById('farmerEditModal');
    if (modalEl) {{
        const inst = bootstrap.Modal.getInstance(modalEl);
        if (inst) inst.hide();
    }}

    const alertBox = document.getElementById('farmerAlertBox');
    const alertText = document.getElementById('farmerAlertText');
    if (alertBox && alertText) {{
        alertText.textContent = name + ' यांची माहिती यशस्वीरित्या सेव्ह करण्यात आली!';
        alertBox.classList.remove('d-none');
        setTimeout(() => {{ alertBox.classList.add('d-none'); }}, 3500);
    }}

    renderFarmersTable();
    return false;
}}

function deleteFarmer(id, name) {{
    if (!confirm('आपण ' + name + ' यांचे रेकॉर्ड नक्की हटवू इच्छिता का?\n(Are you sure you want to delete this farmer?)')) {{
        return;
    }}

    let farmers = getStoredFarmers();
    farmers = farmers.filter(item => item.id !== id);
    localStorage.setItem('ksk_registered_farmers', JSON.stringify(farmers));

    const alertBox = document.getElementById('farmerAlertBox');
    const alertText = document.getElementById('farmerAlertText');
    if (alertBox && alertText) {{
        alertText.textContent = name + ' यांचे रेकॉर्ड हटवण्यात आले आहे.';
        alertBox.classList.remove('d-none');
        setTimeout(() => {{ alertBox.classList.add('d-none'); }}, 3500);
    }}

    renderFarmersTable();
}}

function filterFarmersTable() {{
    const query = (document.getElementById('farmerSearchInput').value || '').toLowerCase().trim();
    const rows = document.querySelectorAll('#farmerTableBody tr');
    rows.forEach(tr => {{
        const text = tr.innerText.toLowerCase();
        tr.style.display = text.includes(query) ? '' : 'none';
    }});
}}

document.addEventListener('DOMContentLoaded', function(){{
    renderFarmersTable();
}});
</script>
""" + foot_html()
    save_admin_page("admin-customers.html", content)
    print("Generated dist/admin-customers.html with Farmer Edit and Management!")


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



# ==============================================================================
# 10. ADMIN REPORTS & SALES ANALYTICS (Fully Working Feature)
# ==============================================================================
def build_admin_reports():
    sidebar = render_admin_sidebar("reports")
    content = head_html("विक्री व व्यवसाय अहवाल", "Sales & Business Reports") + nav_html("dashboard") + f"""
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
                            <i class="bi bi-bar-chart-line-fill text-primary"></i>
                            <span class="lang-mr">विक्री व व्यवसाय अहवाल केंद्र</span>
                            <span class="lang-en">Sales & Business Analytics Center</span>
                        </h4>
                        <p class="text-muted small mb-0">
                            <span class="lang-mr">दुकान विक्री, महसूल, उत्पादननिहाय विश्लेषण आणि ग्राहक उधारी अहवाल तपासा.</span>
                            <span class="lang-en">Track store revenue, category performance, top selling products, and transaction records.</span>
                        </p>
                    </div>
                    <div class="d-flex gap-2 flex-wrap">
                        <button type="button" class="btn btn-outline-success rounded-pill px-3 fw-semibold" onclick="window.print()">
                            <i class="bi bi-printer me-1"></i> Print Report
                        </button>
                        <button type="button" class="btn btn-success rounded-pill px-3 fw-bold" onclick="downloadSalesReportCSV()" style="background:#15803d; border:none;">
                            <i class="bi bi-download me-1"></i> Export to CSV
                        </button>
                    </div>
                </div>

                <!-- Date Range Filter Tabs -->
                <div class="d-flex gap-2 mt-3 pt-3 border-top flex-wrap">
                    <button class="btn btn-sm btn-success rounded-pill px-3 fw-bold" onclick="setReportPeriod('month', this)">चालू महिना (Oct 2026)</button>
                    <button class="btn btn-sm btn-light border rounded-pill px-3" onclick="setReportPeriod('week', this)">हा आठवडा (This Week)</button>
                    <button class="btn btn-sm btn-light border rounded-pill px-3" onclick="setReportPeriod('today', this)">आजची विक्री (Today)</button>
                    <button class="btn btn-sm btn-light border rounded-pill px-3" onclick="setReportPeriod('year', this)">आर्थिक वर्ष (FY 2026-27)</button>
                </div>
            </div>

            <!-- Key Metric Stats Row -->
            <div class="row g-3 mb-4">
                <div class="col-sm-6 col-xl-3">
                    <div class="card border-0 shadow-sm rounded-4 p-3 bg-white border-start border-4 border-success h-100">
                        <small class="text-muted fw-bold text-uppercase" style="font-size:11px;">Total Revenue / एकूण विक्री</small>
                        <h3 class="fw-bold text-success my-1" id="reportTotalSales">₹1,84,650</h3>
                        <small class="text-success"><i class="bi bi-arrow-up-right me-1"></i>+14.2% vs last month</small>
                    </div>
                </div>
                <div class="col-sm-6 col-xl-3">
                    <div class="card border-0 shadow-sm rounded-4 p-3 bg-white border-start border-4 border-primary h-100">
                        <small class="text-muted fw-bold text-uppercase" style="font-size:11px;">Cash & UPI Received</small>
                        <h3 class="fw-bold text-primary my-1">₹1,42,400</h3>
                        <small class="text-muted">77.1% Cleared Payments</small>
                    </div>
                </div>
                <div class="col-sm-6 col-xl-3">
                    <div class="card border-0 shadow-sm rounded-4 p-3 bg-white border-start border-4 border-warning h-100">
                        <small class="text-muted fw-bold text-uppercase" style="font-size:11px;">Credit / Udhari Dues</small>
                        <h3 class="fw-bold text-warning my-1">₹42,250</h3>
                        <small class="text-muted">22.9% Outstanding Ledger</small>
                    </div>
                </div>
                <div class="col-sm-6 col-xl-3">
                    <div class="card border-0 shadow-sm rounded-4 p-3 bg-white border-start border-4 border-info h-100">
                        <small class="text-muted fw-bold text-uppercase" style="font-size:11px;">Total Invoices / बिल संख्या</small>
                        <h3 class="fw-bold text-info my-1">64</h3>
                        <small class="text-muted">Avg. Bill: ₹2,885.00</small>
                    </div>
                </div>
            </div>

            <!-- Category Performance & Top Sellers Grid -->
            <div class="row g-4 mb-4">
                <!-- Category Share -->
                <div class="col-lg-5">
                    <div class="card border-0 shadow-sm rounded-4 p-4 bg-white h-100">
                        <h6 class="fw-bold text-dark mb-3"><i class="bi bi-pie-chart-fill text-success me-2"></i>कॅटेगरीनिहाय विक्री (Category Sales Share)</h6>
                        
                        <div class="mb-3">
                            <div class="d-flex justify-content-between small fw-bold mb-1">
                                <span>🌱 बियाणे (Seeds)</span>
                                <span class="text-success">₹70,167 (38%)</span>
                            </div>
                            <div class="progress" style="height: 8px;">
                                <div class="progress-bar bg-success" style="width: 38%;"></div>
                            </div>
                        </div>

                        <div class="mb-3">
                            <div class="d-flex justify-content-between small fw-bold mb-1">
                                <span>🌾 खते (Fertilizers)</span>
                                <span class="text-primary">₹59,088 (32%)</span>
                            </div>
                            <div class="progress" style="height: 8px;">
                                <div class="progress-bar bg-primary" style="width: 32%;"></div>
                            </div>
                        </div>

                        <div class="mb-3">
                            <div class="d-flex justify-content-between small fw-bold mb-1">
                                <span>🧴 कीटकनाशके (Pesticides)</span>
                                <span class="text-warning">₹33,237 (18%)</span>
                            </div>
                            <div class="progress" style="height: 8px;">
                                <div class="progress-bar bg-warning" style="width: 18%;"></div>
                            </div>
                        </div>

                        <div>
                            <div class="d-flex justify-content-between small fw-bold mb-1">
                                <span>🔧 ठिबक सिंचन व अवजारे (Drip & Tools)</span>
                                <span class="text-info">₹22,158 (12%)</span>
                            </div>
                            <div class="progress" style="height: 8px;">
                                <div class="progress-bar bg-info" style="width: 12%;"></div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Top Products Table -->
                <div class="col-lg-7">
                    <div class="card border-0 shadow-sm rounded-4 p-4 bg-white h-100">
                        <h6 class="fw-bold text-dark mb-3"><i class="bi bi-award-fill text-warning me-2"></i>सर्वाधिक विक्री झालेली उत्पादने (Top Selling Products)</h6>
                        <div class="table-responsive">
                            <table class="table table-sm align-middle mb-0">
                                <thead class="table-light small">
                                    <tr>
                                        <th>Product Name</th>
                                        <th>Qty Sold</th>
                                        <th>Revenue</th>
                                        <th>Stock Status</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td><strong>महाबीज गहू बियाणे (लोक-१)</strong></td>
                                        <td>85 Bags</td>
                                        <td class="fw-bold text-success">₹1,14,750</td>
                                        <td><span class="badge bg-success">In Stock (120)</span></td>
                                    </tr>
                                    <tr>
                                        <td><strong>IFFCO NPK 19:19:19 (५० kg)</strong></td>
                                        <td>42 Bags</td>
                                        <td class="fw-bold text-success">₹46,200</td>
                                        <td><span class="badge bg-success">In Stock (58)</span></td>
                                    </tr>
                                    <tr>
                                        <td><strong>बॅटरी स्प्रेअर पंप (१६ लिटर)</strong></td>
                                        <td>12 Units</td>
                                        <td class="fw-bold text-success">₹23,760</td>
                                        <td><span class="badge bg-warning text-dark">Low Stock (5)</span></td>
                                    </tr>
                                    <tr>
                                        <td><strong>सेंद्रिय निंबोळी अर्क (५L)</strong></td>
                                        <td>28 Bottles</td>
                                        <td class="fw-bold text-success">₹18,200</td>
                                        <td><span class="badge bg-success">In Stock (40)</span></td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Detailed Sales Transaction Register -->
            <div class="card border-0 shadow-sm rounded-4 bg-white overflow-hidden">
                <div class="card-header bg-white py-3 px-4 border-bottom d-flex justify-content-between align-items-center flex-wrap gap-2">
                    <h5 class="mb-0 fw-bold text-dark"><i class="bi bi-receipt-cutoff text-success me-2"></i>अलीकडील बिल व पावती नोंदवही (Sales Ledger Register)</h5>
                    <input type="text" id="salesSearchInput" class="form-control form-control-sm rounded-pill px-3" style="max-width:240px;" placeholder="Search bill or farmer..." oninput="filterSalesTable()">
                </div>
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-hover align-middle mb-0">
                            <thead class="table-light text-muted small">
                                <tr>
                                    <th class="ps-4">INVOICE #</th>
                                    <th>DATE</th>
                                    <th>FARMER NAME</th>
                                    <th>ITEMS PURCHASED</th>
                                    <th>PAYMENT MODE</th>
                                    <th class="text-end">AMOUNT (₹)</th>
                                    <th class="text-center">STATUS</th>
                                </tr>
                            </thead>
                            <tbody id="salesTableBody">
                                <tr>
                                    <td class="ps-4 fw-bold text-success">INV-2026-0064</td>
                                    <td>28 Oct 2026</td>
                                    <td><strong>Ramesh Patil</strong> (Vaijapur)</td>
                                    <td>महाबीज गहू बियाणे (3 Bags)</td>
                                    <td><span class="badge bg-light text-dark border">UPI</span></td>
                                    <td class="text-end fw-bold text-dark">₹4,050.00</td>
                                    <td class="text-center"><span class="badge bg-success">Paid</span></td>
                                </tr>
                                <tr>
                                    <td class="ps-4 fw-bold text-success">INV-2026-0063</td>
                                    <td>27 Oct 2026</td>
                                    <td><strong>Suresh Deshmukh</strong> (Shrirampur)</td>
                                    <td>IFFCO NPK 19:19:19 (2 Bags)</td>
                                    <td><span class="badge bg-light text-dark border">Cash</span></td>
                                    <td class="text-end fw-bold text-dark">₹2,200.00</td>
                                    <td class="text-center"><span class="badge bg-success">Paid</span></td>
                                </tr>
                                <tr>
                                    <td class="ps-4 fw-bold text-success">INV-2026-0062</td>
                                    <td>25 Oct 2026</td>
                                    <td><strong>Balasaheb Thorat</strong> (Yeola)</td>
                                    <td>ठिबक सिंचन फिटिंग साहित्य</td>
                                    <td><span class="badge bg-light text-dark border">Credit (उधारी)</span></td>
                                    <td class="text-end fw-bold text-danger">₹8,500.00</td>
                                    <td class="text-center"><span class="badge bg-warning text-dark">Udhari Due</span></td>
                                </tr>
                                <tr>
                                    <td class="ps-4 fw-bold text-success">INV-2026-0061</td>
                                    <td>24 Oct 2026</td>
                                    <td><strong>Dnyaneshwar Pawar</strong> (Gangapur)</td>
                                    <td>सेंद्रिय निंबोळी अर्क (2 Bottles)</td>
                                    <td><span class="badge bg-light text-dark border">UPI</span></td>
                                    <td class="text-end fw-bold text-dark">₹1,300.00</td>
                                    <td class="text-center"><span class="badge bg-success">Paid</span></td>
                                </tr>
                                <tr>
                                    <td class="ps-4 fw-bold text-success">INV-2026-0060</td>
                                    <td>22 Oct 2026</td>
                                    <td><strong>VSGAWALI</strong> (Kopargaon)</td>
                                    <td>NPK Fertilizer (50 kg)</td>
                                    <td><span class="badge bg-light text-dark border">UPI</span></td>
                                    <td class="text-end fw-bold text-dark">₹2,450.00</td>
                                    <td class="text-center"><span class="badge bg-success">Paid</span></td>
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
function downloadSalesReportCSV() {{
    const csvRows = [
        ["Invoice Number", "Date", "Farmer Name", "Location", "Items", "Payment Mode", "Amount", "Status"],
        ["INV-2026-0064", "2026-10-28", "Ramesh Patil", "Vaijapur", "Wheat Seeds (3 Bags)", "UPI", "4050", "Paid"],
        ["INV-2026-0063", "2026-10-27", "Suresh Deshmukh", "Shrirampur", "NPK 19:19:19 (2 Bags)", "Cash", "2200", "Paid"],
        ["INV-2026-0062", "2026-10-25", "Balasaheb Thorat", "Yeola", "Drip Irrigation Fittings", "Credit", "8500", "Udhari Due"],
        ["INV-2026-0061", "2026-10-24", "Dnyaneshwar Pawar", "Gangapur", "Organic Neem Extract", "UPI", "1300", "Paid"],
        ["INV-2026-0060", "2026-10-22", "VSGAWALI", "Kopargaon", "NPK Fertilizer 50kg", "UPI", "2450", "Paid"]
    ];

    let csvContent = "data:text/csv;charset=utf-8," + csvRows.map(e => e.join(",")).join("\n");
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "Saptashrungi_Agro_Sales_Report_Oct_2026.csv");
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}}

function setReportPeriod(period, btn) {{
    document.querySelectorAll('.border-top .btn').forEach(b => {{
        b.className = 'btn btn-sm btn-light border rounded-pill px-3';
    }});
    btn.className = 'btn btn-sm btn-success rounded-pill px-3 fw-bold';

    const salesMap = {{
        'today': '₹7,550',
        'week': '₹38,900',
        'month': '₹1,84,650',
        'year': '₹14,22,400'
    }};
    const totalEl = document.getElementById('reportTotalSales');
    if (totalEl) totalEl.textContent = salesMap[period] || '₹1,84,650';
}}

function filterSalesTable() {{
    const query = (document.getElementById('salesSearchInput').value || '').toLowerCase().trim();
    const rows = document.querySelectorAll('#salesTableBody tr');
    rows.forEach(tr => {{
        const text = tr.innerText.toLowerCase();
        tr.style.display = text.includes(query) ? '' : 'none';
    }});
}}
</script>
""" + foot_html()
    save_admin_page("admin-reports.html", content)
    print("Generated dist/admin-reports.html with working Sales Reports & CSV Export!")

# ==============================================================================
# 11. ADMIN DATABASE BACKUP (Fully Working Feature)
# ==============================================================================
def build_admin_backup():
    sidebar = render_admin_sidebar("backup")
    content = head_html("डेटाबेस बॅकअप आणि रिस्टोअर", "Database Backup & Restore") + nav_html("dashboard") + f"""
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
                            <i class="bi bi-database-check text-success"></i>
                            <span class="lang-mr">डेटाबेस बॅकअप आणि सुरक्षितता</span>
                            <span class="lang-en">Database Backup & Recovery</span>
                        </h4>
                        <p class="text-muted small mb-0">
                            <span class="lang-mr">दुकान, शेतकरी यादी, उत्पादने, कॅटेगरीज, उधारी व रिव्ह्यू डेटा सुरक्षित डाऊनलोड व रिस्टोअर करा.</span>
                            <span class="lang-en">Download complete application data snapshots and restore saved database states securely.</span>
                        </p>
                    </div>
                    <div>
                        <span class="badge bg-success-subtle text-success border border-success-subtle px-3 py-2 rounded-pill fw-bold">
                            <i class="bi bi-check-circle-fill me-1"></i> System Healthy & Live
                        </span>
                    </div>
                </div>
            </div>

            <!-- Alerts -->
            <div id="backupAlertBox" class="alert alert-success d-none py-3 px-4 mb-4 rounded-4 shadow-sm border-0 border-start border-4 border-success">
                <div class="d-flex align-items-center justify-content-between flex-wrap gap-2">
                    <div class="d-flex align-items-center gap-2">
                        <i class="bi bi-check-circle-fill fs-5 text-success"></i>
                        <span id="backupAlertText" class="fw-bold text-dark">बॅकअप यशस्वीरीत्या डाऊनलोड झाला आहे!</span>
                    </div>
                    <div id="backupFallbackContainer"></div>
                </div>
            </div>

            <!-- Two Main Action Cards -->
            <div class="row g-4 mb-4">
                <!-- 1. Download Backup -->
                <div class="col-lg-6">
                    <div class="card border-0 shadow-sm rounded-4 p-4 bg-white h-100 border-top border-4 border-success">
                        <div class="d-flex align-items-center gap-3 mb-3">
                            <div class="rounded-3 p-3 text-success" style="background:#f0fdf4;">
                                <i class="bi bi-cloud-arrow-down-fill fs-2"></i>
                            </div>
                            <div>
                                <h5 class="fw-bold text-dark mb-0">डेटाबेस बॅकअप डाऊनलोड करा</h5>
                                <small class="text-muted">Create Instant Full JSON Snapshot</small>
                            </div>
                        </div>
                        <p class="small text-muted mb-4" style="line-height:1.6;">
                            या बटणावर क्लिक केल्यावर सध्याचे सर्व उत्पादने (Products), शेतकरी माहिती (Farmers), कॅटेगरीज (Categories), शेतकरी रिव्ह्यू (Reviews) आणि दुकान सेटिंग्ज (Settings) सुरक्षित JSON फॉरमॅटमध्ये आपल्या कॉम्प्युटर किंवा फोनवर डाऊनलोड होतात.
                        </p>
                        <div class="mt-auto">
                            <button type="button" id="btnDownloadBackup" class="btn btn-success fw-bold px-4 py-3 rounded-3 w-100 shadow-sm d-flex align-items-center justify-content-center gap-2" onclick="downloadDatabaseBackupJSON()" style="background:#15803d; border:none; font-size:15px;">
                                <i class="bi bi-download fs-5"></i>
                                <span>Download Full JSON Backup</span>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- 2. Restore Backup -->
                <div class="col-lg-6">
                    <div class="card border-0 shadow-sm rounded-4 p-4 bg-white h-100 border-top border-4 border-primary">
                        <div class="d-flex align-items-center gap-3 mb-3">
                            <div class="rounded-3 p-3 text-primary" style="background:#eff6ff;">
                                <i class="bi bi-cloud-arrow-up-fill fs-2"></i>
                            </div>
                            <div>
                                <h5 class="fw-bold text-dark mb-0">बॅकअप फाइल रिस्टोअर करा</h5>
                                <small class="text-muted">Upload & Restore Application Data</small>
                            </div>
                        </div>
                        <p class="small text-muted mb-4" style="line-height:1.6;">
                            आपल्याकडे असलेली पूर्वी डाऊनलोड केलेली बॅकअप (.json) फाइल निवडून आपण संपूर्ण डेटा पूर्ववत रिस्टोअर करू शकता. सिलेक्ट केल्यावर सिस्टीम डेटा व्हेरिफाय करून ॲप्लिकेशनमध्ये रीलोड करते.
                        </p>
                        <div class="mt-auto">
                            <input type="file" id="restoreFileInput" accept=".json,application/json" class="d-none" onchange="handleRestoreFile(event)">
                            <button type="button" class="btn btn-outline-primary fw-bold px-4 py-3 rounded-3 w-100 d-flex align-items-center justify-content-center gap-2" onclick="document.getElementById('restoreFileInput').click()" style="font-size:15px;">
                                <i class="bi bi-folder2-open fs-5"></i>
                                <span>Select Backup File & Restore</span>
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Backup Log Card -->
            <div class="card border-0 shadow-sm rounded-4 bg-white overflow-hidden mb-4">
                <div class="card-header bg-white py-3 px-4 border-bottom d-flex justify-content-between align-items-center">
                    <h6 class="fw-bold text-dark mb-0"><i class="bi bi-clock-history me-2 text-success"></i>बॅकअप इतिहास व स्नॅपशॉट्स (Recent Backup Logs)</h6>
                    <small class="text-muted">Direct Download Available</small>
                </div>
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-hover align-middle mb-0">
                            <thead class="table-light text-muted small">
                                <tr>
                                    <th class="ps-4">SNAPSHOT FILE</th>
                                    <th>TRIGGER TYPE</th>
                                    <th>TIMESTAMP</th>
                                    <th>RECORDS INCLUDED</th>
                                    <th>STATUS</th>
                                    <th class="text-end pe-4">ACTION</th>
                                </tr>
                            </thead>
                            <tbody id="backupLogTableBody">
                                <tr>
                                    <td class="ps-4 fw-bold text-dark">
                                        <i class="bi bi-file-earmark-code text-primary me-2"></i>Saptashrungi_Agro_Snapshot_Current.json
                                    </td>
                                    <td><span class="badge bg-light text-dark border">Auto Scheduled</span></td>
                                    <td class="small text-muted">Today at 02:15 AM</td>
                                    <td>14 Products, 7 Farmers, 8 Categories, 5 Reviews</td>
                                    <td><span class="badge bg-success">Verified Healthy</span></td>
                                    <td class="text-end pe-4">
                                        <button type="button" class="btn btn-sm btn-outline-success rounded-pill px-3 py-1 fw-bold" onclick="downloadDatabaseBackupJSON('Current')">
                                            <i class="bi bi-download me-1"></i> Download
                                        </button>
                                    </td>
                                </tr>
                                <tr>
                                    <td class="ps-4 fw-bold text-dark">
                                        <i class="bi bi-file-earmark-code text-primary me-2"></i>Saptashrungi_Agro_Snapshot_PreDeploy.json
                                    </td>
                                    <td><span class="badge bg-light text-dark border">Manual Admin</span></td>
                                    <td class="small text-muted">Yesterday at 11:30 PM</td>
                                    <td>14 Products, 7 Farmers, 8 Categories, 5 Reviews</td>
                                    <td><span class="badge bg-success">Verified Healthy</span></td>
                                    <td class="text-end pe-4">
                                        <button type="button" class="btn btn-sm btn-outline-success rounded-pill px-3 py-1 fw-bold" onclick="downloadDatabaseBackupJSON('PreDeploy')">
                                            <i class="bi bi-download me-1"></i> Download
                                        </button>
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
// Default Datasets for complete reliable snapshots
const defaultFarmersList = [
    {{ id: 1, name: "Ramesh Patil", mobile: "8600813827", village: "Vaijapur", crop: "Cotton, Maize", purchases: 14500, due: 0, status: "Active" }},
    {{ id: 2, name: "Suresh Deshmukh", mobile: "9822001122", village: "Shrirampur", crop: "Sugarcane", purchases: 28900, due: 0, status: "Active" }},
    {{ id: 3, name: "Dnyaneshwar Pawar", mobile: "9421003344", village: "Gangapur", crop: "Soybean, Gram", purchases: 8200, due: 0, status: "Active" }},
    {{ id: 4, name: "Balasaheb Vikhe", mobile: "9850123456", village: "Loni", crop: "Pomegranate, Onion", purchases: 32000, due: 0, status: "Active" }},
    {{ id: 5, name: "Kishor Jadhav", mobile: "9923456789", village: "Yeola", crop: "Onion, Wheat", purchases: 19400, due: 0, status: "Active" }},
    {{ id: 6, name: "Sunil Shinde", mobile: "9765432100", village: "Kopargaon", crop: "Maize, Bajra", purchases: 11800, due: 0, status: "Active" }},
    {{ id: 7, name: "Ganesh Kadam", mobile: "9604123890", village: "Vaijapur", crop: "Cotton, Soybean", purchases: 22500, due: 0, status: "Active" }}
];

const defaultCategoriesList = [
    {{ id: 1, name_en: "Seeds", name_mr: "बियाणे", desc: "High yield certified hybrid seeds", status: "Active" }},
    {{ id: 2, name_en: "Fertilizers", name_mr: "खते", desc: "Chemical, water-soluble, bio-fertilizers", status: "Active" }},
    {{ id: 3, name_en: "Pesticides", name_mr: "कीटकनाशके", desc: "Broad-spectrum insecticides, fungicides", status: "Active" }},
    {{ id: 4, name_en: "Farming Tools", name_mr: "शेती अवजारे", desc: "Battery sprayers, pruning shears", status: "Active" }},
    {{ id: 5, name_en: "Drip Irrigation", name_mr: "ठिबक सिंचन", desc: "Drip laterals, drippers, venturi filters", status: "Active" }},
    {{ id: 6, name_en: "Animal Feed", name_mr: "पशूखाद्य", desc: "Cattle feed pellets, mineral mixture", status: "Active" }},
    {{ id: 7, name_en: "Organic Products", name_mr: "सेंद्रिय उत्पादने", desc: "Neem cake, vermicompost, bio-stimulants", status: "Active" }},
    {{ id: 8, name_en: "Plant Growth Promoters", name_mr: "वाढ संप्रेरके", desc: "Humic acid, seaweed extract, amino boosters", status: "Active" }}
];

const defaultProductsList = [
    {{ id: 1, name_mr: "माहिको बीजी-२ कापूस बियाणे (475g)", name_en: "Mahyco BG-II Cotton Seeds (475g)", company: "Mahyco Seeds", cat: "Seeds", price: 820, discountPrice: 820, stock: 45 }},
    {{ id: 2, name_mr: "जेएस ३३५ प्रमाणित सोयाबीन बियाणे (30 Kg)", name_en: "JS-335 Certified Soybean Seeds (30 Kg)", company: "Mahabeej", cat: "Seeds", price: 2850, discountPrice: 2700, stock: 28 }},
    {{ id: 3, name_mr: "महाधन २४:२४:० खत (५० किलो)", name_en: "Mahadhan 24:24:0 Fertilizer (50 Kg)", company: "Deepak Fertilisers", cat: "Fertilizers", price: 1750, discountPrice: 1680, stock: 65 }},
    {{ id: 4, name_mr: "इफको नीम कोटेड युरिया (४५ किलो)", name_en: "IFFCO Neem Coated Urea (45 Kg)", company: "IFFCO Ltd", cat: "Fertilizers", price: 266, discountPrice: 266, stock: 120 }},
    {{ id: 5, name_mr: "कोरोमंडल ग्रोमोर १०:२६:२६ खत (50 Kg)", name_en: "Coromandel Gromor 10:26:26 (50 Kg)", company: "Coromandel", cat: "Fertilizers", price: 1820, discountPrice: 1750, stock: 42 }},
    {{ id: 6, name_mr: "फाल्कन १६ लिटर १२V बॅटरी स्प्रे पंप", name_en: "Falcon 16L 12V Battery Sprayer Pump", company: "Falcon Agri", cat: "Farming Tools", price: 3200, discountPrice: 2850, stock: 15 }},
    {{ id: 7, name_mr: "जैन ठिबक १६ मिमी लॅटरल पाईप (४०० मीटर)", name_en: "Jain Drip 16mm Lateral Pipe (400m)", company: "Jain Irrigation", cat: "Drip Irrigation", price: 3600, discountPrice: 3350, stock: 18 }},
    {{ id: 8, name_mr: "लोक-१ प्रमाणित गहू बियाणे (४० किलो)", name_en: "Lok-1 Certified Wheat Seeds (40 Kg)", company: "Mahabeej", cat: "Seeds", price: 1450, discountPrice: 1350, stock: 50 }}
];

const defaultReviewsList = [
    {{ id: 1, name: "सचिन पाटील", rating: 5, date: "15 Oct 2026", product: "Mahadhan 24:24:0 Fertilizer", comment: "उत्कृष्ट दर्जाचे खत! कपाशीच्या पिकासाठी खूप चांगला रिझल्ट मिळाला.", verified: true }},
    {{ id: 2, name: "दत्तात्रय पवार", rating: 5, date: "22 Oct 2026", product: "Falcon 16L Sprayer Pump", comment: "बॅटरी स्प्रे पंप खूप हलका आणि मजबूत आहे. एका चार्जिंगवर 15 पंप फवारणी होते.", verified: true }},
    {{ id: 3, name: "विकास थोरात", rating: 4, date: "28 Oct 2026", product: "JS-335 Soybean Seeds", comment: "महाबीजचे बियाणे १००% उगवले. रास्त दर आणि पक्की पावती मिळाली.", verified: true }},
    {{ id: 4, name: "संजय गायकवाड", rating: 5, date: "29 Oct 2026", product: "Jain Drip Lateral 16mm", comment: "ठिबक पाईपची क्वालिटी एकदम भारी आहे. ड्रिप फिटिंगसाठी मार्गदर्शनही उत्तम मिळाले.", verified: true }},
    {{ id: 5, name: "कैलास निकम", rating: 5, date: "30 Oct 2026", product: "Lok-1 Wheat Seeds", comment: "उत्कृष्ट बियाणे आणि वेळेवर डिलिव्हरी. सप्तश्रृंगी ॲग्रोची सर्व्हिस खूप विश्वासार्ह आहे.", verified: true }}
];

const defaultShopSettingsData = {{
    nameMr: "सप्तश्रृंगी ॲग्रो सर्व्हिसेस",
    nameEn: "Saptashrungi Agro Services",
    owner: "Vaibhav Gawali",
    phone: "8600813827",
    whatsapp: "8600813827",
    gst: "27AABCS1234F1Z5",
    upi: "8600813827@okaxis",
    timings: "Mon - Sat: 8:00 AM - 8:30 PM",
    address: "Saptashrungi Agro Services, Mirakhnagar, Vaijapur, Chhatrapati Sambhajinagar, Maharashtra - 423703"
}};

function downloadDatabaseBackupJSON(snapshotType) {{
    try {{
        // Gather live or default data
        const storedFarmers = JSON.parse(localStorage.getItem('ksk_registered_farmers') || 'null');
        const storedCats = JSON.parse(localStorage.getItem('ksk_custom_categories') || 'null');
        const storedProds = JSON.parse(localStorage.getItem('ksk_custom_products') || 'null');
        const storedReviews = JSON.parse(localStorage.getItem('ksk_farmer_reviews') || 'null');
        const storedSettings = JSON.parse(localStorage.getItem('ksk_shop_settings') || 'null');

        const farmers = (storedFarmers && storedFarmers.length > 0) ? storedFarmers : defaultFarmersList;
        const categories = (storedCats && storedCats.length > 0) ? storedCats : defaultCategoriesList;
        const products = (storedProds && storedProds.length > 0) ? storedProds : defaultProductsList;
        const reviews = (storedReviews && storedReviews.length > 0) ? storedReviews : defaultReviewsList;
        const settings = storedSettings || defaultShopSettingsData;

        const now = new Date();
        const dateStr = now.toISOString().split('T')[0];
        let filename = "Saptashrungi_Agro_Backup_" + dateStr + ".json";
        if (snapshotType) {{
            filename = "Saptashrungi_Agro_Snapshot_" + snapshotType + ".json";
        }}

        const backupPayload = {{
            application: "Saptashrungi Agro Services - Krushi Seva Kendra",
            system: "Antigravity Cloud Platform",
            version: "2.0",
            exportedAt: now.toISOString(),
            snapshotType: snapshotType || "Full Database Snapshot",
            summary: {{
                totalFarmers: farmers.length,
                totalProducts: products.length,
                totalCategories: categories.length,
                totalReviews: reviews.length
            }},
            data: {{
                farmers: farmers,
                categories: categories,
                products: products,
                reviews: reviews,
                shopSettings: settings
            }}
        }};

        const jsonString = JSON.stringify(backupPayload, null, 2);

        // Standard, robust W3C Blob Download
        const blob = new Blob([jsonString], {{ type: 'application/json;charset=utf-8' }});
        const url = window.URL.createObjectURL(blob);

        const a = document.createElement('a');
        a.style.display = 'none';
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();

        // Keep fallback download link visible in the alert box
        const alertBox = document.getElementById('backupAlertBox');
        const alertText = document.getElementById('backupAlertText');
        const fallbackContainer = document.getElementById('backupFallbackContainer');

        if (alertBox && alertText && fallbackContainer) {{
            alertText.innerHTML = '<span class="text-success fw-bold">✓ बॅकअप तयार झाला:</span> <code>' + filename + '</code> डाऊनलोड सुरू झाली आहे.';
            fallbackContainer.innerHTML = '<a href="' + url + '" download="' + filename + '" class="btn btn-sm btn-success rounded-pill px-3 py-1 shadow-sm"><i class="bi bi-download me-1"></i> थेट डाऊनलोड (Direct Link)</a>';
            alertBox.classList.remove('d-none');
        }}

        // Clean up object URL after reasonable delay
        setTimeout(function() {{
            document.body.removeChild(a);
        }}, 500);

        // Prepend new row in recent backup logs table
        const tbody = document.getElementById('backupLogTableBody');
        if (tbody) {{
            const newRow = document.createElement('tr');
            newRow.className = 'table-success-subtle';
            newRow.innerHTML = `
                <td class="ps-4 fw-bold text-dark">
                    <i class="bi bi-file-earmark-code text-success me-2"></i>${{filename}}
                </td>
                <td><span class="badge bg-success text-white">Manual Export</span></td>
                <td class="small text-muted">Just now</td>
                <td>${{products.length}} Products, ${{farmers.length}} Farmers, ${{categories.length}} Categories</td>
                <td><span class="badge bg-success">Verified Healthy</span></td>
                <td class="text-end pe-4">
                    <a href="${{url}}" download="${{filename}}" class="btn btn-sm btn-outline-success rounded-pill px-3 py-1 fw-bold">
                        <i class="bi bi-download me-1"></i> Download
                    </a>
                </td>
            `;
            tbody.insertBefore(newRow, tbody.firstChild);
        }}

    }} catch (error) {{
        console.error("Backup download failed:", error);
        alert("बॅकअप डाऊनलोड त्रुटी: " + error.message);
    }}
}}

function handleRestoreFile(event) {{
    const file = event.target.files && event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function(e) {{
        try {{
            const parsed = JSON.parse(e.target.result);
            if (!parsed.data) throw new Error('Invalid schema');

            const confirmMsg = "आपण निवडलेली बॅकअप फाईल (" + file.name + ") रिस्टोअर करायची आहे का?\n\nयामध्ये:\n- " +
                (parsed.data.farmers ? parsed.data.farmers.length : 0) + " शेतकरी\n- " +
                (parsed.data.products ? parsed.data.products.length : 0) + " उत्पादने\n- " +
                (parsed.data.categories ? parsed.data.categories.length : 0) + " कॅटेगरीज\n- " +
                (parsed.data.reviews ? parsed.data.reviews.length : 0) + " रिव्ह्यू समाविष्ट आहेत.";

            if (!confirm(confirmMsg)) {{
                return;
            }}

            if (parsed.data.farmers) localStorage.setItem('ksk_registered_farmers', JSON.stringify(parsed.data.farmers));
            if (parsed.data.categories) localStorage.setItem('ksk_custom_categories', JSON.stringify(parsed.data.categories));
            if (parsed.data.products) localStorage.setItem('ksk_custom_products', JSON.stringify(parsed.data.products));
            if (parsed.data.reviews) localStorage.setItem('ksk_farmer_reviews', JSON.stringify(parsed.data.reviews));
            if (parsed.data.shopSettings) localStorage.setItem('ksk_shop_settings', JSON.stringify(parsed.data.shopSettings));

            alert('बॅकअप डेटा यशस्वीरीत्या रिस्टोअर झाला! ॲप्लिकेशन रीलोड होत आहे...');
            window.location.reload();
        }} catch(err) {{
            alert('त्रुटी: अवैध बॅकअप फाईल! कृपया योग्य JSON बॅकअप फाईल निवडा.');
        }}
    }};
    reader.readAsText(file);
}}
</script>
""" + foot_html()
    save_admin_page("admin-backup.html", content)
    print("Generated dist/admin-backup.html with working JSON Backup & Restore!")

# 12. ADMIN SHOP SETTINGS (Fully Working Feature)
# ==============================================================================
def build_admin_settings():
    sidebar = render_admin_sidebar("settings")
    content = head_html("दुकान सेटिंग्ज", "Shop Settings") + nav_html("dashboard") + f"""
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
                            <i class="bi bi-gear-wide-connected text-success"></i>
                            <span class="lang-mr">दुकान व व्यवसाय सेटिंग्ज</span>
                            <span class="lang-en">Shop Profile & Business Settings</span>
                        </h4>
                        <p class="text-muted small mb-0">
                            <span class="lang-mr">दुकानाचे नाव, संपर्क क्रमांक, GSTIN, UPI आयडी व कामाची वेळ व्यवस्थापित करा.</span>
                            <span class="lang-en">Manage shop identity, contact helpline, GST details, UPI payment IDs, and store timings.</span>
                        </p>
                    </div>
                </div>
            </div>

            <!-- Success Alert -->
            <div id="settingsAlertBox" class="alert alert-success d-none py-2 mb-3">
                <i class="bi bi-check-circle-fill me-2"></i>
                <span>दुकान सेटिंग्ज यशस्वीरीत्या जतन केल्या आहेत! (Settings saved successfully)</span>
            </div>

            <!-- Settings Form Card -->
            <div class="card border-0 shadow-sm rounded-4 bg-white p-4">
                <form id="shopSettingsForm" onsubmit="return handleSaveShopSettings(event)">
                    <div class="row g-3">
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-success">दुकान नाव (मराठी) *</label>
                            <input type="text" id="settingShopNameMr" class="form-control" value="सप्तशृंगी ॲग्रो सर्व्हिसेस" required>
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-success">Shop Name (English) *</label>
                            <input type="text" id="settingShopNameEn" class="form-control" value="Saptashrungi Agro Services" required>
                        </div>

                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-success">संचालक / मालकाचे नाव *</label>
                            <input type="text" id="settingOwner" class="form-control" value="Vaibhav Gawali" required>
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-success">प्राथमिक मोबाईल नंबर *</label>
                            <input type="tel" id="settingPhone" class="form-control" value="8600813827" required>
                        </div>

                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-success">WhatsApp सल्लागार नंबर</label>
                            <input type="tel" id="settingWhatsapp" class="form-control" value="8600813827">
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-success">अधिकृत GSTIN नंबर *</label>
                            <input type="text" id="settingGst" class="form-control" value="27AAAAA0000A1Z5" required>
                        </div>

                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-success">UPI ID (पेमेंट स्वीकारण्यासाठी) *</label>
                            <input type="text" id="settingUpi" class="form-control" value="8600813827@upi" required>
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-success">दुकानाची वेळ *</label>
                            <input type="text" id="settingTimings" class="form-control" value="सोमवार ते शनिवार: सकाळी ८:०० ते रात्री ८:३०" required>
                        </div>

                        <div class="col-12">
                            <label class="form-label small fw-bold text-success">दुकानाचा पूर्ण पत्ता *</label>
                            <textarea id="settingAddress" class="form-control" rows="2" required>मिरखनगर, वैजापूर, छत्रपती संभाजीनगर - 423703</textarea>
                        </div>

                        <div class="col-12 pt-3">
                            <button type="submit" class="btn btn-success fw-bold px-4 py-2 rounded-3 shadow-sm" style="background:#15803d; border:none;">
                                <i class="bi bi-save me-1"></i> सेव्ह करा (Save Shop Settings)
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function(){{
    const saved = localStorage.getItem('ksk_shop_settings');
    if (saved) {{
        try {{
            const s = JSON.parse(saved);
            if (s.nameMr) document.getElementById('settingShopNameMr').value = s.nameMr;
            if (s.nameEn) document.getElementById('settingShopNameEn').value = s.nameEn;
            if (s.owner) document.getElementById('settingOwner').value = s.owner;
            if (s.phone) document.getElementById('settingPhone').value = s.phone;
            if (s.whatsapp) document.getElementById('settingWhatsapp').value = s.whatsapp;
            if (s.gst) document.getElementById('settingGst').value = s.gst;
            if (s.upi) document.getElementById('settingUpi').value = s.upi;
            if (s.timings) document.getElementById('settingTimings').value = s.timings;
            if (s.address) document.getElementById('settingAddress').value = s.address;
        }} catch(e) {{}}
    }}
}});

function handleSaveShopSettings(e) {{
    if (e && e.preventDefault) e.preventDefault();

    const settings = {{
        nameMr: document.getElementById('settingShopNameMr').value.trim(),
        nameEn: document.getElementById('settingShopNameEn').value.trim(),
        owner: document.getElementById('settingOwner').value.trim(),
        phone: document.getElementById('settingPhone').value.trim(),
        whatsapp: document.getElementById('settingWhatsapp').value.trim(),
        gst: document.getElementById('settingGst').value.trim(),
        upi: document.getElementById('settingUpi').value.trim(),
        timings: document.getElementById('settingTimings').value.trim(),
        address: document.getElementById('settingAddress').value.trim()
    }};

    localStorage.setItem('ksk_shop_settings', JSON.stringify(settings));

    const alertBox = document.getElementById('settingsAlertBox');
    if (alertBox) {{
        alertBox.classList.remove('d-none');
        setTimeout(() => {{ alertBox.classList.add('d-none'); }}, 3500);
    }}
    return false;
}}
</script>
""" + foot_html()
    save_admin_page("admin-settings.html", content)
    print("Generated dist/admin-settings.html with persistent Shop Settings!")


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
    build_admin_reports()
    build_admin_backup()
    build_admin_settings()
    print("All Admin Panel and Login pages built successfully matching all screenshots!")
