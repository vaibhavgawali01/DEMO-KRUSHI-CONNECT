# -*- coding: utf-8 -*-
import os
import sys

from build_site import head_html, nav_html, foot_html, DIST_DIR

print("Generating all 14 static pages...")

# 1. INDEX
from update_home_page import build_home_page
build_home_page()
print("1. index.html")

# 2. PRODUCTS
products_content = head_html("उत्पादने", "Products Catalog") + nav_html("products") + """
<div class="container my-4">
    <div class="row g-4">
        <!-- Sidebar Filters -->
        <div class="col-lg-3">
            <div class="card border-0 shadow-sm rounded-4">
                <div class="card-header bg-success text-white py-3 rounded-top-4 d-flex justify-content-between align-items-center">
                    <h6 class="mb-0 fw-bold"><i class="bi bi-funnel me-2"></i><span class="lang-mr">फिल्टर</span><span class="lang-en">Filter Products</span></h6>
                    <button type="button" onclick="resetFilters()" class="btn btn-sm text-white-50 p-0 text-decoration-none"><span class="lang-mr">रिसेट</span><span class="lang-en">Reset</span></button>
                </div>
                <div class="card-body p-3">
                    <div class="mb-3">
                        <label class="form-label fw-bold text-success small text-uppercase"><span class="lang-mr">शोध</span><span class="lang-en">Search</span></label>
                        <input type="text" id="searchInput" onkeyup="filterProducts()" class="form-control form-control-sm"
                               data-placeholder-mr="बियाणे, खते किंवा ब्रँड..."
                               data-placeholder-en="Search seeds, fertilizers..."
                               placeholder="बियाणे, खते किंवा ब्रँड...">
                    </div>
                    <div class="mb-4">
                        <label class="form-label fw-bold text-success small text-uppercase"><span class="lang-mr">वर्गवारी</span><span class="lang-en">Category</span></label>
                        <div class="d-flex flex-column gap-1">
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="catFilter" id="cat_all" value="all" checked onchange="filterProducts()">
                                <label class="form-check-label small" for="cat_all"><span class="lang-mr">सर्व वर्गवारी</span><span class="lang-en">All Categories</span></label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="catFilter" id="cat_seeds" value="seeds" onchange="filterProducts()">
                                <label class="form-check-label small" for="cat_seeds"><span class="lang-mr">🌾 बियाणे</span><span class="lang-en">🌾 Seeds</span></label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="catFilter" id="cat_fert" value="fertilizers" onchange="filterProducts()">
                                <label class="form-check-label small" for="cat_fert"><span class="lang-mr">🧪 खते</span><span class="lang-en">🧪 Fertilizers</span></label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="catFilter" id="cat_pest" value="pesticides" onchange="filterProducts()">
                                <label class="form-check-label small" for="cat_pest"><span class="lang-mr">🐛 कीटकनाशके</span><span class="lang-en">🐛 Pesticides</span></label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="catFilter" id="cat_tools" value="tools" onchange="filterProducts()">
                                <label class="form-check-label small" for="cat_tools"><span class="lang-mr">🔧 शेती अवजारे</span><span class="lang-en">🔧 Farm Tools</span></label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="catFilter" id="cat_drip" value="drip" onchange="filterProducts()">
                                <label class="form-check-label small" for="cat_drip"><span class="lang-mr">💧 ठिबक सिंचन</span><span class="lang-en">💧 Drip</span></label>
                            </div>
                        </div>
                    </div>
                    <div class="mb-4">
                        <label class="form-label fw-bold text-success small text-uppercase"><span class="lang-mr">कमाल किंमत</span><span class="lang-en">Max Price</span></label>
                        <input type="range" class="form-range" id="priceRange" min="200" max="4000" step="100" value="4000" oninput="updatePrice(this.value)">
                        <div class="d-flex justify-content-between small text-muted"><span>₹200</span><span id="priceVal" class="fw-bold text-success">₹4000</span></div>
                    </div>
                </div>
            </div>
        </div>

        <div class="col-lg-9">
            <div class="d-flex justify-content-between align-items-center mb-3">
                <h5 class="fw-bold text-dark mb-0">
                    <span class="lang-mr">उपलब्ध कृषी उत्पादने</span>
                    <span class="lang-en">Available Agri Products</span>
                    (<span id="prodCount">8</span>)
                </h5>
                <select id="sortSelect" onchange="filterProducts()" class="form-select form-select-sm w-auto">
                    <option value="newest">नवीन उत्पादने (Newest)</option>
                    <option value="price_asc">किंमत: कमी ते जास्त (Price Low-High)</option>
                    <option value="price_desc">किंमत: जास्त ते कमी (Price High-Low)</option>
                </select>
            </div>
            <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4" id="productsGrid"></div>
        </div>
    </div>
</div>

<script>
const productsData = [
    { id: 1, name_mr: "माहिको बीजी-२ कापूस बियाणे (475g)", name_en: "Mahyco BG-II Cotton Seeds (475g)", company: "Mahyco Seeds", cat: "seeds", price: 820, oldPrice: 864, img: "images/cotton_seeds.jpg", tag_mr: "उत्कृष्ट उगवणक्षमता", tag_en: "High Germination" },
    { id: 2, name_mr: "जेएस ३३५ प्रमाणित सोयाबीन बियाणे (30 Kg)", name_en: "JS-335 Certified Soybean Seeds (30 Kg)", company: "Mahabeej", cat: "seeds", price: 2700, oldPrice: 2850, img: "images/soybean_seeds.jpg", tag_mr: "प्रमाणित बियाणे", tag_en: "Govt Certified" },
    { id: 3, name_mr: "महाधन २४:२४:० खत (५० किलो)", name_en: "Mahadhan 24:24:0 Fertilizer (50 Kg)", company: "Deepak Fertilisers", cat: "fertilizers", price: 1680, oldPrice: 1750, img: "images/fertilizer_npk.jpg", tag_mr: "NPK कॉम्प्लेक्स", tag_en: "NPK Complex" },
    { id: 4, name_mr: "इफको नीम कोटेड युरिया (४५ किलो)", name_en: "IFFCO Neem Coated Urea (45 Kg)", company: "IFFCO Ltd", cat: "fertilizers", price: 266, oldPrice: 266, img: "images/urea_bag.jpg", tag_mr: "शासकीय अनुदानित", tag_en: "Govt Subsidized" },
    { id: 5, name_mr: "कोरोमंडल ग्रोमोर १०:२६:२६ खत (50 Kg)", name_en: "Coromandel Gromor 10:26:26 (50 Kg)", company: "Coromandel", cat: "fertilizers", price: 1750, oldPrice: 1820, img: "images/fertilizer_npk.jpg", tag_mr: "पोटॅशयुक्त खत", tag_en: "High Potash" },
    { id: 6, name_mr: "फाल्कन १६ लिटर १२V बॅटरी स्प्रे पंप", name_en: "Falcon 16L 12V Battery Sprayer Pump", company: "Falcon Agri", cat: "tools", price: 2850, oldPrice: 3200, img: "images/battery_sprayer.jpg", tag_mr: "डबल मोटर तंत्रज्ञान", tag_en: "Dual Motor" },
    { id: 7, name_mr: "जैन ठिबक १६ मिमी लॅटरल पाईप (४०० मीटर)", name_en: "Jain Drip 16mm Lateral Pipe (400m)", company: "Jain Irrigation", cat: "drip", price: 3350, oldPrice: 3600, img: "images/saptashrungi_shop.jpg", tag_mr: "ISI प्रमाणित", tag_en: "ISI Certified" },
    { id: 8, name_mr: "लोक-१ प्रमाणित गहू बियाणे (४० किलो)", name_en: "Lok-1 Certified Wheat Seeds (40 Kg)", company: "Mahabeej", cat: "seeds", price: 1350, oldPrice: 1450, img: "images/wheat_seeds.jpg", tag_mr: "प्रमाणित बियाणे", tag_en: "Govt Certified" }
];

function updatePrice(val) { document.getElementById('priceVal').textContent = '₹' + val; filterProducts(); }
function resetFilters() {
    document.getElementById('searchInput').value = '';
    document.getElementById('cat_all').checked = true;
    document.getElementById('priceRange').value = 4000;
    document.getElementById('priceVal').textContent = '₹4000';
    document.getElementById('sortSelect').value = 'newest';
    filterProducts();
}
function filterProducts() {
    const q = document.getElementById('searchInput').value.toLowerCase();
    const cat = document.querySelector('input[name="catFilter"]:checked').value;
    const maxP = parseFloat(document.getElementById('priceRange').value);
    const sort = document.getElementById('sortSelect').value;

    let filtered = productsData.filter(p => {
        const matchesQ = p.name_mr.toLowerCase().includes(q) || p.name_en.toLowerCase().includes(q) || p.company.toLowerCase().includes(q);
        const matchesCat = (cat === 'all') || (p.cat === cat);
        const matchesP = p.price <= maxP;
        return matchesQ && matchesCat && matchesP;
    });

    if (sort === 'price_asc') filtered.sort((a,b) => a.price - b.price);
    if (sort === 'price_desc') filtered.sort((a,b) => b.price - a.price);

    document.getElementById('prodCount').textContent = filtered.length;
    const grid = document.getElementById('productsGrid');
    grid.innerHTML = '';

    if (filtered.length === 0) {
        grid.innerHTML = '<div class="col-12 py-5 text-center text-muted"><i class="bi bi-search fs-1 d-block mb-2"></i><span class="lang-mr">कोणतीही उत्पादने सापडली नाहीत.</span><span class="lang-en">No products match your criteria.</span></div>';
        return;
    }

    filtered.forEach(p => {
        const col = document.createElement('div');
        col.className = 'col';
        col.innerHTML = `
            <div class="product-featured-card h-100 d-flex flex-column bg-white shadow-sm rounded-4 overflow-hidden">
                <div class="product-featured-img-wrap position-relative">
                    <span class="badge bg-success position-absolute top-0 end-0 m-2 rounded-pill px-2 py-1"><span class="lang-mr">${p.tag_mr}</span><span class="lang-en">${p.tag_en}</span></span>
                    <img src="${p.img}" alt="${p.name_en}" class="w-100" style="height:190px;object-fit:cover;" onerror="this.src='images/saptashrungi_shop.jpg'">
                </div>
                <div class="product-featured-content p-3 d-flex flex-column flex-grow-1">
                    <div class="text-muted small fw-semibold text-uppercase">${p.company}</div>
                    <h6 class="fw-bold my-2 flex-grow-1">
                        <span class="lang-mr">${p.name_mr}</span>
                        <span class="lang-en">${p.name_en}</span>
                    </h6>
                    <div class="product-featured-price-row mb-3">
                        <span class="fs-4 fw-bold text-success">₹${p.price.toLocaleString('en-IN')}</span>
                        ${p.oldPrice > p.price ? `<span class="text-decoration-line-through text-muted ms-2 small">₹${p.oldPrice.toLocaleString('en-IN')}</span>` : ''}
                    </div>
                    <div class="d-flex justify-content-between align-items-center mt-auto pt-2 border-top">
                        <span class="badge bg-success-subtle text-success"><i class="bi bi-check-circle me-1"></i><span class="lang-mr">उपलब्ध</span><span class="lang-en">In Stock</span></span>
                        <a href="https://wa.me/918600813827?text=नमस्कार,%20मला%20${encodeURIComponent(p.name_mr)}%20खरेदी%20करायचे%20आहे." target="_blank" class="btn btn-sm btn-success rounded-pill px-3">
                            <i class="bi bi-whatsapp me-1"></i><span class="lang-mr">मागवा</span><span class="lang-en">Order</span>
                        </a>
                    </div>
                </div>
            </div>
        `;
        grid.appendChild(col);
    });
}
document.addEventListener('DOMContentLoaded', filterProducts);
</script>
""" + foot_html()
with open(os.path.join(DIST_DIR, "products.html"), "w", encoding="utf-8") as f:
    f.write(products_content)
print("2. products.html")

# 3. FERTILIZER CALC
calc_content = head_html("खत कॅल्क्युलेटर", "Fertilizer Calculator") + nav_html("advisory") + """
<div class="container my-4">
    <div class="text-center mb-4">
        <span class="badge bg-success-subtle text-success border border-success-subtle px-3 py-1 rounded-pill mb-2 fw-semibold">
            <i class="bi bi-cpu me-1"></i><span class="lang-mr">स्मार्ट कृषी सल्ला इंजिन</span><span class="lang-en">Smart Agronomy Engine</span>
        </span>
        <h2 class="fw-bold text-success"><span class="lang-mr">खत कॅल्क्युलेटर</span><span class="lang-en">Fertilizer Dosage Calculator</span></h2>
        <p class="text-muted"><span class="lang-mr">पीक व क्षेत्रफळानुसार खतांचे अचूक प्रमाण.</span><span class="lang-en">Scientific recommendation based on crop and acreage.</span></p>
    </div>
    <div class="row g-4 mb-5">
        <div class="col-lg-5">
            <div class="card border-0 shadow-sm rounded-4 p-4 bg-white">
                <form id="calcForm" onsubmit="calculateFertilizer(event)">
                    <div class="mb-3">
                        <label class="form-label fw-bold text-success small text-uppercase">पीक निवडा (Crop)</label>
                        <select id="crop" class="form-select">
                            <option value="cotton" selected>कापूस (Cotton)</option>
                            <option value="sugarcane">ऊस (Sugarcane)</option>
                            <option value="soybean">सोयाबीन (Soybean)</option>
                            <option value="wheat">गहू (Wheat)</option>
                            <option value="onion">कांदा (Onion)</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label class="form-label fw-bold text-success small text-uppercase">क्षेत्रफळ (Acres)</label>
                        <input type="number" step="0.5" min="0.5" max="100" id="acres" class="form-control" value="2" required onchange="calculateFertilizer()">
                    </div>
                    <button type="submit" class="btn btn-krushi w-100 fw-bold py-2 rounded-pill shadow-sm">
                        <i class="bi bi-calculator me-1"></i> <span class="lang-mr">खत प्रमाण काढा</span><span class="lang-en">Calculate Bags</span>
                    </button>
                </form>
            </div>
        </div>
        <div class="col-lg-7">
            <div class="card border-0 shadow-sm rounded-4 p-4 bg-white">
                <div class="alert alert-success d-flex align-items-center gap-2 mb-4">
                    <i class="bi bi-info-circle-fill fs-5"></i>
                    <span id="summaryText"><span class="lang-mr">शिफारस केलेले खतांचे प्रमाण खालीलप्रमाणे आहे:</span><span class="lang-en">Recommended dosage as per university agronomy norms:</span></span>
                </div>
                <div class="row g-3 text-center mb-4" id="bagsRow"></div>
                <div class="text-center pt-2">
                    <a id="btnOrderFert" href="https://wa.me/918600813827" target="_blank" class="btn btn-outline-success rounded-pill px-4 fw-semibold">
                        <i class="bi bi-whatsapp me-1"></i> <span class="lang-mr">ही खते दुकानातून मागवा</span><span class="lang-en">Order on WhatsApp</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>
<script>
function calculateFertilizer(e) {
    if(e) e.preventDefault();
    const crop = document.getElementById('crop').value;
    const acres = parseFloat(document.getElementById('acres').value) || 1;
    let urea = Math.round(acres * 2.5);
    let dap = Math.round(acres * 1.5);
    let mop = Math.round(acres * 1.0);
    let npk = Math.round(acres * 2.0);
    if(crop === 'sugarcane'){ urea = Math.round(acres*5.5); dap = Math.round(acres*3); mop = Math.round(acres*3); npk = Math.round(acres*4); }
    else if(crop === 'soybean'){ urea = Math.round(acres*1); dap = Math.round(acres*2); mop = Math.round(acres*1); npk = Math.round(acres*1.5); }
    
    document.getElementById('bagsRow').innerHTML = `
        <div class="col-6 col-md-3"><div class="p-3 border rounded-3"><div class="fs-2 fw-bold text-success">${urea}</div><small>युरिया / Urea</small></div></div>
        <div class="col-6 col-md-3"><div class="p-3 border rounded-3"><div class="fs-2 fw-bold text-primary">${dap}</div><small>DAP 18:46:0</small></div></div>
        <div class="col-6 col-md-3"><div class="p-3 border rounded-3"><div class="fs-2 fw-bold text-warning">${mop}</div><small>पोटॅश / MOP</small></div></div>
        <div class="col-6 col-md-3"><div class="p-3 border rounded-3"><div class="fs-2 fw-bold text-info">${npk}</div><small>10:26:26 NPK</small></div></div>
    `;
    document.getElementById('btnOrderFert').href = 'https://wa.me/918600813827?text=' + encodeURIComponent(`नमस्कार, मला ${acres} एकरसाठी खते खरेदी करायची आहेत.`);
}
document.addEventListener('DOMContentLoaded', calculateFertilizer);
</script>
""" + foot_html()
with open(os.path.join(DIST_DIR, "fertilizer-calc.html"), "w", encoding="utf-8") as f:
    f.write(calc_content)
print("3. fertilizer-calc.html")

# 4. WEATHER
weather_content = head_html("हवामान अंदाज", "Weather Forecast") + nav_html("advisory") + """
<div class="container my-4">
    <div class="text-center mb-4">
        <span class="badge bg-primary-subtle text-primary px-3 py-1 rounded-pill mb-2 fw-semibold"><i class="bi bi-cloud-sun me-1"></i>हवामान व सल्ला</span>
        <h2 class="fw-bold text-success"><span class="lang-mr">हवामान अंदाज</span><span class="lang-en">Weather Forecast</span></h2>
    </div>
    <div class="row justify-content-center mb-4">
        <div class="col-md-6 d-flex gap-2">
            <input type="text" id="cityInput" class="form-control" value="वैजापूर (Vaijapur)">
            <button onclick="searchWeather()" class="btn btn-krushi px-4">शोधा</button>
        </div>
    </div>
    <div class="row justify-content-center mb-5">
        <div class="col-lg-8">
            <div class="card border-0 shadow-sm rounded-4 text-white p-4" style="background: linear-gradient(135deg, #1565c0, #0288d1);">
                <div class="d-flex justify-content-between align-items-center mb-3">
                    <h3 class="fw-bold mb-0" id="weatherCityName">वैजापूर (Vaijapur)</h3>
                    <span class="badge bg-light text-dark px-3 py-1">Live Advisory</span>
                </div>
                <div class="row align-items-center my-3">
                    <div class="col-md-6"><h1 class="display-3 fw-bold mb-0">29°C</h1><p class="lead mb-0 text-white-50">अंशतः ढगाळ व कोरडे</p></div>
                    <div class="col-md-6 bg-white bg-opacity-10 p-3 rounded-3">
                        <div class="d-flex justify-content-between py-1 border-bottom border-light border-opacity-25"><span>पाऊस:</span><strong>20%</strong></div>
                        <div class="d-flex justify-content-between py-1 border-bottom border-light border-opacity-25"><span>आर्द्रता:</span><strong>65%</strong></div>
                        <div class="d-flex justify-content-between py-1"><span>वारा:</span><strong>12 km/h</strong></div>
                    </div>
                </div>
                <div class="bg-warning text-dark p-3 rounded-3 fw-semibold small mt-3">
                    <i class="bi bi-info-circle-fill me-2"></i>फवारणी सल्ला: आज वाऱ्याचा वेग अनुकूल असून फवारणीसाठी योग्य वेळ आहे.
                </div>
            </div>
        </div>
    </div>
</div>
""" + foot_html()
with open(os.path.join(DIST_DIR, "weather.html"), "w", encoding="utf-8") as f:
    f.write(weather_content)
print("4. weather.html")

# 5. FARMING TIPS
tips_content = head_html("पीक सल्ला", "Farming Tips") + nav_html("advisory") + """
<div class="container my-4">
    <div class="text-center mb-5">
        <span class="badge bg-success px-3 py-1 rounded-pill mb-2">कृषी तज्ज्ञ सल्ला</span>
        <h2 class="fw-bold text-success"><span class="lang-mr">पीक संरक्षण व कीड नियंत्रण</span><span class="lang-en">Crop Care & Pest Advice</span></h2>
    </div>
    <div class="row g-4 mb-5">
        <div class="col-md-6">
            <div class="card h-100 border-0 shadow-sm rounded-4 p-4 bg-white">
                <span class="badge bg-success w-auto d-inline-block mb-2">कापूस (Cotton)</span>
                <h5 class="fw-bold">पातेगळ व बोंड वाढ टप्पा</h5>
                <p class="text-muted small">कापूस पिकात पातेगळ रोखण्यासाठी बोरॉन (१ ग्रॅम/लिटर) आणि ००:५२:३४ ची फवारणी करावी. बोंडअळीसाठी कामगंध सापळे लावावेत.</p>
            </div>
        </div>
        <div class="col-md-6">
            <div class="card h-100 border-0 shadow-sm rounded-4 p-4 bg-white">
                <span class="badge bg-success w-auto d-inline-block mb-2">सोयाबीन (Soybean)</span>
                <h5 class="fw-bold">शेंगा भरण्याचा टप्पा</h5>
                <p class="text-muted small">शेंगांमध्ये दाणा भरताना पोटॅशियम नायट्रेट (१३:००:४५ - १ किलो/१०० लिटर) फवारावे, ज्यामुळे दाण्याचा आकार मोठा होतो.</p>
            </div>
        </div>
    </div>
</div>
""" + foot_html()
with open(os.path.join(DIST_DIR, "farming-tips.html"), "w", encoding="utf-8") as f:
    f.write(tips_content)
print("5. farming-tips.html")

# 6. ABOUT
about_content = head_html("आमच्याबद्दल", "About Us") + nav_html("about") + """
<div class="container my-5">
    <div class="text-center mb-5">
        <h2 class="fw-bold text-success"><span class="lang-mr">सप्तशृंगी ॲग्रो सर्व्हिसेस, मिरखनगर</span><span class="lang-en">Saptashrungi Agro Services</span></h2>
        <p class="text-muted">मिरखनगर, वैजापूर येथील अग्रगण्य व अधिकृत कृषी सेवा केंद्र</p>
    </div>
    <div class="row align-items-center g-4">
        <div class="col-md-6">
            <p class="text-muted" style="line-height:1.8;">
                सप्तशृंगी ॲग्रो सर्व्हिसेस हे मिरखनगर, वैजापूर येथील अधिकृत कृषी केंद्र आहे. येथे १००% प्रमाणित बियाणे, खते, कीटकनाशके आणि आधुनिक ठिबक सिंचन साहित्य रास्त दरात उपलब्ध आहे.
            </p>
        </div>
        <div class="col-md-6">
            <img src="images/saptashrungi_shop.jpg" alt="Shop" class="img-fluid rounded-4 shadow-sm" onerror="this.src='images/saptashrungi_logo_round.jpg'">
        </div>
    </div>
</div>
""" + foot_html()
with open(os.path.join(DIST_DIR, "about.html"), "w", encoding="utf-8") as f:
    f.write(about_content)
print("6. about.html")

# 7. CONTACT
contact_content = head_html("संपर्क", "Contact Us") + nav_html("contact") + """
<div class="container my-5">
    <div class="text-center mb-5">
        <h2 class="fw-bold text-success"><span class="lang-mr">आमच्याशी संपर्क साधा</span><span class="lang-en">Contact Us</span></h2>
        <p class="text-muted">मिरखनगर, वैजापूर, छत्रपती संभाजीनगर - ४२३७०३ | फोन: +91 8600813827</p>
    </div>
    <div class="row g-4 justify-content-center">
        <div class="col-md-6">
            <div class="card border-0 shadow-sm rounded-4 p-4 bg-white text-center">
                <i class="bi bi-telephone-fill fs-1 text-success mb-3"></i>
                <h5>थेट संपर्क करा</h5>
                <p class="text-muted"><a href="tel:+918600813827" class="fw-bold text-dark text-decoration-none">+91 8600813827</a></p>
                <a href="https://wa.me/918600813827" target="_blank" class="btn btn-success rounded-pill px-4"><i class="bi bi-whatsapp me-1"></i>व्हॉट्सॲप</a>
            </div>
        </div>
    </div>
</div>
""" + foot_html()
with open(os.path.join(DIST_DIR, "contact.html"), "w", encoding="utf-8") as f:
    f.write(contact_content)
print("7. contact.html")

# 8. FAQ
faq_content = head_html("FAQ", "FAQ") + nav_html("faq") + """
<div class="container my-5" style="max-width:850px;">
    <div class="text-center mb-5">
        <h2 class="fw-bold text-success">वारंवार विचारले जाणारे प्रश्न (FAQ)</h2>
    </div>
    <div class="accordion shadow-sm rounded-4" id="faqAccordion">
        <div class="accordion-item border-0 border-bottom">
            <h2 class="accordion-header"><button class="accordion-button fw-bold" type="button" data-bs-toggle="collapse" data-bs-target="#c1">१. तुमच्याकडे मिळणारे बियाणे व खते प्रमाणित आहेत का?</button></h2>
            <div id="c1" class="accordion-collapse collapse show" data-bs-parent="#faqAccordion"><div class="accordion-body text-muted">होय, १००% प्रमाणित. आम्ही महाराष्ट्र शासन कृषी विभागाचे अधिकृत परवानाधारक केंद्र आहोत.</div></div>
        </div>
        <div class="accordion-item border-0">
            <h2 class="accordion-header"><button class="accordion-button collapsed fw-bold" type="button" data-bs-toggle="collapse" data-bs-target="#c2">२. दुकानाची वेळ काय आहे?</button></h2>
            <div id="c2" class="accordion-collapse collapse" data-bs-parent="#faqAccordion"><div class="accordion-body text-muted">सोमवार ते शनिवार सकाळी ८:०० ते रात्री ८:३०.</div></div>
        </div>
    </div>
</div>
""" + foot_html()
with open(os.path.join(DIST_DIR, "faq.html"), "w", encoding="utf-8") as f:
    f.write(faq_content)
print("8. faq.html")

# 9. OFFERS
offers_content = head_html("ऑफर्स", "Offers") + nav_html("offers") + """
<div class="container my-4">
    <div class="text-center mb-5">
        <span class="badge bg-warning text-dark px-3 py-1 rounded-pill mb-2 fw-bold">विशेष ऑफर्स</span>
        <h2 class="fw-bold text-success">हंगामी सवलत योजना व कूपन्स</h2>
    </div>
    <div class="row g-4">
        <div class="col-md-4">
            <div class="card h-100 border-0 shadow-sm rounded-4 p-4 bg-white" style="border-top: 4px solid #16a34a !important;">
                <span class="badge bg-success w-auto mb-2">१०% सूट</span>
                <h5 class="fw-bold">प्रमाणित बियाण्यांवर १०% सूट</h5>
                <p class="small text-muted">महाबीज व माहिको बियाण्यांवर थेट १०% सूट.</p>
                <div class="bg-light p-2 rounded border mt-auto d-flex justify-content-between align-items-center"><code>KHARIF10</code><a href="products.html" class="btn btn-sm btn-krushi">Use Code</a></div>
            </div>
        </div>
    </div>
</div>
""" + foot_html()
with open(os.path.join(DIST_DIR, "offers.html"), "w", encoding="utf-8") as f:
    f.write(offers_content)
print("9. offers.html")

# 10. REGISTER (Full bilingual + proper registration without direct auto-login)
from build_register_page import build_register_page
build_register_page()
print("10. register.html")

# 11. FORGOT PASSWORD
forgot_content = head_html("पासवर्ड रीसेट", "Forgot Password") + nav_html("login") + """
<div class="container my-5" style="max-width:480px;">
    <div class="card border-0 shadow-lg rounded-4 p-4 text-center bg-white">
        <i class="bi bi-key-fill fs-1 text-success mb-3"></i>
        <h4 class="fw-bold mb-2">पासवर्ड रीसेट साहाय्य</h4>
        <p class="text-muted small mb-4">पासवर्ड रीसेट करण्यासाठी दुकानाच्या अधिकृत हेल्पलाइनवर संपर्क साधा.</p>
        <a href="tel:+918600813827" class="btn btn-krushi rounded-pill py-2 mb-2"><i class="bi bi-telephone-fill me-2"></i>+91 8600813827</a>
        <a href="login.html" class="text-success small text-decoration-none mt-3">« लॉगिन पानाकडे परत जा</a>
    </div>
</div>
""" + foot_html()
with open(os.path.join(DIST_DIR, "forgot-password.html"), "w", encoding="utf-8") as f:
    f.write(forgot_content)
print("11. forgot-password.html")

# 12. LOGIN.HTML & 13. ADMIN PORTAL PAGES (Matching authentic Spring Boot templates & screenshots)
from build_admin_and_login import (
    build_login_page,
    build_admin_dashboard,
    build_admin_products,
    build_admin_product_form,
    build_admin_udhari,
    build_admin_inventory,
    build_admin_categories,
    build_admin_customers,
    build_admin_reviews,
    build_admin_reports,
    build_admin_backup,
    build_admin_settings,
)

build_login_page()
print("12. login.html")

build_admin_dashboard()
build_admin_products()
build_admin_product_form()
build_admin_udhari()
build_admin_inventory()
build_admin_categories()
build_admin_customers()
build_admin_reviews()
build_admin_reports()
build_admin_backup()
build_admin_settings()
print("13. admin-dashboard.html and admin portal pages")

# 14. FARMER & USER PANEL PAGES (Matching Screenshot 1 & 2)
from build_customer_pages import build_all_customer_pages
build_all_customer_pages()
print("14. Customer / Farmer pages (dashboard, profile, orders, udhari, pay, payments, notifications)")

# Update dist/_redirects
redirects_content = """/products /products.html 200
/about /about.html 200
/contact /contact.html 200
/farming-tips /farming-tips.html 200
/fertilizer-calculator /fertilizer-calc.html 200
/weather /weather.html 200
/faq /faq.html 200
/login /login.html 200
/register /register.html 200
/forgot-password /forgot-password.html 200
/offers /offers.html 200
/admin /admin-dashboard.html 200
/admin/ /admin-dashboard.html 200
/admin/dashboard /admin-dashboard.html 200
/admin-dashboard /admin-dashboard.html 200
/admin/products /admin-products.html 200
/admin-products /admin-products.html 200
/admin/product-form /admin-product-form.html 200
/admin-product-form /admin-product-form.html 200
/admin/categories /admin-categories.html 200
/admin-categories /admin-categories.html 200
/admin/inventory /admin-inventory.html 200
/admin-inventory /admin-inventory.html 200
/admin/udhari /admin-udhari.html 200
/admin-udhari /admin-udhari.html 200
/admin/customers /admin-customers.html 200
/admin-customers /admin-customers.html 200
/admin/reviews /admin-reviews.html 200
/admin-reviews /admin-reviews.html 200
/admin/reports /admin-reports.html 200
/admin-reports /admin-reports.html 200
/admin/backup /admin-backup.html 200
/admin-backup /admin-backup.html 200
/admin/settings /admin-settings.html 200
/admin-settings /admin-settings.html 200
/farmer/dashboard /farmer-dashboard.html 200
/farmer-dashboard /farmer-dashboard.html 200
/farmer/cart /cart.html 200
/cart /cart.html 200
/checkout /checkout.html 200
/profile /profile.html 200
/customer/dashboard /farmer-dashboard.html 200
/customer/profile /farmer-profile.html 200
/farmer/profile /farmer-profile.html 200
/customer/orders /farmer-orders.html 200
/farmer/orders /farmer-orders.html 200
/orders /farmer-orders.html 200
/customer/udhari /farmer-udhari.html 200
/farmer/udhari /farmer-udhari.html 200
/customer/pay /farmer-pay.html 200
/farmer/pay /farmer-pay.html 200
/customer/payments /farmer-payments.html 200
/customer/payment-history /farmer-payments.html 200
/farmer/payments /farmer-payments.html 200
/customer/notifications /farmer-notifications.html 200
/farmer/notifications /farmer-notifications.html 200
"""
with open(os.path.join(DIST_DIR, "_redirects"), "w", encoding="utf-8") as f:
    f.write(redirects_content)
print("Updated dist/_redirects")

print("ALL 14 STATIC PAGES GENERATED SUCCESSFULLY!")
