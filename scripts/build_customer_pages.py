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
    with rock-solid inline styling and brand classes.
    """
    def is_act(tab):
        return active_tab == tab

    def nav_style(tab):
        if is_act(tab):
            return "display: flex !important; align-items: center !important; gap: 12px !important; padding: 11px 16px !important; border-radius: 14px !important; color: #ffffff !important; text-decoration: none !important; font-weight: 700 !important; font-size: 13.5px !important; background: linear-gradient(135deg, #16a34a 0%, #15803d 100%) !important; box-shadow: 0 6px 18px rgba(22, 163, 74, 0.4) !important;"
        return "display: flex !important; align-items: center !important; gap: 12px !important; padding: 11px 16px !important; border-radius: 14px !important; color: #cbd5e1 !important; text-decoration: none !important; font-weight: 600 !important; font-size: 13.5px !important; transition: all 0.2s ease !important;"

    def act_cls(tab):
        return "customer-sidebar-item active" if is_act(tab) else "customer-sidebar-item"

    return f"""
<div class="customer-sidebar-shell mb-4" style="background: linear-gradient(180deg, #091f14 0%, #0d281a 100%) !important; border: 1px solid rgba(255, 255, 255, 0.08) !important; border-radius: 22px !important; padding: 26px 16px !important; box-shadow: 0 14px 36px -4px rgba(0, 0, 0, 0.22) !important;">
    <!-- User Profile Header (Screenshot 1) -->
    <div class="customer-sidebar-user text-center pb-3 mb-3" style="border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;">
        <div class="customer-avatar-circle mx-auto mb-2" style="width: 66px !important; height: 66px !important; border-radius: 50% !important; background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important; color: #ffffff !important; display: flex !important; align-items: center !important; justify-content: center !important; font-size: 28px !important; margin: 0 auto 10px !important; box-shadow: 0 6px 18px rgba(16, 185, 129, 0.4) !important; border: 3px solid rgba(255, 255, 255, 0.2) !important;">
            <i class="bi bi-person-fill"></i>
        </div>
        <h6 class="mb-1 fw-bold text-white text-uppercase" id="sidebarUserDisplayName" style="letter-spacing: 0.6px; font-size: 15px;">Vaibhav Gawali</h6>
        <small class="text-secondary small text-uppercase d-block" id="sidebarUserDisplayLoc" style="font-size: 11px; letter-spacing: 0.5px; color: #94a3b8 !important;">TAMASWADI, छत्रपती संभाजीनगर</small>
    </div>

    <!-- Section: FARMER MENU -->
    <div class="customer-sidebar-title" style="color: #86efac !important; font-size: 11px !important; font-weight: 800 !important; text-transform: uppercase !important; letter-spacing: 1.2px !important; padding: 8px 14px 6px !important; display: block !important;">
        <span class="lang-mr">शेतकरी मेनू</span>
        <span class="lang-en">FARMER MENU</span>
    </div>
    <nav class="customer-sidebar-nav" style="display: flex !important; flex-direction: column !important; gap: 4px !important; margin-bottom: 14px !important;">
        <a href="farmer-dashboard.html" class="{act_cls('dashboard')}" style="{nav_style('dashboard')}">
            <i class="bi bi-grid-fill fs-5" style="width: 22px; text-align: center;"></i>
            <span class="lang-mr">डॅशबोर्ड</span>
            <span class="lang-en">Dashboard</span>
        </a>
        <a href="farmer-orders.html" class="{act_cls('orders')}" style="{nav_style('orders')}">
            <i class="bi bi-bag-fill fs-5" style="width: 22px; text-align: center;"></i>
            <span class="lang-mr">माझ्या ऑर्डर्स</span>
            <span class="lang-en">My Orders</span>
        </a>
        <a href="farmer-udhari.html" class="{act_cls('udhari')}" style="{nav_style('udhari')}">
            <i class="bi bi-credit-card-2-front-fill fs-5" style="width: 22px; text-align: center;"></i>
            <span class="lang-mr">उधारी खातेवही</span>
            <span class="lang-en">My Credit Ledger</span>
        </a>
        <a href="farmer-pay.html" class="{act_cls('pay')}" style="{nav_style('pay')}">
            <i class="bi bi-qr-code-scan fs-5" style="width: 22px; text-align: center;"></i>
            <span class="lang-mr">💳 Pay Now (UPI)</span>
            <span class="lang-en">💳 Pay Now (UPI)</span>
        </a>
        <a href="farmer-payments.html" class="{act_cls('payments')}" style="{nav_style('payments')}">
            <i class="bi bi-receipt-cutoff fs-5" style="width: 22px; text-align: center;"></i>
            <span class="lang-mr">जमा पावत्या</span>
            <span class="lang-en">Payment History</span>
        </a>
        <a href="farmer-notifications.html" class="{act_cls('notifications')}" style="{nav_style('notifications')}">
            <i class="bi bi-bell-fill fs-5" style="width: 22px; text-align: center;"></i>
            <span class="lang-mr">सूचना व अलर्ट</span>
            <span class="lang-en">Notifications</span>
        </a>
        <a href="farmer-profile.html" class="{act_cls('profile')}" style="{nav_style('profile')}">
            <i class="bi bi-person-lines-fill fs-5" style="width: 22px; text-align: center;"></i>
            <span class="lang-mr">माझी माहिती / प्रोफाइल</span>
            <span class="lang-en">Profile</span>
        </a>
    </nav>

    <!-- Section: AGRI TOOLS -->
    <div class="customer-sidebar-title" style="color: #86efac !important; font-size: 11px !important; font-weight: 800 !important; text-transform: uppercase !important; letter-spacing: 1.2px !important; padding: 10px 14px 6px !important; display: block !important;">
        <span class="lang-mr">कृषी साधने</span>
        <span class="lang-en">AGRI TOOLS</span>
    </div>
    <nav class="customer-sidebar-nav" style="display: flex !important; flex-direction: column !important; gap: 4px !important; margin-bottom: 14px !important;">
        <a href="weather.html" class="customer-sidebar-item" style="{nav_style('weather')}">
            <i class="bi bi-cloud-sun-fill text-info fs-5" style="width: 22px; text-align: center;"></i>
            <span class="lang-mr">हवामान अंदाज</span>
            <span class="lang-en">Agri Weather</span>
        </a>
        <a href="farming-tips.html" class="customer-sidebar-item" style="{nav_style('tips')}">
            <i class="bi bi-journal-check text-warning fs-5" style="width: 22px; text-align: center;"></i>
            <span class="lang-mr">पीक सल्ला</span>
            <span class="lang-en">Crop Tips</span>
        </a>
    </nav>

    <!-- Logout Action -->
    <button type="button" onclick="handleLogout()" class="customer-sidebar-logout" style="width: 100% !important; background: rgba(239, 68, 68, 0.12) !important; color: #ef4444 !important; border: 1px solid rgba(239, 68, 68, 0.25) !important; border-radius: 12px !important; padding: 11px 16px !important; font-weight: 700 !important; font-size: 13.5px !important; display: flex !important; align-items: center !important; justify-content: center !important; gap: 8px !important; cursor: pointer !important; margin-top: 14px !important; transition: all 0.2s ease !important;">
        <i class="bi bi-box-arrow-right fs-5"></i>
        <span><span class="lang-mr">बाहेर पडा (Logout)</span><span class="lang-en">Logout</span></span>
    </button>
</div>
<script>
(function(){{
    var name = localStorage.getItem('user_name') || 'Vaibhav Gawali';
    var loc = localStorage.getItem('user_location') || 'TAMASWADI, छत्रपती संभाजीनगर';
    var elSideName = document.getElementById('sidebarUserDisplayName');
    var elSideLoc = document.getElementById('sidebarUserDisplayLoc');
    var elGreet = document.getElementById('farmerGreetName');
    if (elSideName) elSideName.textContent = name;
    if (elSideLoc) elSideLoc.textContent = loc;
    if (elGreet) elGreet.textContent = name;
}})();
</script>
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
    sidebar = render_customer_sidebar("dashboard")
    raw_dashboard = """
<div class="farmer-dashboard-wrapper py-4" style="background:#f6f9f6; min-height:88vh;">
    <div class="container my-2" style="max-width: 1320px;">
        <div class="row g-4">
            <!-- Left Dark Emerald Sidebar (Screenshot 1) -->
            <div class="col-lg-3 col-md-4">
                <!-- SIDEBAR_PLACEHOLDER -->
            </div>

            <!-- Right Workspace (Screenshot 2) -->
            <div class="col-lg-9 col-md-8">
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

        <!-- 2. Quick Stats: 2 KPI Cards (Brand Redesign) -->
        <div class="row g-3 mb-4">
            <!-- 1. PENDING DUE -->
            <div class="col-sm-6">
                <div class="farmer-stat-card h-100 d-flex flex-column justify-content-between" style="border-left: 5px solid #ea580c !important;">
                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <span class="badge bg-light text-muted border px-2 py-1 small fw-bold text-uppercase" style="letter-spacing: 0.6px; font-size: 11px;">
                            <span class="lang-mr">बाकी उधारी</span>
                            <span class="lang-en">PENDING DUE</span>
                        </span>
                        <div class="stat-icon-wrapper" style="background:#fff7ed; color:#ea580c;">
                            <i class="bi bi-wallet2"></i>
                        </div>
                    </div>
                    <div>
                        <div class="stat-amount text-danger mb-1">₹0.00</div>
                        <div>
                            <span class="stat-pill" style="background:#ecfdf5; color:#059669;">
                                <i class="bi bi-check-circle-fill"></i>
                                <span class="lang-mr">उधारी निरंक</span>
                                <span class="lang-en">Nil Balance</span>
                            </span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 2. TOTAL PURCHASES -->
            <div class="col-sm-6">
                <div class="farmer-stat-card h-100 d-flex flex-column justify-content-between" style="border-left: 5px solid #0284c7 !important;">
                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <span class="badge bg-light text-muted border px-2 py-1 small fw-bold text-uppercase" style="letter-spacing: 0.6px; font-size: 11px;">
                            <span class="lang-mr">एकूण खरेदी</span>
                            <span class="lang-en">TOTAL PURCHASES</span>
                        </span>
                        <div class="stat-icon-wrapper" style="background:#f0f9ff; color:#0284c7;">
                            <i class="bi bi-bag-check-fill"></i>
                        </div>
                    </div>
                    <div>
                        <div class="stat-amount text-primary mb-1">₹0.00</div>
                        <div>
                            <span class="stat-pill" style="background:#f0f9ff; color:#0284c7;">
                                <i class="bi bi-calendar-check"></i>
                                <span class="lang-mr">चालू महिना खरेदी: ₹0</span>
                                <span class="lang-en">This Month: ₹0</span>
                            </span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- 3. Main Workspace: Two Columns (Left ~65%, Right ~35%) -->
        <div class="row g-4">
            <!-- Left Column: Recent Orders & Reviews -->
            <div class="col-lg-8">
                <!-- Recent Orders Card (Screenshot 2 / User Request: Empty State) -->
                <div class="card farmer-card mb-4">
                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <h5 class="fw-bold text-dark m-0">
                            <span class="lang-mr">अलीकडील ऑर्डर्स</span>
                            <span class="lang-en">Recent Orders</span>
                        </h5>
                        <a href="products.html" class="text-primary small fw-semibold text-decoration-none d-flex align-items-center gap-1">
                            <span class="lang-mr">उत्पादने पाहा</span>
                            <span class="lang-en">Browse Products</span> &rarr;
                        </a>
                    </div>

                    <!-- Clean Empty Orders State matching user request -->
                    <div class="text-center py-4 my-2">
                        <div class="mb-3">
                            <div class="d-inline-flex align-items-center justify-content-center rounded-circle shadow-sm" style="width: 76px; height: 76px; background: #f0fdf4; border: 2px dashed #86efac;">
                                <i class="bi bi-bag-x text-success" style="font-size: 2.2rem;"></i>
                            </div>
                        </div>
                        <h6 class="fw-bold text-dark mb-1">
                            <span class="lang-mr">सध्या कोणतीही चालू ऑर्डर नाही</span>
                            <span class="lang-en">No Recent Orders</span>
                        </h6>
                        <p class="text-muted small mb-3" style="max-width: 380px; margin: 0 auto; line-height: 1.5;">
                            <span class="lang-mr">आपण अद्याप कोणतीही नवीन ऑर्डर केलेली नाही. उच्च दर्जाची प्रमाणित बियाणे, खते व शेती अवजारे खरेदी करण्यासाठी खालील बटणावर क्लिक करा.</span>
                            <span class="lang-en">You haven't placed any orders recently. Explore our certified seeds, fertilizers, and farming tools.</span>
                        </p>
                        <a href="products.html" class="btn btn-success fw-bold px-4 py-2 rounded-3 text-white shadow-sm d-inline-flex align-items-center gap-2" style="background: #16a34a; border: none;">
                            <i class="bi bi-cart-plus"></i>
                            <span class="lang-mr">उत्पादने खरेदी करा</span>
                            <span class="lang-en">Start Shopping</span>
                        </a>
                    </div>
                </div>

                <!-- Farmer Reviews & Ratings Card (User Request: Read other reviews & Submit own review) -->
                <div class="card farmer-card mb-4">
                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <h5 class="fw-bold text-dark m-0 d-flex align-items-center gap-2">
                            <span class="text-warning">⭐</span>
                            <span class="lang-mr">शेतकरी अभिप्राय आणि रेटिंग</span>
                            <span class="lang-en">Farmer Reviews & Ratings</span>
                        </h5>
                        <button type="button" onclick="openReadReviewsModal()" class="btn btn-link text-primary small fw-semibold text-decoration-none p-0 d-flex align-items-center gap-1">
                            <span class="lang-mr">सर्व पाहा</span>
                            <span class="lang-en">View All</span> &rarr;
                        </button>
                    </div>

                    <div class="p-3 rounded-4 mb-3" style="background:#f0fdf4; border: 1px solid #bbf7d0;">
                        <div class="d-flex justify-content-between align-items-center mb-2">
                            <span class="badge px-3 py-1 rounded-pill fw-bold text-white" id="dashReviewsAvgBadge" style="background:#15803d !important;">
                                4.9 / 5.0 ⭐
                            </span>
                            <span class="text-muted small fw-semibold" id="dashReviewsCountBadge">500+ Farmers</span>
                        </div>
                        <p class="small text-muted mb-0">
                            <span class="lang-mr">इतर शेतकऱ्यांचे अनुभव वाचा किंवा आपण स्वतः खरेदी केलेल्या उत्पादनाचा अभिप्राय व रेटिंग नोंदवा.</span>
                            <span class="lang-en">Read verified experiences from other farmers or share your valuable feedback and rating.</span>
                        </p>
                    </div>

                    <div class="d-flex gap-2 flex-wrap">
                        <button type="button" onclick="openReadReviewsModal()" class="btn btn-outline-success rounded-3 fw-bold px-3 py-2 d-flex align-items-center gap-2">
                            <i class="bi bi-chat-left-text"></i>
                            <span class="lang-mr">इतर शेतकऱ्यांचे अभिप्राय वाचा</span>
                            <span class="lang-en">Read Other Reviews</span>
                        </button>
                        <button type="button" onclick="openSubmitReviewModal()" class="btn btn-success rounded-3 fw-bold px-3 py-2 text-white d-flex align-items-center gap-2" style="background:#16a34a; border-color:#16a34a;">
                            <i class="bi bi-pencil-square"></i>
                            <span class="lang-mr">अभिप्राय द्या (Give Review)</span>
                            <span class="lang-en">Write a Review</span>
                        </button>
                    </div>
                </div>
            </div>

            <!-- Right Column: Quick Actions, Due Alert, Daily Tip -->
            <div class="col-lg-4">
                <!-- Quick Actions 2x2 Grid (Screenshot 2) -->
                <div class="card farmer-card mb-4">
                    <h6 class="fw-bold text-dark mb-3 px-1">
                        <span class="lang-mr">⚡ झटपट कृती</span>
                        <span class="lang-en">⚡ Quick Actions</span>
                    </h6>
                    <div class="row g-2">
                        <!-- 1. Shopping -->
                        <div class="col-6">
                            <a href="products.html" class="farmer-quick-btn" style="background: #f0fdf4; border-color: #bbf7d0; color: #15803d;">
                                <div class="btn-icon-bubble" style="background: #dcfce7; color: #15803d;">
                                    <i class="bi bi-cart-check"></i>
                                </div>
                                <span class="lang-mr">खरेदी</span>
                                <span class="lang-en">Shopping</span>
                            </a>
                        </div>
                        <!-- 2. Invoices -->
                        <div class="col-6">
                            <a href="farmer-orders.html" class="farmer-quick-btn" style="background: #f8fafc; border-color: #e2e8f0; color: #334155;">
                                <div class="btn-icon-bubble" style="background: #e2e8f0; color: #334155;">
                                    <i class="bi bi-file-earmark-text"></i>
                                </div>
                                <span class="lang-mr">पावत्या</span>
                                <span class="lang-en">Invoices</span>
                            </a>
                        </div>
                        <!-- 3. Alerts -->
                        <div class="col-6">
                            <a href="farmer-notifications.html" class="farmer-quick-btn" style="background: #fffbeb; border-color: #fde68a; color: #b45309;">
                                <div class="btn-icon-bubble" style="background: #fef3c7; color: #b45309;">
                                    <i class="bi bi-bell"></i>
                                </div>
                                <span class="lang-mr">अलर्ट्स</span>
                                <span class="lang-en">Alerts</span>
                            </a>
                        </div>
                        <!-- 4. Contact -->
                        <div class="col-6">
                            <a href="javascript:void(0)" onclick="openStoreContactModal()" class="farmer-quick-btn" style="background: #faf5ff; border-color: #e9d5ff; color: #7c3aed;">
                                <div class="btn-icon-bubble" style="background: #f3e8ff; color: #7c3aed;">
                                    <i class="bi bi-telephone"></i>
                                </div>
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
            </div><!-- end right workspace -->
        </div><!-- end row -->
    </div><!-- end container -->
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


<!-- 6. Read Farmer Reviews Modal (User Request: Read other farmers' reviews) -->
<div class="modal fade" id="readFarmerReviewsModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered modal-dialog-scrollable">
        <div class="modal-content border-0 shadow-lg rounded-4">
            <div class="modal-header border-0 pb-0 d-flex justify-content-between align-items-center">
                <div>
                    <h5 class="modal-title fw-bold text-success d-flex align-items-center gap-2">
                        <i class="bi bi-star-fill text-warning"></i>
                        <span class="lang-mr">इतर शेतकऱ्यांचे अभिप्राय व रेटिंग्ज</span>
                        <span class="lang-en">Verified Farmer Reviews & Ratings</span>
                    </h5>
                    <small class="text-muted">सप्तशृंगी ॲग्रो सर्व्हिसेस, मिरखनगर येथील शेतकऱ्यांचे प्रत्यक्ष अनुभव</small>
                </div>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body p-4">
                <!-- Summary bar -->
                <div class="d-flex align-items-center justify-content-between p-3 rounded-4 mb-4" style="background:#f0fdf4; border:1px solid #bbf7d0;">
                    <div class="d-flex align-items-center gap-3">
                        <div class="display-6 fw-bold text-success mb-0" id="modalReviewsAvgScore">4.9</div>
                        <div>
                            <div class="text-warning fs-5">⭐⭐⭐⭐⭐</div>
                            <small class="text-muted"><span id="modalReviewsTotalCount">5</span> शेतकऱ्यांचे अभिप्राय (Verified)</small>
                        </div>
                    </div>
                    <button type="button" class="btn btn-sm btn-success rounded-pill px-3 fw-bold" onclick="switchToSubmitReview()" style="background:#16a34a;">
                        <i class="bi bi-pencil-square me-1"></i> आपला अभिप्राय द्या
                    </button>
                </div>

                <!-- Reviews Feed List -->
                <div id="farmerReviewsFeedList" class="d-flex flex-column gap-3">
                    <!-- Populated dynamically via JS -->
                </div>
            </div>
            <div class="modal-footer border-0 pt-0">
                <button type="button" class="btn btn-light rounded-pill px-4" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-success rounded-pill px-4 fw-bold" onclick="switchToSubmitReview()" style="background:#16a34a;">
                    <i class="bi bi-star me-1"></i> अभिप्राय नोंदवा (Write Review)
                </button>
            </div>
        </div>
    </div>
</div>

<!-- 7. Submit Farmer Review & Rating Modal (User Request: Farmer review & rating karta aali pahije) -->
<div class="modal fade" id="submitFarmerReviewModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content border-0 shadow-lg rounded-4">
            <div class="modal-header border-0 pb-0">
                <h5 class="modal-title fw-bold text-success d-flex align-items-center gap-2">
                    <i class="bi bi-pencil-fill"></i>
                    <span class="lang-mr">आपला अभिप्राय व रेटिंग नोंदवा</span>
                    <span class="lang-en">Submit Your Review & Rating</span>
                </h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body p-4">
                <div id="reviewSuccessMsg" class="alert alert-success d-none py-2 mb-3 small">
                    <i class="bi bi-check-circle-fill me-1"></i>
                    <span class="lang-mr">धन्यवाद! आपला अभिप्राय यशस्वीरित्या नोंदवला गेला आहे.</span>
                    <span class="lang-en">Thank you! Your review has been submitted successfully.</span>
                </div>

                <form id="farmerReviewForm" onsubmit="return handleFarmerReviewSubmit(event)">
                    <!-- Star Rating Interactive Picker -->
                    <div class="mb-3 text-center p-3 rounded-4 bg-light border">
                        <label class="form-label small fw-bold text-dark d-block mb-1">रेटिंग निवडा (Select Stars) *</label>
                        <div class="d-flex justify-content-center gap-2 fs-2 text-warning" id="starPickerContainer" style="cursor: pointer;">
                            <i class="bi bi-star-fill star-item" data-value="1" onclick="selectStarRating(1)"></i>
                            <i class="bi bi-star-fill star-item" data-value="2" onclick="selectStarRating(2)"></i>
                            <i class="bi bi-star-fill star-item" data-value="3" onclick="selectStarRating(3)"></i>
                            <i class="bi bi-star-fill star-item" data-value="4" onclick="selectStarRating(4)"></i>
                            <i class="bi bi-star-fill star-item" data-value="5" onclick="selectStarRating(5)"></i>
                        </div>
                        <input type="hidden" id="selectedStarValue" value="5">
                        <small class="text-success fw-bold d-block mt-1" id="starRatingDesc">५ स्टार - उत्कृष्ट सेवा व उत्पादने (Excellent)</small>
                    </div>

                    <div class="row g-2 mb-3">
                        <div class="col-sm-6">
                            <label class="form-label small fw-bold text-success">शेतकरी नाव *</label>
                            <input type="text" id="revFarmerName" class="form-control" required value="VSGAWALI">
                        </div>
                        <div class="col-sm-6">
                            <label class="form-label small fw-bold text-success">गाव / तालुका *</label>
                            <input type="text" id="revFarmerLoc" class="form-control" required value="कोपरगाव, अहिल्यानगर">
                        </div>
                    </div>

                    <div class="mb-3">
                        <label class="form-label small fw-bold text-success">खरेदी केलेले उत्पादन / विषय *</label>
                        <select id="revProduct" class="form-select" required>
                            <option value="NPK 19:19:19 खत (IFFCO)" selected>NPK 19:19:19 खत (IFFCO)</option>
                            <option value="महाबीज गहू बियाणे (लोक-१)">महाबीज गहू बियाणे (लोक-१)</option>
                            <option value="कापूस बियाणे (हायब्रीड)">कापूस बियाणे (हायब्रीड)</option>
                            <option value="सेंद्रिय कीटकनाशक व निंबोळी अर्क">सेंद्रिय कीटकनाशक व निंबोळी अर्क</option>
                            <option value="ठिबक सिंचन साहित्य व फिटिंग">ठिबक सिंचन साहित्य व फिटिंग</option>
                            <option value="शेती अवजारे (बॅटरी स्प्रेअर / विडर)">शेती अवजारे (बॅटरी स्प्रेअर / विडर)</option>
                            <option value="दुकान सेवा व कृषी सल्ला">दुकान सेवा व कृषी सल्ला</option>
                        </select>
                    </div>

                    <div class="mb-4">
                        <label class="form-label small fw-bold text-success">आपला अनुभव / अभिप्राय *</label>
                        <textarea id="revComment" class="form-control" rows="3" placeholder="उत्पादनाचा रिझल्ट कसा आला? सेवा कशी वाटली? सविस्तर लिहा..." required></textarea>
                    </div>

                    <button type="submit" class="btn btn-success fw-bold w-100 py-2 rounded-3 shadow-sm" style="background:#15803d; border:none;">
                        <i class="bi bi-star-fill me-1"></i>
                        <span class="lang-mr">अभिप्राय सबमिट करा</span>
                        <span class="lang-en">Submit Review</span>
                    </button>
                </form>
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

    updateDashboardReviewStats();
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

const DEFAULT_FARMER_REVIEWS = [
    {
        id: 1,
        name: "रामेश्वर पाटील",
        village: "वैजापूर, छत्रपती संभाजीनगर",
        product: "महाबीज गहू बियाणे (लोक-१)",
        rating: 5,
        date: "26 Oct 2026",
        comment: "सप्तशृंगी ॲग्रो कडून घेतलेले गहू बियाणे १००% उगवून आले. दर्जेदार बियाणे आणि रास्त भाव. दुकानदार योग्य सल्ला देतात.",
        verified: true
    },
    {
        id: 2,
        name: "सचिन गायकवाड",
        village: "कोपरगाव, अहिल्यानगर",
        product: "IFFCO NPK 19:19:19 खत",
        rating: 5,
        date: "20 Oct 2026",
        comment: "विद्राव्य खताचा रिझल्ट अतिशय चांगला आला. कांद्याची पात हिरवीगार झाली. वेळेवर माल मिळाला.",
        verified: true
    },
    {
        id: 3,
        name: "बाळासाहेब थोरात",
        village: "येवला, नाशिक",
        product: "ठिबक सिंचन फिल्टर व लॅटरल",
        rating: 5,
        date: "15 Oct 2026",
        comment: "ठिबकचे साहित्य योग्य किमतीत मिळाले. फिटिंगसाठी योग्य मार्गदर्शन केले. अतिशय प्रामाणिक सेवा.",
        verified: true
    },
    {
        id: 4,
        name: "ज्ञानेश्वर शिंदे",
        village: "धोंदलगाव, वैजापूर",
        product: "बॅटरी स्प्रेअर पंप (१६ लिटर)",
        rating: 4,
        date: "10 Oct 2026",
        comment: "बॅटरी पंप चांगला चालतो. एकदा चार्ज केल्यावर १५-२० टाक्या फवारणी होते. वॉरंटी पण दिली.",
        verified: true
    },
    {
        id: 5,
        name: "संजय कदम",
        village: "मिरखनगर, वैजापूर",
        product: "सेंद्रिय निंबोळी पेंड व खत",
        rating: 5,
        date: "04 Oct 2026",
        comment: "सेंद्रिय उत्पादने अस्सल आहेत. रासायनिक खतांचा खर्च कमी झाला. आमचे हक्काचे कृषी सेवा केंद्र!",
        verified: true
    }
];

function getStoredFarmerReviews() {
    const raw = localStorage.getItem('ksk_farmer_reviews');
    if (!raw) {
        localStorage.setItem('ksk_farmer_reviews', JSON.stringify(DEFAULT_FARMER_REVIEWS));
        return DEFAULT_FARMER_REVIEWS;
    }
    try {
        return JSON.parse(raw);
    } catch(e) {
        return DEFAULT_FARMER_REVIEWS;
    }
}

function updateDashboardReviewStats() {
    const reviews = getStoredFarmerReviews();
    const countBadge = document.getElementById('dashReviewsCountBadge');
    const avgBadge = document.getElementById('dashReviewsAvgBadge');
    if (countBadge) countBadge.textContent = (500 + reviews.length) + '+ Farmers';
    if (avgBadge && reviews.length > 0) {
        const sum = reviews.reduce((acc, r) => acc + (Number(r.rating) || 5), 0);
        avgBadge.textContent = (sum / reviews.length).toFixed(1) + ' / 5.0 ⭐';
    }
}

function openReadReviewsModal() {
    renderReviewsFeed();
    const modalEl = document.getElementById('readFarmerReviewsModal');
    if (modalEl && typeof bootstrap !== 'undefined') {
        const m = new bootstrap.Modal(modalEl);
        m.show();
    }
}

function openSubmitReviewModal() {
    // Pre-fill user name and village
    const savedName = localStorage.getItem('user_name') || 'VSGAWALI';
    const savedLoc = localStorage.getItem('user_location') || 'कोपरगाव, अहिल्यानगर';
    const nameEl = document.getElementById('revFarmerName');
    const locEl = document.getElementById('revFarmerLoc');
    if (nameEl) nameEl.value = savedName;
    if (locEl) locEl.value = savedLoc;

    selectStarRating(5);

    const modalEl = document.getElementById('submitFarmerReviewModal');
    if (modalEl && typeof bootstrap !== 'undefined') {
        const m = new bootstrap.Modal(modalEl);
        m.show();
    }
}

function switchToSubmitReview() {
    const readModalEl = document.getElementById('readFarmerReviewsModal');
    if (readModalEl) {
        const modalInstance = bootstrap.Modal.getInstance(readModalEl);
        if (modalInstance) modalInstance.hide();
    }
    setTimeout(openSubmitReviewModal, 300);
}

function selectStarRating(val) {
    const input = document.getElementById('selectedStarValue');
    if (input) input.value = val;

    const stars = document.querySelectorAll('#starPickerContainer .star-item');
    stars.forEach(star => {
        const starVal = Number(star.getAttribute('data-value'));
        if (starVal <= val) {
            star.className = 'bi bi-star-fill star-item text-warning';
        } else {
            star.className = 'bi bi-star star-item text-muted';
        }
    });

    const descEl = document.getElementById('starRatingDesc');
    const descs = {
        1: '१ स्टार - असमाधानकारक (Poor)',
        2: '२ स्टार - साधारण (Fair)',
        3: '३ स्टार - बरे (Good)',
        4: '४ स्टार - खूप चांगले (Very Good)',
        5: '५ स्टार - उत्कृष्ट सेवा व उत्पादने (Excellent)'
    };
    if (descEl) descEl.textContent = descs[val] || '';
}

function renderReviewsFeed() {
    const reviews = getStoredFarmerReviews();
    const feed = document.getElementById('farmerReviewsFeedList');
    const avgScoreEl = document.getElementById('modalReviewsAvgScore');
    const totalCountEl = document.getElementById('modalReviewsTotalCount');

    if (totalCountEl) totalCountEl.textContent = reviews.length;
    if (avgScoreEl && reviews.length > 0) {
        const sum = reviews.reduce((acc, r) => acc + (Number(r.rating) || 5), 0);
        avgScoreEl.textContent = (sum / reviews.length).toFixed(1);
    }

    if (!feed) return;

    feed.innerHTML = reviews.map(r => {
        let stars = '';
        for (let i = 1; i <= 5; i++) {
            stars += (i <= r.rating) ? '⭐' : '☆';
        }

        return `
            <div class="p-3 rounded-4 bg-white border shadow-sm">
                <div class="d-flex justify-content-between align-items-start mb-2">
                    <div class="d-flex align-items-center gap-2">
                        <div class="rounded-circle bg-success-subtle text-success fw-bold d-flex align-items-center justify-content-center" style="width: 40px; height: 40px; font-size: 1.1rem;">
                            🌾
                        </div>
                        <div>
                            <h6 class="mb-0 fw-bold text-dark">${r.name}</h6>
                            <small class="text-muted"><i class="bi bi-geo-alt-fill text-danger me-1"></i>${r.village || 'महाराष्ट्र'}</small>
                        </div>
                    </div>
                    <div class="text-end">
                        <span class="badge bg-success-subtle text-success border border-success-subtle px-2 py-1 rounded-pill small">
                            <i class="bi bi-patch-check-fill me-1"></i>Verified Farmer
                        </span>
                        <small class="text-muted d-block mt-1">${r.date || 'Recent'}</small>
                    </div>
                </div>

                <div class="mb-2">
                    <span class="text-warning fs-6">${stars}</span>
                    <span class="badge bg-light text-dark border ms-2">${r.product || 'कृषी सेवा'}</span>
                </div>

                <p class="small text-dark mb-0" style="line-height: 1.55;">
                    "${r.comment}"
                </p>
            </div>
        `;
    }).join('');
}

function handleFarmerReviewSubmit(e) {
    if (e && e.preventDefault) e.preventDefault();

    const name = document.getElementById('revFarmerName').value.trim();
    const village = document.getElementById('revFarmerLoc').value.trim();
    const product = document.getElementById('revProduct').value;
    const rating = Number(document.getElementById('selectedStarValue').value) || 5;
    const comment = document.getElementById('revComment').value.trim();

    if (!comment) {
        alert('कृपया आपला अभिप्राय लिहा!');
        return false;
    }

    const now = new Date();
    const dateStr = now.getDate() + ' ' + now.toLocaleString('en-US', { month: 'short' }) + ' ' + now.getFullYear();

    const newRev = {
        id: Date.now(),
        name: name,
        village: village,
        product: product,
        rating: rating,
        date: dateStr,
        comment: comment,
        verified: true
    };

    let reviews = getStoredFarmerReviews();
    reviews.unshift(newRev);
    localStorage.setItem('ksk_farmer_reviews', JSON.stringify(reviews));

    const alertBox = document.getElementById('reviewSuccessMsg');
    if (alertBox) alertBox.classList.remove('d-none');

    document.getElementById('farmerReviewForm').reset();
    updateDashboardReviewStats();

    setTimeout(() => {
        if (alertBox) alertBox.classList.add('d-none');
        const modalEl = document.getElementById('submitFarmerReviewModal');
        if (modalEl) {
            const inst = bootstrap.Modal.getInstance(modalEl);
            if (inst) inst.hide();
        }
        openReadReviewsModal();
    }, 1800);

    return false;
}


// --- Real-Time Credit Ledger Sync for Farmer Dashboard ---
async function syncFarmerUdhariDashboard() {
    var name = localStorage.getItem('user_name') || 'VSGAWALI';
    var mobile = localStorage.getItem('user_phone') || localStorage.getItem('user_mobile') || '';
    var farmerId = localStorage.getItem('user_farmer_id') || localStorage.getItem('farmer_id') || ('KSK-' + (mobile || name));

    var greetEl = document.getElementById('farmerGreetName');
    if (greetEl) greetEl.textContent = name;
    var sideNameEl = document.getElementById('sidebarUserDisplayName');
    if (sideNameEl) sideNameEl.textContent = name;

    var pendingDue = 0;
    var foundOnline = false;

    // 1. Try fetching live from backend API if available
    try {
        var apiUrl = (window.API_BASE_URL || '') + '/api/ledger/' + encodeURIComponent(farmerId) + '?mobile=' + encodeURIComponent(mobile) + '&name=' + encodeURIComponent(name);
        var res = await fetch(apiUrl, { cache: 'no-store' });
        if (res.ok) {
            var data = await res.json();
            if (data && data.data) {
                pendingDue = parseFloat(data.data.pendingDue) || 0;
                foundOnline = true;
            }
        }
    } catch(e) {}

    // 2. If offline or not in API, compute from ksk_udhari_records in localStorage
    if (!foundOnline) {
        var raw = localStorage.getItem('ksk_udhari_records');
        var records = [];
        if (raw) {
            try { records = JSON.parse(raw); } catch(err) { records = []; }
        }
        var cleanMobile = mobile.replace(/\D/g, '');
        var normName = name.trim().toLowerCase();

        var matching = records.filter(function(r) {
            if (!r) return false;
            if (r.farmerId && farmerId && (r.farmerId.toLowerCase() === farmerId.toLowerCase())) return true;
            if (r.mobile && cleanMobile && (r.mobile.replace(/\D/g, '') === cleanMobile)) return true;
            if (r.name) {
                var rName = r.name.trim().toLowerCase();
                if (rName === normName || rName.includes(normName) || normName.includes(rName)) return true;
                if ((normName.includes('vsg') || normName.includes('gawali')) && (rName.includes('vsg') || rName.includes('gawali'))) return true;
            }
            return false;
        });

        var totalDebit = 0;
        var totalCredit = 0;
        matching.forEach(function(r) {
            var amt = parseFloat(r.amount) || 0;
            var status = (r.status || '').toLowerCase();
            if (status === 'paid') {
                totalCredit += amt;
            } else {
                totalDebit += amt;
            }
        });
        pendingDue = Math.max(0, totalDebit - totalCredit);
    }

    // 3. Update Farmer Dashboard UI components
    var heroAmount = document.getElementById('farmerHeroDueAmount');
    var heroBadgeWrap = document.getElementById('farmerBalanceBadgeWrap');
    var heroText = document.getElementById('farmerHeroDueText');
    var kpiAmount = document.getElementById('farmerKpiDueAmount');
    var kpiPillWrap = document.getElementById('farmerKpiDuePillWrap');

    var formatted = '₹' + pendingDue.toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 });

    if (pendingDue > 0) {
        if (heroAmount) {
            heroAmount.textContent = formatted;
            heroAmount.style.color = '#dc2626';
        }
        if (heroBadgeWrap) {
            heroBadgeWrap.innerHTML = '<span class="badge text-white px-3 py-1 rounded-pill fw-bold" style="background:#dc2626 !important; font-size:13px;"><i class="bi bi-exclamation-triangle-fill me-1"></i> <span class="lang-mr">थकीत बाकी उधारी</span><span class="lang-en">Outstanding Dues</span></span>';
        }
        if (heroText) {
            heroText.className = 'm-0 mt-2 text-danger fw-semibold small';
            heroText.innerHTML = '<span class="lang-mr">⚠️ आपल्या खात्यावर <strong>' + formatted + '</strong> उधारी प्रलंबित आहे. कृपया वेळेत परतफेड करा.</span><span class="lang-en">⚠️ You have <strong>' + formatted + '</strong> outstanding credit due on your account.</span>';
        }
        if (kpiAmount) {
            kpiAmount.textContent = formatted;
            kpiAmount.className = 'stat-amount text-danger mb-1';
        }
        if (kpiPillWrap) {
            kpiPillWrap.innerHTML = '<span class="stat-pill" style="background:#fee2e2; color:#dc2626;"><i class="bi bi-clock-history"></i> <span class="lang-mr">बाकी प्रलंबित</span><span class="lang-en">Due Pending</span></span>';
        }
    } else {
        if (heroAmount) {
            heroAmount.textContent = '₹0.00';
            heroAmount.style.color = '#059669';
        }
        if (heroBadgeWrap) {
            heroBadgeWrap.innerHTML = '<span class="badge text-white px-3 py-1 rounded-pill fw-bold" style="background:#059669 !important; font-size:13px;"><i class="bi bi-check-circle-fill me-1"></i> <span class="lang-mr">✓ शून्य बाकी</span><span class="lang-en">✓ Nil Balance</span></span>';
        }
        if (heroText) {
            heroText.className = 'm-0 mt-2 text-success fw-semibold small';
            heroText.innerHTML = '<span class="lang-mr">🌟 उत्तम! आपल्या खात्यावर सध्या कोणतीही उधारी बाकी नाही.</span><span class="lang-en">🌟 Great! You have zero outstanding credit dues on your account.</span>';
        }
        if (kpiAmount) {
            kpiAmount.textContent = '₹0.00';
            kpiAmount.className = 'stat-amount text-success mb-1';
        }
        if (kpiPillWrap) {
            kpiPillWrap.innerHTML = '<span class="stat-pill" style="background:#ecfdf5; color:#059669;"><i class="bi bi-check-circle-fill"></i> <span class="lang-mr">शून्य बाकी</span><span class="lang-en">Nil Balance</span></span>';
        }
    }
}

document.addEventListener('DOMContentLoaded', function(){
    syncFarmerUdhariDashboard();
});
window.addEventListener('storage', function(e){
    if (e.key === 'ksk_udhari_records' || e.key === 'user_name') {
        syncFarmerUdhariDashboard();
    }
});

</script>
"""
    content = head_html("शेतकरी डॅशबोर्ड", "Farmer Dashboard") + nav_html("dashboard") + raw_dashboard.replace("<!-- SIDEBAR_PLACEHOLDER -->", sidebar) + foot_html()
    save_customer_page("farmer-dashboard.html", content)
    save_customer_page("dashboard.html", content)
    print("Generated dist/farmer-dashboard.html matching Screenshot 2 with Sidebar!")

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
# ==============================================================================
# 4. FARMER UDHARI (CREDIT LEDGER)
# ==============================================================================
def build_farmer_udhari():
    sidebar = render_customer_sidebar("udhari")
    content = (head_html("माझी उधारी", "Credit Ledger") + nav_html("dashboard") + """
<div class="container my-4" style="max-width: 1240px;">
    <div class="row g-4">
        <div class="col-lg-3 col-md-4">
            {sidebar}
        </div>
        <div class="col-lg-9 col-md-8">
            <!-- Header Balance Highlight Card -->
            <div class="farmer-balance-card mb-4" id="ledgerHeaderCard">
                <div class="row align-items-center g-3">
                    <div class="col-md-7">
                        <div class="d-flex align-items-center gap-2 mb-2" id="ledgerBadgeWrap">
                            <span class="badge text-white px-3 py-1 rounded-pill fw-bold" style="background:#059669 !important;">
                                <i class="bi bi-check-circle-fill me-1"></i> <span class="lang-mr">✓ शून्य बाकी</span><span class="lang-en">✓ Nil Balance</span>
                            </span>
                        </div>
                        <h1 class="display-5 fw-bold m-0" id="ledgerPendingDueAmount" style="color:#059669; font-weight:800;">₹0.00</h1>
                        <span class="fs-6 fw-semibold text-muted">
                            <span class="lang-mr">चालू बाकी उधारी रक्कम</span>
                            <span class="lang-en">Current Outstanding Due Balance</span>
                        </span>
                        <div class="d-flex flex-wrap gap-2 mt-3">
                            <div class="bg-white px-3 py-2 rounded-3 border shadow-sm small">
                                <span class="text-muted d-block" style="font-size:11px;"><span class="lang-mr">खाते स्थिती</span><span class="lang-en">Status</span>:</span>
                                <strong class="text-success" id="ledgerAccountStatus">सक्रिय / Active</strong>
                            </div>
                            <div class="bg-white px-3 py-2 rounded-3 border shadow-sm small">
                                <span class="text-muted d-block" style="font-size:11px;"><span class="lang-mr">एकूण उचल (Credit)</span><span class="lang-en">Total Credit</span>:</span>
                                <strong class="text-dark" id="ledgerTotalCredit">₹0.00</strong>
                            </div>
                            <div class="bg-white px-3 py-2 rounded-3 border shadow-sm small">
                                <span class="text-muted d-block" style="font-size:11px;"><span class="lang-mr">एकूण जमा (Paid)</span><span class="lang-en">Total Repaid</span>:</span>
                                <strong class="text-success" id="ledgerTotalPaid">₹0.00</strong>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-5 text-md-end">
                        <a href="farmer-pay.html" class="btn btn-success fw-bold px-4 py-2 rounded-3 shadow-sm mb-2 d-inline-block" style="background:#15803d;">
                            💳 <span class="lang-mr">UPI द्वारे भरा</span><span class="lang-en">Pay via UPI</span>
                        </a>
                        <div>
                            <button class="btn btn-sm btn-outline-secondary" onclick="window.print()"><i class="bi bi-printer me-1"></i> <span class="lang-mr">पासबुक प्रिंट करा</span><span class="lang-en">Print Passbook</span></button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Ledger Table -->
            <div class="card border-0 shadow-sm rounded-4 bg-white overflow-hidden">
                <div class="card-header bg-white py-3 px-4 border-bottom d-flex justify-content-between align-items-center flex-wrap gap-2">
                    <h6 class="fw-bold mb-0 text-dark"><i class="bi bi-clock-history me-2 text-success"></i><span class="lang-mr">खातेवही व्यवहार तपशील (Credit Ledger Transactions)</span><span class="lang-en">Ledger Transactions</span></h6>
                    <span class="badge bg-light text-muted border px-2 py-1 small" id="ledgerTxnCount">0 नोंदी</span>
                </div>
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-hover align-middle mb-0">
                            <thead class="table-light text-muted small">
                                <tr>
                                    <th><span class="lang-mr">तारीख</span><span class="lang-en">Date</span></th>
                                    <th><span class="lang-mr">तपशील</span><span class="lang-en">Description</span></th>
                                    <th><span class="lang-mr">नावे (Debit)</span><span class="lang-en">Debit (₹)</span></th>
                                    <th><span class="lang-mr">जमा (Credit)</span><span class="lang-en">Credit (₹)</span></th>
                                    <th><span class="lang-mr">शिल्लक (Balance)</span><span class="lang-en">Balance (₹)</span></th>
                                    <th><span class="lang-mr">स्थिती</span><span class="lang-en">Status</span></th>
                                </tr>
                            </thead>
                            <tbody id="farmerLedgerTbody">
                                <tr>
                                    <td colspan="6" class="text-center py-4 text-muted">
                                        <i class="bi bi-hourglass-split me-1"></i> Loading credit ledger transactions...
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
async function loadFarmerCreditLedger() {
    var name = localStorage.getItem('user_name') || 'VSGAWALI';
    var mobile = localStorage.getItem('user_phone') || localStorage.getItem('user_mobile') || '';
    var farmerId = localStorage.getItem('user_farmer_id') || localStorage.getItem('farmer_id') || ('KSK-' + (mobile || name));

    var sideNameEl = document.getElementById('sidebarUserDisplayName');
    if (sideNameEl) sideNameEl.textContent = name;

    var txns = [];
    var pendingDue = 0;
    var totalCredit = 0;
    var totalPaid = 0;
    var fetchedOnline = false;

    try {
        var apiUrl = (window.API_BASE_URL || '') + '/api/ledger/' + encodeURIComponent(farmerId) + '?mobile=' + encodeURIComponent(mobile) + '&name=' + encodeURIComponent(name);
        var res = await fetch(apiUrl, { cache: 'no-store' });
        if (res.ok) {
            var data = await res.json();
            if (data && data.data) {
                totalCredit = parseFloat(data.data.totalCredit) || 0;
                totalPaid = parseFloat(data.data.totalPaid) || 0;
                pendingDue = parseFloat(data.data.pendingDue) || 0;
                txns = data.data.transactions || [];
                fetchedOnline = true;
            }
        }
    } catch(e) {}

    if (!fetchedOnline) {
        var raw = localStorage.getItem('ksk_udhari_records');
        var records = [];
        if (raw) {
            try { records = JSON.parse(raw); } catch(err) { records = []; }
        }
        var cleanMobile = mobile.replace(/\D/g, '');
        var normName = name.trim().toLowerCase();

        var matching = records.filter(function(r) {
            if (!r) return false;
            if (r.farmerId && farmerId && (r.farmerId.toLowerCase() === farmerId.toLowerCase())) return true;
            if (r.mobile && cleanMobile && (r.mobile.replace(/\D/g, '') === cleanMobile)) return true;
            if (r.name) {
                var rName = r.name.trim().toLowerCase();
                if (rName === normName || rName.includes(normName) || normName.includes(rName)) return true;
                if ((normName.includes('vsg') || normName.includes('gawali')) && (rName.includes('vsg') || rName.includes('gawali'))) return true;
            }
            return false;
        });

        matching.forEach(function(r) {
            var amt = parseFloat(r.amount) || 0;
            var status = (r.status || '').toLowerCase();
            if (status === 'paid') {
                totalPaid += amt;
                txns.push({
                    date: r.dueDate || new Date().toISOString().split('T')[0],
                    notes: (r.notes || 'उधारी परतफेड') + ' (Paid via UPI/Cash)',
                    debit: 0,
                    credit: amt,
                    balance: 0,
                    status: 'Paid'
                });
            } else {
                totalCredit += amt;
                txns.push({
                    date: r.dueDate || new Date().toISOString().split('T')[0],
                    notes: r.notes || 'कृषी माल उधारी खरेदी (Store Credit Purchase)',
                    debit: amt,
                    credit: 0,
                    balance: amt,
                    status: r.status || 'Active'
                });
            }
        });
        pendingDue = Math.max(0, totalCredit - totalPaid);
    }

    // Update Header KPI
    var dueEl = document.getElementById('ledgerPendingDueAmount');
    var badgeWrap = document.getElementById('ledgerBadgeWrap');
    var creditEl = document.getElementById('ledgerTotalCredit');
    var paidEl = document.getElementById('ledgerTotalPaid');
    var countEl = document.getElementById('ledgerTxnCount');

    var formattedDue = '₹' + pendingDue.toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    if (dueEl) {
        dueEl.textContent = formattedDue;
        dueEl.style.color = pendingDue > 0 ? '#dc2626' : '#059669';
    }
    if (badgeWrap) {
        if (pendingDue > 0) {
            badgeWrap.innerHTML = '<span class="badge text-white px-3 py-1 rounded-pill fw-bold" style="background:#dc2626 !important;"><i class="bi bi-exclamation-triangle-fill me-1"></i> <span class="lang-mr">थकीत उधारी बाकी</span><span class="lang-en">Pending Dues</span></span>';
        } else {
            badgeWrap.innerHTML = '<span class="badge text-white px-3 py-1 rounded-pill fw-bold" style="background:#059669 !important;"><i class="bi bi-check-circle-fill me-1"></i> <span class="lang-mr">✓ शून्य बाकी (Nil Balance)</span><span class="lang-en">✓ Nil Balance</span></span>';
        }
    }
    if (creditEl) creditEl.textContent = '₹' + totalCredit.toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    if (paidEl) paidEl.textContent = '₹' + totalPaid.toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    if (countEl) countEl.textContent = txns.length + ' नोंदी';

    // Render Table
    var tbody = document.getElementById('farmerLedgerTbody');
    if (!tbody) return;

    if (txns.length === 0) {
        tbody.innerHTML = `
            <tr>
                <td colspan="6" class="text-center py-5">
                    <div class="mb-2 text-success fs-1"><i class="bi bi-shield-check"></i></div>
                    <h6 class="fw-bold text-dark mb-1"><span class="lang-mr">कोणतीही थकीत उधारी नोंद नाही</span><span class="lang-en">No Credit Transactions</span></h6>
                    <p class="text-muted small mb-0"><span class="lang-mr">आपल्या खात्यावर सध्या कोणतीही उधारी किंवा बाकी रक्कम प्रलंबित नाही.</span><span class="lang-en">All your purchases are fully paid with zero outstanding balance.</span></p>
                </td>
            </tr>
        `;
        return;
    }

    tbody.innerHTML = txns.map(function(t) {
        var isDebit = (parseFloat(t.debit) || 0) > 0;
        var debitText = isDebit ? ('₹' + parseFloat(t.debit).toLocaleString('en-IN', { minimumFractionDigits: 2 })) : '-';
        var creditText = (parseFloat(t.credit) || 0) > 0 ? ('₹' + parseFloat(t.credit).toLocaleString('en-IN', { minimumFractionDigits: 2 })) : '-';
        var balText = '₹' + (parseFloat(t.balance) || 0).toLocaleString('en-IN', { minimumFractionDigits: 2 });
        var statusBadge = (t.status === 'Paid') ? '<span class="badge bg-success-subtle text-success border border-success-subtle">Paid</span>' : '<span class="badge bg-danger-subtle text-danger border border-danger-subtle">Due / बाकी</span>';

        return `
            <tr>
                <td class="text-nowrap fw-semibold text-secondary">${t.date || '-'}</td>
                <td><strong class="text-dark">${t.notes || 'कृषी माल खरेदी'}</strong></td>
                <td class="fw-bold text-danger">${debitText}</td>
                <td class="fw-bold text-success">${creditText}</td>
                <td class="fw-bold ${parseFloat(t.balance) > 0 ? 'text-danger' : 'text-success'}">${balText}</td>
                <td>${statusBadge}</td>
            </tr>
        `;
    }).join('');
}

document.addEventListener('DOMContentLoaded', loadFarmerCreditLedger);
window.addEventListener('storage', function(e){
    if (e.key === 'ksk_udhari_records' || e.key === 'user_name') {
        loadFarmerCreditLedger();
    }
});
</script>
""").replace("{sidebar}", sidebar) + foot_html()
    save_customer_page("farmer-udhari.html", content)
    print("Generated dist/farmer-udhari.html with dynamic real-time credit ledger!")

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
