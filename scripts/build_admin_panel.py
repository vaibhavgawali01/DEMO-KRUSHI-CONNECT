import os
from build_site import head_html, nav_html, foot_html, DIST_DIR

def admin_nav_pills(active="dashboard"):
    items = [
        ("dashboard", "admin-dashboard.html", "bi-grid-1x2-fill", "डॅशबोर्ड", "Dashboard"),
        ("products", "admin-products.html", "bi-box-seam-fill", "उत्पादने", "Products"),
        ("product-form", "admin-product-form.html", "bi-plus-circle-fill", "➕ उत्पादन जोडा", "➕ Add Product"),
        ("udhari", "admin-udhari.html", "bi-wallet2", "उधारी खाते", "Credit Ledger"),
        ("inventory", "admin-inventory.html", "bi-boxes", "इन्व्हेंटरी व एक्सपायरी", "Inventory & Expiry")
    ]
    html = '<div class="d-flex flex-wrap gap-2 mb-4 p-2 bg-white rounded-4 shadow-sm border">'
    for key, url, icon, mr, en in items:
        isActive = (key == active)
        cls = "btn btn-sm rounded-pill fw-bold px-3 py-2 " + ("btn-success text-white shadow-sm" if isActive else "btn-light text-dark")
        html += '<a href="' + url + '" class="' + cls + '"><i class="bi ' + icon + ' me-1"></i><span class="lang-mr">' + mr + '</span><span class="lang-en">' + en + '</span></a>'
    html += '</div>'
    return html

# 1. ADMIN DASHBOARD
def build_admin_dashboard():
    pills = admin_nav_pills("dashboard")
    content = head_html("ॲडमिन डॅशबोर्ड", "Admin Dashboard") + nav_html("dashboard") + """
<div class="container-fluid px-3 px-lg-4 my-4" style="max-width:1400px;">
    <!-- Welcome Header -->
    <div class="card border-0 shadow-sm rounded-4 text-white p-4 mb-4 overflow-hidden position-relative" style="background: linear-gradient(135deg, #0a2e0a 0%, #1b5e20 60%, #14532d 100%);">
        <div class="row align-items-center g-3 position-relative" style="z-index:2;">
            <div class="col-md-7">
                <span class="badge bg-white bg-opacity-25 text-white px-3 py-1 rounded-pill mb-2 fw-semibold">
                    🌱 <span class="lang-mr">सप्तशृंगी ॲग्रो सर्व्हिसेस, मिरखनगर</span><span class="lang-en">Saptashrungi Agro Services, Mirakhnagar</span>
                </span>
                <h2 class="display-6 fw-bold mb-1"><span class="lang-mr">व्यवस्थापन डॅशबोर्ड</span><span class="lang-en">Admin Dashboard</span></h2>
                <p class="text-white-50 small mb-0"><span class="lang-mr">विक्री, इन्व्हेंटरी, शेतकरी उधारी खाती आणि दुकानाच्या कामगिरीचा थेट आढावा.</span><span class="lang-en">Overview of sales, inventory, farmer accounts, and store performance.</span></p>
            </div>
            <div class="col-md-5 text-md-end d-flex gap-2 justify-content-md-end flex-wrap">
                <a href="admin-product-form.html" class="btn btn-light text-success fw-bold px-3 py-2 rounded-pill shadow-sm">
                    ➕ <span class="lang-mr">Add Product (उत्पादन जोडा)</span><span class="lang-en">Add Product</span>
                </a>
                <a href="admin-products.html" class="btn btn-outline-light fw-bold px-3 py-2 rounded-pill">
                    📦 <span class="lang-mr">उत्पादने</span><span class="lang-en">Products</span>
                </a>
                <button onclick="handleLogout()" class="btn btn-danger fw-bold px-3 py-2 rounded-pill shadow-sm">
                    <i class="bi bi-box-arrow-right me-1"></i><span class="lang-mr">लॉगआउट</span><span class="lang-en">Logout</span>
                </button>
            </div>
        </div>
    </div>
""" + pills + """
    <!-- Low Stock Alert Banner -->
    <div class="alert alert-warning border-0 shadow-sm rounded-4 d-flex align-items-center justify-content-between flex-wrap gap-2 mb-4 p-3" style="background:#fffbeb; border-left: 5px solid #f59e0b !important;">
        <div class="d-flex align-items-center gap-3">
            <div style="width:40px;height:40px;border-radius:10px;background:#fef3c7;display:flex;align-items:center;justify-content:center;font-size:1.25rem;">⚠️</div>
            <div>
                <h6 class="fw-bold mb-0 text-dark"><span class="lang-mr">कमी साठा चेतावणी (Low Stock Alerts)</span><span class="lang-en">Low Stock Alerts</span></h6>
                <small class="text-muted"><span class="lang-mr"><strong>३ उत्पादनांचा</strong> साठा कमी झाला आहे (उदा. फाल्कन बॅटरी पंप, 10:26:26 खत).</span><span class="lang-en"><strong>3 products</strong> are running below safety threshold.</span></small>
            </div>
        </div>
        <a href="admin-inventory.html" class="btn btn-sm btn-warning fw-bold px-3 py-2 rounded-pill">
            <span class="lang-mr">इन्व्हेंटरी तपासा &rarr;</span><span class="lang-en">Check Inventory &rarr;</span>
        </a>
    </div>

    <!-- 4 Main Stats Cards: Total Products, Total Users, Udhari Outstanding, Monthly Revenue -->
    <div class="row g-3 mb-4">
        <!-- 1. Total Products -->
        <div class="col-sm-6 col-xl-3">
            <a href="admin-products.html" class="card border-0 shadow-sm rounded-4 p-3 bg-white h-100 text-decoration-none text-dark">
                <div class="d-flex justify-content-between align-items-start mb-2">
                    <span class="text-muted small fw-bold"><span class="lang-mr">एकूण उत्पादने (Total Products)</span><span class="lang-en">Total Products</span></span>
                    <div class="rounded-circle d-flex align-items-center justify-content-center" style="width:38px;height:38px;background:#dbeafe;color:#0284c7;"><i class="bi bi-box-seam-fill"></i></div>
                </div>
                <h3 class="fw-bold text-dark mb-1">128</h3>
                <small class="text-success"><i class="bi bi-check-circle-fill me-1"></i>125 स्टॉकमध्ये उपलब्ध</small>
            </a>
        </div>

        <!-- 2. Total Users -->
        <div class="col-sm-6 col-xl-3">
            <div class="card border-0 shadow-sm rounded-4 p-3 bg-white h-100">
                <div class="d-flex justify-content-between align-items-start mb-2">
                    <span class="text-muted small fw-bold"><span class="lang-mr">एकूण युझर्स (Total Users)</span><span class="lang-en">Total Users</span></span>
                    <div class="rounded-circle d-flex align-items-center justify-content-center" style="width:38px;height:38px;background:#f3e8ff;color:#7c3aed;"><i class="bi bi-people-fill"></i></div>
                </div>
                <h3 class="fw-bold text-primary mb-1">520+</h3>
                <small class="text-muted"><span class="lang-mr">नोंदणीकृत शेतकरी ग्राहक</span><span class="lang-en">Registered Farmers</span></small>
            </div>
        </div>

        <!-- 3. Udhari Outstanding -->
        <div class="col-sm-6 col-xl-3">
            <a href="admin-udhari.html" class="card border-0 shadow-sm rounded-4 p-3 bg-white h-100 text-decoration-none text-dark" style="border-left: 4px solid #dc2626 !important;">
                <div class="d-flex justify-content-between align-items-start mb-2">
                    <span class="text-danger small fw-bold"><span class="lang-mr">बाकी उधारी (Udhari Outstanding)</span><span class="lang-en">Udhari Outstanding</span></span>
                    <div class="rounded-circle d-flex align-items-center justify-content-center" style="width:38px;height:38px;background:#fee2e2;color:#dc2626;"><i class="bi bi-wallet-fill"></i></div>
                </div>
                <h3 class="fw-bold text-danger mb-1">₹42,800</h3>
                <small class="text-danger"><i class="bi bi-exclamation-circle-fill me-1"></i>१२ शेतकऱ्यांकडे बाकी</small>
            </a>
        </div>

        <!-- 4. Monthly Revenue -->
        <div class="col-sm-6 col-xl-3">
            <div class="card border-0 shadow-sm rounded-4 p-3 bg-white h-100">
                <div class="d-flex justify-content-between align-items-start mb-2">
                    <span class="text-muted small fw-bold"><span class="lang-mr">मासिक महसूल (Monthly Revenue)</span><span class="lang-en">Monthly Revenue</span></span>
                    <div class="rounded-circle d-flex align-items-center justify-content-center" style="width:38px;height:38px;background:#dcfce7;color:#16a34a;"><i class="bi bi-cash-stack"></i></div>
                </div>
                <h3 class="fw-bold text-success mb-1">₹1,48,500</h3>
                <small class="text-success"><i class="bi bi-arrow-up-short"></i>+18.4% चालू महिना</small>
            </div>
        </div>
    </div>

    <!-- Recent Orders Table -->
    <div class="card border-0 shadow-sm rounded-4 overflow-hidden bg-white mb-4">
        <div class="card-header bg-white py-3 px-4 border-0 d-flex justify-content-between align-items-center">
            <div class="d-flex align-items-center gap-2">
                <i class="bi bi-receipt text-success fs-5"></i>
                <h5 class="fw-bold mb-0 text-dark"><span class="lang-mr">अलीकडील ऑर्डर्स व पावत्या (Recent Orders)</span><span class="lang-en">Recent Orders & Invoices</span></h5>
            </div>
            <a href="admin-products.html" class="btn btn-sm btn-outline-success rounded-pill px-3 fw-bold">
                <span class="lang-mr">सर्व उत्पादने &rarr;</span><span class="lang-en">View Products &rarr;</span>
            </a>
        </div>
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="table-light">
                    <tr>
                        <th class="ps-4">पावती क्र. (Order ID)</th>
                        <th>शेतकरी ग्राहक (Customer Name)</th>
                        <th>तारीख</th>
                        <th>उत्पादने व प्रमाण</th>
                        <th class="text-end">रक्कम (Amount)</th>
                        <th class="text-center">स्थिती (Status)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="ps-4"><strong class="text-success">#KSK-8492</strong></td>
                        <td><strong>रमेश पाटील</strong><br><small class="text-muted">९८२२०१२३४५ • वैजापूर</small></td>
                        <td>३० ऑक्टोबर २०२६</td>
                        <td>माहिको बीजी-२ कापूस (२ बॅग्स)</td>
                        <td class="text-end fw-bold text-success">₹1,640.00</td>
                        <td class="text-center"><span class="badge bg-success">वितरित (Delivered)</span></td>
                    </tr>
                    <tr>
                        <td class="ps-4"><strong class="text-success">#KSK-8491</strong></td>
                        <td><strong>विलास जगताप</strong><br><small class="text-muted">९८२३४५६७८० • मिरखनगर</small></td>
                        <td>२९ ऑक्टोबर २०२६</td>
                        <td>महाधन २४:२४:० खत (५० किलो, २ बॅग्स)</td>
                        <td class="text-end fw-bold text-success">₹3,360.00</td>
                        <td class="text-center"><span class="badge bg-success">वितरित (Delivered)</span></td>
                    </tr>
                    <tr>
                        <td class="ps-4"><strong class="text-success">#KSK-8490</strong></td>
                        <td><strong>सचिन काळे</strong><br><small class="text-muted">९४२१५५६६७७ • लाडगाव</small></td>
                        <td>२९ ऑक्टोबर २०२६</td>
                        <td>फाल्कन १६L बॅटरी स्प्रे पंप</td>
                        <td class="text-end fw-bold text-success">₹2,800.00</td>
                        <td class="text-center"><span class="badge bg-primary">तयार (Processing)</span></td>
                    </tr>
                    <tr>
                        <td class="ps-4"><strong class="text-success">#KSK-8489</strong></td>
                        <td><strong>गजानन थोरात</strong><br><small class="text-muted">९८९०११२२३३ • शिऊर</small></td>
                        <td>२८ ऑक्टोबर २०२६</td>
                        <td>कोरोमंडेल १०:२६:२६ ग्रोमोर खत</td>
                        <td class="text-end fw-bold text-success">₹1,470.00</td>
                        <td class="text-center"><span class="badge bg-success">वितरित (Delivered)</span></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
""" + foot_html()
    with open(os.path.join(DIST_DIR, "admin-dashboard.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated dist/admin-dashboard.html")

# 2. ADMIN PRODUCTS
def build_admin_products():
    pills = admin_nav_pills("products")
    content = head_html("उत्पादने व्यवस्थापन", "Product Management") + nav_html("dashboard") + """
<div class="container-fluid px-3 px-lg-4 my-4" style="max-width:1400px;">
    <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-3 mb-4">
        <div>
            <h1 class="h3 fw-bold text-dark m-0 d-flex align-items-center gap-2">
                <span>📦</span> <span class="lang-mr">उत्पादने व्यवस्थापन</span><span class="lang-en">Product Management</span>
            </h1>
            <p class="text-muted small m-0 mt-1">
                <span class="lang-mr">बियाणे, खते, कीटकनाशके व ड्रिप साहित्याची यादी आणि साठा व्यवस्थापन</span>
                <span class="lang-en">Manage catalog products, stock levels, prices, and suppliers</span>
            </p>
        </div>
        <div class="d-flex gap-2">
            <a href="admin-product-form.html" class="btn btn-success fw-bold px-4 py-2 rounded-pill shadow-sm">
                ➕ <span class="lang-mr">Add Product (नवीन उत्पादन)</span><span class="lang-en">Add Product</span>
            </a>
        </div>
    </div>
""" + pills + """
    <!-- Search & Filter Controls -->
    <div class="card border-0 shadow-sm rounded-4 p-3 mb-4 bg-white">
        <div class="row g-2 align-items-center">
            <div class="col-md-5">
                <div class="input-group">
                    <span class="input-group-text bg-light border-0"><i class="bi bi-search"></i></span>
                    <input type="text" id="adminProdSearch" onkeyup="filterAdminTable()" class="form-control border-0 bg-light" placeholder="उत्पादन किंवा कंपनीचे नाव शोधा...">
                </div>
            </div>
            <div class="col-md-4">
                <select id="adminProdCat" onchange="filterAdminTable()" class="form-select border-0 bg-light">
                    <option value="">सर्व कॅटेगरी (All Categories)</option>
                    <option value="बियाणे">बियाणे (Seeds)</option>
                    <option value="खते">खते (Fertilizers)</option>
                    <option value="कीटकनाशके">कीटकनाशके (Pesticides)</option>
                    <option value="कृषी अवजारे">कृषी अवजारे व पंप (Tools & Sprayers)</option>
                    <option value="ठिबक सिंचन">ठिबक सिंचन (Drip Irrigation)</option>
                </select>
            </div>
            <div class="col-md-3 text-md-end">
                <span class="text-muted small fw-semibold" id="prodCountBadge">एकूण उत्पादने: 6</span>
            </div>
        </div>
    </div>

    <!-- Product List Table -->
    <div class="card border-0 shadow-sm rounded-4 overflow-hidden bg-white mb-4">
        <div class="table-responsive">
            <table class="table align-middle mb-0" id="adminProdTable" style="font-size: 13.5px;">
                <thead class="table-light">
                    <tr>
                        <th class="ps-3" style="width: 70px;">Image</th>
                        <th style="min-width: 220px;">उत्पादनाचे नाव (Product Name)</th>
                        <th>कंपनी (Company)</th>
                        <th>कॅटेगरी (Category)</th>
                        <th class="text-end">किंमत (Price)</th>
                        <th class="text-center">साठा (Stock)</th>
                        <th class="text-center">स्थिती (Status)</th>
                        <th class="text-center pe-3" style="width: 140px;">कृती (Actions)</th>
                    </tr>
                </thead>
                <tbody id="adminProdTbody">
                    <!-- Row 1 -->
                    <tr class="prod-row" data-cat="बियाणे" data-name="माहिको बीजी-२ कापूस बियाणे mahyco bg-ii cotton">
                        <td class="ps-3">
                            <img src="images/cotton_seeds.jpg" alt="Cotton" class="rounded-3 border" style="width:48px;height:48px;object-fit:cover;" onerror="this.src='images/saptashrungi_shop.jpg'">
                        </td>
                        <td>
                            <strong class="text-dark d-block">माहिको बीजी-२ कापूस बियाणे</strong>
                            <small class="text-muted">Mahyco BG-II Cotton Seeds (475g)</small>
                        </td>
                        <td><span class="badge bg-light text-dark border">Mahyco Seeds</span></td>
                        <td><span class="badge bg-success-subtle text-success">बियाणे (Seeds)</span></td>
                        <td class="text-end fw-bold text-success">₹820.00</td>
                        <td class="text-center"><span class="badge bg-success px-3 py-1 rounded-pill">45 बॅग्स</span></td>
                        <td class="text-center"><span class="badge bg-success-subtle text-success border border-success px-2 py-1 rounded-pill">सक्रीय (Active)</span></td>
                        <td class="text-center pe-3">
                            <div class="d-inline-flex gap-1">
                                <a href="admin-product-form.html?id=1" class="btn btn-sm btn-outline-primary px-2 py-1"><i class="bi bi-pencil-square"></i></a>
                                <button onclick="deleteProductRow(this)" class="btn btn-sm btn-outline-danger px-2 py-1"><i class="bi bi-trash"></i></button>
                            </div>
                        </td>
                    </tr>
                    <!-- Row 2 -->
                    <tr class="prod-row" data-cat="खते" data-name="महाधन २४:२४:० खत mahadhan 24:24:0">
                        <td class="ps-3">
                            <img src="images/npk_fertilizer.jpg" alt="Fertilizer" class="rounded-3 border" style="width:48px;height:48px;object-fit:cover;" onerror="this.src='images/saptashrungi_shop.jpg'">
                        </td>
                        <td>
                            <strong class="text-dark d-block">महाधन २४:२४:० खत</strong>
                            <small class="text-muted">Mahadhan 24:24:0 Fertilizer (50kg)</small>
                        </td>
                        <td><span class="badge bg-light text-dark border">Mahadhan</span></td>
                        <td><span class="badge bg-success-subtle text-success">खते (Fertilizers)</span></td>
                        <td class="text-end fw-bold text-success">₹1,680.00</td>
                        <td class="text-center"><span class="badge bg-success px-3 py-1 rounded-pill">28 बॅग्स</span></td>
                        <td class="text-center"><span class="badge bg-success-subtle text-success border border-success px-2 py-1 rounded-pill">सक्रीय (Active)</span></td>
                        <td class="text-center pe-3">
                            <div class="d-inline-flex gap-1">
                                <a href="admin-product-form.html?id=2" class="btn btn-sm btn-outline-primary px-2 py-1"><i class="bi bi-pencil-square"></i></a>
                                <button onclick="deleteProductRow(this)" class="btn btn-sm btn-outline-danger px-2 py-1"><i class="bi bi-trash"></i></button>
                            </div>
                        </td>
                    </tr>
                    <!-- Row 3 -->
                    <tr class="prod-row" data-cat="कृषी अवजारे" data-name="फाल्कन १६L बॅटरी स्प्रे पंप falcon battery sprayer">
                        <td class="ps-3">
                            <img src="images/battery_sprayer.jpg" alt="Sprayer" class="rounded-3 border" style="width:48px;height:48px;object-fit:cover;" onerror="this.src='images/saptashrungi_shop.jpg'">
                        </td>
                        <td>
                            <strong class="text-dark d-block">फाल्कन १६L बॅटरी स्प्रे पंप</strong>
                            <small class="text-muted">Falcon 16L Battery Knapsack Sprayer</small>
                        </td>
                        <td><span class="badge bg-light text-dark border">Falcon Agri</span></td>
                        <td><span class="badge bg-info-subtle text-info">कृषी अवजारे</span></td>
                        <td class="text-end fw-bold text-success">₹2,800.00</td>
                        <td class="text-center"><span class="badge bg-warning text-dark px-3 py-1 rounded-pill">3 नग (कमी)</span></td>
                        <td class="text-center"><span class="badge bg-warning-subtle text-warning border border-warning px-2 py-1 rounded-pill">कमी साठा (Low)</span></td>
                        <td class="text-center pe-3">
                            <div class="d-inline-flex gap-1">
                                <a href="admin-product-form.html?id=3" class="btn btn-sm btn-outline-primary px-2 py-1"><i class="bi bi-pencil-square"></i></a>
                                <button onclick="deleteProductRow(this)" class="btn btn-sm btn-outline-danger px-2 py-1"><i class="bi bi-trash"></i></button>
                            </div>
                        </td>
                    </tr>
                    <!-- Row 4 -->
                    <tr class="prod-row" data-cat="खते" data-name="कोरोमंडेल १०:२६:२६ ग्रोमोर coromandel gromor">
                        <td class="ps-3">
                            <img src="images/npk_fertilizer.jpg" alt="Gromor" class="rounded-3 border" style="width:48px;height:48px;object-fit:cover;" onerror="this.src='images/saptashrungi_shop.jpg'">
                        </td>
                        <td>
                            <strong class="text-dark d-block">कोरोमंडेल १०:२६:२६ ग्रोमोर खत</strong>
                            <small class="text-muted">Coromandel Gromor 10:26:26 (50kg)</small>
                        </td>
                        <td><span class="badge bg-light text-dark border">Coromandel</span></td>
                        <td><span class="badge bg-success-subtle text-success">खते (Fertilizers)</span></td>
                        <td class="text-end fw-bold text-success">₹1,470.00</td>
                        <td class="text-center"><span class="badge bg-warning text-dark px-3 py-1 rounded-pill">4 बॅग्स</span></td>
                        <td class="text-center"><span class="badge bg-warning-subtle text-warning border border-warning px-2 py-1 rounded-pill">कमी साठा</span></td>
                        <td class="text-center pe-3">
                            <div class="d-inline-flex gap-1">
                                <a href="admin-product-form.html?id=4" class="btn btn-sm btn-outline-primary px-2 py-1"><i class="bi bi-pencil-square"></i></a>
                                <button onclick="deleteProductRow(this)" class="btn btn-sm btn-outline-danger px-2 py-1"><i class="bi bi-trash"></i></button>
                            </div>
                        </td>
                    </tr>
                    <!-- Row 5 -->
                    <tr class="prod-row" data-cat="कीटकनाशके" data-name="सिजेंटा ॲम्प्लिगो ampligo syngenta">
                        <td class="ps-3">
                            <img src="images/pesticide_bottle.jpg" alt="Pesticide" class="rounded-3 border" style="width:48px;height:48px;object-fit:cover;" onerror="this.src='images/saptashrungi_shop.jpg'">
                        </td>
                        <td>
                            <strong class="text-dark d-block">सिजेंटा ॲम्प्लिगो कीटकनाशक (100ml)</strong>
                            <small class="text-muted">Syngenta Ampligo Insecticide</small>
                        </td>
                        <td><span class="badge bg-light text-dark border">Syngenta</span></td>
                        <td><span class="badge bg-danger-subtle text-danger">कीटकनाशके</span></td>
                        <td class="text-end fw-bold text-success">₹780.00</td>
                        <td class="text-center"><span class="badge bg-success px-3 py-1 rounded-pill">18 बाटल्या</span></td>
                        <td class="text-center"><span class="badge bg-success-subtle text-success border border-success px-2 py-1 rounded-pill">सक्रीय</span></td>
                        <td class="text-center pe-3">
                            <div class="d-inline-flex gap-1">
                                <a href="admin-product-form.html?id=5" class="btn btn-sm btn-outline-primary px-2 py-1"><i class="bi bi-pencil-square"></i></a>
                                <button onclick="deleteProductRow(this)" class="btn btn-sm btn-outline-danger px-2 py-1"><i class="bi bi-trash"></i></button>
                            </div>
                        </td>
                    </tr>
                    <!-- Row 6 -->
                    <tr class="prod-row" data-cat="ठिबक सिंचन" data-name="नेटाफिम १६मिमी इनलाईन ड्रिप पाइप netafim inline drip pipe">
                        <td class="ps-3">
                            <img src="images/drip_irrigation.jpg" alt="Drip" class="rounded-3 border" style="width:48px;height:48px;object-fit:cover;" onerror="this.src='images/saptashrungi_shop.jpg'">
                        </td>
                        <td>
                            <strong class="text-dark d-block">नेटाफिम १६मिमी इनलाईन ड्रिप पाईप (४०० मी.)</strong>
                            <small class="text-muted">Netafim 16mm Inline Drip Lateral (400m)</small>
                        </td>
                        <td><span class="badge bg-light text-dark border">Netafim</span></td>
                        <td><span class="badge bg-primary-subtle text-primary">ठिबक सिंचन</span></td>
                        <td class="text-end fw-bold text-success">₹2,450.00</td>
                        <td class="text-center"><span class="badge bg-success px-3 py-1 rounded-pill">12 बंडल</span></td>
                        <td class="text-center"><span class="badge bg-success-subtle text-success border border-success px-2 py-1 rounded-pill">सक्रीय</span></td>
                        <td class="text-center pe-3">
                            <div class="d-inline-flex gap-1">
                                <a href="admin-product-form.html?id=6" class="btn btn-sm btn-outline-primary px-2 py-1"><i class="bi bi-pencil-square"></i></a>
                                <button onclick="deleteProductRow(this)" class="btn btn-sm btn-outline-danger px-2 py-1"><i class="bi bi-trash"></i></button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- Empty State Container (shown when 0 products match) -->
        <div id="adminEmptyState" class="text-center py-5 px-3 d-none" style="background: linear-gradient(135deg,#f0f9f0,#e8f5e9);">
            <div style="font-size:3.5rem;" class="mb-3">📦</div>
            <h4 class="fw-bold text-dark mb-2">📦 कोणतेही Products नाहीत</h4>
            <p class="text-muted mb-4 small">नवीन product add करा — ते सर्व ग्राहकांसाठी कॅटलॉगमध्ये दिसेल.</p>
            <a href="admin-product-form.html" class="btn btn-success px-5 py-2 fw-bold rounded-pill shadow-lg">
                ➕ नवीन उत्पादन जोडा (Add Product)
            </a>
        </div>
    </div>
</div>

<script>
function filterAdminTable() {
    const q = (document.getElementById('adminProdSearch').value || '').toLowerCase();
    const cat = document.getElementById('adminProdCat').value;
    const rows = document.querySelectorAll('.prod-row');
    let visible = 0;

    rows.forEach(r => {
        const name = (r.getAttribute('data-name') || '').toLowerCase();
        const rowCat = r.getAttribute('data-cat') || '';
        const matchQ = !q || name.includes(q);
        const matchCat = !cat || rowCat.includes(cat);
        if (matchQ && matchCat) {
            r.classList.remove('d-none');
            visible++;
        } else {
            r.classList.add('d-none');
        }
    });

    const emptyBox = document.getElementById('adminEmptyState');
    const table = document.getElementById('adminProdTable');
    if (visible === 0) {
        emptyBox.classList.remove('d-none');
        table.classList.add('d-none');
    } else {
        emptyBox.classList.add('d-none');
        table.classList.remove('d-none');
    }
    document.getElementById('prodCountBadge').textContent = 'दिसत आहेत: ' + visible + ' उत्पादने';
}

function deleteProductRow(btn) {
    if (confirm('तुम्हाला खात्री आहे की हे उत्पादन काढून टाकायचे आहे?')) {
        const row = btn.closest('tr');
        row.remove();
        filterAdminTable();
    }
}
</script>
""" + foot_html()
    with open(os.path.join(DIST_DIR, "admin-products.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated dist/admin-products.html")

# 3. ADMIN PRODUCT FORM
def build_admin_product_form():
    pills = admin_nav_pills("product-form")
    content = head_html("उत्पादन फॉर्म", "Product Form") + nav_html("dashboard") + """
<div class="container my-4" style="max-width:960px;">
    <div class="d-flex justify-content-between align-items-center mb-4">
        <div>
            <h1 class="h3 fw-bold text-dark m-0 d-flex align-items-center gap-2">
                <span>➕</span> <span class="lang-mr">नवीन कृषी उत्पादन जोडा / बदला</span><span class="lang-en">Add / Edit Agricultural Product</span>
            </h1>
            <p class="text-muted small m-0 mt-1">
                <span class="lang-mr">उत्पादनाचे तपशील, दर, जीएसटी, साठा मर्यादा व फोटो भरा</span>
                <span class="lang-en">Configure product specifications, price, GST, stock threshold and image</span>
            </p>
        </div>
        <a href="admin-products.html" class="btn btn-light border px-3 py-2 rounded-pill shadow-sm">
            ← <span class="lang-mr">उत्पादने यादी</span><span class="lang-en">Back to Products</span>
        </a>
    </div>
""" + pills + """
    <div class="card border-0 shadow-sm rounded-4 p-4 bg-white">
        <form id="adminProductForm" onsubmit="handleProductSave(event)">
            <div class="row g-3">
                <!-- 1. Name (English) -->
                <div class="col-md-6">
                    <label class="form-label small fw-bold text-success text-uppercase">
                        Product Name (English) *
                    </label>
                    <input type="text" id="fName" class="form-control" required placeholder="e.g. Mahyco Bollgard II Cotton Seeds (475g)" value="Mahyco Bollgard II Cotton Seeds (475g)">
                </div>

                <!-- 2. NameMr (Marathi) -->
                <div class="col-md-6">
                    <label class="form-label small fw-bold text-success text-uppercase">
                        उत्पादनाचे नाव (मराठी) *
                    </label>
                    <input type="text" id="fNameMr" class="form-control" required placeholder="उदा. माहिको बीजी-२ कापूस बियाणे" value="माहिको बीजी-२ कापूस बियाणे">
                </div>

                <!-- 3. Company -->
                <div class="col-md-4">
                    <label class="form-label small fw-bold text-success text-uppercase">
                        Company / Manufacturer *
                    </label>
                    <input type="text" id="fCompany" class="form-control" required placeholder="उदा. Mahyco, Bayer, Syngenta, IFFCO" value="Mahyco Seeds">
                </div>

                <!-- 4. Category -->
                <div class="col-md-4">
                    <label class="form-label small fw-bold text-success text-uppercase">
                        Category / वर्ग *
                    </label>
                    <select id="fCategory" class="form-select" required>
                        <option value="बियाणे" selected>बियाणे (Seeds)</option>
                        <option value="खते">खते (Fertilizers)</option>
                        <option value="कीटकनाशके">कीटकनाशके (Pesticides)</option>
                        <option value="कृषी अवजारे">कृषी अवजारे व पंप (Farm Tools & Sprayers)</option>
                        <option value="ठिबक सिंचन">ठिबक सिंचन (Drip Irrigation)</option>
                    </select>
                </div>

                <!-- 5. GST Rate -->
                <div class="col-md-4">
                    <label class="form-label small fw-bold text-success text-uppercase">
                        GST Rate (%) *
                    </label>
                    <select id="fGstRate" class="form-select" required>
                        <option value="0" selected>0% (बियाणे / करमुक्त)</option>
                        <option value="5">5% (खते / पशुखाद्य)</option>
                        <option value="12">12% (ड्रिप सिंचन / पंप)</option>
                        <option value="18">18% (कीटकनाशके / टॉनिक)</option>
                    </select>
                </div>

                <!-- 6. Price (MRP) -->
                <div class="col-md-3">
                    <label class="form-label small fw-bold text-success text-uppercase">
                        Price / MRP (₹) *
                    </label>
                    <input type="number" step="0.01" id="fPrice" class="form-control" required placeholder="864.00" value="864.00">
                </div>

                <!-- 7. Discount Price -->
                <div class="col-md-3">
                    <label class="form-label small fw-bold text-success text-uppercase">
                        Discount Price (₹)
                    </label>
                    <input type="number" step="0.01" id="fDiscountPrice" class="form-control" placeholder="820.00" value="820.00">
                </div>

                <!-- 8. Stock Quantity -->
                <div class="col-md-3">
                    <label class="form-label small fw-bold text-success text-uppercase">
                        Stock Quantity *
                    </label>
                    <input type="number" id="fStockQuantity" class="form-control" required min="0" value="45">
                </div>

                <!-- 9. Minimum Stock Alert Threshold -->
                <div class="col-md-3">
                    <label class="form-label small fw-bold text-success text-uppercase">
                        Minimum Stock Alert *
                    </label>
                    <input type="number" id="fMinimumStock" class="form-control" required min="1" value="10">
                </div>

                <!-- 10. Image Upload & Preview -->
                <div class="col-md-12">
                    <label class="form-label small fw-bold text-success text-uppercase">
                        Image Upload (उत्पादन फोटो)
                    </label>
                    <input type="file" id="fImageFile" accept="image/*" class="form-control" onchange="previewProductImg(event)">
                    <div class="form-text">Choose JPG, PNG or WebP image. Max 10MB.</div>
                    <div class="mt-2 d-flex align-items-center gap-3" id="imgPreviewWrap">
                        <img id="imgPreviewEl" src="images/cotton_seeds.jpg" alt="Preview" class="rounded-3 border shadow-sm p-1" style="width:72px;height:72px;object-fit:cover;">
                        <span class="small text-muted" id="imgPreviewText">माहिको कापूस बियाणे फोटो लोड आहे</span>
                    </div>
                </div>

                <!-- 11. Description -->
                <div class="col-12">
                    <label class="form-label small fw-bold text-success text-uppercase">
                        Description / सविस्तर माहिती
                    </label>
                    <textarea id="fDescription" class="form-control" rows="3" placeholder="उत्पादनाची वैशिष्ट्ये, फायदे, प्रमाण व शिफारस...">उच्च प्रतीचे बीजी-२ तंत्रज्ञान, बोंडअळीपासून संरक्षण व भरघोस उत्पादनाची खात्री. ४७५ ग्रॅम पॅक.</textarea>
                </div>
            </div>

            <div class="mt-4 pt-3 border-top d-flex gap-2">
                <button type="submit" id="btnSaveProd" class="btn btn-success fw-bold px-4 py-2 rounded-pill shadow-sm">
                    <i class="bi bi-check-circle-fill me-1"></i> Save Product (उत्पादन जतन करा)
                </button>
                <a href="admin-products.html" class="btn btn-light border px-4 py-2 rounded-pill">
                    रद्द करा (Cancel)
                </a>
            </div>

            <div id="saveSuccessAlert" class="alert alert-success mt-3 d-none text-center rounded-3">
                <i class="bi bi-check-circle-fill me-1"></i>
                <strong>उत्पादन यशस्वीरीत्या जतन केले!</strong> उत्पादने यादीकडे नेले जात आहे...
            </div>
        </form>
    </div>
</div>

<script>
function previewProductImg(e) {
    const file = e.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(evt) {
            document.getElementById('imgPreviewEl').src = evt.target.result;
            document.getElementById('imgPreviewText').textContent = file.name;
        };
        reader.readAsDataURL(file);
    }
}

function handleProductSave(e) {
    e.preventDefault();
    const btn = document.getElementById('btnSaveProd');
    const alertBox = document.getElementById('saveSuccessAlert');
    btn.disabled = true;
    btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>जतन होत आहे...';
    alertBox.classList.remove('d-none');
    setTimeout(() => {
        window.location.href = 'admin-products.html';
    }, 800);
}
</script>
""" + foot_html()
    with open(os.path.join(DIST_DIR, "admin-product-form.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated dist/admin-product-form.html")

# 4. ADMIN UDHARI
def build_admin_udhari():
    pills = admin_nav_pills("udhari")
    content = head_html("उधारी खातेवही", "Credit Management") + nav_html("dashboard") + """
<div class="container-fluid px-3 px-lg-4 my-4" style="max-width:1400px;">
    <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-3 mb-4">
        <div>
            <h1 class="h3 fw-bold text-dark m-0 d-flex align-items-center gap-2">
                <span>💰</span> <span class="lang-mr">शेतकरी उधारी व्यवस्थापन व खातेवही</span><span class="lang-en">Customer Credit Ledger</span>
            </h1>
            <p class="text-muted small m-0 mt-1">
                <span class="lang-mr">शेतकऱ्यांनी नेलेल्या वस्तू, उधारी रक्कम, जमा, बाकी व देय तारीख व्यवस्थापन</span>
                <span class="lang-en">Track customer credit balances, payment receipts, due dates and settlements</span>
            </p>
        </div>
        <div>
            <button class="btn btn-success fw-bold px-4 py-2 rounded-pill shadow-sm" onclick="alert('नवीन उधारी नोंद फॉर्म उघडत आहे...')">
                ➕ <span class="lang-mr">+ नवीन उधारी नोंद करा</span><span class="lang-en">+ Add Credit Record</span>
            </button>
        </div>
    </div>
""" + pills + """
    <!-- 3 Summary Metric Cards -->
    <div class="row g-3 mb-4">
        <div class="col-md-4">
            <div class="card border-0 shadow-sm rounded-4 p-3 bg-white h-100">
                <div class="d-flex justify-content-between align-items-start mb-2">
                    <span class="text-muted small fw-bold">एकूण दिलेली उधारी (Total Credit Issued)</span>
                    <div class="rounded-circle d-flex align-items-center justify-content-center" style="width:38px;height:38px;background:#dbeafe;color:#0284c7;"><i class="bi bi-credit-card"></i></div>
                </div>
                <h3 class="fw-bold text-dark mb-1">₹1,12,500</h3>
                <small class="text-muted">चालू हंगामातील एकूण उधारी</small>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card border-0 shadow-sm rounded-4 p-3 bg-white h-100">
                <div class="d-flex justify-content-between align-items-start mb-2">
                    <span class="text-muted small fw-bold">एकूण जमा रक्कम (Total Recovered)</span>
                    <div class="rounded-circle d-flex align-items-center justify-content-center" style="width:38px;height:38px;background:#dcfce7;color:#16a34a;"><i class="bi bi-check-circle-fill"></i></div>
                </div>
                <h3 class="fw-bold text-success mb-1">₹69,700</h3>
                <small class="text-success">६२% रक्कम यशस्वी जमा</small>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card border-0 shadow-sm rounded-4 p-3 bg-white h-100" style="border-left: 4px solid #dc2626 !important;">
                <div class="d-flex justify-content-between align-items-start mb-2">
                    <span class="text-danger small fw-bold">🔴 बाकी उधारी (Outstanding Balance)</span>
                    <div class="rounded-circle d-flex align-items-center justify-content-center" style="width:38px;height:38px;background:#fee2e2;color:#dc2626;"><i class="bi bi-exclamation-triangle-fill"></i></div>
                </div>
                <h3 class="fw-bold text-danger mb-1">₹42,800</h3>
                <small class="text-danger">३ खात्यांची मुदत संपलेली (Overdue)</small>
            </div>
        </div>
    </div>

    <!-- Udhari Table with Mark as Paid option -->
    <div class="card border-0 shadow-sm rounded-4 overflow-hidden bg-white mb-4">
        <div class="card-header bg-white py-3 px-4 border-0 d-flex justify-content-between align-items-center">
            <h5 class="fw-bold mb-0 text-dark"><i class="bi bi-people-fill text-success me-2"></i>ग्राहक उधारी यादी (Customer Credit Accounts)</h5>
            <span class="badge bg-light text-dark border px-3 py-1">१२ सक्रिय खाती</span>
        </div>
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0" style="font-size: 13.5px;">
                <thead class="table-light">
                    <tr>
                        <th class="ps-4">ग्राहक नाव (Customer Name)</th>
                        <th>गाव (Village)</th>
                        <th>नेलेल्या वस्तू (Items Taken)</th>
                        <th class="text-end">एकूण रक्कम</th>
                        <th class="text-end">जमा रक्कम</th>
                        <th class="text-end text-danger">बाकी रक्कम (Amount)</th>
                        <th class="text-center">देय तारीख (Due Date)</th>
                        <th class="text-center">स्थिती (Status)</th>
                        <th class="text-center pe-4" style="width: 170px;">कृती (Mark Paid)</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- Row 1 -->
                    <tr id="udhariRow1">
                        <td class="ps-4">
                            <strong class="text-dark d-block">रमेश पाटील</strong>
                            <small class="text-muted"><i class="bi bi-telephone text-success"></i> ९८२२०१२३४५</small>
                        </td>
                        <td><span class="badge bg-light text-dark border">वैजापूर</span></td>
                        <td>कापूस बियाणे व एनपीके खत</td>
                        <td class="text-end fw-semibold">₹12,500.00</td>
                        <td class="text-end text-success fw-semibold">₹10,000.00</td>
                        <td class="text-end fw-bold text-danger fs-6" id="udhariBal1">₹2,500.00</td>
                        <td class="text-center"><span class="badge bg-light text-dark border">१५ नोव्हेंबर २०२६</span></td>
                        <td class="text-center" id="udhariStatus1"><span class="badge bg-warning text-dark">चालू उधारी (Active)</span></td>
                        <td class="text-center pe-4">
                            <button onclick="markAsPaid(1, 'रमेश पाटील', '2,500.00')" class="btn btn-sm btn-outline-success rounded-pill px-3 py-1 fw-bold shadow-sm" id="btnPaid1">
                                <i class="bi bi-check2-all me-1"></i> Mark as Paid
                            </button>
                        </td>
                    </tr>
                    <!-- Row 2 -->
                    <tr id="udhariRow2">
                        <td class="ps-4">
                            <strong class="text-dark d-block">विलास जगताप</strong>
                            <small class="text-muted"><i class="bi bi-telephone text-success"></i> ९८२३४५६७८०</small>
                        </td>
                        <td><span class="badge bg-light text-dark border">मिरखनगर</span></td>
                        <td>महाधन २४:२४:० (२ बॅग्स)</td>
                        <td class="text-end fw-semibold">₹6,720.00</td>
                        <td class="text-end text-success fw-semibold">₹3,000.00</td>
                        <td class="text-end fw-bold text-danger fs-6" id="udhariBal2">₹3,720.00</td>
                        <td class="text-center"><span class="badge bg-light text-dark border">१० नोव्हेंबर २०२६</span></td>
                        <td class="text-center" id="udhariStatus2"><span class="badge bg-warning text-dark">चालू उधारी</span></td>
                        <td class="text-center pe-4">
                            <button onclick="markAsPaid(2, 'विलास जगताप', '3,720.00')" class="btn btn-sm btn-outline-success rounded-pill px-3 py-1 fw-bold shadow-sm" id="btnPaid2">
                                <i class="bi bi-check2-all me-1"></i> Mark as Paid
                            </button>
                        </td>
                    </tr>
                    <!-- Row 3 -->
                    <tr id="udhariRow3">
                        <td class="ps-4">
                            <strong class="text-dark d-block">सचिन काळे</strong>
                            <small class="text-muted"><i class="bi bi-telephone text-success"></i> ९४२१५५६६७७</small>
                        </td>
                        <td><span class="badge bg-light text-dark border">लाडगाव</span></td>
                        <td>फाल्कन बॅटरी स्प्रे पंप</td>
                        <td class="text-end fw-semibold">₹2,800.00</td>
                        <td class="text-end text-success fw-semibold">₹0.00</td>
                        <td class="text-end fw-bold text-danger fs-6" id="udhariBal3">₹2,800.00</td>
                        <td class="text-center"><span class="badge bg-danger text-white">२५ ऑक्टोबर (Overdue)</span></td>
                        <td class="text-center" id="udhariStatus3"><span class="badge bg-danger">थकबाकी (Overdue)</span></td>
                        <td class="text-center pe-4">
                            <button onclick="markAsPaid(3, 'सचिन काळे', '2,800.00')" class="btn btn-sm btn-outline-success rounded-pill px-3 py-1 fw-bold shadow-sm" id="btnPaid3">
                                <i class="bi bi-check2-all me-1"></i> Mark as Paid
                            </button>
                        </td>
                    </tr>
                    <!-- Row 4 -->
                    <tr id="udhariRow4">
                        <td class="ps-4">
                            <strong class="text-dark d-block">गजानन थोरात</strong>
                            <small class="text-muted"><i class="bi bi-telephone text-success"></i> ९८९०११२२३३</small>
                        </td>
                        <td><span class="badge bg-light text-dark border">शिऊर</span></td>
                        <td>१०:२६:२६ ग्रोमोर व सिजेंटा ॲम्प्लिगो</td>
                        <td class="text-end fw-semibold">₹4,500.00</td>
                        <td class="text-end text-success fw-semibold">₹4,500.00</td>
                        <td class="text-end fw-bold text-success fs-6" id="udhariBal4">₹0.00</td>
                        <td class="text-center"><span class="badge bg-light text-dark border">२० ऑक्टोबर २०२६</span></td>
                        <td class="text-center" id="udhariStatus4"><span class="badge bg-success">पूर्ण भरली (Paid)</span></td>
                        <td class="text-center pe-4">
                            <span class="text-success small fw-bold"><i class="bi bi-check-circle-fill me-1"></i>पूर्ण भरले</span>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>

<script>
function markAsPaid(rowId, name, amount) {
    if (confirm(name + ' यांचे उधारी खाते पूर्ण भरले म्हणून चिन्हांकित करायचे आहे का? (रक्कम: ₹' + amount + ')')) {
        document.getElementById('udhariBal' + rowId).textContent = '₹0.00';
        document.getElementById('udhariBal' + rowId).className = 'text-end fw-bold text-success fs-6';
        document.getElementById('udhariStatus' + rowId).innerHTML = '<span class="badge bg-success">पूर्ण भरली (Paid in Full)</span>';
        const btn = document.getElementById('btnPaid' + rowId);
        btn.disabled = true;
        btn.className = 'btn btn-sm btn-success rounded-pill px-3 py-1 fw-bold';
        btn.innerHTML = '<i class="bi bi-check-circle-fill me-1"></i> Paid!';
    }
}
</script>
""" + foot_html()
    with open(os.path.join(DIST_DIR, "admin-udhari.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated dist/admin-udhari.html")

# 5. ADMIN INVENTORY & EXPIRY
def build_admin_inventory():
    pills = admin_nav_pills("inventory")
    content = head_html("साठा व एक्सपायरी", "Inventory & Expiry") + nav_html("dashboard") + """
<div class="container-fluid px-3 px-lg-4 my-4" style="max-width:1400px;">
    <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-3 mb-4">
        <div>
            <h1 class="h3 fw-bold text-dark m-0 d-flex align-items-center gap-2">
                <span>📊</span> <span class="lang-mr">इन्व्हेंटरी व मुदत समाप्ती ट्रॅकिंग (Inventory & Expiry)</span><span class="lang-en">Inventory & Expiry Tracking</span>
            </h1>
            <p class="text-muted small m-0 mt-1">
                <span class="lang-mr">रंग संकेतानुसार साठा पातळी (लाल=कमी, पिवळा=सावधानता, हिरवा=पुरेसा) आणि बॅच एक्सपायरी</span>
                <span class="lang-en">Stock levels with color coding (red=low, yellow=warning, green=ok) and batch expiry tracking</span>
            </p>
        </div>
        <div class="d-flex gap-2">
            <a href="admin-product-form.html" class="btn btn-success fw-bold px-4 py-2 rounded-pill shadow-sm">
                ➕ <span class="lang-mr">Add Product (नवीन उत्पादन)</span><span class="lang-en">Add Product</span>
            </a>
        </div>
    </div>
""" + pills + """
    <!-- 1. STOCK LEVELS TABLE WITH COLOR CODING -->
    <div class="card border-0 shadow-sm rounded-4 overflow-hidden bg-white mb-4">
        <div class="card-header bg-white py-3 px-4 border-0 d-flex justify-content-between align-items-center flex-wrap gap-2">
            <div>
                <h5 class="fw-bold mb-0 text-dark">
                    <i class="bi bi-bar-chart-fill text-success me-2"></i>
                    <span class="lang-mr">साठा पातळी व रंग संकेत (Stock Levels with Color Coding)</span>
                    <span class="lang-en">Stock Levels with Color Coding</span>
                </h5>
                <small class="text-muted">
                    Color Legend: 
                    <span class="badge bg-danger ms-1">🔴 Red = Low</span>
                    <span class="badge bg-warning text-dark ms-1">🟡 Yellow = Warning</span>
                    <span class="badge bg-success ms-1">🟢 Green = OK</span>
                </small>
            </div>
            <a href="admin-products.html" class="btn btn-sm btn-outline-success rounded-pill px-3">कॅटलॉग पाहा</a>
        </div>
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0" style="font-size: 13.5px;">
                <thead class="table-light">
                    <tr>
                        <th class="ps-4">उत्पादनाचे नाव (Product)</th>
                        <th>कॅटेगरी (Category)</th>
                        <th class="text-center">किमान मर्यादा (Min Stock)</th>
                        <th class="text-center">सध्याचा साठा (Current Stock)</th>
                        <th class="text-center">स्थिती (Stock Level)</th>
                        <th class="text-center pe-4">कृती (Action)</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- Red / Low row -->
                    <tr style="background: rgba(239, 68, 68, 0.04);">
                        <td class="ps-4">
                            <strong class="text-dark d-block">फाल्कन १६L बॅटरी स्प्रे पंप</strong>
                            <small class="text-muted">Falcon 16L Battery Sprayer</small>
                        </td>
                        <td><span class="badge bg-light text-dark border">कृषी अवजारे</span></td>
                        <td class="text-center fw-semibold text-secondary">5 नग</td>
                        <td class="text-center">
                            <!-- RED BADGE -->
                            <span class="badge bg-danger text-white px-3 py-2 fs-6 rounded-pill">
                                3 नग
                            </span>
                        </td>
                        <td class="text-center">
                            <span class="badge bg-danger-subtle text-danger border border-danger px-3 py-1 rounded-pill fw-bold">
                                🔴 कमी साठा (Low)
                            </span>
                        </td>
                        <td class="text-center pe-4">
                            <a href="admin-product-form.html?id=3" class="btn btn-sm btn-danger rounded-pill px-3 py-1 fw-bold">
                                ⚠️ रिस्टॉक करा
                            </a>
                        </td>
                    </tr>

                    <!-- Yellow / Warning row -->
                    <tr style="background: rgba(245, 158, 11, 0.04);">
                        <td class="ps-4">
                            <strong class="text-dark d-block">कोरोमंडेल १०:२६:२६ ग्रोमोर खत</strong>
                            <small class="text-muted">Coromandel Gromor 10:26:26</small>
                        </td>
                        <td><span class="badge bg-light text-dark border">खते (Fertilizers)</span></td>
                        <td class="text-center fw-semibold text-secondary">5 बॅग्स</td>
                        <td class="text-center">
                            <!-- YELLOW BADGE -->
                            <span class="badge bg-warning text-dark px-3 py-2 fs-6 rounded-pill">
                                7 बॅग्स
                            </span>
                        </td>
                        <td class="text-center">
                            <span class="badge bg-warning-subtle text-warning-emphasis border border-warning px-3 py-1 rounded-pill fw-bold">
                                🟡 मध्यम साठा (Warning)
                            </span>
                        </td>
                        <td class="text-center pe-4">
                            <a href="admin-product-form.html?id=4" class="btn btn-sm btn-outline-warning rounded-pill px-3 py-1 fw-bold">
                                साठा वाढवा
                            </a>
                        </td>
                    </tr>

                    <!-- Green / OK row 1 -->
                    <tr>
                        <td class="ps-4">
                            <strong class="text-dark d-block">माहिको बीजी-२ कापूस बियाणे</strong>
                            <small class="text-muted">Mahyco BG-II Cotton Seeds (475g)</small>
                        </td>
                        <td><span class="badge bg-light text-dark border">बियाणे (Seeds)</span></td>
                        <td class="text-center fw-semibold text-secondary">10 बॅग्स</td>
                        <td class="text-center">
                            <!-- GREEN BADGE -->
                            <span class="badge bg-success text-white px-3 py-2 fs-6 rounded-pill">
                                45 बॅग्स
                            </span>
                        </td>
                        <td class="text-center">
                            <span class="badge bg-success-subtle text-success border border-success px-3 py-1 rounded-pill fw-bold">
                                🟢 पुरेसा साठा (OK)
                            </span>
                        </td>
                        <td class="text-center pe-4">
                            <span class="text-success small fw-semibold"><i class="bi bi-check-circle-fill me-1"></i>सुरक्षित साठा</span>
                        </td>
                    </tr>

                    <!-- Green / OK row 2 -->
                    <tr>
                        <td class="ps-4">
                            <strong class="text-dark d-block">महाधन २४:२४:० खत</strong>
                            <small class="text-muted">Mahadhan 24:24:0 Fertilizer (50kg)</small>
                        </td>
                        <td><span class="badge bg-light text-dark border">खते (Fertilizers)</span></td>
                        <td class="text-center fw-semibold text-secondary">10 बॅग्स</td>
                        <td class="text-center">
                            <!-- GREEN BADGE -->
                            <span class="badge bg-success text-white px-3 py-2 fs-6 rounded-pill">
                                28 बॅग्स
                            </span>
                        </td>
                        <td class="text-center">
                            <span class="badge bg-success-subtle text-success border border-success px-3 py-1 rounded-pill fw-bold">
                                🟢 पुरेसा साठा (OK)
                            </span>
                        </td>
                        <td class="text-center pe-4">
                            <span class="text-success small fw-semibold"><i class="bi bi-check-circle-fill me-1"></i>सुरक्षित साठा</span>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- 2. EXPIRY TRACKING SECTION -->
    <div class="card border-0 shadow-sm rounded-4 overflow-hidden bg-white mb-4">
        <div class="card-header bg-white py-3 px-4 border-0 d-flex justify-content-between align-items-center">
            <div>
                <h5 class="fw-bold mb-0 text-dark">
                    <i class="bi bi-calendar-x-fill text-danger me-2"></i>
                    <span class="lang-mr">मुदत समाप्ती ट्रॅकिंग (Expiry Tracking)</span>
                    <span class="lang-en">Product Batch Expiry Tracking</span>
                </h5>
                <small class="text-muted">रासायनिक औषधे, बियाणे व विद्राव्य खतांची एक्सपायरी स्थिती</small>
            </div>
            <span class="badge bg-light text-dark border px-3 py-1">४ बॅचेस सक्रिय</span>
        </div>
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0" style="font-size: 13.5px;">
                <thead class="table-light">
                    <tr>
                        <th class="ps-4">उत्पादन (Product)</th>
                        <th>बॅच नंबर (Batch No)</th>
                        <th>उत्पादन तारीख (Mfg Date)</th>
                        <th>मुदत समाप्ती (Expiry Date)</th>
                        <th class="text-center">स्थिती (Expiry Status)</th>
                        <th class="text-center pe-4">उपलब्ध साठा</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="ps-4">
                            <strong class="text-dark d-block">सिजेंटा ॲम्प्लिगो कीटकनाशक (100ml)</strong>
                            <small class="text-muted">Syngenta Ampligo</small>
                        </td>
                        <td><code>BCH-2025-09</code></td>
                        <td>सप्टेंबर २०२५</td>
                        <td><span class="badge bg-light text-dark border">२८ फेब्रुवारी २०२७</span></td>
                        <td class="text-center">
                            <span class="badge bg-success text-white px-3 py-1 rounded-pill">
                                ✅ सुरक्षित (Safe)
                            </span>
                        </td>
                        <td class="text-center pe-4 fw-bold">18 बाटल्या</td>
                    </tr>
                    <tr>
                        <td class="ps-4">
                            <strong class="text-dark d-block">बायर कॉन्फिडोर कीटकनाशक (50ml)</strong>
                            <small class="text-muted">Bayer Confidor</small>
                        </td>
                        <td><code>BCH-2024-11</code></td>
                        <td>नोव्हेंबर २०२४</td>
                        <td><span class="badge bg-warning text-dark border border-warning">३० नोव्हेंबर २०२६</span></td>
                        <td class="text-center">
                            <span class="badge bg-warning text-dark px-3 py-1 rounded-pill">
                                ⚠️ लवकरच संपणार (Expiring Soon - 30 days)
                            </span>
                        </td>
                        <td class="text-center pe-4 fw-bold text-warning">8 बाटल्या</td>
                    </tr>
                    <tr>
                        <td class="ps-4">
                            <strong class="text-dark d-block">माहिको बीजी-२ कापूस बियाणे</strong>
                            <small class="text-muted">Mahyco BG-II Cotton Seeds</small>
                        </td>
                        <td><code>MAH-2026-A1</code></td>
                        <td>जानेवारी २०२६</td>
                        <td><span class="badge bg-light text-dark border">३१ डिसेंबर २०२६</span></td>
                        <td class="text-center">
                            <span class="badge bg-success text-white px-3 py-1 rounded-pill">
                                ✅ सुरक्षित (Safe)
                            </span>
                        </td>
                        <td class="text-center pe-4 fw-bold">45 बॅग्स</td>
                    </tr>
                    <tr style="background: rgba(239,68,68,0.03);">
                        <td class="ps-4">
                            <strong class="text-dark d-block">जुन्या बॅचचे मायक्रोन्युट्रिएंट टॉनिक</strong>
                            <small class="text-muted">Sample Micronutrient Tonic</small>
                        </td>
                        <td><code>TONIC-2024-X</code></td>
                        <td>मार्च २०२४</td>
                        <td><span class="badge bg-danger text-white">१५ ऑक्टोबर २०२६</span></td>
                        <td class="text-center">
                            <span class="badge bg-danger text-white px-3 py-1 rounded-pill">
                                ❌ मुदत संपली (Expired)
                            </span>
                        </td>
                        <td class="text-center pe-4 fw-bold text-danger">2 बाटल्या (बाजूला काढा)</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
""" + foot_html()
    with open(os.path.join(DIST_DIR, "admin-inventory.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated dist/admin-inventory.html")

if __name__ == "__main__":
    build_admin_dashboard()
    build_admin_products()
    build_admin_product_form()
    build_admin_udhari()
    build_admin_inventory()
    print("All 5 Admin Panel pages built successfully!")
