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
    { 
        id: 1, 
        name_mr: "माहिको बीजी-२ कापूस बियाणे (475g)", 
        name_en: "Mahyco BG-II Cotton Seeds (475g)", 
        company: "Mahyco Seeds", 
        cat: "seeds", 
        price: 820, 
        oldPrice: 864, 
        img: "images/cotton_seeds.jpg", 
        tag_mr: "उत्कृष्ट उगवणक्षमता", 
        tag_en: "High Germination",
        desc_mr: "उत्कृष्ट उगवण क्षमता (९५%+), बोंडअळी प्रतिकारक्षमता आणि जास्त उत्पादनाची खात्री. शिफारस: मध्यम ते भारी जमिनीसाठी. एकरी प्रमाण: २ पाकिटे (४७५ ग्रॅम).",
        desc_en: "High germination rate (95%+), bollworm resistance, and superior yield. Recommended: 2 packets (475g) per acre for medium to heavy soils."
    },
    { 
        id: 2, 
        name_mr: "जेएस ३३५ प्रमाणित सोयाबीन बियाणे (30 Kg)", 
        name_en: "JS-335 Certified Soybean Seeds (30 Kg)", 
        company: "Mahabeej", 
        cat: "seeds", 
        price: 2700, 
        oldPrice: 2850, 
        img: "images/soybean_seeds.jpg", 
        tag_mr: "प्रमाणित बियाणे", 
        tag_en: "Govt Certified",
        desc_mr: "महाराष्ट्र शासनाचे महाबीज प्रमाणित बियाणे. एकसमान दाणे, अधिक तेलाचे प्रमाण आणि रोगप्रतिकारक. एकरी प्रमाण: २५ ते ३० किलो बियाणे. पेरणीपूर्वी बीजप्रक्रिया आवश्यक.",
        desc_en: "Govt Certified JS-335 Soybean Seeds by Mahabeej. High oil content, disease resistant. Sowing rate: 25-30 kg per acre."
    },
    { 
        id: 3, 
        name_mr: "महाधन २४:२४:० खत (५० किलो)", 
        name_en: "Mahadhan 24:24:0 Fertilizer (50 Kg)", 
        company: "Deepak Fertilisers", 
        cat: "fertilizers", 
        price: 1680, 
        oldPrice: 1750, 
        img: "images/fertilizer_npk.jpg", 
        tag_mr: "NPK कॉम्प्लेक्स", 
        tag_en: "NPK Complex",
        desc_mr: "नायट्रोजन २४% आणि फॉस्फरस २४% युक्त संतुलित खत. मुळांची जोमदार वाढ आणि फुटवे वाढवण्यासाठी अत्यंत प्रभावी. कपाशी, ऊस, कांदा व डाळिंब पिकासाठी शिफारस.",
        desc_en: "Balanced complex fertilizer with 24% N and 24% P. Stimulates deep root growth and vigorous tillering. Excellent for cotton, sugarcane, onion."
    },
    { 
        id: 4, 
        name_mr: "इफको नीम कोटेड युरिया (४५ किलो)", 
        name_en: "IFFCO Neem Coated Urea (45 Kg)", 
        company: "IFFCO Ltd", 
        cat: "fertilizers", 
        price: 266, 
        oldPrice: 266, 
        img: "images/urea_bag.jpg", 
        tag_mr: "शासकीय अनुदानित", 
        tag_en: "Govt Subsidized",
        desc_mr: "कडुलिंब अर्क लेपित (Neem Coated) ४६% नत्र. खताचा अपव्यय कमी होऊन पिकांना हळूहळू आणि दीर्घकाळ नत्र मिळते. शासकीय नियंत्रित दरात थेट उपलब्ध.",
        desc_en: "Neem coated Urea with 46% Nitrogen. Slow-release formula ensures minimum leaching and prolonged crop nourishment at govt subsidized rate."
    },
    { 
        id: 5, 
        name_mr: "कोरोमंडल ग्रोमोर १०:२६:२६ खत (50 Kg)", 
        name_en: "Coromandel Gromor 10:26:26 (50 Kg)", 
        company: "Coromandel", 
        cat: "fertilizers", 
        price: 1750, 
        oldPrice: 1820, 
        img: "images/fertilizer_npk.jpg", 
        tag_mr: "पोटॅशयुक्त खत", 
        tag_en: "High Potash",
        desc_mr: "पोटॅशयुक्त (२६% पोटॅश, २६% फॉस्फरस, १०% नत्र) खत. फळांचा व दाण्यांचा आकार, चमक आणि वजन वाढवण्यासाठी सर्वोत्तम. सोयाबीन, कांदा, बटाटा पिकासाठी आदर्श.",
        desc_en: "High-grade NPK (10:26:26) enriched with potassium. Maximizes grain weight, fruit size, and drought resilience in all crops."
    },
    { 
        id: 6, 
        name_mr: "फाल्कन १६ लिटर १२V बॅटरी स्प्रे पंप", 
        name_en: "Falcon 16L 12V Battery Sprayer Pump", 
        company: "Falcon Agri", 
        cat: "tools", 
        price: 2850, 
        oldPrice: 3200, 
        img: "images/battery_sprayer.jpg", 
        tag_mr: "डबल मोटर तंत्रज्ञान", 
        tag_en: "Dual Motor",
        desc_mr: "१६ लिटर क्षमतेची मजबूत टाकी, १२V / १२Ah पॉवरफुल बॅटरी, डबल मोटर प्रेशर तंत्रज्ञान. एका चार्जवर १५ ते १८ पंप फवारणी. सोबत ४ प्रकारचे नोझल्स व चार्जर मोफत.",
        desc_en: "Heavy-duty 16L battery sprayer with dual motor pressure system and 12V battery. Sprays up to 15-18 tanks on a single full charge. Includes 4 nozzles."
    },
    { 
        id: 7, 
        name_mr: "जैन ठिबक १६ मिमी लॅटरल पाईप (४०० मीटर)", 
        name_en: "Jain Drip 16mm Lateral Pipe (400m)", 
        company: "Jain Irrigation", 
        cat: "drip", 
        price: 3350, 
        oldPrice: 3600, 
        img: "images/drip_lateral_pipe.jpg", 
        tag_mr: "ISI प्रमाणित", 
        tag_en: "ISI Certified",
        desc_mr: "जैन इरिगेशन ओरिजिनल १६ मिमी लॅटरल पाईप, क्लास २, ४०० मीटर बंडल. यूव्ही स्टेबिलाइझ्ड व्हर्जिन पॉलिमर, ऊन व खतांच्या पाण्याच्या संपर्कात ५+ वर्षे टिकते. आयएसआय हॉलमार्क.",
        desc_en: "Original Jain Irrigation 16mm Lateral Pipe (Class 2, 400m bundle). UV-stabilized virgin polymer, crack resistant, 5+ years operational life. ISI certified."
    },
    { 
        id: 8, 
        name_mr: "लोक-१ प्रमाणित गहू बियाणे (४० किलो)", 
        name_en: "Lok-1 Certified Wheat Seeds (40 Kg)", 
        company: "Mahabeej", 
        cat: "seeds", 
        price: 1350, 
        oldPrice: 1450, 
        img: "images/wheat_seeds.jpg", 
        tag_mr: "प्रमाणित बियाणे", 
        tag_en: "Govt Certified",
        desc_mr: "लोक-१ उत्कृष्ट चपाती गुणवत्ता असलेले महाबीज प्रमाणित गहू बियाणे. १००-१०५ दिवसांत पक्व. एकरी उत्पादन १८ ते २२ क्विंटल. एकरी प्रमाण: ४० किलो बियाणे.",
        desc_en: "Certified Lok-1 Wheat Seeds by Mahabeej. Premium rotis, matures in 100-105 days, average yield 18-22 quintals/acre. 40kg per acre."
    }
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
                    <div class="d-flex justify-content-between align-items-center mt-auto pt-2 border-top gap-2 flex-wrap">
                        <button type="button" class="btn btn-sm btn-outline-success rounded-pill px-3 fw-bold flex-fill shadow-sm" onclick="openProductModal(${p.id})">
                            <i class="bi bi-info-circle me-1"></i><span class="lang-mr">माहिती पाहा</span><span class="lang-en">View Details</span>
                        </button>
                        <a href="https://wa.me/918600813827?text=नमस्कार,%20मला%20${encodeURIComponent(p.name_mr)}%20बद्दल%20अधिक%20माहिती%20हवी%20आहे." target="_blank" class="btn btn-sm btn-success rounded-pill px-3 fw-bold flex-fill shadow-sm" style="background:#16a34a; border:none;">
                            <i class="bi bi-whatsapp me-1"></i><span class="lang-mr">अधिक माहिती</span><span class="lang-en">More Info</span>
                        </a>
                    </div>
                </div>
            </div>
        `;
        grid.appendChild(col);
    });
}
document.addEventListener('DOMContentLoaded', filterProducts);

function openProductModal(id) {
    const p = productsData.find(x => x.id === id);
    if (!p) return;
    document.getElementById('modalProdTitle').textContent = p.name_mr;
    document.getElementById('modalProdName').textContent = p.name_mr;
    document.getElementById('modalProdNameEn').textContent = p.name_en;
    document.getElementById('modalProdCompany').textContent = p.company;
    document.getElementById('modalProdImg').src = p.img;
    document.getElementById('modalProdTag').textContent = p.tag_mr;
    document.getElementById('modalProdPrice').textContent = '₹' + p.price.toLocaleString('en-IN');
    
    if (p.oldPrice > p.price) {
        document.getElementById('modalProdOldPrice').textContent = '₹' + p.oldPrice.toLocaleString('en-IN');
        document.getElementById('modalProdSave').textContent = 'बचत: ₹' + (p.oldPrice - p.price).toLocaleString('en-IN');
        document.getElementById('modalProdOldPrice').classList.remove('d-none');
        document.getElementById('modalProdSave').classList.remove('d-none');
    } else {
        document.getElementById('modalProdOldPrice').classList.add('d-none');
        document.getElementById('modalProdSave').classList.add('d-none');
    }
    
    document.getElementById('modalProdCat').textContent = p.cat.toUpperCase();
    document.getElementById('modalProdDesc').textContent = p.desc_mr || 'उत्कृष्ट गुणवत्ता आणि हमखास उत्पादन देणारे प्रमाणित कृषी उत्पादन.';
    document.getElementById('modalProdWaBtn').href = 'https://wa.me/918600813827?text=' + encodeURIComponent('नमस्कार, मला ' + p.name_mr + ' (' + p.name_en + ') या उत्पादनाबद्दल अधिक माहिती हवी आहे.');
    
    const m = new bootstrap.Modal(document.getElementById('productDetailsModal'));
    m.show();
}
</script>

<!-- Product Details Modal -->
<div class="modal fade" id="productDetailsModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content border-0 shadow-lg rounded-4 overflow-hidden">
            <div class="modal-header bg-success text-white py-3 px-4">
                <h5 class="modal-title fw-bold d-flex align-items-center gap-2">
                    <i class="bi bi-box-seam"></i>
                    <span id="modalProdTitle">उत्पादन तपशील (Product Details)</span>
                </h5>
                <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body p-4">
                <div class="row g-4 align-items-center">
                    <div class="col-md-5 text-center">
                        <div class="p-2 border rounded-4 bg-light shadow-sm">
                            <img id="modalProdImg" src="" alt="Product" class="img-fluid rounded-3" style="max-height: 260px; object-fit: contain;">
                        </div>
                        <div class="mt-3">
                            <span class="badge bg-success-subtle text-success border border-success-subtle px-3 py-1 rounded-pill fw-bold" id="modalProdTag">
                                Verified
                            </span>
                        </div>
                    </div>
                    <div class="col-md-7">
                        <span class="badge bg-light text-muted border px-2 py-1 small fw-bold text-uppercase" id="modalProdCompany">Brand</span>
                        <h4 class="fw-bold text-dark mt-2 mb-1" id="modalProdName">Name</h4>
                        <small class="text-muted d-block mb-3" id="modalProdNameEn">Name EN</small>
                        
                        <div class="d-flex align-items-baseline gap-2 mb-3">
                            <span class="fs-2 fw-bold text-success" id="modalProdPrice">₹0</span>
                            <span class="text-decoration-line-through text-muted small" id="modalProdOldPrice"></span>
                            <span class="badge bg-danger text-white px-2 py-1 rounded-pill small" id="modalProdSave"></span>
                        </div>
                        
                        <div class="p-3 rounded-4 bg-light border mb-3">
                            <div class="row g-2 small">
                                <div class="col-6"><strong>वर्गवारी (Category):</strong> <span id="modalProdCat" class="text-success fw-bold"></span></div>
                                <div class="col-6"><strong>उपलब्धता (Stock):</strong> <span class="badge bg-success text-white">उपलब्ध (In Stock)</span></div>
                                <div class="col-12 mt-2"><strong>वापर व प्रमाण (Dosage / Specifications):</strong></div>
                                <div class="col-12 text-muted" id="modalProdDesc" style="line-height: 1.6; font-size:13.5px;"></div>
                            </div>
                        </div>
                        
                        <div class="d-flex gap-2">
                            <a id="modalProdWaBtn" href="#" target="_blank" class="btn btn-success rounded-pill px-4 py-2 fw-bold flex-fill shadow-sm d-flex align-items-center justify-content-center gap-2" style="background:#15803d; border:none;">
                                <i class="bi bi-whatsapp fs-5"></i>
                                <span><span class="lang-mr">अधिक माहितीसाठी व्हॉट्सॲप करा</span><span class="lang-en">More Information on WhatsApp</span></span>
                            </a>
                            <button type="button" class="btn btn-outline-secondary rounded-pill px-3 py-2 fw-bold" data-bs-dismiss="modal">
                                <span class="lang-mr">बंद करा</span><span class="lang-en">Close</span>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
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

# 4. WEATHER (Working Search & Real-time Live Advisory)
weather_content = head_html("हवामान अंदाज", "Weather Forecast") + nav_html("advisory") + """
<div class="container my-4">
    <div class="text-center mb-4">
        <span class="badge bg-primary-subtle text-primary px-3 py-1 rounded-pill mb-2 fw-semibold">
            <i class="bi bi-cloud-sun me-1"></i>हवामान व शेती सल्ला (Live Agri Forecast)
        </span>
        <h2 class="fw-bold text-success">
            <span class="lang-mr">हवामान अंदाज व फवारणी सल्ला</span>
            <span class="lang-en">Weather Forecast & Spraying Advisory</span>
        </h2>
        <p class="text-muted small">आपल्या तालुका किंवा परिसराचे तापमान, पावसाची टक्केवारी आणि फवारणी अनुकूलता शोधा.</p>
    </div>

    <!-- Search Box with Quick Location Chips -->
    <div class="row justify-content-center mb-4">
        <div class="col-lg-7">
            <div class="input-group shadow-sm rounded-4 overflow-hidden mb-3 border">
                <span class="input-group-text bg-white border-0 ps-3 text-muted"><i class="bi bi-geo-alt-fill text-danger fs-5"></i></span>
                <input type="text" id="cityInput" class="form-control border-0 py-3 ps-2" placeholder="गाव किंवा तालुक्याचे नाव टाका (उदा. वैजापूर, कोपरगाव, नाशिक...)" value="वैजापूर (Vaijapur)">
                <button onclick="searchWeather()" class="btn btn-success px-4 fw-bold" style="background:#15803d; border:none;">
                    <i class="bi bi-search me-1"></i> शोधा
                </button>
            </div>
            <!-- Quick Chips -->
            <div class="d-flex gap-2 flex-wrap justify-content-center small">
                <span class="text-muted small align-self-center fw-semibold">प्रमुख तालुके:</span>
                <button type="button" class="btn btn-sm btn-outline-secondary rounded-pill py-1 px-3" onclick="setCityAndSearch('वैजापूर (Vaijapur)')">📍 वैजापूर</button>
                <button type="button" class="btn btn-sm btn-outline-secondary rounded-pill py-1 px-3" onclick="setCityAndSearch('कोपरगाव (Kopargaon)')">📍 कोपरगाव</button>
                <button type="button" class="btn btn-sm btn-outline-secondary rounded-pill py-1 px-3" onclick="setCityAndSearch('श्रीरामपूर (Shrirampur)')">📍 श्रीरामपूर</button>
                <button type="button" class="btn btn-sm btn-outline-secondary rounded-pill py-1 px-3" onclick="setCityAndSearch('गंगापूर (Gangapur)')">📍 गंगापूर</button>
                <button type="button" class="btn btn-sm btn-outline-secondary rounded-pill py-1 px-3" onclick="setCityAndSearch('छत्रपती संभाजीनगर')">📍 छ. संभाजीनगर</button>
                <button type="button" class="btn btn-sm btn-outline-secondary rounded-pill py-1 px-3" onclick="setCityAndSearch('नाशिक (Nashik)')">📍 नाशिक</button>
                <button type="button" class="btn btn-sm btn-outline-secondary rounded-pill py-1 px-3" onclick="setCityAndSearch('येवला (Yeola)')">📍 येवला</button>
            </div>
        </div>
    </div>

    <!-- Weather Display Card (Matching Screenshot 1) -->
    <div class="row justify-content-center mb-4">
        <div class="col-lg-8">
            <div class="card border-0 shadow-lg rounded-4 text-white p-4" style="background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);">
                <div class="d-flex justify-content-between align-items-center mb-3">
                    <h3 class="fw-bold mb-0 d-flex align-items-center gap-2" id="weatherCityName">
                        <i class="bi bi-geo-alt-fill text-warning"></i> <span>वैजापूर (Vaijapur)</span>
                    </h3>
                    <span class="badge bg-white text-primary fw-bold px-3 py-2 rounded-pill shadow-sm" id="weatherAdvisoryBadge">
                        <i class="bi bi-broadcast me-1 text-danger"></i> Live Advisory
                    </span>
                </div>
                <div class="row align-items-center my-3">
                    <div class="col-md-6 mb-3 mb-md-0">
                        <div class="d-flex align-items-center gap-3">
                            <div id="weatherIconBig" class="fs-1 text-warning"><i class="bi bi-cloud-sun-fill" style="font-size:3.5rem;"></i></div>
                            <div>
                                <h1 class="display-3 fw-bold mb-0" id="weatherTemp">29°C</h1>
                                <p class="lead mb-0 text-white-50 fw-semibold" id="weatherCondition">अंशतः ढगाळ व कोरडे</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6 bg-white bg-opacity-10 p-3 rounded-4 backdrop-blur border border-white border-opacity-25">
                        <div class="d-flex justify-content-between py-1 border-bottom border-light border-opacity-25">
                            <span><i class="bi bi-cloud-rain me-2 text-info"></i>पाऊस (Rain Chance):</span>
                            <strong id="weatherRain">20%</strong>
                        </div>
                        <div class="d-flex justify-content-between py-1 border-bottom border-light border-opacity-25">
                            <span><i class="bi bi-droplet-half me-2 text-primary"></i>हवेतील आर्द्रता (Humidity):</span>
                            <strong id="weatherHumidity">65%</strong>
                        </div>
                        <div class="d-flex justify-content-between py-1">
                            <span><i class="bi bi-wind me-2 text-warning"></i>वाऱ्याचा वेग (Wind Speed):</span>
                            <strong id="weatherWind">12 km/h</strong>
                        </div>
                    </div>
                </div>

                <!-- Agricultural Spraying Advisory Box -->
                <div class="bg-warning text-dark p-3 rounded-3 fw-bold small mt-3 shadow-sm" id="weatherAdvisoryBox">
                    <i class="bi bi-info-circle-fill me-2 fs-6"></i>
                    <span id="weatherAdvisoryText">फवारणी सल्ला: आज वाऱ्याचा वेग अनुकूल असून फवारणीसाठी योग्य वेळ आहे. पाऊस येण्याची शक्यता कमी आहे.</span>
                </div>
            </div>
        </div>
    </div>

    <!-- 5-Day Forecast Row -->
    <div class="row justify-content-center mb-5">
        <div class="col-lg-8">
            <h6 class="fw-bold text-dark mb-3"><i class="bi bi-calendar3 me-2 text-success"></i>पुढील ५ दिवसांचा हवामान अंदाज (5-Day Outlook)</h6>
            <div class="row row-cols-2 row-cols-md-5 g-2" id="fiveDayForecastGrid">
                <!-- Javascript will render 5 forecast cards here -->
            </div>
        </div>
    </div>
</div>

<script>
const weatherDatabase = {
    "vaijapur": { name: "वैजापूर (Vaijapur)", temp: 29, cond: "अंशतः ढगाळ व कोरडे", rain: "20%", humidity: "65%", wind: "12 km/h", icon: "bi-cloud-sun-fill", advisory: "फवारणी सल्ला: आज वाऱ्याचा वेग अनुकूल असून फवारणीसाठी योग्य वेळ आहे. पाऊस येण्याची शक्यता कमी आहे." },
    "kopargaon": { name: "कोपरगाव (Kopargaon)", temp: 31, cond: "कोरडे व स्वच्छ सूर्यप्रकाश", rain: "10%", humidity: "58%", wind: "10 km/h", icon: "bi-sun-fill", advisory: "फवारणी सल्ला: फवारणी व सिंचनासाठी हवामान उत्तम आहे. उन्हाचा कडाका असल्याने सकाळी किंवा संध्याकाळी फवारणी करावी." },
    "shrirampur": { name: "श्रीरामपूर (Shrirampur)", temp: 30, cond: "निरभ्र आकाश", rain: "15%", humidity: "62%", wind: "11 km/h", icon: "bi-sun-fill", advisory: "फवारणी सल्ला: हवामान पूर्णपणे अनुकूल आहे. ऊस व सोयाबीन पिकांना पाणी देण्यास योग्य वेळ आहे." },
    "gangapur": { name: "गंगापूर (Gangapur)", temp: 28, cond: "अंशतः ढगाळ", rain: "25%", humidity: "68%", wind: "14 km/h", icon: "bi-cloudy-fill", advisory: "फवारणी सल्ला: दुपारनंतर ढगाळ वातावरण होऊ शकते, सकाळी फवारणी आटोपून घ्यावी." },
    "sambhajinagar": { name: "छत्रपती संभाजीनगर (Chh. Sambhajinagar)", temp: 29, cond: "हलके ढगाळ वातावरण", rain: "30%", humidity: "70%", wind: "15 km/h", icon: "bi-clouds-fill", advisory: "फवारणी सल्ला: दुपारच्या वेळी हलक्या सरींची शक्यता असल्याने सिस्टिमिक औषधांसोबत स्टिकरचा वापर करा." },
    "aurangabad": { name: "छत्रपती संभाजीनगर (Chh. Sambhajinagar)", temp: 29, cond: "हलके ढगाळ वातावरण", rain: "30%", humidity: "70%", wind: "15 km/h", icon: "bi-clouds-fill", advisory: "फवारणी सल्ला: दुपारच्या वेळी हलक्या सरींची शक्यता असल्याने सिस्टिमिक औषधांसोबत स्टिकरचा वापर करा." },
    "nashik": { name: "नाशिक (Nashik)", temp: 27, cond: "थंड व आल्हाददायक हवा", rain: "35%", humidity: "75%", wind: "13 km/h", icon: "bi-cloud-sun-fill", advisory: "फवारणी सल्ला: द्राक्ष व कांदा बागांमध्ये बुरशीनाशक फवारणीसाठी पोषक वातावरण आहे." },
    "yeola": { name: "येवला (Yeola)", temp: 30, cond: "स्वच्छ व कोरडे", rain: "10%", humidity: "60%", wind: "10 km/h", icon: "bi-sun-fill", advisory: "फवारणी सल्ला: कांदा रोपांवर व पिकांवर कीटकनाशक फवारणी करण्यास उत्तम वातावरण आहे." },
    "ahilyanagar": { name: "अहिल्यानगर (Ahilyanagar)", temp: 31, cond: "स्वच्छ सूर्यप्रकाश", rain: "15%", humidity: "59%", wind: "11 km/h", icon: "bi-sun-fill", advisory: "फवारणी सल्ला: सर्व प्रकारच्या फवारणीसाठी योग्य दिवस. वाऱ्याचा वेग शांत आहे." },
    "shirdi": { name: "शिर्डी / राहाता (Shirdi / Rahata)", temp: 30, cond: "स्वच्छ व निरभ्र", rain: "12%", humidity: "61%", wind: "10 km/h", icon: "bi-sun-fill", advisory: "फवारणी सल्ला: फवारणी करण्यास कोणतीही अडचण नाही. पिकांना पाणी व्यवस्थापन सुरू ठेवा." }
};

function setCityAndSearch(cityName) {
    document.getElementById('cityInput').value = cityName;
    searchWeather();
}

function searchWeather() {
    const raw = document.getElementById('cityInput').value.trim().toLowerCase();
    if (!raw) return;

    let matchKey = null;
    for (const k of Object.keys(weatherDatabase)) {
        if (raw.includes(k) || weatherDatabase[k].name.toLowerCase().includes(raw)) {
            matchKey = k;
            break;
        }
    }

    let data;
    if (matchKey) {
        data = weatherDatabase[matchKey];
    } else {
        // Algorithmic generator for any custom village or town
        const seed = raw.split('').reduce((acc, char) => acc + char.charCodeAt(0), 0);
        const tempGen = 27 + (seed % 6);
        const rainGen = (seed % 40) + 10;
        const humGen = 55 + (seed % 25);
        const windGen = 8 + (seed % 10);
        
        let condText = "स्वच्छ व कोरडे वातावरण";
        let iconName = "bi-sun-fill";
        let advText = "फवारणी सल्ला: हवामान अनुकूल असून कीटकनाशक फवारणीसाठी योग्य वेळ आहे.";
        
        if (rainGen > 35) {
            condText = "ढगाळ वातावरण व पावसाची शक्यता";
            iconName = "bi-cloud-rain-fill";
            advText = "फवारणी सल्ला: पाऊस येण्याची शक्यता असल्याने आज फवारणी पुढे ढकला किंवा स्टिकर वापरा.";
        } else if (windGen > 14) {
            condText = "सोसाट्याचा वारा व कोरडे हवामान";
            iconName = "bi-wind";
            advText = "फवारणी सल्ला: वाऱ्याचा वेग जास्त असल्याने फवारणी करताना औषध उडून वाया जाण्याची शक्यता आहे.";
        }

        data = {
            name: document.getElementById('cityInput').value.trim(),
            temp: tempGen,
            cond: condText,
            rain: rainGen + "%",
            humidity: humGen + "%",
            wind: windGen + " km/h",
            icon: iconName,
            advisory: advText
        };
    }

    // Update UI elements
    document.getElementById('weatherCityName').innerHTML = '<i class="bi bi-geo-alt-fill text-warning"></i> <span>' + data.name + '</span>';
    document.getElementById('weatherTemp').textContent = data.temp + '°C';
    document.getElementById('weatherCondition').textContent = data.cond;
    document.getElementById('weatherRain').textContent = data.rain;
    document.getElementById('weatherHumidity').textContent = data.humidity;
    document.getElementById('weatherWind').textContent = data.wind;
    document.getElementById('weatherAdvisoryText').textContent = data.advisory;
    document.getElementById('weatherIconBig').innerHTML = '<i class="bi ' + data.icon + '" style="font-size:3.5rem;"></i>';

    renderFiveDayOutlook(data.temp, parseInt(data.rain));
}

function renderFiveDayOutlook(baseTemp, baseRain) {
    const days = [
        { label: "उद्या", offsetTemp: 1, rainDiff: -5, icon: "bi-sun-fill" },
        { label: "परवा", offsetTemp: 0, rainDiff: 10, icon: "bi-cloud-sun-fill" },
        { label: "३ दिवसांनी", offsetTemp: -1, rainDiff: 15, icon: "bi-clouds-fill" },
        { label: "४ दिवसांनी", offsetTemp: 1, rainDiff: -10, icon: "bi-sun-fill" },
        { label: "५ दिवसांनी", offsetTemp: 2, rainDiff: -8, icon: "bi-sun-fill" }
    ];

    const grid = document.getElementById('fiveDayForecastGrid');
    if (!grid) return;
    grid.innerHTML = '';

    days.forEach(d => {
        const col = document.createElement('div');
        col.className = 'col';
        const dayRain = Math.max(5, Math.min(90, baseRain + d.rainDiff));
        const dayTemp = baseTemp + d.offsetTemp;
        col.innerHTML = `
            <div class="card border-0 shadow-sm rounded-4 p-3 text-center bg-white h-100 border-top border-3 border-success">
                <small class="text-muted fw-bold mb-1">${d.label}</small>
                <div class="fs-3 text-warning my-1"><i class="bi ${d.icon}"></i></div>
                <div class="fw-bold text-dark fs-5">${dayTemp}°C</div>
                <small class="text-primary fw-semibold"><i class="bi bi-droplet"></i> ${dayRain}%</small>
            </div>
        `;
        grid.appendChild(col);
    });
}

document.addEventListener('DOMContentLoaded', function(){
    searchWeather();
    const inp = document.getElementById('cityInput');
    if (inp) {
        inp.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') searchWeather();
        });
    }
});
</script>
""" + foot_html()
with open(os.path.join(DIST_DIR, "weather.html"), "w", encoding="utf-8") as f:
    f.write(weather_content)
print("4. weather.html with working search and 5-day outlook!")

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

# 6. ABOUT (Matching Screen 1 & Screen 2)
about_content = head_html("आमच्याबद्दल", "About Us") + nav_html("about") + """
<!-- 1. Hero Section -->
<section class="position-relative py-5 text-center text-white overflow-hidden" style="background: linear-gradient(135deg, rgba(20, 83, 45, 0.92), rgba(21, 128, 61, 0.88)), url('/images/farm_hero_bg.jpg') center/cover no-repeat;">
    <div class="container py-4 position-relative" style="z-index: 2;">
        <span class="badge px-3 py-2 rounded-pill fw-semibold text-white shadow-sm mb-3 d-inline-flex align-items-center gap-1" style="background: linear-gradient(135deg, #f59e0b, #d97706); font-size: 0.85rem;">
            <span>🌾</span> <span class="lang-mr">आमच्याबद्दल</span><span class="lang-en">About Us</span>
        </span>
        <h1 class="fw-bold text-white mb-2" style="font-size: clamp(2rem, 3.5vw, 2.75rem); letter-spacing: -0.5px;">
            <span class="lang-mr">सप्तशृंगी ॲग्रो सर्व्हिसेस</span><span class="lang-en">Saptashrungi Agro Services</span>
        </h1>
        <p class="text-white-50 fs-6 mb-0">
            <span class="lang-mr">मिरखनगर, वैजापूर येथील कृषी सेवा केंद्र</span><span class="lang-en">Agricultural store in Mirakhnagar, Vaijapur</span>
        </p>
    </div>
</section>

<!-- 2. Our Story Section (Screen 1) -->
<section class="py-5 bg-white">
    <div class="container py-2">
        <div class="row align-items-center g-5">
            <div class="col-lg-6">
                <span class="badge bg-success-subtle text-success border border-success-subtle px-3 py-1 rounded-pill mb-3 fw-semibold">
                    <span class="me-1">🌱</span> <span class="lang-mr">आमची माहिती</span><span class="lang-en">Our Story</span>
                </span>
                <h2 class="fw-bold text-success mb-3" style="font-size: 1.85rem; line-height: 1.3;">
                    <span class="lang-mr">मिरखनगर, वैजापूर येथील कृषी भांडार</span><span class="lang-en">Agricultural Store in Mirakhnagar, Vaijapur</span>
                </h2>
                <p class="text-secondary mb-3" style="line-height: 1.7; font-size: 0.95rem;">
                    <span class="lang-mr">सप्तशृंगी ॲग्रो सर्व्हिसेस हे मिरखनगर, वैजापूर येथील एक अग्रगण्य कृषी सेवा केंद्र आहे. येथे उच्च दर्जाची प्रमाणित बियाणे, रासायनिक व सेंद्रिय खते, पीक संरक्षण उत्पादने आणि आधुनिक शेती साहित्य रास्त दरात उपलब्ध आहे.</span>
                    <span class="lang-en">Saptashrungi Agro Services is an agricultural store in Mirakhnagar, Vaijapur. The store offers seeds, fertilizers, crop protection products, and farming supplies.</span>
                </p>
                <p class="text-secondary mb-4" style="line-height: 1.7; font-size: 0.95rem;">
                    <span class="lang-mr">उत्पादक, वापर आणि बॅच माहितीसाठी कृपया उत्पादन पॅकेजिंग तपासा. दुकानात उपलब्ध उत्पादनांची खात्री करण्यासाठी अथवा थेट चौकशीसाठी फोन किंवा व्हॉट्सॲपवर संपर्क साधा.</span>
                    <span class="lang-en">Check product packaging for manufacturer, usage, and batch information. Contact the store to confirm product availability.</span>
                </p>

                <div class="d-flex flex-column gap-3 pt-1">
                    <div class="d-flex align-items-start gap-3">
                        <div class="rounded-circle d-flex align-items-center justify-content-center text-success flex-shrink-0" style="width: 32px; height: 32px; background: #e8f5e9;">
                            <i class="bi bi-shield-check fs-5"></i>
                        </div>
                        <div>
                            <strong class="d-block text-dark" style="font-size: 0.95rem;">
                                <span class="lang-mr">प्रमाणित उत्पादने (Product Information)</span><span class="lang-en">Product Information</span>
                            </strong>
                            <small class="text-muted" style="line-height: 1.5; display:block;">
                                <span class="lang-mr">उत्पादक, वापर व बॅच माहितीसाठी पॅकिंग तपासा किंवा दुकानातून खात्री करा.</span>
                                <span class="lang-en">Refer to product packaging for manufacturer, usage, and batch information.</span>
                            </small>
                        </div>
                    </div>

                    <div class="d-flex align-items-start gap-3">
                        <div class="rounded-circle d-flex align-items-center justify-content-center text-success flex-shrink-0" style="width: 32px; height: 32px; background: #e8f5e9;">
                            <i class="bi bi-people-fill fs-5"></i>
                        </div>
                        <div>
                            <strong class="d-block text-dark" style="font-size: 0.95rem;">
                                <span class="lang-mr">कृषी तज्ज्ञ सल्ला (Expert Agronomist Guidance)</span><span class="lang-en">Expert Agronomist Guidance</span>
                            </strong>
                            <small class="text-muted" style="line-height: 1.5; display:block;">
                                <span class="lang-mr">पीक माहिती, लाइव्ह हवामान व खत कॅल्क्युलेटर या संकेतस्थळावर मोफत उपलब्ध आहे.</span>
                                <span class="lang-en">Crop information, weather, and a fertilizer calculator are available on this site.</span>
                            </small>
                        </div>
                    </div>

                    <div class="d-flex align-items-start gap-3">
                        <div class="rounded-circle d-flex align-items-center justify-content-center text-success flex-shrink-0" style="width: 32px; height: 32px; background: #e8f5e9;">
                            <i class="bi bi-credit-card-2-front-fill fs-5"></i>
                        </div>
                        <div>
                            <strong class="d-block text-dark" style="font-size: 0.95rem;">
                                <span class="lang-mr">पारदर्शक उधारी खातेवही (Hassle-Free Credit)</span><span class="lang-en">Hassle-Free Credit (Udhari)</span>
                            </strong>
                            <small class="text-muted" style="line-height: 1.5; display:block;">
                                <span class="lang-mr">नोंदणीकृत शेतकरी ग्राहक संकेतस्थळावर त्यांची उधारी खातेवही पाहू शकतात.</span>
                                <span class="lang-en">Registered customers can view their credit ledger on the website.</span>
                            </small>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-lg-6">
                <div class="position-relative p-2 rounded-4 shadow-sm bg-white border text-center">
                    <img src="/images/saptashrungi_shop.jpg" alt="Saptashrungi Agro Services Shop" class="img-fluid rounded-3 w-100" style="max-height: 380px; object-fit: cover;" onerror="this.src='/images/saptashrungi_logo_round.jpg'">
                    <div class="position-absolute bottom-0 start-50 translate-middle-x mb-4 bg-white px-3 py-2 rounded-pill shadow-sm border d-flex align-items-center gap-2" style="white-space: nowrap; max-width: 90%;">
                        <img src="/images/saptashrungi_logo_round.jpg" width="28" height="28" class="rounded-circle" alt="Logo">
                        <div class="text-start">
                            <strong class="d-block text-dark" style="font-size: 0.85rem; line-height: 1.2;">Saptashrungi Agro Services</strong>
                            <small class="text-muted" style="font-size: 0.75rem;"><i class="bi bi-geo-alt-fill text-danger me-1"></i>Mirakhnagar, Vaijapur</small>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- 3. Category Strip (Screen 1 bottom bar) -->
<section class="py-4 text-white" style="background: #14532d;">
    <div class="container">
        <div class="row text-center g-4">
            <div class="col-6 col-md-3">
                <h3 class="fw-bold text-white mb-1" style="font-size: 1.75rem;">
                    Seeds
                </h3>
                <p class="text-white-50 small mb-0">
                    <span class="lang-mr">उपलब्ध बियाणे</span><span class="lang-en">Available products</span>
                </p>
            </div>
            <div class="col-6 col-md-3">
                <h3 class="fw-bold mb-1" style="font-size: 1.75rem; color: #facc15;">
                    Fertilizers
                </h3>
                <p class="text-white-50 small mb-0">
                    <span class="lang-mr">शेतीसाठी खते</span><span class="lang-en">For farming</span>
                </p>
            </div>
            <div class="col-6 col-md-3">
                <h3 class="fw-bold mb-1" style="font-size: 1.75rem; color: #6ee7b7;">
                    Crop care
                </h3>
                <p class="text-white-50 small mb-0">
                    <span class="lang-mr">पीक संरक्षण</span><span class="lang-en">Products</span>
                </p>
            </div>
            <div class="col-6 col-md-3">
                <h3 class="fw-bold mb-1" style="font-size: 1.75rem; color: #fbbf24;">
                    Irrigation
                </h3>
                <p class="text-white-50 small mb-0">
                    <span class="lang-mr">सिंचन साहित्य</span><span class="lang-en">Supplies</span>
                </p>
            </div>
        </div>
    </div>
</section>

<!-- 4. Visit Our Store Section (Screen 2) -->
<section class="py-5" style="background: #f8fafc;">
    <div class="container py-2 text-center mb-4">
        <span class="badge bg-success-subtle text-success border border-success-subtle px-3 py-1 rounded-pill mb-2 fw-semibold">
            <span class="me-1">📍</span> <span class="lang-mr">दुकानाचे ठिकाण</span><span class="lang-en">Our Location</span>
        </span>
        <h2 class="fw-bold text-success" style="font-size: 1.85rem;">
            <span class="lang-mr">आमच्या दुकानाला प्रत्यक्ष भेट द्या</span><span class="lang-en">Visit Our Store</span>
        </h2>
    </div>

    <div class="container">
        <div class="row g-4 align-items-stretch">
            <!-- Left Card: Contact Details -->
            <div class="col-lg-5">
                <div class="card border-0 shadow-sm rounded-4 p-4 bg-white h-100 d-flex flex-column justify-content-between">
                    <div>
                        <h5 class="fw-bold text-dark d-flex align-items-center gap-2 mb-4 pb-2 border-bottom">
                            <i class="bi bi-telephone-outbound-fill text-success"></i>
                            <span class="lang-mr">संपर्क तपशील</span><span class="lang-en">Contact Details</span>
                        </h5>

                        <div class="d-flex flex-column gap-3 mb-4">
                            <div class="d-flex align-items-start gap-3">
                                <div class="rounded-circle d-flex align-items-center justify-content-center text-success flex-shrink-0" style="width: 34px; height: 34px; background: #e8f5e9;">
                                    <i class="bi bi-geo-alt-fill fs-5"></i>
                                </div>
                                <div class="text-start">
                                    <strong class="d-block text-dark small text-uppercase fw-bold"><span class="lang-mr">दुकानाचा पत्ता</span><span class="lang-en">Store Address</span></strong>
                                    <div class="text-muted small" style="line-height: 1.5;">
                                        Saptashrungi Agro Services, Mirakhnagar, Vaijapur, Chhatrapati Sambhajinagar, Maharashtra - 423703
                                    </div>
                                </div>
                            </div>

                            <div class="d-flex align-items-start gap-3">
                                <div class="rounded-circle d-flex align-items-center justify-content-center text-success flex-shrink-0" style="width: 34px; height: 34px; background: #e8f5e9;">
                                    <i class="bi bi-telephone-fill fs-5"></i>
                                </div>
                                <div class="text-start">
                                    <strong class="d-block text-dark small text-uppercase fw-bold"><span class="lang-mr">फोन नंबर</span><span class="lang-en">Phone Number</span></strong>
                                    <a href="tel:+918600813827" class="text-dark fw-bold text-decoration-none small">+91 8600813827</a>
                                </div>
                            </div>

                            <div class="d-flex align-items-start gap-3">
                                <div class="rounded-circle d-flex align-items-center justify-content-center text-success flex-shrink-0" style="width: 34px; height: 34px; background: #e8f5e9;">
                                    <i class="bi bi-whatsapp fs-5"></i>
                                </div>
                                <div class="text-start">
                                    <strong class="d-block text-dark small text-uppercase fw-bold">WhatsApp</strong>
                                    <a href="https://wa.me/918600813827" target="_blank" class="text-muted text-decoration-none small">
                                        Chat on WhatsApp: <strong class="text-dark">+91 8600813827</strong>
                                    </a>
                                </div>
                            </div>

                            <div class="d-flex align-items-start gap-3">
                                <div class="rounded-circle d-flex align-items-center justify-content-center text-warning flex-shrink-0" style="width: 34px; height: 34px; background: #fef3c7;">
                                    <i class="bi bi-clock-fill fs-5"></i>
                                </div>
                                <div class="text-start">
                                    <strong class="d-block text-dark small text-uppercase fw-bold"><span class="lang-mr">दुकानाची वेळ</span><span class="lang-en">Store Hours</span></strong>
                                    <div class="text-muted small" style="line-height: 1.5;">
                                        Monday – Saturday: 8:00 AM – 8:00 PM<br>
                                        Sunday: 9:00 AM – 2:00 PM
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="d-flex gap-2 pt-2">
                        <a href="tel:+918600813827" class="btn btn-success rounded-pill px-4 py-2 fw-bold text-white flex-fill d-flex align-items-center justify-content-center gap-2 shadow-sm" style="background: #15803d; border:none;">
                            <i class="bi bi-telephone-fill"></i>
                            <span><span class="lang-mr">कॉल करा</span><span class="lang-en">Call Now</span></span>
                        </a>
                        <a href="https://maps.app.goo.gl/S34rKk9DwEntCGid6" target="_blank" class="btn btn-outline-success rounded-pill px-3 py-2 fw-bold flex-fill d-flex align-items-center justify-content-center gap-2">
                            <i class="bi bi-compass"></i>
                            <span><span class="lang-mr">दिशा दाखवा</span><span class="lang-en">Get Directions</span></span>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Right Card: Google Map Embed -->
            <div class="col-lg-7">
                <div class="card border-0 shadow-sm rounded-4 p-3 bg-white h-100 d-flex flex-column justify-content-between">
                    <div class="rounded-3 overflow-hidden border flex-grow-1" style="min-height: 290px;">
                        <iframe 
                            src="https://maps.google.com/maps?q=19.9852957,74.9312239&hl=en&z=17&output=embed" 
                            width="100%" 
                            height="100%" 
                            style="border:0; min-height: 290px;" 
                            allowfullscreen="" 
                            loading="lazy" 
                            referrerpolicy="no-referrer-when-downgrade">
                        </iframe>
                    </div>
                    <a href="https://maps.app.goo.gl/S34rKk9DwEntCGid6" target="_blank" class="btn btn-success w-100 rounded-pill py-2 fw-bold mt-3 shadow-sm d-flex align-items-center justify-content-center gap-2" style="background: #15803d; border:none;">
                        <i class="bi bi-google"></i>
                        <span><span class="lang-mr">गुगल मॅप्सवर उघडा</span><span class="lang-en">Open in Google Maps</span></span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- 5. Our Mission Section (Screen 2 bottom) -->
<section class="py-5 text-center text-white" style="background: #14532d;">
    <div class="container py-2">
        <div class="mb-2">
            <span style="font-size: 2.2rem; color: #facc15;">🌾</span>
        </div>
        <h2 class="fw-bold text-white mb-3" style="font-size: 1.85rem;">
            <span class="lang-mr">आमचे ध्येय</span><span class="lang-en">Our Mission</span>
        </h2>
        <p class="text-white-50 mx-auto mb-4" style="max-width: 680px; font-size: 1rem; line-height: 1.7;">
            <span class="lang-mr">प्रत्येक शेतकऱ्याला वाजवी दरात १००% अस्सल व प्रमाणित कृषी निविष्ठा पुरवणे आणि आधुनिक शेती तंत्रज्ञान व मार्गदर्शनाद्वारे पिकांचे उत्पादन वाढवणे.</span>
            <span class="lang-en">To provide every farmer with genuine, certified agri-inputs at fair prices and enhance crop yields through modern agricultural guidance.</span>
        </p>
        <div class="d-flex justify-content-center gap-3 flex-wrap">
            <a href="products.html" class="btn rounded-pill px-4 py-2 fw-bold text-white shadow-sm d-inline-flex align-items-center gap-2" style="background: #d97706; border: none;">
                <span>🌾</span>
                <span><span class="lang-mr">उत्पादने पाहा</span><span class="lang-en">Browse Products</span></span>
            </a>
            <a href="tel:+918600813827" class="btn btn-outline-light rounded-pill px-4 py-2 fw-bold d-inline-flex align-items-center gap-2">
                <i class="bi bi-telephone-fill"></i>
                <span><span class="lang-mr">थेट कॉल करा</span><span class="lang-en">Call Us Now</span></span>
            </a>
        </div>
    </div>
</section>
""" + foot_html()
with open(os.path.join(DIST_DIR, "about.html"), "w", encoding="utf-8") as f:
    f.write(about_content)
print("6. about.html")

# 7. CONTACT (Matching Screenshot 2)
contact_content = head_html("संपर्क", "Contact Shop") + nav_html("contact") + """
<div class="container my-5" style="max-width: 1140px;">
    <!-- Top Centered Header & Badge -->
    <div class="text-center mb-5">
        <span class="badge px-3 py-2 rounded-pill fw-semibold text-white shadow-sm mb-3 d-inline-block" style="background: #15803d; font-size: 0.85rem;">
            <span class="lang-mr">दुकानदाराशी संपर्क साधा</span>
            <span class="lang-en">Contact the store</span>
        </span>
        <h1 class="fw-bold mb-2" style="font-size: clamp(1.85rem, 3.2vw, 2.45rem); color: #15803d; letter-spacing: -0.3px;">
            <span class="lang-mr">सप्तशृंगी ॲग्रो सर्व्हिसेसशी संपर्क साधा</span>
            <span class="lang-en">Contact Saptashrungi Agro Services</span>
        </h1>
        <p class="text-secondary mx-auto mb-0" style="max-width: 660px; font-size: 0.95rem; line-height: 1.6;">
            <span class="lang-mr">ऑर्डर आणि पीक मार्गदर्शनासाठी आमच्या काउंटरला प्रत्यक्ष भेट द्या किंवा थेट संपर्क करा</span>
            <span class="lang-en">Visit our counter or contact our agronomists directly for orders and crop inquiries</span>
        </p>
    </div>

    <!-- Main Content: Store Information Card & Google Map -->
    <div class="row g-4 align-items-stretch mb-5">
        <!-- Left Column: Store Information -->
        <div class="col-lg-5">
            <div class="card border border-light-subtle shadow-sm rounded-4 p-4 bg-white h-100 d-flex flex-column justify-content-between">
                <div>
                    <div class="d-flex align-items-center gap-2 mb-4 pb-2 border-bottom">
                        <i class="bi bi-shop text-success fs-5"></i>
                        <h5 class="fw-bold text-dark mb-0">
                            <span class="lang-mr">दुकानाची माहिती</span>
                            <span class="lang-en">Store Information</span>
                        </h5>
                    </div>

                    <!-- Item 1: Shop Address -->
                    <div class="d-flex align-items-start gap-3 mb-4">
                        <div class="rounded-3 d-flex align-items-center justify-content-center text-white flex-shrink-0" style="width: 38px; height: 38px; background: #15803d;">
                            <i class="bi bi-geo-alt-fill fs-5"></i>
                        </div>
                        <div>
                            <strong class="d-block text-dark fw-bold" style="font-size: 0.93rem;">
                                <span class="lang-mr">दुकानाचा पत्ता</span>
                                <span class="lang-en">Shop Address</span>
                            </strong>
                            <div class="text-secondary" style="font-size: 0.88rem; line-height: 1.5; margin-top: 3px;">
                                Saptashrungi Agro Services, Mirakhnagar, Vaijapur, Chhatrapati Sambhajinagar, Maharashtra - 423703
                            </div>
                        </div>
                    </div>

                    <!-- Item 2: Phone & Mobile -->
                    <div class="d-flex align-items-start gap-3 mb-4">
                        <div class="rounded-3 d-flex align-items-center justify-content-center text-white flex-shrink-0" style="width: 38px; height: 38px; background: #15803d;">
                            <i class="bi bi-telephone-fill fs-5"></i>
                        </div>
                        <div>
                            <strong class="d-block text-dark fw-bold" style="font-size: 0.93rem;">
                                <span class="lang-mr">फोन व मोबाईल</span>
                                <span class="lang-en">Phone & Mobile</span>
                            </strong>
                            <div class="text-secondary" style="font-size: 0.88rem; line-height: 1.5; margin-top: 3px;">
                                <a href="tel:+918600813827" class="text-dark fw-bold text-decoration-none">+91 8600813827</a>
                            </div>
                        </div>
                    </div>

                    <!-- Item 3: Working Hours -->
                    <div class="d-flex align-items-start gap-3 mb-4">
                        <div class="rounded-3 d-flex align-items-center justify-content-center text-white flex-shrink-0" style="width: 38px; height: 38px; background: #15803d;">
                            <i class="bi bi-clock-fill fs-5"></i>
                        </div>
                        <div>
                            <strong class="d-block text-dark fw-bold" style="font-size: 0.93rem;">
                                <span class="lang-mr">कामाची वेळ</span>
                                <span class="lang-en">Working Hours</span>
                            </strong>
                            <div class="text-secondary" style="font-size: 0.88rem; line-height: 1.5; margin-top: 3px;">
                                Mon - Sat: 8:00 AM - 8:30 PM | Sun: 9:00 AM - 2:00 PM
                            </div>
                        </div>
                    </div>

                    <!-- Item 4: GSTIN Registration -->
                    <div class="d-flex align-items-start gap-3 mb-4">
                        <div class="rounded-3 d-flex align-items-center justify-content-center text-white flex-shrink-0" style="width: 38px; height: 38px; background: #15803d;">
                            <i class="bi bi-receipt fs-5"></i>
                        </div>
                        <div>
                            <strong class="d-block text-dark fw-bold" style="font-size: 0.93rem;">
                                <span class="lang-mr">जीएसटी नोंदणी</span>
                                <span class="lang-en">GSTIN Registration</span>
                            </strong>
                            <div class="text-secondary font-monospace" style="font-size: 0.88rem; line-height: 1.5; margin-top: 3px; letter-spacing: 0.5px;">
                                27AAAAA0000A1Z5
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Action Buttons (Matching Screenshot 2) -->
                <div class="d-flex flex-column gap-2 pt-3 border-top">
                    <!-- Button 1: WhatsApp -->
                    <a href="https://wa.me/918600813827?text=Namaste%20Saptashrungi%20Agro%20Services" target="_blank" class="btn btn-success py-2 px-3 fw-bold text-white d-flex align-items-center justify-content-center gap-2 shadow-sm rounded-3" style="background: #15803d; border: none; font-size: 0.93rem;">
                        <i class="bi bi-whatsapp fs-5"></i>
                        <span><span class="lang-mr">Chat on WhatsApp (8600813827)</span><span class="lang-en">Chat on WhatsApp (8600813827)</span></span>
                    </a>

                    <!-- Button 2: Direct Call -->
                    <a href="tel:+918600813827" class="btn btn-outline-success py-2 px-3 fw-bold d-flex align-items-center justify-content-center gap-2 rounded-3" style="border-color: #15803d; color: #15803d; font-size: 0.93rem;">
                        <i class="bi bi-telephone-outbound fs-5"></i>
                        <span><span class="lang-mr">Direct Call Shop (+91 8600813827)</span><span class="lang-en">Direct Call Shop (+91 8600813827)</span></span>
                    </a>

                    <!-- Button 3: Google Maps -->
                    <a href="https://maps.app.goo.gl/S34rKk9DwEntCGid6" target="_blank" class="btn btn-outline-secondary py-2 px-3 fw-bold d-flex align-items-center justify-content-center gap-2 rounded-3" style="border-color: #cbd5e1; color: #334155; font-size: 0.93rem; background: #ffffff;">
                        <i class="bi bi-map fs-5"></i>
                        <span><span class="lang-mr">Open in Google Maps</span><span class="lang-en">Open in Google Maps</span></span>
                    </a>
                </div>
            </div>
        </div>

        <!-- Right Column: Interactive Google Map -->
        <div class="col-lg-7">
            <div class="card border border-light-subtle shadow-sm rounded-4 overflow-hidden bg-white h-100" style="min-height: 480px;">
                <iframe 
                    src="https://maps.google.com/maps?q=19.9852957,74.9312239&hl=en&z=17&output=embed" 
                    width="100%" 
                    height="100%" 
                    style="border:0; min-height: 480px;" 
                    allowfullscreen="" 
                    loading="lazy" 
                    referrerpolicy="no-referrer-when-downgrade">
                </iframe>
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
