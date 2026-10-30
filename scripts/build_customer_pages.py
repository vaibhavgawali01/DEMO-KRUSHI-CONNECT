# -*- coding: utf-8 -*-
"""
Builder for Krushi Seva Kendra - Farmer / Customer Panel
Replicates authentic templates & screenshots (Farmer Dashboard & Profile Settings)
"""
import os
import sys

BASE_DIR = r"c:\Users\HP\OneDrive\Documents\krushi seva"
DIST_DIR = os.path.join(BASE_DIR, "dist")
sys.path.append(os.path.join(BASE_DIR, "scripts"))

from build_site import head_html, nav_html, foot_html

def save_customer_page(filename, content):
    p = os.path.join(DIST_DIR, filename)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    
    # Also save in dist/customer/ and dist/farmer/
    cust_dir = os.path.join(DIST_DIR, "customer")
    farmer_dir = os.path.join(DIST_DIR, "farmer")
    os.makedirs(cust_dir, exist_ok=True)
    os.makedirs(farmer_dir, exist_ok=True)
    
    clean_name = filename.replace("farmer-", "")
    with open(os.path.join(cust_dir, clean_name), "w", encoding="utf-8") as f:
        f.write(content)
    with open(os.path.join(farmer_dir, clean_name), "w", encoding="utf-8") as f:
        f.write(content)

def render_customer_sidebar(active_tab):
    """
    Renders the authentic dark customer sidebar from Screenshot 1 (sidebar-customer)
    """
    def is_active(tab):
        return "active" if active_tab == tab else ""
    
    return f"""
<div class="customer-sidebar-shell mb-4">
    <!-- User Profile Header (Screenshot 1) -->
    <div class="customer-sidebar-user">
        <div class="customer-avatar-circle">
            <i class="bi bi-person-fill"></i>
        </div>
        <h6 class="mb-1 fw-bold text-white" id="sidebarUserDisplayName" style="letter-spacing:0.5px;">VSGAWALI</h6>
        <small class="text-secondary small text-uppercase" id="sidebarUserDisplayLoc" style="font-size:0.75rem;letter-spacing:0.5px;">KOPARGAON, AHILYANAGAR</small>
    </div>

    <!-- Section: FARMER MENU -->
    <div class="customer-sidebar-title">
        <span class="lang-mr">शेतकरी मेनू</span>
        <span class="lang-en">FARMER MENU</span>
    </div>
    <nav class="customer-sidebar-nav">
        <a href="farmer-dashboard.html" class="customer-sidebar-item {is_active('dashboard')}">
            <i class="bi bi-grid-1x2-fill text-success fs-5"></i>
            <span class="lang-mr">डॅशबोर्ड</span>
            <span class="lang-en">Dashboard</span>
        </a>
        <a href="farmer-orders.html" class="customer-sidebar-item {is_active('orders')}">
            <i class="bi bi-bag-check-fill text-primary fs-5"></i>
            <span class="lang-mr">माझ्या ऑर्डर्स</span>
            <span class="lang-en">My Orders</span>
        </a>
        <a href="farmer-udhari.html" class="customer-sidebar-item {is_active('udhari')}">
            <i class="bi bi-credit-card-2-front-fill text-warning fs-5"></i>
            <span class="lang-mr">उधारी खातेवही</span>
            <span class="lang-en">My Credit Ledger</span>
        </a>
        <a href="farmer-pay.html" class="customer-sidebar-item {is_active('pay')}">
            <i class="bi bi-qr-code-scan text-info fs-5"></i>
            <span class="lang-mr">💳 Pay Now (UPI)</span>
            <span class="lang-en">💳 Pay Now (UPI)</span>
        </a>
        <a href="farmer-payments.html" class="customer-sidebar-item {is_active('payments')}">
            <i class="bi bi-receipt-cutoff text-secondary fs-5"></i>
            <span class="lang-mr">जमा पावत्या</span>
            <span class="lang-en">Payment History</span>
        </a>
        <a href="farmer-notifications.html" class="customer-sidebar-item {is_active('notifications')}">
            <i class="bi bi-bell-fill text-danger fs-5"></i>
            <span class="lang-mr">सूचना व अलर्ट</span>
            <span class="lang-en">Notifications</span>
        </a>
        <a href="farmer-profile.html" class="customer-sidebar-item {is_active('profile')}">
            <i class="bi bi-person-lines-fill text-success fs-5"></i>
            <span class="lang-mr">माझी माहिती / प्रोफाइल</span>
            <span class="lang-en">Profile</span>
        </a>
    </nav>

    <!-- Section: AGRI TOOLS -->
    <div class="customer-sidebar-title">
        <span class="lang-mr">कृषी साधने</span>
        <span class="lang-en">AGRI TOOLS</span>
    </div>
    <nav class="customer-sidebar-nav">
        <a href="weather.html" class="customer-sidebar-item">
            <i class="bi bi-cloud-sun text-primary fs-5"></i>
            <span class="lang-mr">हवामान अंदाज</span>
            <span class="lang-en">Agri Weather</span>
        </a>
        <a href="farming-tips.html" class="customer-sidebar-item">
            <i class="bi bi-journal-check text-warning fs-5"></i>
            <span class="lang-mr">पीक सल्ला</span>
            <span class="lang-en">Crop Tips</span>
        </a>
    </nav>

    <!-- Logout Action -->
    <button type="button" onclick="handleLogout()" class="customer-sidebar-logout">
        <i class="bi bi-box-arrow-right"></i>
        <span class="lang-mr">बाहेर पडा (Logout)</span>
        <span class="lang-en">Logout</span>
    </button>
</div>
"""

# ==============================================================================
# 1. FARMER PROFILE (Matching Screenshot 1)
# ==============================================================================
def build_farmer_profile():
    sidebar = render_customer_sidebar("profile")
    content = head_html("शेतकरी प्रोफाइल", "Farmer Profile Settings") + nav_html("dashboard") + f"""
<div class="container my-4" style="max-width: 1240px;">
    <div class="row g-4">
        <!-- Dark Sidebar (Screenshot 1) -->
        <div class="col-lg-3 col-md-4">
            {sidebar}
        </div>

        <!-- Main Profile Settings Area -->
        <div class="col-lg-9 col-md-8">
            <div class="card border-0 shadow-sm rounded-4 bg-white overflow-hidden">
                <div class="card-header bg-white py-3 px-4 border-bottom">
                    <h5 class="mb-0 fw-bold text-success d-flex align-items-center gap-2">
                        <i class="bi bi-person-lines-fill"></i>
                        <span class="lang-mr">Farmer Profile Settings / माझी माहिती</span>
                        <span class="lang-en">Farmer Profile Settings / माझी माहिती</span>
                    </h5>
                </div>
                <div class="card-body p-4">
                    <div id="profileAlert" class="alert alert-success d-none py-2 mb-3">
                        <i class="bi bi-check-circle-fill me-2"></i>
                        <span class="lang-mr">माहिती यशस्वीरित्या जतन केली आहे!</span>
                        <span class="lang-en">Profile settings saved successfully!</span>
                    </div>

                    <form id="profileForm" onsubmit="return handleSaveProfile(event)">
                        <div class="row g-3">
                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-success">
                                    <span class="lang-mr">Full Name / नाव *</span>
                                    <span class="lang-en">Full Name / नाव *</span>
                                </label>
                                <input type="text" id="profName" class="form-control" required value="VSGAWALI">
                            </div>

                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-success">
                                    <span class="lang-mr">Mobile Number (Read-only)</span>
                                    <span class="lang-en">Mobile Number (Read-only)</span>
                                </label>
                                <input type="text" id="profMobile" class="form-control bg-light" readonly value="8605000000">
                            </div>

                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-success">
                                    <span class="lang-mr">Email Address (Read-only)</span>
                                    <span class="lang-en">Email Address (Read-only)</span>
                                </label>
                                <input type="email" id="profEmail" class="form-control bg-light" readonly value="VSG0000000@GMAIL.COM">
                            </div>

                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-success">
                                    <span class="lang-mr">Village / गाव *</span>
                                    <span class="lang-en">Village / गाव *</span>
                                </label>
                                <input type="text" id="profVillage" class="form-control" required value="KOPARGAON">
                            </div>

                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-success">
                                    <span class="lang-mr">Taluka / तालुका</span>
                                    <span class="lang-en">Taluka / तालुका</span>
                                </label>
                                <input type="text" id="profTaluka" class="form-control" value="KPARGAON">
                            </div>

                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-success">
                                    <span class="lang-mr">District / जिल्हा</span>
                                    <span class="lang-en">District / जिल्हा</span>
                                </label>
                                <input type="text" id="profDistrict" class="form-control" value="AHILYANAGAR">
                            </div>

                            <div class="col-12">
                                <label class="form-label small fw-bold text-success">
                                    <span class="lang-mr">Farm Address / शेताचा पत्ता</span>
                                    <span class="lang-en">Farm Address / शेताचा पत्ता</span>
                                </label>
                                <textarea id="profAddress" class="form-control" rows="3">KOPARGAON</textarea>
                            </div>

                            <div class="col-md-6">
                                <label class="form-label small fw-bold text-success">
                                    <span class="lang-mr">Change Password (Leave blank to keep current)</span>
                                    <span class="lang-en">Change Password (Leave blank to keep current)</span>
                                </label>
                                <input type="password" id="profPassword" class="form-control" placeholder="New Password">
                            </div>

                            <div class="col-12 pt-2">
                                <button type="submit" class="btn btn-success fw-bold px-4 py-2 rounded-3 shadow-sm" style="background:#15803d; border-color:#15803d;">
                                    <span class="lang-mr">Update Profile / माहिती साठवा</span>
                                    <span class="lang-en">Update Profile / माहिती साठवा</span>
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
document.addEventListener('DOMContentLoaded', function(){{
    var savedName = localStorage.getItem('user_name') || 'VSGAWALI';
    var savedLoc = localStorage.getItem('user_location') || 'KOPARGAON, AHILYANAGAR';
    var savedPhone = localStorage.getItem('user_phone') || '8605000000';
    
    var elName = document.getElementById('profName');
    var elMobile = document.getElementById('profMobile');
    var elSideName = document.getElementById('sidebarUserDisplayName');
    var elSideLoc = document.getElementById('sidebarUserDisplayLoc');
    
    if (elName && savedName) elName.value = savedName;
    if (elMobile && savedPhone) elMobile.value = savedPhone;
    if (elSideName && savedName) elSideName.textContent = savedName;
    if (elSideLoc && savedLoc) elSideLoc.textContent = savedLoc;
}});

function handleSaveProfile(e) {{
    e.preventDefault();
    var newName = document.getElementById('profName').value.trim();
    var village = document.getElementById('profVillage').value.trim();
    var dist = document.getElementById('profDistrict').value.trim();
    
    if (newName) {{
        localStorage.setItem('user_name', newName);
        var newLoc = (village ? village : 'KOPARGAON') + (dist ? ', ' + dist : ', AHILYANAGAR');
        localStorage.setItem('user_location', newLoc);
        
        var elSideName = document.getElementById('sidebarUserDisplayName');
        var elSideLoc = document.getElementById('sidebarUserDisplayLoc');
        if (elSideName) elSideName.textContent = newName;
        if (elSideLoc) elSideLoc.textContent = newLoc;
    }}
    
    var alertBox = document.getElementById('profileAlert');
    if (alertBox) {{
        alertBox.classList.remove('d-none');
        setTimeout(function(){{ alertBox.classList.add('d-none'); }}, 3500);
    }}
    return false;
}}
</script>
""" + foot_html()
    save_customer_page("farmer-profile.html", content)
    save_customer_page("profile.html", content)
    print("Generated dist/farmer-profile.html matching Screenshot 1")

# ==============================================================================
# 2. FARMER DASHBOARD (Matching Screenshot 2 Pixel-to-Pixel)
# ==============================================================================
def build_farmer_dashboard():
    content = head_html("शेतकरी डॅशबोर्ड", "Farmer Dashboard") + nav_html("dashboard") + """
<div class="farmer-dashboard-wrapper py-4" style="background:#f8faf8; min-height:85vh;">
    <div class="container" style="max-width: 1240px;">
        <!-- Top Greeting Header (Screenshot 2) -->
        <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-3 mb-4">
            <div>
                <h1 class="h3 fw-bold m-0" style="color: #1a5f3d;">
                    <span class="lang-mr">नमस्ते, </span><span class="lang-en">Hello, </span><span id="farmerGreetName">VSGAWALI</span> 🌾
                </h1>
                <p class="text-muted small m-0 mt-1" id="dashCurrentDate">
                    Saturday, October 31, 2026 | Dashboard Overview
                </p>
            </div>
            <div class="d-flex gap-2 align-items-center flex-wrap">
                <a href="farmer-notifications.html" class="btn btn-light border d-flex align-items-center gap-2 px-3 py-2 rounded-3 text-dark text-decoration-none shadow-sm" style="font-size: 14px; background:#fff;">
                    <i class="bi bi-bell-fill text-warning"></i>
                    <span><span class="lang-mr">० सूचना</span><span class="lang-en">0 Alerts</span></span>
                </a>
                <a href="farmer-profile.html" class="btn btn-light border d-flex align-items-center gap-2 px-3 py-2 rounded-3 text-dark text-decoration-none shadow-sm" style="font-size: 14px; background:#fff;">
                    <i class="bi bi-person-fill text-success"></i>
                    <span><span class="lang-mr">माझे प्रोफाइल</span><span class="lang-en">Profile</span></span>
                </a>
            </div>
        </div>

        <!-- 1. Top Green Nil Balance Banner (Screenshot 2) -->
        <div class="farmer-balance-card mb-4">
            <div class="row align-items-center g-3">
                <div class="col-lg-7">
                    <div class="d-flex align-items-center gap-2 mb-2">
                        <span class="badge text-white px-3 py-1 rounded-pill fw-bold" style="background:#059669 !important; font-size:13px;">
                            <i class="bi bi-check-circle-fill me-1"></i>
                            <span class="lang-mr">✔ उधारी निरंक</span>
                            <span class="lang-en">✔ Nil Balance</span>
                        </span>
                    </div>
                    <div class="d-flex align-items-baseline gap-3">
                        <h1 class="display-5 fw-bold m-0" style="color: #059669; font-weight:800;">₹0.00</h1>
                        <span class="fs-6 fw-semibold text-muted">
                            <span class="lang-mr">माझी एकूण बाकी रक्कम</span>
                            <span class="lang-en">My Total Pending Balance</span>
                        </span>
                    </div>
                    <p class="m-0 mt-2 text-success fw-semibold small">
                        <span class="lang-mr">🎉 अभिनंदन! आपल्या खात्यावर सध्या कोणतीही उधारी बाकी नाही.</span>
                        <span class="lang-en">🎉 Great! You have zero outstanding credit dues on your account.</span>
                    </p>
                </div>
                <div class="col-lg-5 text-lg-end">
                    <a href="farmer-udhari.html" class="btn btn-white bg-white text-dark border px-4 py-2 rounded-3 fw-bold shadow-sm d-inline-flex align-items-center gap-2">
                        <i class="bi bi-file-earmark-text text-primary"></i>
                        <span class="lang-mr">उधारी खाते पाहा</span>
                        <span class="lang-en">View Credit Ledger</span>
                    </a>
                </div>
            </div>
        </div>

        <!-- 2. Quick Stats: 3 KPI Cards (Screenshot 2) -->
        <div class="row g-3 mb-4">
            <!-- 1. PENDING DUE -->
            <div class="col-sm-6 col-lg-4">
                <div class="farmer-stat-card h-100 d-flex flex-column justify-content-between" style="border-left: 4px solid #ea580c !important;">
                    <div class="d-flex justify-content-between align-items-start mb-2">
                        <p class="m-0 text-muted fw-semibold text-uppercase small" style="font-size: 12px; letter-spacing: 0.5px;">
                            <span class="lang-mr">बाकी उधारी</span>
                            <span class="lang-en">PENDING DUE</span>
                        </p>
                        <i class="bi bi-exclamation-circle text-danger fs-5"></i>
                    </div>
                    <p class="h3 fw-bold m-0 text-danger">₹0</p>
                    <p class="m-0 mt-2 text-muted small" style="font-size: 12px;">
                        <span class="lang-mr">उधारी निरंक</span>
                        <span class="lang-en">Nil Balance</span>
                    </p>
                </div>
            </div>

            <!-- 2. AVAILABLE CREDIT LIMIT -->
            <div class="col-sm-6 col-lg-4">
                <div class="farmer-stat-card h-100 d-flex flex-column justify-content-between" style="border-left: 4px solid #16a34a !important;">
                    <div class="d-flex justify-content-between align-items-start mb-2">
                        <p class="m-0 text-muted fw-semibold text-uppercase small" style="font-size: 12px; letter-spacing: 0.5px;">
                            <span class="lang-mr">उपलब्ध उधारी मर्यादा</span>
                            <span class="lang-en">AVAILABLE CREDIT LIMIT</span>
                        </p>
                        <i class="bi bi-credit-card text-success fs-5"></i>
                    </div>
                    <p class="h3 fw-bold m-0 text-success">₹15,000</p>
                    <p class="m-0 mt-2 text-muted small" style="font-size: 12px;">
                        <span class="lang-mr">एकूण मर्यादा: ₹15,000</span>
                        <span class="lang-en">Total Limit: ₹15,000</span>
                    </p>
                </div>
            </div>

            <!-- 3. TOTAL PURCHASES -->
            <div class="col-sm-6 col-lg-4">
                <div class="farmer-stat-card h-100 d-flex flex-column justify-content-between" style="border-left: 4px solid #0284c7 !important;">
                    <div class="d-flex justify-content-between align-items-start mb-2">
                        <p class="m-0 text-muted fw-semibold text-uppercase small" style="font-size: 12px; letter-spacing: 0.5px;">
                            <span class="lang-mr">एकूण खरेदी</span>
                            <span class="lang-en">TOTAL PURCHASES</span>
                        </p>
                        <i class="bi bi-cart3 text-primary fs-5"></i>
                    </div>
                    <p class="h3 fw-bold m-0 text-primary">₹0</p>
                    <p class="m-0 mt-2 text-muted small" style="font-size: 12px;">
                        <span class="lang-mr">या महिन्यात: ₹0</span>
                        <span class="lang-en">This Month: ₹0</span>
                    </p>
                </div>
            </div>
        </div>

        <!-- 3. Main Workspace: Two Columns (Left ~65%, Right ~35%) -->
        <div class="row g-4">
            <!-- Left Column: Recent Orders & Reviews -->
            <div class="col-lg-8">
                <!-- Recent Orders Card (Screenshot 2) -->
                <div class="card border-0 shadow-sm rounded-4 p-4 bg-white mb-4">
                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <h5 class="fw-bold text-dark m-0">
                            <span class="lang-mr">अलीकडील ऑर्डर्स</span>
                            <span class="lang-en">Recent Orders</span>
                        </h5>
                        <a href="farmer-orders.html" class="text-primary small fw-semibold text-decoration-none d-flex align-items-center gap-1">
                            <span class="lang-mr">सर्व पाहा</span>
                            <span class="lang-en">View All</span> &rarr;
                        </a>
                    </div>

                    <!-- Order Item 1 -->
                    <div class="farmer-order-row">
                        <div class="d-flex align-items-center gap-3">
                            <div class="rounded-3 d-flex align-items-center justify-content-center" style="width: 44px; height: 44px; background: #f0fdf4; color: #16a34a; font-size: 1.25rem;">
                                🌱
                            </div>
                            <div>
                                <h6 class="fw-bold mb-1 text-dark">NPK Fertilizer (50 kg)</h6>
                                <small class="text-muted d-block mb-1">Order: KSK-2026-00342 | 28 Aug 2026</small>
                                <span class="badge bg-success-subtle text-success border border-success-subtle px-2 py-1 rounded-pill small">Ready for Delivery</span>
                            </div>
                        </div>
                        <div class="text-end">
                            <h6 class="fw-bold text-dark mb-2">₹2,450</h6>
                            <button type="button" class="btn btn-sm btn-light border px-3 py-1 rounded-3" onclick="openOrderTrack('KSK-2026-00342', 'NPK Fertilizer (50 kg)', '28 Aug 2026', 'Ready for Delivery', 4)">Track</button>
                        </div>
                    </div>

                    <!-- Order Item 2 -->
                    <div class="farmer-order-row">
                        <div class="d-flex align-items-center gap-3">
                            <div class="rounded-3 d-flex align-items-center justify-content-center" style="width: 44px; height: 44px; background: #fffbeb; color: #d97706; font-size: 1.25rem;">
                                🧴
                            </div>
                            <div>
                                <h6 class="fw-bold mb-1 text-dark">Organic Pesticide (1 Liter)</h6>
                                <small class="text-muted d-block mb-1">Order: KSK-2026-00341 | 25 Aug 2026</small>
                                <span class="badge bg-info-subtle text-info border border-info-subtle px-2 py-1 rounded-pill small">Processing</span>
                            </div>
                        </div>
                        <div class="text-end">
                            <h6 class="fw-bold text-dark mb-2">₹650</h6>
                            <button type="button" class="btn btn-sm btn-light border px-3 py-1 rounded-3" onclick="openOrderTrack('KSK-2026-00341', 'Organic Pesticide (1 Liter)', '25 Aug 2026', 'Processing', 2)">Track</button>
                        </div>
                    </div>

                    <!-- Order Item 3 -->
                    <div class="farmer-order-row">
                        <div class="d-flex align-items-center gap-3">
                            <div class="rounded-3 d-flex align-items-center justify-content-center" style="width: 44px; height: 44px; background: #fdf4ff; color: #9333ea; font-size: 1.25rem;">
                                🔧
                            </div>
                            <div>
                                <h6 class="fw-bold mb-1 text-dark">Manual Farming Tool</h6>
                                <small class="text-muted d-block mb-1">Order: KSK-2026-00340 | 20 Aug 2026</small>
                                <span class="badge bg-primary-subtle text-primary border border-primary-subtle px-2 py-1 rounded-pill small">Delivered</span>
                            </div>
                        </div>
                        <div class="text-end">
                            <h6 class="fw-bold text-dark mb-2">₹1,200</h6>
                            <button type="button" class="btn btn-sm btn-light border px-3 py-1 rounded-3" onclick="openOrderInvoice('KSK-2026-00340')">Invoice</button>
                        </div>
                    </div>
                </div>

                <!-- Farmer Reviews & Ratings Card (Screenshot 2) -->
                <div class="card border-0 shadow-sm rounded-4 p-4 bg-white mb-4">
                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <h5 class="fw-bold text-dark m-0 d-flex align-items-center gap-2">
                            <span class="text-warning">⭐</span>
                            <span class="lang-mr">शेतकरी अभिप्राय आणि रेटिंग</span>
                            <span class="lang-en">Farmer Reviews & Ratings</span>
                        </h5>
                        <a href="index.html#reviews" class="text-primary small fw-semibold text-decoration-none">
                            <span class="lang-mr">सर्व पाहा</span>
                            <span class="lang-en">View All</span>
                        </a>
                    </div>

                    <div class="p-3 rounded-4 mb-3" style="background:#f0fdf4; border: 1px solid #bbf7d0;">
                        <div class="d-flex justify-content-between align-items-center mb-2">
                            <span class="badge px-3 py-1 rounded-pill fw-bold text-white" style="background:#15803d !important;">
                                4.9 / 5.0 ⭐
                            </span>
                            <span class="text-muted small fw-semibold">500+ Farmers</span>
                        </div>
                        <p class="small text-muted mb-0">
                            <span class="lang-mr">आपण खरेदी केलेल्या कृषी उत्पादनांविषयी आपला मोलाचा अनुभव शेअर करा.</span>
                            <span class="lang-en">Share your valuable experience with products you purchased.</span>
                        </p>
                    </div>

                    <div class="d-flex gap-2 flex-wrap">
                        <a href="index.html#reviews" class="btn btn-outline-success rounded-3 fw-bold px-3 py-2 d-flex align-items-center gap-2">
                            <i class="bi bi-chat-left-text"></i>
                            <span class="lang-mr">अभिप्राय वाचा</span>
                            <span class="lang-en">Read Reviews</span>
                        </a>
                        <a href="products.html" class="btn btn-success rounded-3 fw-bold px-3 py-2 text-white d-flex align-items-center gap-2" style="background:#16a34a; border-color:#16a34a;">
                            <span class="lang-mr">उत्पादने खरेदी करा</span>
                            <span class="lang-en">Browse Products</span>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Right Column: Quick Actions, Due Alert, Daily Tip -->
            <div class="col-lg-4">
                <!-- Quick Actions 2x2 Grid (Screenshot 2) -->
                <div class="card border-0 shadow-sm rounded-4 p-3 bg-white mb-4">
                    <h6 class="fw-bold text-dark mb-3 px-1">
                        <span class="lang-mr">⚡ झटपट कृती</span>
                        <span class="lang-en">⚡ Quick Actions</span>
                    </h6>
                    <div class="row g-2">
                        <!-- 1. Shopping -->
                        <div class="col-6">
                            <a href="products.html" class="farmer-quick-btn" style="background: #f0fdf4; color: #16a34a;">
                                <i class="bi bi-cart-check fs-4 mb-1"></i>
                                <span class="lang-mr">खरेदी</span>
                                <span class="lang-en">Shopping</span>
                            </a>
                        </div>
                        <!-- 2. Invoices -->
                        <div class="col-6">
                            <a href="farmer-orders.html" class="farmer-quick-btn" style="background: #f8fafc; color: #475569;">
                                <i class="bi bi-file-earmark-text fs-4 mb-1"></i>
                                <span class="lang-mr">पावत्या</span>
                                <span class="lang-en">Invoices</span>
                            </a>
                        </div>
                        <!-- 3. Alerts -->
                        <div class="col-6">
                            <a href="farmer-notifications.html" class="farmer-quick-btn" style="background: #fffbeb; color: #d97706;">
                                <i class="bi bi-exclamation-circle fs-4 mb-1"></i>
                                <span class="lang-mr">अलर्ट्स</span>
                                <span class="lang-en">Alerts</span>
                            </a>
                        </div>
                        <!-- 4. Contact -->
                        <div class="col-6">
                            <a href="javascript:void(0)" onclick="openStoreContactModal()" class="farmer-quick-btn" style="background: #faf5ff; color: #7c3aed;">
                                <i class="bi bi-telephone fs-4 mb-1"></i>
                                <span class="lang-mr">संपर्क</span>
                                <span class="lang-en">Contact</span>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Payment Due Soon Box (Screenshot 2) -->
                <div class="card border-0 shadow-sm rounded-4 p-3 mb-4" style="background: #fef2f2; border-left: 4px solid #dc2626 !important;">
                    <div class="d-flex align-items-center gap-2 mb-1">
                        <i class="bi bi-exclamation-triangle-fill text-danger fs-5"></i>
                        <h6 class="fw-bold text-danger mb-0">
                            <span class="lang-mr">देय रक्कम सूचना</span>
                            <span class="lang-en">Payment Due Soon</span>
                        </h6>
                    </div>
                    <p class="small text-muted mb-2">
                        <span class="lang-mr">देय रक्कम: ₹0</span>
                        <span class="lang-en">Amount Due: ₹0</span>
                    </p>
                    <button type="button" onclick="openQuickPayModal()" class="btn btn-danger fw-bold rounded-3 py-2 px-3 small w-100" style="background:#dc2626; border:none;">
                        <span class="lang-mr">आत्ताच भरा (Pay Now)</span>
                        <span class="lang-en">Pay Now</span>
                    </button>
                </div>

                <!-- Daily Farming Tip Box (Screenshot 2) -->
                <div class="card border-0 shadow-sm rounded-4 p-3 mb-4" style="background: #f0fdf4; border: 1px solid #bbf7d0;">
                    <h6 class="fw-bold text-success mb-2">
                        <span class="lang-mr">💡 आजचा शेती सल्ला</span>
                        <span class="lang-en">💡 Daily Farming Tip</span>
                    </h6>
                    <p class="small text-muted mb-2" style="line-height: 1.55;">
                        <span class="lang-mr">मातीतील ओलावा २ इंच खोलीवर कायम ठेवा. योग्य व संतुलित पाणी दिल्यास पिकाची उत्पादकता वाढते.</span>
                        <span class="lang-en">Keep soil moist at 2 inches depth. Regular and balanced watering improves crop yield significantly.</span>
                    </p>
                    <a href="javascript:void(0)" onclick="openTipsModal()" class="text-success fw-bold small text-decoration-none">
                        <span class="lang-mr">अधिक सल्ले पाहा &rarr;</span>
                        <span class="lang-en">More Tips &rarr;</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- ================= MODALS FOR INTERACTIVE FEATURES ================= -->

<!-- 1. Order Tracking Stepper Modal -->
<div class="modal fade" id="orderTrackModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content border-0 shadow-lg rounded-4">
            <div class="modal-header border-0 pb-0">
                <h5 class="modal-title fw-bold text-success d-flex align-items-center gap-2">
                    <i class="bi bi-geo-alt-fill"></i>
                    <span class="lang-mr">ऑर्डर ट्रॅकिंग</span>
                    <span class="lang-en">Order Tracking</span>
                </h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body p-4">
                <div class="p-3 rounded-3 mb-4 bg-light border">
                    <div class="d-flex justify-content-between align-items-center mb-1">
                        <span class="fw-bold text-dark fs-6" id="trackOrderTitle">NPK Fertilizer (50 kg)</span>
                        <span class="badge bg-success-subtle text-success border border-success-subtle px-2 py-1" id="trackOrderBadge">Ready for Delivery</span>
                    </div>
                    <small class="text-muted d-block" id="trackOrderIdDate">Order: KSK-2026-00342 | 28 Aug 2026</small>
                </div>

                <!-- 4-step Stepper -->
                <div class="tracking-stepper position-relative mb-4">
                    <div class="d-flex align-items-center mb-3">
                        <div class="track-step-circle done me-3"><i class="bi bi-check-lg"></i></div>
                        <div>
                            <h6 class="mb-0 fw-bold text-dark">Order Confirmed</h6>
                            <small class="text-muted">Order received & stock allocated</small>
                        </div>
                    </div>
                    <div class="d-flex align-items-center mb-3">
                        <div class="track-step-circle done me-3"><i class="bi bi-check-lg"></i></div>
                        <div>
                            <h6 class="mb-0 fw-bold text-dark">Payment Received</h6>
                            <small class="text-muted">Paid & verified via UPI</small>
                        </div>
                    </div>
                    <div class="d-flex align-items-center mb-3">
                        <div class="track-step-circle done me-3"><i class="bi bi-check-lg"></i></div>
                        <div>
                            <h6 class="mb-0 fw-bold text-dark">Quality Packed</h6>
                            <small class="text-muted">Inspected by Saptashrungi Agro team</small>
                        </div>
                    </div>
                    <div class="d-flex align-items-center">
                        <div class="track-step-circle active me-3"><i class="bi bi-truck"></i></div>
                        <div>
                            <h6 class="mb-0 fw-bold text-primary" id="trackStepFinalTitle">Ready for Pickup / Out for Delivery</h6>
                            <small class="text-muted" id="trackStepFinalDesc">Visit Kendra at Mirakhnagar or await scheduled delivery</small>
                        </div>
                    </div>
                </div>

                <div class="alert alert-success d-flex align-items-center gap-2 mb-0 py-2">
                    <i class="bi bi-shop text-success fs-5"></i>
                    <div class="small">
                        <strong>Pickup Location:</strong> Saptashrungi Agro Services, Mirakhnagar, Vaijapur.<br>
                        <span class="text-muted">Timings: Mon - Sat 8:00 AM - 8:30 PM | Helpline: 8600813827</span>
                    </div>
                </div>
            </div>
            <div class="modal-footer border-0 pt-0">
                <a href="tel:+918600813827" class="btn btn-outline-success rounded-pill px-3"><i class="bi bi-telephone me-1"></i> Call Kendra</a>
                <a href="https://wa.me/918600813827" target="_blank" class="btn btn-success rounded-pill px-3" style="background:#16a34a;"><i class="bi bi-whatsapp me-1"></i> WhatsApp</a>
            </div>
        </div>
    </div>
</div>

<!-- 2. Tax Invoice Receipt Modal -->
<div class="modal fade" id="orderInvoiceModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered">
        <div class="modal-content border-0 shadow-lg rounded-4">
            <div class="modal-header border-0 pb-0">
                <h5 class="modal-title fw-bold text-success d-flex align-items-center gap-2">
                    <i class="bi bi-receipt"></i>
                    <span class="lang-mr">कर बीजक (Tax Invoice)</span>
                    <span class="lang-en">Official Tax Invoice</span>
                </h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body p-4" id="printableInvoiceArea">
                <div class="border rounded-4 p-4 bg-white">
                    <!-- Shop Header -->
                    <div class="d-flex justify-content-between align-items-start border-bottom pb-3 mb-3">
                        <div class="d-flex align-items-center gap-3">
                            <img src="images/saptashrungi_logo_round.jpg" alt="Logo" class="rounded-circle shadow-sm" style="width: 58px; height: 58px; object-fit: cover;">
                            <div>
                                <h5 class="fw-bold mb-0 text-success">सप्तशृंगी ॲग्रो सर्व्हिसेस</h5>
                                <small class="text-muted d-block fw-semibold">Saptashrungi Agro Services | कृषी सेवा केंद्र</small>
                                <small class="text-muted d-block" style="font-size: 11px;">Mirakhnagar, Vaijapur, Chhatrapati Sambhajinagar - 423703</small>
                                <small class="text-muted d-block" style="font-size: 11px;">Mob: +91 8600813827 | GSTIN: 27AAAAA0000A1Z5</small>
                            </div>
                        </div>
                        <div class="text-end">
                            <span class="badge text-white px-3 py-1 rounded-pill mb-1 fw-bold" style="background:#15803d;">TAX INVOICE</span>
                            <h6 class="fw-bold mb-0 text-dark">#INV-2026-00340</h6>
                            <small class="text-muted">Date: 20 Aug 2026</small>
                        </div>
                    </div>

                    <!-- Billed To -->
                    <div class="row mb-3 bg-light p-3 rounded-3 g-2">
                        <div class="col-sm-6">
                            <span class="text-muted small d-block">खरेदीदार शेतकरी (Billed To):</span>
                            <strong class="text-dark" id="invoiceFarmerName">VSGAWALI</strong>
                            <div class="small text-muted" id="invoiceFarmerLoc">Kopargaon, Ahilyanagar</div>
                        </div>
                        <div class="col-sm-6 text-sm-end">
                            <span class="text-muted small d-block">Payment Mode:</span>
                            <strong class="text-success"><i class="bi bi-check-circle-fill me-1"></i> UPI (Paid Online)</strong>
                            <div class="small text-muted">Status: Delivered & Cleared</div>
                        </div>
                    </div>

                    <!-- Items Table -->
                    <div class="table-responsive mb-3">
                        <table class="table table-bordered align-middle mb-0">
                            <thead class="table-light small">
                                <tr>
                                    <th>#</th>
                                    <th>Item Description</th>
                                    <th>HSN</th>
                                    <th class="text-center">Qty</th>
                                    <th class="text-end">Rate (₹)</th>
                                    <th class="text-end">GST (18%)</th>
                                    <th class="text-end">Amount (₹)</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>1</td>
                                    <td><strong>Manual Farming Tool (शेती अवजारे)</strong><br><small class="text-muted">High-grade steel hoe & weeder</small></td>
                                    <td>8201</td>
                                    <td class="text-center">1</td>
                                    <td class="text-end">₹1,016.95</td>
                                    <td class="text-end">₹183.05</td>
                                    <td class="text-end fw-bold">₹1,200.00</td>
                                </tr>
                            </tbody>
                            <tfoot>
                                <tr>
                                    <td colspan="6" class="text-end fw-bold">Subtotal:</td>
                                    <td class="text-end">₹1,016.95</td>
                                </tr>
                                <tr>
                                    <td colspan="6" class="text-end fw-bold">CGST (9%) + SGST (9%):</td>
                                    <td class="text-end">₹183.05</td>
                                </tr>
                                <tr class="table-success">
                                    <td colspan="6" class="text-end fw-bold fs-6">Grand Total (एकूण देय):</td>
                                    <td class="text-end fw-bold fs-6 text-success">₹1,200.00</td>
                                </tr>
                            </tfoot>
                        </table>
                    </div>

                    <div class="small text-muted text-center pt-2 border-top">
                        धन्यवाद! सप्तशृंगी ॲग्रो सर्व्हिसेस, मिरखनगर आपल्या समृद्ध शेतीसाठी सदैव तत्पर आहे.
                    </div>
                </div>
            </div>
            <div class="modal-footer border-0 pt-0">
                <button type="button" class="btn btn-outline-secondary rounded-pill px-3" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-success rounded-pill px-4" onclick="window.print()" style="background:#16a34a;"><i class="bi bi-printer me-1"></i> Print / Download PDF</button>
            </div>
        </div>
    </div>
</div>

<!-- 3. Quick UPI Pay Modal -->
<div class="modal fade" id="farmerQuickPayModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content border-0 shadow-lg rounded-4">
            <div class="modal-header border-0 pb-0">
                <h5 class="modal-title fw-bold text-success d-flex align-items-center gap-2">
                    <i class="bi bi-qr-code-scan"></i>
                    <span class="lang-mr">त्वरित UPI पेमेंट</span>
                    <span class="lang-en">Quick UPI Payment</span>
                </h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body p-4 text-center">
                <div class="bg-white p-3 rounded-4 shadow-sm border d-inline-block mb-3">
                    <img src="https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=upi://pay?pa=8600813827@upi%26pn=Saptashrungi%20Agro%20Services" alt="UPI QR" style="width:160px;height:160px;">
                </div>
                <h6 class="fw-bold mb-1 text-dark">सप्तशृंगी ॲग्रो सर्व्हिसेस</h6>
                <p class="text-muted small mb-2">UPI ID: <strong class="text-success">8600813827@upi</strong></p>
                
                <div class="d-flex justify-content-center gap-2 my-3">
                    <a href="upi://pay?pa=8600813827@upi&pn=Saptashrungi%20Agro" class="btn btn-sm btn-outline-primary rounded-pill px-3"><i class="bi bi-phone me-1"></i> Google Pay</a>
                    <a href="upi://pay?pa=8600813827@upi&pn=Saptashrungi%20Agro" class="btn btn-sm btn-outline-primary rounded-pill px-3"><i class="bi bi-wallet2 me-1"></i> PhonePe</a>
                    <a href="upi://pay?pa=8600813827@upi&pn=Saptashrungi%20Agro" class="btn btn-sm btn-outline-primary rounded-pill px-3"><i class="bi bi-lightning-charge me-1"></i> Paytm</a>
                </div>

                <div class="alert alert-info py-2 small mb-0 text-start">
                    <i class="bi bi-info-circle-fill me-1"></i> आपल्या खात्यावर सध्या ₹0 उधारी बाकी आहे. नवीन खरेदी किंवा आगाऊ जमा रकमेसाठी थेट स्कॅन करा.
                </div>
            </div>
            <div class="modal-footer border-0 pt-0">
                <button type="button" class="btn btn-light rounded-pill px-3" data-bs-dismiss="modal">Close</button>
                <a href="farmer-pay.html" class="btn btn-success rounded-pill px-4" style="background:#16a34a;">Full Payment Page &rarr;</a>
            </div>
        </div>
    </div>
</div>

<!-- 4. Store Contact Modal -->
<div class="modal fade" id="farmerStoreContactModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content border-0 shadow-lg rounded-4">
            <div class="modal-header border-0 pb-0">
                <h5 class="modal-title fw-bold text-success d-flex align-items-center gap-2">
                    <i class="bi bi-shop"></i>
                    <span class="lang-mr">दुकान संपर्क व पत्ता</span>
                    <span class="lang-en">Store Contact & Location</span>
                </h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body p-4">
                <div class="d-flex gap-3 align-items-start mb-3">
                    <img src="images/saptashrungi_shop.jpg" class="rounded-3 shadow-sm border" style="width: 85px; height: 85px; object-fit: cover;">
                    <div>
                        <h6 class="fw-bold text-dark mb-1">सप्तशृंगी ॲग्रो सर्व्हिसेस</h6>
                        <p class="small text-muted mb-1"><i class="bi bi-geo-alt-fill text-danger me-1"></i> मिरखनगर, वैजापूर, छत्रपती संभाजीनगर - 423703</p>
                        <p class="small text-muted mb-0"><i class="bi bi-clock-fill text-warning me-1"></i> सोम - शनि: सकाळी ८:०० ते रात्री ८:३०</p>
                    </div>
                </div>

                <div class="row g-2 mb-3">
                    <div class="col-6">
                        <a href="tel:+918600813827" class="btn btn-success w-100 py-2 rounded-3 fw-bold d-flex align-items-center justify-content-center gap-2" style="background:#16a34a;">
                            <i class="bi bi-telephone-fill"></i> Call Now
                        </a>
                    </div>
                    <div class="col-6">
                        <a href="https://wa.me/918600813827" target="_blank" class="btn btn-outline-success w-100 py-2 rounded-3 fw-bold d-flex align-items-center justify-content-center gap-2">
                            <i class="bi bi-whatsapp"></i> WhatsApp
                        </a>
                    </div>
                </div>

                <div class="p-3 rounded-3 bg-light border text-center">
                    <a href="https://maps.google.com/?q=Saptashrungi+Agro+Services+Mirakhnagar" target="_blank" class="btn btn-sm btn-primary rounded-pill px-3">
                        <i class="bi bi-map me-1"></i> Open in Google Maps
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- 5. Daily Tips Modal -->
<div class="modal fade" id="farmerTipsModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content border-0 shadow-lg rounded-4">
            <div class="modal-header border-0 pb-0">
                <h5 class="modal-title fw-bold text-success d-flex align-items-center gap-2">
                    <i class="bi bi-lightbulb-fill text-warning"></i>
                    <span class="lang-mr">दैनिक शेती सल्ले</span>
                    <span class="lang-en">Daily Farming Tips</span>
                </h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body p-4">
                <div class="p-3 rounded-3 mb-3" style="background:#f0fdf4;border:1px solid #bbf7d0;">
                    <h6 class="fw-bold text-success mb-1">💧 पाणी व्यवस्थापन</h6>
                    <p class="small text-muted mb-0">मातीतील ओलावा २ इंच खोलीवर कायम ठेवा. ठिबक सिंचनाचा वापर केल्यास ४०% पाण्याची बचत होते व पिकाची वाढ जोमदार होते.</p>
                </div>
                <div class="p-3 rounded-3 mb-3" style="background:#fffbeb;border:1px solid #fde68a;">
                    <h6 class="fw-bold text-warning mb-1">🌿 खत व्यवस्थापन (NPK डोस)</h6>
                    <p class="small text-muted mb-0">पिकाच्या फुलोरा व फळधारणेच्या काळात १९:१९:१९ किंवा १२:६१:०० विद्राव्य खतांची योग्य मात्रेत फवारणी करावी.</p>
                </div>
                <div class="p-3 rounded-3" style="background:#eff6ff;border:1px solid #bfdbfe;">
                    <h6 class="fw-bold text-primary mb-1">🐛 कीड व रोग नियंत्रण</h6>
                    <p class="small text-muted mb-0">मावा व तुडतुड्यांच्या नियंत्रणासाठी निंबोळी अर्क ५% किंवा योग्य शिफारशीत कीटकनाशकाची वेळेवर फवारणी करा.</p>
                </div>
            </div>
            <div class="modal-footer border-0 pt-0">
                <a href="farming-tips.html" class="btn btn-success rounded-pill px-4" style="background:#16a34a;">सर्व सल्ले पाहा &rarr;</a>
            </div>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function(){
    var savedName = localStorage.getItem('user_name') || 'VSGAWALI';
    var greetEl = document.getElementById('farmerGreetName');
    if (greetEl && savedName) greetEl.textContent = savedName;

    var invNameEl = document.getElementById('invoiceFarmerName');
    if (invNameEl && savedName) invNameEl.textContent = savedName;

    var savedLoc = localStorage.getItem('user_location') || 'Kopargaon, Ahilyanagar';
    var invLocEl = document.getElementById('invoiceFarmerLoc');
    if (invLocEl && savedLoc) invLocEl.textContent = savedLoc;

    // Set real current day/date format
    var dateEl = document.getElementById('dashCurrentDate');
    if (dateEl) {
        var now = new Date();
        var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
        dateEl.textContent = now.toLocaleDateString('en-US', options) + ' | Dashboard Overview';
    }
});

function openOrderTrack(orderId, prodName, dateStr, badgeStr, stepNum) {
    var titleEl = document.getElementById('trackOrderTitle');
    var badgeEl = document.getElementById('trackOrderBadge');
    var idDateEl = document.getElementById('trackOrderIdDate');
    if (titleEl) titleEl.textContent = prodName;
    if (badgeEl) badgeEl.textContent = badgeStr;
    if (idDateEl) idDateEl.textContent = 'Order: ' + orderId + ' | ' + dateStr;
    
    var modalEl = document.getElementById('orderTrackModal');
    if (modalEl && typeof bootstrap !== 'undefined') {
        var m = new bootstrap.Modal(modalEl);
        m.show();
    }
}

function openOrderInvoice(orderId) {
    var modalEl = document.getElementById('orderInvoiceModal');
    if (modalEl && typeof bootstrap !== 'undefined') {
        var m = new bootstrap.Modal(modalEl);
        m.show();
    }
}

function openQuickPayModal() {
    var modalEl = document.getElementById('farmerQuickPayModal');
    if (modalEl && typeof bootstrap !== 'undefined') {
        var m = new bootstrap.Modal(modalEl);
        m.show();
    }
}

function openStoreContactModal() {
    var modalEl = document.getElementById('farmerStoreContactModal');
    if (modalEl && typeof bootstrap !== 'undefined') {
        var m = new bootstrap.Modal(modalEl);
        m.show();
    }
}

function openTipsModal() {
    var modalEl = document.getElementById('farmerTipsModal');
    if (modalEl && typeof bootstrap !== 'undefined') {
        var m = new bootstrap.Modal(modalEl);
        m.show();
    }
}
</script>
""" + foot_html()
    save_customer_page("farmer-dashboard.html", content)
    print("Generated dist/farmer-dashboard.html matching Screenshot 2")

# ==============================================================================
# 3. FARMER ORDERS
# ==============================================================================
def build_farmer_orders():
    sidebar = render_customer_sidebar("orders")
    content = head_html("माझ्या ऑर्डर्स", "My Orders") + nav_html("dashboard") + f"""
<div class="container my-4" style="max-width: 1240px;">
    <div class="row g-4">
        <div class="col-lg-3 col-md-4">
            {sidebar}
        </div>
        <div class="col-lg-9 col-md-8">
            <div class="card border-0 shadow-sm rounded-4 bg-white overflow-hidden">
                <div class="card-header bg-white py-3 px-4 border-bottom d-flex justify-content-between align-items-center">
                    <h5 class="mb-0 fw-bold text-success"><i class="bi bi-bag-check-fill me-2"></i><span class="lang-mr">माझ्या ऑर्डर्स आणि खरेदी इतिहास</span><span class="lang-en">My Orders History</span></h5>
                    <a href="products.html" class="btn btn-sm btn-success rounded-pill px-3"><i class="bi bi-plus me-1"></i>New Order</a>
                </div>
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-hover align-middle mb-0">
                            <thead class="table-light text-muted small">
                                <tr>
                                    <th class="ps-4">Order #</th>
                                    <th>Date</th>
                                    <th>Items</th>
                                    <th>Total Amount</th>
                                    <th>Payment</th>
                                    <th>Status</th>
                                    <th class="text-end pe-4">Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="ps-4 fw-bold text-dark">KSK-2026-00342</td>
                                    <td>28 Aug 2026</td>
                                    <td>NPK Fertilizer 50kg (1 Bag)</td>
                                    <td class="fw-bold text-success">₹2,450.00</td>
                                    <td><span class="badge bg-light text-dark border">UPI</span> <span class="text-success small fw-semibold">Paid</span></td>
                                    <td><span class="badge bg-success-subtle text-success">Ready for Delivery</span></td>
                                    <td class="text-end pe-4">
                                        <button class="btn btn-sm btn-outline-success" onclick="alert('Order KSK-2026-00342: Package Ready for Delivery at Saptashrungi Agro Kendra.')"><i class="bi bi-truck me-1"></i> Track</button>
                                    </td>
                                </tr>
                                <tr>
                                    <td class="ps-4 fw-bold text-dark">KSK-2026-00341</td>
                                    <td>25 Aug 2026</td>
                                    <td>Organic Pesticide (1 Liter)</td>
                                    <td class="fw-bold text-success">₹650.00</td>
                                    <td><span class="badge bg-light text-dark border">Cash</span> <span class="text-success small fw-semibold">Paid</span></td>
                                    <td><span class="badge bg-info-subtle text-info">Processing</span></td>
                                    <td class="text-end pe-4">
                                        <button class="btn btn-sm btn-outline-success" onclick="alert('Order KSK-2026-00341: Processing & Quality checking in progress.')"><i class="bi bi-truck me-1"></i> Track</button>
                                    </td>
                                </tr>
                                <tr>
                                    <td class="ps-4 fw-bold text-dark">KSK-2026-00340</td>
                                    <td>20 Aug 2026</td>
                                    <td>Manual Farming Tool (1 Unit)</td>
                                    <td class="fw-bold text-success">₹1,200.00</td>
                                    <td><span class="badge bg-light text-dark border">UPI</span> <span class="text-success small fw-semibold">Paid</span></td>
                                    <td><span class="badge bg-primary-subtle text-primary">Delivered</span></td>
                                    <td class="text-end pe-4">
                                        <button class="btn btn-sm btn-outline-primary" onclick="window.location.href='farmer-dashboard.html'"><i class="bi bi-file-earmark-pdf"></i> Bill</button>
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
    save_customer_page("farmer-orders.html", content)
    save_customer_page("orders.html", content)
    print("Generated dist/farmer-orders.html")

# ==============================================================================
# 4. FARMER UDHARI (CREDIT LEDGER)
# ==============================================================================
def build_farmer_udhari():
    sidebar = render_customer_sidebar("udhari")
    content = head_html("उधारी खाते", "Credit Ledger") + nav_html("dashboard") + f"""
<div class="container my-4" style="max-width: 1240px;">
    <div class="row g-4">
        <div class="col-lg-3 col-md-4">
            {sidebar}
        </div>
        <div class="col-lg-9 col-md-8">
            <!-- Header Balance Highlight Card -->
            <div class="farmer-balance-card mb-4">
                <div class="row align-items-center g-3">
                    <div class="col-md-7">
                        <div class="d-flex align-items-center gap-2 mb-2">
                            <span class="badge text-white px-3 py-1 rounded-pill fw-bold" style="background:#059669 !important;">
                                <i class="bi bi-check-circle-fill me-1"></i> उधारी निरंक (Nil Balance)
                            </span>
                        </div>
                        <h1 class="display-5 fw-bold m-0" style="color:#059669; font-weight:800;">₹0.00</h1>
                        <span class="fs-6 fw-semibold text-muted">चालू बाकी उधारी रक्कम (Current Outstanding Due)</span>
                        <div class="d-flex flex-wrap gap-2 mt-3">
                            <div class="bg-white px-3 py-2 rounded-3 border shadow-sm small"><span class="text-muted d-block" style="font-size:11px;">एकूण मर्यादा (Credit Limit):</span><strong>₹15,000.00</strong></div>
                            <div class="bg-white px-3 py-2 rounded-3 border shadow-sm small"><span class="text-muted d-block" style="font-size:11px;">उपलब्ध मर्यादा (Available):</span><strong class="text-success">₹15,000.00</strong></div>
                            <div class="bg-white px-3 py-2 rounded-3 border shadow-sm small"><span class="text-muted d-block" style="font-size:11px;">बाकी रक्कम (Due):</span><strong class="text-success">₹0.00</strong></div>
                        </div>
                    </div>
                    <div class="col-md-5 text-md-end">
                        <a href="farmer-pay.html" class="btn btn-success fw-bold px-4 py-2 rounded-3 shadow-sm mb-2 d-inline-block" style="background:#15803d;">
                            💳 Pay via UPI
                        </a>
                        <div>
                            <button class="btn btn-sm btn-outline-secondary" onclick="alert('Credit Ledger statement generated for farmer.')"><i class="bi bi-download me-1"></i> Download Passbook</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Ledger Table -->
            <div class="card border-0 shadow-sm rounded-4 bg-white overflow-hidden">
                <div class="card-header bg-white py-3 px-4 border-bottom">
                    <h6 class="fw-bold mb-0 text-dark"><i class="bi bi-clock-history me-2 text-success"></i>खातेवही व्यवहार इतिहास (Ledger Transactions)</h6>
                </div>
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-hover align-middle mb-0">
                            <thead class="table-light text-muted small">
                                <tr><th>तारीख</th><th>तपशील</th><th>नावे (Debit)</th><th>जमा (Credit)</th><th>शिल्लक (Balance)</th></tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>28 Aug 2026</td>
                                    <td>UPI द्वारे परतफेड (Ref: UPI/20260828/9982)</td>
                                    <td class="text-muted">-</td>
                                    <td class="text-success fw-bold">+₹2,450.00</td>
                                    <td class="fw-bold text-success">₹0.00</td>
                                </tr>
                                <tr>
                                    <td>28 Aug 2026</td>
                                    <td>खरेदी पावती #KSK-2026-00342 (NPK खत)</td>
                                    <td class="text-danger fw-bold">₹2,450.00</td>
                                    <td class="text-muted">-</td>
                                    <td class="fw-bold text-danger">₹2,450.00</td>
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
    save_customer_page("farmer-udhari.html", content)
    print("Generated dist/farmer-udhari.html")

# ==============================================================================
# 5. FARMER PAY (UPI PAYMENT)
# ==============================================================================
def build_farmer_pay():
    sidebar = render_customer_sidebar("pay")
    content = head_html("पेमेंट करा", "Pay Now - UPI Payment") + nav_html("dashboard") + f"""
<div class="container my-4" style="max-width: 1240px;">
    <div class="row g-4">
        <div class="col-lg-3 col-md-4">
            {sidebar}
        </div>
        <div class="col-lg-9 col-md-8">
            <div class="d-flex align-items-center gap-3 mb-4">
                <div style="width:50px;height:50px;background:linear-gradient(135deg,#16a34a,#15803d);border-radius:14px;display:flex;align-items:center;justify-content:center;">
                    <i class="bi bi-qr-code text-white fs-4"></i>
                </div>
                <div>
                    <h4 class="fw-bold text-dark mb-0">UPI Payment</h4>
                    <small class="text-muted">सप्तशृंगी ॲग्रो सर्व्हिसेस ला थेट पेमेंट करा</small>
                </div>
            </div>

            <div class="row g-4">
                <!-- QR Box -->
                <div class="col-md-6">
                    <div class="card border-0 shadow-sm rounded-4 text-center p-4 h-100" style="background:#f0fdf4; border:1.5px solid #bbf7d0 !important;">
                        <span class="badge mb-3 px-3 py-2 rounded-pill fw-bold align-self-center" style="background:#16a34a;color:white;">📱 QR Code Scan करा</span>
                        <div class="bg-white p-3 rounded-4 shadow-sm d-inline-block mx-auto mb-3">
                            <img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=upi://pay?pa=8600813827@upi%26pn=Saptashrungi%20Agro%20Services" alt="UPI QR Code" class="img-fluid" style="width:190px;height:190px;">
                        </div>
                        <h6 class="fw-bold text-dark mb-1">सप्तशृंगी ॲग्रो सर्व्हिसेस</h6>
                        <p class="small text-muted mb-2">UPI ID: <strong class="text-success">8600813827@upi</strong></p>
                        <p class="small text-muted">Google Pay, PhonePe, Paytm किंवा BHIM द्वारे स्कॅन करून पैसे भरा.</p>
                    </div>
                </div>

                <!-- Payment Details Form -->
                <div class="col-md-6">
                    <div class="card border-0 shadow-sm rounded-4 p-4 bg-white h-100">
                        <h5 class="fw-bold text-dark mb-3">पेमेंट तपशील भरा</h5>
                        <form onsubmit="alert('पेमेंट पडताळणी पूर्ण झाली! पावती लवकरच अपडेट होईल.'); return false;">
                            <div class="mb-3">
                                <label class="form-label small fw-bold text-success">शेतकरी नाव</label>
                                <input type="text" class="form-control" id="payFarmerName" value="VSGAWALI" readonly>
                            </div>
                            <div class="mb-3">
                                <label class="form-label small fw-bold text-success">रक्कम (₹)</label>
                                <input type="number" class="form-control form-control-lg fw-bold text-success" value="1000" min="10" required>
                            </div>
                            <div class="mb-3">
                                <label class="form-label small fw-bold text-success">UPI Transaction ID / Ref #</label>
                                <input type="text" class="form-control" placeholder="उदा. 423456789012" required>
                            </div>
                            <button type="submit" class="btn btn-success fw-bold w-100 py-2 rounded-3 shadow-sm" style="background:#15803d;">
                                <i class="bi bi-check2-circle me-1"></i> पेमेंट नोंदवा (Submit Receipt)
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function(){{
    var saved = localStorage.getItem('user_name');
    var el = document.getElementById('payFarmerName');
    if (saved && el) el.value = saved;
}});
</script>
""" + foot_html()
    save_customer_page("farmer-pay.html", content)
    print("Generated dist/farmer-pay.html")

# ==============================================================================
# 6. FARMER PAYMENTS (PAYMENT HISTORY)
# ==============================================================================
def build_farmer_payments():
    sidebar = render_customer_sidebar("payments")
    content = head_html("जमा पावत्या", "Payment History") + nav_html("dashboard") + f"""
<div class="container my-4" style="max-width: 1240px;">
    <div class="row g-4">
        <div class="col-lg-3 col-md-4">
            {sidebar}
        </div>
        <div class="col-lg-9 col-md-8">
            <div class="card border-0 shadow-sm rounded-4 bg-white overflow-hidden">
                <div class="card-header bg-white py-3 px-4 border-bottom">
                    <h5 class="mb-0 fw-bold text-success"><i class="bi bi-receipt-cutoff me-2"></i>My Payment Receipts / जमा पावत्या</h5>
                </div>
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-hover align-middle mb-0">
                            <thead class="table-light text-muted small">
                                <tr>
                                    <th class="ps-4">Receipt #</th>
                                    <th>Date</th>
                                    <th>Amount</th>
                                    <th>Method</th>
                                    <th>Transaction Ref</th>
                                    <th class="text-end pe-4">Action</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="ps-4 fw-bold text-dark">RCP-2026-0045</td>
                                    <td>28 Aug 2026</td>
                                    <td class="fw-bold text-success">₹2,450.00</td>
                                    <td><span class="badge bg-light text-dark border">UPI</span></td>
                                    <td>UPI/20260828/9982</td>
                                    <td class="text-end pe-4">
                                        <button class="btn btn-sm btn-outline-success" onclick="alert('Receipt RCP-2026-0045 downloaded.')"><i class="bi bi-download"></i> Receipt</button>
                                    </td>
                                </tr>
                                <tr>
                                    <td class="ps-4 fw-bold text-dark">RCP-2026-0038</td>
                                    <td>15 Jul 2026</td>
                                    <td class="fw-bold text-success">₹1,500.00</td>
                                    <td><span class="badge bg-light text-dark border">Cash</span></td>
                                    <td>CASH-RCP-019</td>
                                    <td class="text-end pe-4">
                                        <button class="btn btn-sm btn-outline-success" onclick="alert('Receipt RCP-2026-0038 downloaded.')"><i class="bi bi-download"></i> Receipt</button>
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
    save_customer_page("farmer-payments.html", content)
    print("Generated dist/farmer-payments.html")

# ==============================================================================
# 7. FARMER NOTIFICATIONS
# ==============================================================================
def build_farmer_notifications():
    sidebar = render_customer_sidebar("notifications")
    content = head_html("सूचना व अलर्ट", "Notifications") + nav_html("dashboard") + f"""
<div class="container my-4" style="max-width: 1240px;">
    <div class="row g-4">
        <div class="col-lg-3 col-md-4">
            {sidebar}
        </div>
        <div class="col-lg-9 col-md-8">
            <div class="card border-0 shadow-sm rounded-4 bg-white overflow-hidden">
                <div class="card-header bg-white py-3 px-4 border-bottom d-flex justify-content-between align-items-center">
                    <h5 class="mb-0 fw-bold text-success"><i class="bi bi-bell-fill me-2"></i>My Notifications & Alerts / सूचना</h5>
                    <button class="btn btn-sm btn-outline-secondary" onclick="alert('All marked as read')">Mark All as Read</button>
                </div>
                <div class="card-body p-4">
                    <div class="d-flex flex-column gap-3">
                        <div class="p-3 rounded-4 border d-flex gap-3 align-items-start" style="background:#f0fdf4; border-color:#bbf7d0 !important;">
                            <i class="bi bi-check-circle-fill text-success fs-4"></i>
                            <div>
                                <h6 class="fw-bold mb-1 text-dark">Order Ready for Delivery (KSK-2026-00342)</h6>
                                <p class="small text-muted mb-1">आपले NPK खत 50kg पॅक तयार आहे. दुकानातून घेऊन जाऊ शकता किंवा डिलिव्हरीची वाट पाहा.</p>
                                <small class="text-muted">28 Aug 2026, 11:30 AM</small>
                            </div>
                        </div>

                        <div class="p-3 rounded-4 border d-flex gap-3 align-items-start" style="background:#fffbeb; border-color:#fde68a !important;">
                            <i class="bi bi-cloud-sun-fill text-warning fs-4"></i>
                            <div>
                                <h6 class="fw-bold mb-1 text-dark">हवामान सल्ला: पुढील ४८ तासांत पावसाची शक्यता</h6>
                                <p class="small text-muted mb-1">वैजापूर व परिसरात हलक्या पावसाची शक्यता असल्याने फवारणी करताना काळजी घ्या.</p>
                                <small class="text-muted">27 Aug 2026, 08:00 AM</small>
                            </div>
                        </div>

                        <div class="p-3 rounded-4 border d-flex gap-3 align-items-start bg-light">
                            <i class="bi bi-info-circle-fill text-primary fs-4"></i>
                            <div>
                                <h6 class="fw-bold mb-1 text-dark">नवीन कापूस बियाणे स्टॉक उपलब्ध!</h6>
                                <p class="small text-muted mb-1">माहिको आणि अंकुर कापूस बियाण्यांचा ताजा साठा सप्तशृंगी ॲग्रो, मिरखनगर येथे उपलब्ध झाला आहे.</p>
                                <small class="text-muted">20 Aug 2026, 04:15 PM</small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
""" + foot_html()
    save_customer_page("farmer-notifications.html", content)
    print("Generated dist/farmer-notifications.html")

def build_all_customer_pages():
    build_farmer_dashboard()
    build_farmer_profile()
    build_farmer_orders()
    build_farmer_udhari()
    build_farmer_pay()
    build_farmer_payments()
    build_farmer_notifications()
    print("All Customer / Farmer Panel pages built successfully!")

if __name__ == "__main__":
    build_all_customer_pages()
