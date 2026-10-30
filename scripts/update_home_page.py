# -*- coding: utf-8 -*-
import os
import re

BASE_DIR = r"c:\Users\HP\OneDrive\Documents\krushi seva"
DIST_DIR = os.path.join(BASE_DIR, "dist")

from build_site import head_html, nav_html, foot_html

def build_home_page():
    html = head_html("मुख्यपृष्ठ", "Home") + nav_html("home") + """
<!-- ===== HERO SECTION ===== -->
<section class="hero-section">
    <!-- 🌾 Farm Background with Ken Burns Animation -->
    <div class="hero-farm-bg" id="heroBg"></div>
    <!-- Cinematic Dark Overlay -->
    <div class="video-overlay"></div>

    <!-- Spacious, Glassmorphic Hero Card -->
    <div class="hero-content">
        <!-- Eyebrow Pill Badge -->
        <div class="hero-pill-badge">
            <span class="hero-pill-dot"></span>
            <span class="lang-mr">सप्तशृंगी ॲग्रो सर्व्हिसेस</span>
            <span class="lang-en">SAPTASHRUNGI AGRO SERVICES</span>
            <span class="hero-pill-tag">
                <span class="lang-mr">बियाणे, खते व शेती साहित्य</span>
                <span class="lang-en">SEEDS, FERTILIZERS &amp; FARM SUPPLIES</span>
            </span>
        </div>

        <!-- Master Headline -->
        <h1 class="hero-title">
            <span class="lang-mr">शेतीसाठी उत्पादने<br class="d-none d-md-block"> आणि <span class="hero-gradient-text">उपयुक्त माहिती</span></span>
            <span class="lang-en">Agricultural Products<br class="d-none d-md-block"> and <span class="hero-gradient-text">Farming Information</span></span>
        </h1>

        <!-- Subtitle -->
        <p class="hero-desc">
            <span class="lang-mr">बियाणे, खते, पीक संरक्षण औषधे आणि सिंचन साहित्य यांची माहिती व खरेदीसाठी मिरखनगर, वैजापूर येथील कृषी सेवा केंद्र.</span>
            <span class="lang-en">Browse seeds, fertilizers, crop protection products, and irrigation supplies from our agricultural store in Mirakhnagar, Vaijapur.</span>
        </p>

        <!-- Action Buttons -->
        <div class="hero-buttons">
            <a href="products.html" class="btn-hero-primary">
                <i class="bi bi-grid-fill"></i>
                <span class="lang-mr">उत्पादने पहा</span>
                <span class="lang-en">Explore Products</span>
                <i class="bi bi-arrow-right"></i>
            </a>
            <a href="https://wa.me/918600813827?text=नमस्कार,%20मला%20कृषी%20उत्पादनांविषयी%20माहिती%20हवी%20आहे." target="_blank" class="btn-hero-outline">
                <i class="bi bi-whatsapp text-success"></i>
                <span class="lang-mr">व्हॉट्सॲप सल्ला</span>
                <span class="lang-en">WhatsApp Advisory</span>
            </a>
            <a href="farming-tips.html" class="btn-hero-outline">
                <i class="bi bi-journal-text text-warning"></i>
                <span class="lang-mr">कृषी सल्लागार</span>
                <span class="lang-en">Farming Advice</span>
            </a>
        </div>

        <!-- Trust Badges Strip -->
        <div class="hero-trust-strip">
            <div class="hero-trust-item">
                <i class="bi bi-patch-check-fill text-success"></i>
                <span class="lang-mr">बियाणे, खते व पीक संरक्षण साहित्य</span>
                <span class="lang-en">Seeds, fertilizers &amp; farm supplies</span>
            </div>
            <div class="hero-trust-item">
                <i class="bi bi-people-fill text-success"></i>
                <span class="lang-mr">५००+ शेतकरी बांधवांचा विश्वास</span>
                <span class="lang-en">Trusted by 500+ Farmers</span>
            </div>
            <div class="hero-trust-item">
                <i class="bi bi-geo-alt-fill text-success"></i>
                <span class="lang-mr">मिरखनगर, वैजापूर</span>
                <span class="lang-en">Mirakhnagar, Vaijapur</span>
            </div>
        </div>
    </div>
</section>

<!-- ===== ⚡ QUICK ACTION CARDS (Screenshot 2) ===== -->
<section class="container-fluid px-3 px-md-5" style="margin-top:-40px; position:relative; z-index:10;">
    <div class="row g-3 justify-content-center">
        <!-- Card 1: Explore Products -->
        <div class="col-6 col-md-3">
            <a href="products.html" class="text-decoration-none">
                <div class="quick-action-card" style="--card-color:#1b5e20; --card-bg:#f0fdf4;">
                    <div class="qa-icon">🌱</div>
                    <div class="qa-title"><span class="lang-mr">उत्पादने पहा</span><span class="lang-en">Explore Products</span></div>
                    <div class="qa-sub"><span class="lang-mr">सर्व कृषी साहित्य</span><span class="lang-en">Browse All Products</span></div>
                    <div class="qa-arrow">→</div>
                </div>
            </a>
        </div>

        <!-- Card 2: Contact Shop -->
        <div class="col-6 col-md-3">
            <a href="tel:+918600813827" class="text-decoration-none">
                <div class="quick-action-card" style="--card-color:#0369a1; --card-bg:#f0f9ff;">
                    <div class="qa-icon">📞</div>
                    <div class="qa-title"><span class="lang-mr">संपर्क करा</span><span class="lang-en">Contact Shop</span></div>
                    <div class="qa-sub"><span class="lang-mr">कॉल किंवा व्हॉट्सॲप</span><span class="lang-en">Call or WhatsApp</span></div>
                    <div class="qa-arrow">→</div>
                </div>
            </a>
        </div>

        <!-- Card 3: Check Udhari -->
        <div class="col-6 col-md-3">
            <a href="customer-udhari.html" class="text-decoration-none">
                <div class="quick-action-card" style="--card-color:#b45309; --card-bg:#fffbeb;">
                    <div class="qa-icon">💳</div>
                    <div class="qa-title"><span class="lang-mr">उधारी तपासा</span><span class="lang-en">Check Udhari</span></div>
                    <div class="qa-sub"><span class="lang-mr">खाते व बाकी रक्कम</span><span class="lang-en">Credit Balance</span></div>
                    <div class="qa-arrow">→</div>
                </div>
            </a>
        </div>

        <!-- Card 4: Visit Shop (Map) -->
        <div class="col-6 col-md-3">
            <a href="https://maps.app.goo.gl/S34rKk9DwEntCGid6" target="_blank" rel="noopener noreferrer" class="text-decoration-none">
                <div class="quick-action-card" style="--card-color:#7c3aed; --card-bg:#fdf4ff;">
                    <div class="qa-icon">📍</div>
                    <div class="qa-title"><span class="lang-mr">दुकानाला भेट द्या</span><span class="lang-en">Visit Shop</span></div>
                    <div class="qa-sub"><span class="lang-mr">गुगल मॅप दिशा</span><span class="lang-en">Get Directions</span></div>
                    <div class="qa-arrow">→</div>
                </div>
            </a>
        </div>
    </div>
</section>

<!-- ===== 🌾 WHY CHOOSE SAPTASHRUNGI - 6 CARDS (Screenshot 2) ===== -->
<section class="container my-4 pt-2">
    <div class="text-center mb-4">
        <span class="badge px-3 py-1 rounded-pill fw-semibold mb-2 d-inline-block"
              style="background:linear-gradient(135deg,#e8f5e9,#c8e6c9);color:#1b5e20;font-size:0.78rem;">
            <span class="lang-mr">⭐ आम्हीच का?</span><span class="lang-en">⭐ Why Choose Us?</span>
        </span>
        <h2 class="fw-bold text-success mb-1" style="font-size:1.6rem;">
            <span class="lang-mr">सप्तशृंगी ॲग्रोलाच पसंती का?</span><span class="lang-en">Why Choose Saptashrungi Agro?</span>
        </h2>
        <p class="text-muted small" style="max-width:500px;margin:0 auto;">
            <span class="lang-mr">दुकानाची माहिती आणि उपलब्ध सुविधा</span><span class="lang-en">Store information and available services</span>
        </p>
    </div>

    <div class="row g-3">
        <!-- 1. Genuine Products -->
        <div class="col-md-4 col-sm-6">
            <div class="why-card">
                <div class="why-icon-wrap" style="background:#e8f5e9;">
                    <span style="font-size:1.35rem;">✅</span>
                </div>
                <h5 class="why-title"><span class="lang-mr">अस्सल उत्पादने</span><span class="lang-en">Genuine Products</span></h5>
                <p class="why-desc">
                    <span class="lang-mr">उत्पादनाची कंपनी, बॅच आणि वापरासंबंधी माहिती पॅकेजिंगवर तपासा.</span>
                    <span class="lang-en">Check the product packaging for manufacturer, batch, and usage information.</span>
                </p>
            </div>
        </div>

        <!-- 2. Quality Seeds -->
        <div class="col-md-4 col-sm-6">
            <div class="why-card">
                <div class="why-icon-wrap" style="background:#f0f9ff;">
                    <span style="font-size:1.35rem;">🌱</span>
                </div>
                <h5 class="why-title"><span class="lang-mr">दर्जेदार बियाणे</span><span class="lang-en">Quality Seeds</span></h5>
                <p class="why-desc">
                    <span class="lang-mr">वेगवेगळ्या पिकांसाठी उपलब्ध बियाण्यांची माहिती उत्पादन यादीत पाहा.</span>
                    <span class="lang-en">Browse the product list for seed options for different crops.</span>
                </p>
            </div>
        </div>

        <!-- 3. Fertilizers -->
        <div class="col-md-4 col-sm-6">
            <div class="why-card">
                <div class="why-icon-wrap" style="background:#fffbeb;">
                    <span style="font-size:1.35rem;">🧪</span>
                </div>
                <h5 class="why-title"><span class="lang-mr">खते</span><span class="lang-en">Fertilizers</span></h5>
                <p class="why-desc">
                    <span class="lang-mr">उपलब्ध खतांचे प्रकार, किंमत आणि तपशील उत्पादन यादीत पाहा.</span>
                    <span class="lang-en">See available fertilizer types, prices, and details in the product list.</span>
                </p>
            </div>
        </div>

        <!-- 4. Crop Protection -->
        <div class="col-md-4 col-sm-6">
            <div class="why-card">
                <div class="why-icon-wrap" style="background:#fdf4ff;">
                    <span style="font-size:1.35rem;">🛡️</span>
                </div>
                <h5 class="why-title"><span class="lang-mr">पीक संरक्षण</span><span class="lang-en">Crop Protection</span></h5>
                <p class="why-desc">
                    <span class="lang-mr">कीटकनाशके आणि बुरशीनाशकांची उपलब्धता व वापराची माहिती उत्पादनानुसार पाहा.</span>
                    <span class="lang-en">Browse available insecticides and fungicides, along with product-specific usage information.</span>
                </p>
            </div>
        </div>

        <!-- 5. Farmer Guidance -->
        <div class="col-md-4 col-sm-6">
            <div class="why-card">
                <div class="why-icon-wrap" style="background:#f0fdf4;">
                    <span style="font-size:1.35rem;">👨‍🌾</span>
                </div>
                <h5 class="why-title"><span class="lang-mr">शेतकरी मार्गदर्शन</span><span class="lang-en">Farmer Guidance</span></h5>
                <p class="why-desc">
                    <span class="lang-mr">वेबसाइटवरील पीक माहिती व खत कॅल्क्युलेटरचा उपयोग करा; उत्पादनाचे लेबलही वाचा.</span>
                    <span class="lang-en">Use the crop information and fertilizer calculator on this site, and follow product labels.</span>
                </p>
            </div>
        </div>

        <!-- 6. Local Support + Udhari -->
        <div class="col-md-4 col-sm-6">
            <div class="why-card">
                <div class="why-icon-wrap" style="background:#fff0f0;">
                    <span style="font-size:1.35rem;">🤝</span>
                </div>
                <h5 class="why-title"><span class="lang-mr">स्थानिक आधार व उधारी</span><span class="lang-en">Local Support &amp; Udhari</span></h5>
                <p class="why-desc">
                    <span class="lang-mr">मिरखनगर, वैजापूर येथील दुकान. उपलब्ध पेमेंट पद्धती आणि उधारीची माहिती दुकानाशी संपर्क करून घ्या.</span>
                    <span class="lang-en">Store located in Mirakhnagar, Vaijapur. Contact the store for payment and credit facility details.</span>
                </p>
            </div>
        </div>
    </div>
</section>

<!-- ===== 🏪 FLAGSHIP STOREFRONT SHOWCASE V2 (Screenshot 3) ===== -->
<section class="container my-5" style="max-width: 1280px;">
    <div class="flagship-store-card">
        <div class="row g-0 align-items-stretch">
            <!-- Left: High-Res Store Image Showcase -->
            <div class="col-lg-6">
                <div class="flagship-img-container">
                    <img src="images/saptashrungi_shop.jpg" alt="Saptashrungi Agro Services Shop" class="flagship-img" onerror="this.src='images/saptashrungi_shop.jpg'">
                    <div class="flagship-img-overlay"></div>
                    
                    <!-- Live Outlet Status Badge -->
                    <div class="flagship-badge-top">
                        <span class="flagship-badge-dot"></span>
                        <span class="lang-mr">शासकीय मान्यताप्राप्त अधिकृत केंद्र</span>
                        <span class="lang-en">Government Authorized Outlet</span>
                    </div>

                    <!-- Bottom Floating Info Badges -->
                    <div class="flagship-badge-bottom">
                        <span class="flagship-pill-chip">
                            <i class="bi bi-clock me-1 text-warning"></i>
                            <span class="lang-mr">सकाळी ८:०० ते रात्री ८:३०</span>
                            <span class="lang-en">Open 8:00 AM - 8:30 PM</span>
                        </span>
                        <span class="flagship-pill-chip">
                            <i class="bi bi-geo-alt-fill me-1 text-danger"></i>
                            <span class="lang-mr">मिरखनगर, वैजापूर</span>
                            <span class="lang-en">Mirakhnagar, Vaijapur</span>
                        </span>
                    </div>
                </div>
            </div>

            <!-- Right: Content & Action Details -->
            <div class="col-lg-6 p-4 p-md-4 d-flex flex-column justify-content-between">
                <div>
                    <!-- Header with Verified Logo & Badge -->
                    <div class="d-flex align-items-center gap-3 mb-3">
                        <div class="position-relative">
                            <img src="images/saptashrungi_logo_round.jpg" alt="Shop Logo" class="flagship-logo-ring">
                            <i class="bi bi-patch-check-fill text-success position-absolute bottom-0 end-0 fs-5" style="background:#fff; border-radius:50%; line-height:1;"></i>
                        </div>
                        <div>
                            <span class="badge px-3 py-1 rounded-pill fw-bold text-success" style="background: rgba(22, 163, 74, 0.12); border: 1px solid rgba(22, 163, 74, 0.25); font-size: 0.75rem;">
                                <span class="lang-mr">🌿 कृषी सेवा केंद्र</span><span class="lang-en">🌿 Agricultural Store</span>
                            </span>
                            <h2 class="flagship-title-gradient mb-0 mt-1">
                                <span class="lang-mr">सप्तशृंगी ॲग्रो सर्व्हिसेस</span><span class="lang-en">Saptashrungi Agro Services</span>
                            </h2>
                        </div>
                    </div>

                    <!-- Description -->
                    <p class="text-secondary mb-3" style="line-height: 1.65; font-size: 0.95rem;">
                        <span class="lang-mr">बियाणे, रासायनिक व सेंद्रिय खते, कीटकनाशके, फवारणी यंत्रे आणि ठिबक सिंचन साहित्याची माहिती व उपलब्धता येथे पाहा.</span>
                        <span class="lang-en">Browse information about seeds, chemical and organic fertilizers, crop protection, sprayers, and drip irrigation supplies.</span>
                    </p>

                    <!-- Feature Badges Strip -->
                    <div class="d-flex flex-wrap gap-2 mb-4">
                        <span class="flagship-feature-pill">
                            <i class="bi bi-patch-check text-success"></i>
                            <span class="lang-mr">बियाण्यांची माहिती</span><span class="lang-en">Seed information</span>
                        </span>
                        <span class="flagship-feature-pill">
                            <i class="bi bi-tag text-primary"></i>
                            <span class="lang-mr">किंमत व कर तपशील</span><span class="lang-en">Price and tax details</span>
                        </span>
                        <span class="flagship-feature-pill">
                            <i class="bi bi-credit-card-2-front text-warning"></i>
                            <span class="lang-mr">उधारी खाते उपलब्ध</span><span class="lang-en">Credit Facility</span>
                        </span>
                    </div>
                </div>

                <!-- Action CTA Buttons -->
                <div class="d-flex gap-2 flex-wrap pt-3 border-top" style="border-color: rgba(22, 163, 74, 0.15) !important;">
                    <a href="products.html" class="btn-flagship-primary">
                        <i class="bi bi-cart3 fs-5"></i>
                        <span class="lang-mr">साहित्य खरेदी करा</span><span class="lang-en">Shop Inputs</span>
                    </a>
                    <a href="https://maps.app.goo.gl/S34rKk9DwEntCGid6" target="_blank" rel="noopener noreferrer" class="btn-flagship-map">
                        <i class="bi bi-geo-alt-fill text-danger fs-5"></i>
                        <span class="lang-mr">दुकानाचा नकाशा</span><span class="lang-en">Store Map</span>
                    </a>
                    <a href="tel:+918600813827" class="btn-flagship-call">
                        <i class="bi bi-telephone-fill text-success fs-5"></i>
                        <span class="lang-mr">कॉल करा 8600813827</span><span class="lang-en">Call 8600813827</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ===== 🌱 EXPLORE AGRICULTURAL CATEGORIES - 8 CARDS (Screenshot 4) ===== -->
<section class="container my-5">
    <div class="text-center mb-4">
        <span class="badge px-3 py-1 rounded-pill fw-semibold mb-2 d-inline-block text-success"
              style="background: rgba(22, 163, 74, 0.12); border: 1px solid rgba(22, 163, 74, 0.25); font-size: 0.78rem;">
            <span class="lang-mr">🌱 आमची उत्पादने</span><span class="lang-en">🌱 Product Range</span>
        </span>
        <h2 class="fw-bold text-success mb-2" style="font-size: 1.85rem;">
            <span class="lang-mr">कृषी उत्पादनांची वर्गवारी</span><span class="lang-en">Explore Agricultural Categories</span>
        </h2>
        <p class="text-muted small mx-auto" style="max-width: 580px;">
            <span class="lang-mr">सर्व प्रकारची प्रमाणित शेती उत्पादने आणि आधुनिक साधने एकाच ठिकाणी उपलब्ध</span>
            <span class="lang-en">Comprehensive range of verified farming inputs and modern equipment</span>
        </p>
    </div>
    
    <div class="row row-cols-2 row-cols-md-4 row-cols-lg-4 g-3">
        <!-- 1. Animal Feed -->
        <div class="col">
            <a href="products.html?category=6" class="category-card-v2 h-100 cat-theme-animalfeed text-decoration-none">
                <div class="w-100 d-flex flex-column align-items-center">
                    <div class="category-icon-box-v2">
                        <i class="bi bi-egg-fried"></i>
                    </div>
                    <div class="category-title-v2"><span class="lang-mr">पशूखाद्य</span><span class="lang-en">Animal Feed</span></div>
                    <div class="category-sub-v2"><span class="lang-mr">सरकी पेंड, मिनरल मिक्श्चर</span><span class="lang-en">Cattle feed pellets, mineral mixtures and supplements.</span></div>
                </div>
                <div class="category-explore-link mt-2">
                    <span class="lang-mr">पहा</span><span class="lang-en">Explore</span>
                    <i class="bi bi-arrow-right"></i>
                </div>
            </a>
        </div>

        <!-- 2. Drip Irrigation -->
        <div class="col">
            <a href="products.html?category=5" class="category-card-v2 h-100 cat-theme-irrigation text-decoration-none">
                <div class="w-100 d-flex flex-column align-items-center">
                    <div class="category-icon-box-v2">
                        <i class="bi bi-water"></i>
                    </div>
                    <div class="category-title-v2"><span class="lang-mr">ठिबक सिंचन</span><span class="lang-en">Drip Irrigation</span></div>
                    <div class="category-sub-v2"><span class="lang-mr">ठिबक नळी, ड्रिपर्स व फिल्टर्स</span><span class="lang-en">Drip laterals, drippers, screen filters and fittings.</span></div>
                </div>
                <div class="category-explore-link mt-2">
                    <span class="lang-mr">पहा</span><span class="lang-en">Explore</span>
                    <i class="bi bi-arrow-right"></i>
                </div>
            </a>
        </div>

        <!-- 3. Farming Tools (Purple Active Highlight as in Screenshot 4) -->
        <div class="col">
            <a href="products.html?category=4" class="category-card-v2 h-100 cat-theme-tools text-decoration-none" style="border: 1.5px solid #a855f7 !important; box-shadow: 0 4px 15px rgba(168,85,247,0.15);">
                <div class="w-100 d-flex flex-column align-items-center">
                    <div class="category-icon-box-v2" style="background:#f3e8ff; color:#7c3aed;">
                        <i class="bi bi-tools"></i>
                    </div>
                    <div class="category-title-v2"><span class="lang-mr">कृषी अवजारे</span><span class="lang-en">Farming Tools</span></div>
                    <div class="category-sub-v2"><span class="lang-mr">फवारणी पंप, ताडपत्री व साधने</span><span class="lang-en">Battery sprayers, pruning shears, tarpaulins and hand tools.</span></div>
                </div>
                <div class="category-explore-link mt-2">
                    <span class="lang-mr">पहा</span><span class="lang-en">Explore</span>
                    <i class="bi bi-arrow-right"></i>
                </div>
            </a>
        </div>

        <!-- 4. Fertilizers -->
        <div class="col">
            <a href="products.html?category=2" class="category-card-v2 h-100 cat-theme-fertilizers text-decoration-none">
                <div class="w-100 d-flex flex-column align-items-center">
                    <div class="category-icon-box-v2">
                        <i class="bi bi-droplet-half"></i>
                    </div>
                    <div class="category-title-v2"><span class="lang-mr">खते</span><span class="lang-en">Fertilizers</span></div>
                    <div class="category-sub-v2"><span class="lang-mr">रासायनिक, विद्राव्य, NPK व सूक्ष्मद्रव्ये</span><span class="lang-en">Chemical, water-soluble, NPK and micronutrient fertilizers.</span></div>
                </div>
                <div class="category-explore-link mt-2">
                    <span class="lang-mr">पहा</span><span class="lang-en">Explore</span>
                    <i class="bi bi-arrow-right"></i>
                </div>
            </a>
        </div>

        <!-- 5. Organic Products -->
        <div class="col">
            <a href="products.html?category=7" class="category-card-v2 h-100 cat-theme-organic text-decoration-none">
                <div class="w-100 d-flex flex-column align-items-center">
                    <div class="category-icon-box-v2">
                        <i class="bi bi-recycle"></i>
                    </div>
                    <div class="category-title-v2"><span class="lang-mr">सेंद्रिय उत्पादने</span><span class="lang-en">Organic Products</span></div>
                    <div class="category-sub-v2"><span class="lang-mr">कडुलिंब पेंड, गांडूळखत व बायो उत्पादने</span><span class="lang-en">Neem cake, vermicompost and organic bio-stimulants.</span></div>
                </div>
                <div class="category-explore-link mt-2">
                    <span class="lang-mr">पहा</span><span class="lang-en">Explore</span>
                    <i class="bi bi-arrow-right"></i>
                </div>
            </a>
        </div>

        <!-- 6. Pesticides -->
        <div class="col">
            <a href="products.html?category=3" class="category-card-v2 h-100 cat-theme-pesticides text-decoration-none">
                <div class="w-100 d-flex flex-column align-items-center">
                    <div class="category-icon-box-v2">
                        <i class="bi bi-bug-fill"></i>
                    </div>
                    <div class="category-title-v2"><span class="lang-mr">कीटकनाशके</span><span class="lang-en">Pesticides</span></div>
                    <div class="category-sub-v2"><span class="lang-mr">कीटकनाशके, बुरशीनाशके व तणनाशके</span><span class="lang-en">Broad-spectrum insecticides, fungicides, and weedicides.</span></div>
                </div>
                <div class="category-explore-link mt-2">
                    <span class="lang-mr">पहा</span><span class="lang-en">Explore</span>
                    <i class="bi bi-arrow-right"></i>
                </div>
            </a>
        </div>

        <!-- 7. Plant Growth Promoters -->
        <div class="col">
            <a href="products.html?category=8" class="category-card-v2 h-100 cat-theme-promoters text-decoration-none">
                <div class="w-100 d-flex flex-column align-items-center">
                    <div class="category-icon-box-v2">
                        <i class="bi bi-flower2"></i>
                    </div>
                    <div class="category-title-v2"><span class="lang-mr">वाढ प्रवर्तक</span><span class="lang-en">Plant Growth Promoters</span></div>
                    <div class="category-sub-v2"><span class="lang-mr">ह्युमिक ॲसिड, सी-वीड व टॉनिक</span><span class="lang-en">Humic acid, seaweed extract and flowering boosters.</span></div>
                </div>
                <div class="category-explore-link mt-2">
                    <span class="lang-mr">पहा</span><span class="lang-en">Explore</span>
                    <i class="bi bi-arrow-right"></i>
                </div>
            </a>
        </div>

        <!-- 8. Seeds -->
        <div class="col">
            <a href="products.html?category=1" class="category-card-v2 h-100 cat-theme-seeds text-decoration-none">
                <div class="w-100 d-flex flex-column align-items-center">
                    <div class="category-icon-box-v2">
                        <i class="bi bi-flower1"></i>
                    </div>
                    <div class="category-title-v2"><span class="lang-mr">बियाणे</span><span class="lang-en">Seeds</span></div>
                    <div class="category-sub-v2"><span class="lang-mr">अधिक उत्पन्न देणारे प्रमाणित संकरित बियाणे</span><span class="lang-en">High yield certified hybrid and organic crop seeds.</span></div>
                </div>
                <div class="category-explore-link mt-2">
                    <span class="lang-mr">पहा</span><span class="lang-en">Explore</span>
                    <i class="bi bi-arrow-right"></i>
                </div>
            </a>
        </div>
    </div>
</section>

<!-- ===== ⭐ FEATURED PRODUCTS (Screenshot 5) ===== -->
<section class="container featured-section my-5">
    <div class="featured-header d-flex justify-content-between align-items-center mb-4">
        <div>
            <div class="d-flex align-items-center gap-2 mb-1">
                <span class="badge px-3 py-1 rounded-pill fw-bold text-success" style="background: rgba(22, 163, 74, 0.12); border: 1px solid rgba(22, 163, 74, 0.25); font-size: 0.75rem;">
                    <span class="lang-mr">⭐ मुख्य उत्पादने</span><span class="lang-en">⭐ Top Picks</span>
                </span>
            </div>
            <h2 class="featured-title mb-1 fw-bold" style="font-size: 1.85rem;">
                <span class="lang-mr">वैशिष्ट्यपूर्ण उत्पादने (Featured products)</span><span class="lang-en">Featured products</span>
            </h2>
            <p class="featured-subtitle text-muted mb-0">
                <span class="lang-mr">उत्पादनांचे तपशील आणि सध्याचे दर पाहा.</span>
                <span class="lang-en">Browse product details and current prices.</span>
            </p>
        </div>
        <div>
            <a href="products.html" class="featured-view-all text-decoration-none fw-semibold">
                <span class="lang-mr">सर्व उत्पादने पहा</span><span class="lang-en">View all</span>
                <i class="bi bi-arrow-right ms-1"></i>
            </a>
        </div>
    </div>

    <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
        <!-- Product 1: Wheat Seeds (Lok-1) -->
        <div class="col">
            <div class="product-featured-card">
                <div class="product-featured-img-wrap">
                    <span class="product-featured-discount-badge">7% OFF</span>
                    <span class="product-featured-cat-badge"><span class="lang-mr">बियाणे</span><span class="lang-en">Seeds</span></span>
                    <img src="images/wheat_seeds.jpg" alt="Wheat Seeds (Lok-1)" loading="lazy" decoding="async" onerror="this.src='images/saptashrungi_shop.jpg'">
                </div>
                <div class="product-featured-content">
                    <div class="product-featured-company">MAHABEEJ</div>
                    <div class="product-featured-title">
                        <a href="products.html" class="text-decoration-none">
                            <span class="lang-mr">गहू बियाणे (लोक-१)</span>
                            <span class="lang-en">Wheat Seeds (Lok-1)</span>
                        </a>
                    </div>
                    <div class="product-featured-price-row">
                        <span class="product-featured-price">₹1,350</span>
                        <span class="product-featured-strike">₹1,450</span>
                        <span class="product-featured-unit">/ 40 kg bag</span>
                    </div>

                    <!-- Stock & Rating Meta -->
                    <div class="product-featured-meta">
                        <div class="product-featured-stock">
                            <span class="stock-dot"></span>
                            <span><span class="lang-mr">उपलब्ध आहे</span><span class="lang-en">In stock</span></span>
                        </div>
                        <div class="product-featured-rating">
                            <span>★</span>
                            <span>4.95</span>
                            <span class="fw-normal">(48)</span>
                        </div>
                    </div>

                    <!-- More Information Block -->
                    <div class="product-featured-info-block">
                        <div class="product-featured-info-row">
                            <i class="bi bi-receipt-cutoff"></i>
                            <span class="product-featured-info-label">GST:</span>
                            <span>0.00%</span>
                        </div>
                        <div class="product-featured-info-row">
                            <i class="bi bi-box-seam"></i>
                            <span class="product-featured-info-label"><span class="lang-mr">साठा:</span><span class="lang-en">Stock:</span></span>
                            <span>60 units</span>
                        </div>
                        <div class="product-featured-info-row">
                            <i class="bi bi-building"></i>
                            <span class="product-featured-info-label"><span class="lang-mr">ब्रँड:</span><span class="lang-en">Brand:</span></span>
                            <span>MAHABEEJ</span>
                        </div>
                    </div>

                    <!-- Action Row: View Product Button & WhatsApp -->
                    <div class="d-flex align-items-center gap-2">
                        <a href="products.html" class="btn-view-product flex-grow-1 text-decoration-none">
                            <i class="bi bi-eye-fill me-1"></i>
                            <span class="lang-mr">उत्पादन पहा</span><span class="lang-en">View Product</span>
                        </a>
                        <a href="https://wa.me/918600813827?text=नमस्कार,%20मला%20Wheat%20Seeds%20(Lok-1)%20बद्दल%20अधिक%20माहिती%20हवी%20आहे."
                           target="_blank" rel="noopener noreferrer"
                           class="btn-card-whatsapp-icon"
                           title="WhatsApp Order">
                            <i class="bi bi-whatsapp"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>

        <!-- Product 2: Soybean Seeds (JS-335) -->
        <div class="col">
            <div class="product-featured-card">
                <div class="product-featured-img-wrap">
                    <span class="product-featured-discount-badge">8% OFF</span>
                    <span class="product-featured-cat-badge"><span class="lang-mr">बियाणे</span><span class="lang-en">Seeds</span></span>
                    <img src="images/soybean_seeds.jpg" alt="Soybean Seeds (JS-335)" loading="lazy" decoding="async" onerror="this.src='images/saptashrungi_shop.jpg'">
                </div>
                <div class="product-featured-content">
                    <div class="product-featured-company">MAHABEEJ</div>
                    <div class="product-featured-title">
                        <a href="products.html" class="text-decoration-none">
                            <span class="lang-mr">सोयाबीन बियाणे (JS-335)</span>
                            <span class="lang-en">Soybean Seeds (JS-335)</span>
                        </a>
                    </div>
                    <div class="product-featured-price-row">
                        <span class="product-featured-price">₹2,950</span>
                        <span class="product-featured-strike">₹3,200</span>
                        <span class="product-featured-unit">/ 30 kg bag</span>
                    </div>

                    <!-- Stock & Rating Meta -->
                    <div class="product-featured-meta">
                        <div class="product-featured-stock">
                            <span class="stock-dot"></span>
                            <span><span class="lang-mr">उपलब्ध आहे</span><span class="lang-en">In stock</span></span>
                        </div>
                        <div class="product-featured-rating">
                            <span>★</span>
                            <span>4.92</span>
                            <span class="fw-normal">(36)</span>
                        </div>
                    </div>

                    <!-- More Information Block -->
                    <div class="product-featured-info-block">
                        <div class="product-featured-info-row">
                            <i class="bi bi-receipt-cutoff"></i>
                            <span class="product-featured-info-label">GST:</span>
                            <span>0.00%</span>
                        </div>
                        <div class="product-featured-info-row">
                            <i class="bi bi-box-seam"></i>
                            <span class="product-featured-info-label"><span class="lang-mr">साठा:</span><span class="lang-en">Stock:</span></span>
                            <span>40 units</span>
                        </div>
                        <div class="product-featured-info-row">
                            <i class="bi bi-building"></i>
                            <span class="product-featured-info-label"><span class="lang-mr">ब्रँड:</span><span class="lang-en">Brand:</span></span>
                            <span>MAHABEEJ</span>
                        </div>
                    </div>

                    <!-- Action Row: View Product Button & WhatsApp -->
                    <div class="d-flex align-items-center gap-2">
                        <a href="products.html" class="btn-view-product flex-grow-1 text-decoration-none">
                            <i class="bi bi-eye-fill me-1"></i>
                            <span class="lang-mr">उत्पादन पहा</span><span class="lang-en">View Product</span>
                        </a>
                        <a href="https://wa.me/918600813827?text=नमस्कार,%20मला%20Soybean%20Seeds%20(JS-335)%20बद्दल%20अधिक%20माहिती%20हवी%20आहे."
                           target="_blank" rel="noopener noreferrer"
                           class="btn-card-whatsapp-icon"
                           title="WhatsApp Order">
                            <i class="bi bi-whatsapp"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>

        <!-- Product 3: NPK 19:19:19 -->
        <div class="col">
            <div class="product-featured-card">
                <div class="product-featured-img-wrap">
                    <span class="product-featured-discount-badge">20% OFF</span>
                    <span class="product-featured-cat-badge"><span class="lang-mr">खते</span><span class="lang-en">Fertilizers</span></span>
                    <img src="images/npk_191919.jpg" alt="NPK 19:19:19" loading="lazy" decoding="async" onerror="this.src='images/saptashrungi_shop.jpg'">
                </div>
                <div class="product-featured-content">
                    <div class="product-featured-company">IFFCO</div>
                    <div class="product-featured-title">
                        <a href="products.html" class="text-decoration-none">
                            <span class="lang-mr">इफको NPK १९:१९:१९</span>
                            <span class="lang-en">NPK 19:19:19</span>
                        </a>
                    </div>
                    <div class="product-featured-price-row">
                        <span class="product-featured-price">₹1,890</span>
                        <span class="product-featured-strike">₹2,350</span>
                        <span class="product-featured-unit">/ 50 kg bag</span>
                    </div>

                    <!-- Stock & Rating Meta -->
                    <div class="product-featured-meta">
                        <div class="product-featured-stock">
                            <span class="stock-dot"></span>
                            <span><span class="lang-mr">उपलब्ध आहे</span><span class="lang-en">In stock</span></span>
                        </div>
                        <div class="product-featured-rating">
                            <span>★</span>
                            <span>4.90</span>
                            <span class="fw-normal">(42)</span>
                        </div>
                    </div>

                    <!-- More Information Block -->
                    <div class="product-featured-info-block">
                        <div class="product-featured-info-row">
                            <i class="bi bi-receipt-cutoff"></i>
                            <span class="product-featured-info-label">GST:</span>
                            <span>5.00%</span>
                        </div>
                        <div class="product-featured-info-row">
                            <i class="bi bi-box-seam"></i>
                            <span class="product-featured-info-label"><span class="lang-mr">साठा:</span><span class="lang-en">Stock:</span></span>
                            <span>85 units</span>
                        </div>
                        <div class="product-featured-info-row">
                            <i class="bi bi-building"></i>
                            <span class="product-featured-info-label"><span class="lang-mr">ब्रँड:</span><span class="lang-en">Brand:</span></span>
                            <span>IFFCO</span>
                        </div>
                    </div>

                    <!-- Action Row: View Product Button & WhatsApp -->
                    <div class="d-flex align-items-center gap-2">
                        <a href="products.html" class="btn-view-product flex-grow-1 text-decoration-none">
                            <i class="bi bi-eye-fill me-1"></i>
                            <span class="lang-mr">उत्पादन पहा</span><span class="lang-en">View Product</span>
                        </a>
                        <a href="https://wa.me/918600813827?text=नमस्कार,%20मला%20NPK%2019:19:19%20बद्दल%20अधिक%20माहिती%20हवी%20आहे."
                           target="_blank" rel="noopener noreferrer"
                           class="btn-card-whatsapp-icon"
                           title="WhatsApp Order">
                            <i class="bi bi-whatsapp"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ===== 💬 COMPACT REVIEWS SECTION (शेतकरी अभिप्राय व मते) ===== -->
<section id="reviews" class="container my-4 py-2">
    <!-- Compact Header -->
    <div class="text-center mb-3">
        <span class="badge px-3 py-1 rounded-pill fw-semibold mb-1 text-success bg-success-subtle border border-success-subtle" style="font-size: 0.8rem;">
            ⭐ <span class="lang-mr">शेतकरी अभिप्राय व रेटिंग</span><span class="lang-en">Farmer Reviews &amp; Ratings</span>
        </span>
        <h3 class="fw-bold text-dark mb-1" style="font-size: 1.45rem;">
            <span class="lang-mr">शेतकरी बांधवांचे अनुभव</span><span class="lang-en">What Farmers Say</span>
        </h3>
    </div>

    <!-- Rating Summary Pill Strip -->
    <div class="d-flex align-items-center justify-content-center gap-3 flex-wrap bg-white rounded-pill shadow-sm border py-2 px-4 mx-auto mb-3" style="max-width: 620px;">
        <div class="d-flex align-items-center gap-1 text-warning fw-bold">
            <span class="text-dark">4.9</span>
            <i class="bi bi-star-fill text-warning"></i>
        </div>
        <span class="text-muted small">•</span>
        <span class="text-dark small fw-semibold"><span class="lang-mr">५००+ समाधानी शेतकरी</span><span class="lang-en">500+ Happy Farmers</span></span>
        <span class="text-muted small">•</span>
        <span class="text-success small fw-semibold"><i class="bi bi-patch-check-fill me-1"></i><span class="lang-mr">१००% अस्सल उत्पादने</span><span class="lang-en">100% Genuine Supplies</span></span>
    </div>

    <!-- Compact Reviews Row (3 Clean Cards) -->
    <div class="row g-3 justify-content-center">
        <!-- Review 1 -->
        <div class="col-md-4">
            <div class="card h-100 border-0 shadow-sm rounded-4 p-3 bg-white border border-light-subtle">
                <div class="d-flex align-items-center justify-content-between mb-2">
                    <div class="d-flex align-items-center gap-2">
                        <div class="rounded-circle d-flex align-items-center justify-content-center text-white fw-bold" style="width: 34px; height: 34px; background: #16a34a; font-size: 0.82rem;">
                            RP
                        </div>
                        <div>
                            <strong class="d-block text-dark small" style="line-height: 1.2;"><span class="lang-mr">रमेश पाटील</span><span class="lang-en">Ramesh Patil</span></strong>
                            <small class="text-muted" style="font-size: 0.72rem;"><span class="lang-mr">वैजापूर (कापूस)</span><span class="lang-en">Vaijapur (Cotton)</span></small>
                        </div>
                    </div>
                    <div class="text-warning" style="font-size: 0.75rem;">
                        <i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i>
                    </div>
                </div>
                <p class="text-secondary small mb-0 fst-italic" style="font-size: 0.84rem; line-height: 1.45;">
                    <span class="lang-mr">« कापूस बियाणे १००% उगवण आणि उत्तम दर्जा. वेळेवर शेतपोच सेवा मिळाली! »</span>
                    <span class="lang-en">« Certified cotton seeds with 100% germination. Punctual farm delivery! »</span>
                </p>
            </div>
        </div>

        <!-- Review 2 -->
        <div class="col-md-4">
            <div class="card h-100 border-0 shadow-sm rounded-4 p-3 bg-white border border-light-subtle">
                <div class="d-flex align-items-center justify-content-between mb-2">
                    <div class="d-flex align-items-center gap-2">
                        <div class="rounded-circle d-flex align-items-center justify-content-center text-white fw-bold" style="width: 34px; height: 34px; background: #0284c7; font-size: 0.82rem;">
                            SD
                        </div>
                        <div>
                            <strong class="d-block text-dark small" style="line-height: 1.2;"><span class="lang-mr">सुरेश देशमुख</span><span class="lang-en">Suresh Deshmukh</span></strong>
                            <small class="text-muted" style="font-size: 0.72rem;"><span class="lang-mr">श्रीरामपूर (ऊस)</span><span class="lang-en">Shrirampur (Cane)</span></small>
                        </div>
                    </div>
                    <div class="text-warning" style="font-size: 0.75rem;">
                        <i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i>
                    </div>
                </div>
                <p class="text-secondary small mb-0 fst-italic" style="font-size: 0.84rem; line-height: 1.45;">
                    <span class="lang-mr">« अस्सल खते आणि अचूक मार्गदर्शन. रास्त दर आणि उधारी सुविधा खूप सोयीची आहे. »</span>
                    <span class="lang-en">« Genuine fertilizers, expert advice, fair prices and helpful credit facility. »</span>
                </p>
            </div>
        </div>

        <!-- Review 3 -->
        <div class="col-md-4">
            <div class="card h-100 border-0 shadow-sm rounded-4 p-3 bg-white border border-light-subtle">
                <div class="d-flex align-items-center justify-content-between mb-2">
                    <div class="d-flex align-items-center gap-2">
                        <div class="rounded-circle d-flex align-items-center justify-content-center text-white fw-bold" style="width: 34px; height: 34px; background: #d97706; font-size: 0.82rem;">
                            DP
                        </div>
                        <div>
                            <strong class="d-block text-dark small" style="line-height: 1.2;"><span class="lang-mr">ज्ञानेश्वर पवार</span><span class="lang-en">Dnyaneshwar Pawar</span></strong>
                            <small class="text-muted" style="font-size: 0.72rem;"><span class="lang-mr">गंगापूर (सोयाबीन)</span><span class="lang-en">Gangapur (Soybean)</span></small>
                        </div>
                    </div>
                    <div class="text-warning" style="font-size: 0.75rem;">
                        <i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i>
                    </div>
                </div>
                <p class="text-secondary small mb-0 fst-italic" style="font-size: 0.84rem; line-height: 1.45;">
                    <span class="lang-mr">« कीटकनाशकांमुळे अळीचे २ दिवसांत नियंत्रण. प्रामाणिक सल्ला देणारे हक्काचे कृषी केंद्र! »</span>
                    <span class="lang-en">« Effective crop protection and honest agronomic guidance. Highly recommended! »</span>
                </p>
            </div>
        </div>
    </div>

    <!-- Compact Action -->
    <div class="text-center mt-3">
        <a href="https://wa.me/918600813827?text=नमस्कार,%20मी%20सप्तशृंगी%20ॲग्रो%20सर्व्हिसेसबद्दल%20अभिप्राय%20देऊ%20इच्छितो." target="_blank" class="btn btn-sm btn-outline-success rounded-pill px-3 py-1 fw-semibold text-decoration-none">
            <i class="bi bi-chat-heart me-1"></i>
            <span class="lang-mr">अभिप्राय द्या</span><span class="lang-en">Share Feedback</span>
        </a>
    </div>
</section>

<!-- ===== 🛡️ STORE INFORMATION AND SERVICES (4-Card Grid) ===== -->
<section class="container my-5 py-3">
    <div class="text-center mb-5">
        <span class="badge px-3 py-1 rounded-pill fw-semibold mb-2 d-inline-block text-success"
              style="background: rgba(22, 163, 74, 0.12); border: 1px solid rgba(22, 163, 74, 0.25); font-size: 0.78rem;">
            <span class="lang-mr">⭐ दुकानाची माहिती</span><span class="lang-en">⭐ Store information</span>
        </span>
        <h2 class="fw-bold text-success mb-2" style="font-size: 1.85rem;">
            <span class="lang-mr">सप्तशृंगी ॲग्रो सर्व्हिसेस</span><span class="lang-en">Saptashrungi Agro Services</span>
        </h2>
        <p class="text-muted small mx-auto" style="max-width: 580px;">
            <span class="lang-mr">उत्पादनांची माहिती, दुकानाची संपर्क माहिती आणि उपलब्ध ऑनलाइन सुविधा.</span>
            <span class="lang-en">Product information, store contact details, and available online services.</span>
        </p>
    </div>

    <div class="row g-4">
        <!-- 1. Product details -->
        <div class="col-md-3 col-sm-6">
            <div class="trust-card-v2">
                <div class="trust-icon-box-v2" style="background: linear-gradient(135deg, #10b981 0%, #059669 100%);">
                    <i class="bi bi-shield-check"></i>
                </div>
                <h5 class="fw-bold text-dark mb-2" style="font-size: 1.05rem;">
                    <span class="lang-mr">उत्पादन तपशील</span><span class="lang-en">Product details</span>
                </h5>
                <p class="small text-muted mb-0">
                    <span class="lang-mr">उत्पादनाचे नाव, किंमत आणि उपलब्ध तपशील उत्पादन पानावर पाहा.</span>
                    <span class="lang-en">View product names, prices, and available details on each product page.</span>
                </p>
            </div>
        </div>

        <!-- 2. Price information -->
        <div class="col-md-3 col-sm-6">
            <div class="trust-card-v2">
                <div class="trust-icon-box-v2" style="background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%);">
                    <i class="bi bi-tag-fill"></i>
                </div>
                <h5 class="fw-bold text-dark mb-2" style="font-size: 1.05rem;">
                    <span class="lang-mr">किंमत व कर तपशील</span><span class="lang-en">Prices and taxes</span>
                </h5>
                <p class="small text-muted mb-0">
                    <span class="lang-mr">उत्पादन पानावर दर्शवलेली किंमत आणि ऑर्डरवेळी लागू होणारे कर तपासा.</span>
                    <span class="lang-en">Review listed product prices and any applicable taxes during checkout.</span>
                </p>
            </div>
        </div>

        <!-- 3. Credit ledger -->
        <div class="col-md-3 col-sm-6">
            <div class="trust-card-v2">
                <div class="trust-icon-box-v2" style="background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);">
                    <i class="bi bi-credit-card-2-front-fill"></i>
                </div>
                <h5 class="fw-bold text-dark mb-2" style="font-size: 1.05rem;">
                    <span class="lang-mr">उधारी खाते</span><span class="lang-en">Credit ledger</span>
                </h5>
                <p class="small text-muted mb-0">
                    <span class="lang-mr">नोंदणीकृत ग्राहकांना त्यांच्या डॅशबोर्डवर उधारीची नोंद पाहता येते.</span>
                    <span class="lang-en">Registered customers can view their credit ledger in the dashboard.</span>
                </p>
            </div>
        </div>

        <!-- 4. Farming information -->
        <div class="col-md-3 col-sm-6">
            <div class="trust-card-v2">
                <div class="trust-icon-box-v2" style="background: linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%);">
                    <i class="bi bi-chat-heart-fill"></i>
                </div>
                <h5 class="fw-bold text-dark mb-2" style="font-size: 1.05rem;">
                    <span class="lang-mr">शेतीविषयक माहिती</span><span class="lang-en">Farming information</span>
                </h5>
                <p class="small text-muted mb-0">
                    <span class="lang-mr">पीकविषयक माहिती, हवामान पान आणि खत कॅल्क्युलेटर वेबसाइटवर उपलब्ध आहेत.</span>
                    <span class="lang-en">Crop information, a weather page, and a fertilizer calculator are available on this site.</span>
                </p>
            </div>
        </div>
    </div>
</section>

<!-- ===== 📍 STORE LOCATION & GOOGLE MAPS SECTION ===== -->
<section class="container mb-5">
    <div class="card border-0 shadow-sm rounded-4 overflow-hidden" style="background: #ffffff; border: 1px solid #e5e7eb !important;">
        <div class="row g-0">
            <!-- Left: Google Maps Interactive Embed -->
            <div class="col-lg-7">
                <div class="h-100" style="min-height: 280px;">
                    <iframe 
                        src="https://maps.google.com/maps?q=19.9852957,74.9312239&hl=mr&z=17&output=embed" 
                        width="100%" 
                        height="100%" 
                        style="border:0; min-height: 280px; width: 100%; display: block;" 
                        allowfullscreen="" 
                        loading="lazy" 
                        referrerpolicy="no-referrer-when-downgrade">
                    </iframe>
                </div>
            </div>
            
            <!-- Right: Location Details & Action Buttons -->
            <div class="col-lg-5 p-4 p-lg-4 d-flex flex-column justify-content-between">
                <div>
                    <div class="d-flex align-items-center gap-2 mb-2">
                        <span class="badge bg-danger-subtle text-danger border border-danger px-3 py-1 rounded-pill fw-bold">
                            <span class="lang-mr">📍 दुकानाचा पत्ता</span><span class="lang-en">📍 Store Location</span>
                        </span>
                    </div>
                    <h3 class="fw-bold text-dark mb-3">
                        <span class="lang-mr">सप्तशृंगी ॲग्रो सर्व्हिसेस</span><span class="lang-en">Saptashrungi Agro Services</span>
                    </h3>
                    
                    <div class="d-flex flex-column gap-3 mb-4 text-muted small">
                        <div class="d-flex align-items-start gap-3">
                            <div class="rounded-circle d-flex align-items-center justify-content-center bg-light text-danger flex-shrink-0" style="width: 36px; height: 36px; font-size: 18px;">
                                <i class="bi bi-geo-alt-fill"></i>
                            </div>
                            <div>
                                <strong class="text-dark d-block"><span class="lang-mr">पत्ता:</span><span class="lang-en">Address:</span></strong>
                                <span>Saptashrungi Agro Services, Mirakhnagar, Vaijapur, Chhatrapati Sambhajinagar, Maharashtra - 423703</span>
                            </div>
                        </div>

                        <div class="d-flex align-items-start gap-3">
                            <div class="rounded-circle d-flex align-items-center justify-content-center bg-light text-primary flex-shrink-0" style="width: 36px; height: 36px; font-size: 18px;">
                                <i class="bi bi-clock-fill"></i>
                            </div>
                            <div>
                                <strong class="text-dark d-block"><span class="lang-mr">वेळ:</span><span class="lang-en">Opening Hours:</span></strong>
                                <span><span class="lang-mr">सोमवार ते शनिवार: सकाळी ८:०० ते रात्री ८:३०</span><span class="lang-en">Mon - Sat: 8:00 AM – 8:30 PM</span></span>
                            </div>
                        </div>

                        <div class="d-flex align-items-start gap-3">
                            <div class="rounded-circle d-flex align-items-center justify-content-center bg-light text-success flex-shrink-0" style="width: 36px; height: 36px; font-size: 18px;">
                                <i class="bi bi-telephone-fill"></i>
                            </div>
                            <div>
                                <strong class="text-dark d-block"><span class="lang-mr">संपर्क क्रमांक:</span><span class="lang-en">Direct Contact:</span></strong>
                                <span><a href="tel:+918600813827" class="text-dark fw-bold text-decoration-none">+91 8600813827</a></span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="d-flex flex-column gap-2">
                    <a href="https://maps.app.goo.gl/S34rKk9DwEntCGid6" target="_blank" rel="noopener noreferrer" class="btn btn-success py-2 px-3 fw-semibold shadow-sm d-flex align-items-center justify-content-center gap-2" style="background-color: #16a34a; border: none;">
                        <i class="bi bi-map-fill fs-5"></i> <span><span class="lang-mr">📍 गुगल मॅपवर उघडा</span><span class="lang-en">📍 Open in Google Maps</span></span>
                    </a>
                    <div class="d-flex gap-2">
                        <a href="https://www.google.com/maps/dir/?api=1&destination=19.9852957,74.9312239" target="_blank" rel="noopener noreferrer" class="btn btn-light border py-2 px-3 fw-semibold text-dark flex-fill d-flex align-items-center justify-content-center gap-1 text-decoration-none">
                            <i class="bi bi-cursor-fill text-primary"></i> <span><span class="lang-mr">मार्ग पहा</span><span class="lang-en">Get Directions</span></span>
                        </a>
                        <a href="https://wa.me/918600813827?text=Namaste%20Saptashrungi%20Agro%20Services" target="_blank" rel="noopener noreferrer" class="btn btn-light border py-2 px-3 fw-semibold text-success flex-fill d-flex align-items-center justify-content-center gap-1 text-decoration-none">
                            <i class="bi bi-whatsapp"></i> <span class="lang-mr">व्हॉट्सॲप (8600813827)</span><span class="lang-en">WhatsApp (8600813827)</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
""" + foot_html()
    
    with open(os.path.join(DIST_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Successfully built dist/index.html with all rich sections from screenshots!")

if __name__ == "__main__":
    build_home_page()
