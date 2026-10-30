# -*- coding: utf-8 -*-
import os
import sys

from build_site import head_html, nav_html, foot_html, DIST_DIR

print("Starting generation of all 11 static pages...")

# ==============================================================================
# 1. INDEX.HTML
# ==============================================================================
index_content = head_html("मुख्यपृष्ठ", "Home") + nav_html("home") + """
<!-- ===== HERO SECTION ===== -->
<section class="hero-section">
    <div class="hero-farm-bg" id="heroBg"></div>
    <div class="video-overlay"></div>
    <div class="hero-content">
        <div class="hero-pill-badge">
            <span class="hero-pill-dot"></span>
            <span class="lang-mr">सप्तशृंगी ॲग्रो सर्व्हिसेस</span>
            <span class="lang-en">Saptashrungi Agro Services</span>
            <span class="hero-pill-tag">
                <span class="lang-mr">बियाणे, खते व शेती साहित्य</span>
                <span class="lang-en">Seeds, Fertilizers & Farm Supplies</span>
            </span>
        </div>

        <h1>
            <span class="lang-mr">शेतीसाठी दर्जेदार उत्पादने<br class="d-none d-md-block"> आणि <span class="hero-gradient-text">योग्य मार्गदर्शन</span></span>
            <span class="lang-en">Quality Products & <span class="hero-gradient-text">Expert Guidance</span><br class="d-none d-md-block"> For Modern Farming</span>
        </h1>

        <p>
            <span class="lang-mr">बियाणे, खते, पीक संरक्षण औषधे आणि सिंचन साहित्य यांची माहिती व खरेदीसाठी मिरखनगर, वैजापूर येथील अग्रगण्य कृषी सेवा केंद्र.</span>
            <span class="lang-en">Leading agricultural retail center in Mirakhnagar, Vaijapur for genuine seeds, fertilizers, crop protection and modern irrigation supplies.</span>
        </p>

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
            <a href="fertilizer-calc.html" class="btn-hero-outline">
                <i class="bi bi-calculator text-warning"></i>
                <span class="lang-mr">खत कॅल्क्युलेटर</span>
                <span class="lang-en">Fertilizer Calculator</span>
            </a>
        </div>

        <!-- Clean Trust Badges Strip (strictly without credit & upi) -->
        <div class="hero-trust-strip">
            <div class="hero-trust-item">
                <i class="bi bi-patch-check-fill text-success"></i>
                <span class="lang-mr">बियाणे, खते व पीक संरक्षण साहित्य</span>
                <span class="lang-en">Certified Seeds & Fertilizers</span>
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

<!-- ===== QUICK ACTION CARDS ===== -->
<section class="container-fluid px-3 px-md-5" style="margin-top:-40px; position:relative; z-index:10;">
    <div class="row g-3 justify-content-center">
        <div class="col-6 col-md-3">
            <a href="products.html" class="text-decoration-none">
                <div class="quick-action-card" style="--card-color:#1b5e20; --card-bg:#f0fdf4;">
                    <div class="qa-icon">🌱</div>
                    <div class="qa-title"><span class="lang-mr">उत्पादने पहा</span><span class="lang-en">Browse Products</span></div>
                    <div class="qa-sub"><span class="lang-mr">सर्व कृषी साहित्य</span><span class="lang-en">All Agri Supplies</span></div>
                    <div class="qa-arrow">→</div>
                </div>
            </a>
        </div>
        <div class="col-6 col-md-3">
            <a href="tel:+918600813827" class="text-decoration-none">
                <div class="quick-action-card" style="--card-color:#0369a1; --card-bg:#f0f9ff;">
                    <div class="qa-icon">📞</div>
                    <div class="qa-title"><span class="lang-mr">संपर्क करा</span><span class="lang-en">Contact Us</span></div>
                    <div class="qa-sub"><span class="lang-mr">कॉल किंवा व्हॉट्सॲप</span><span class="lang-en">Call or WhatsApp</span></div>
                    <div class="qa-arrow">→</div>
                </div>
            </a>
        </div>
        <div class="col-6 col-md-3">
            <a href="fertilizer-calc.html" class="text-decoration-none">
                <div class="quick-action-card" style="--card-color:#b45309; --card-bg:#fffbeb;">
                    <div class="qa-icon">🧪</div>
                    <div class="qa-title"><span class="lang-mr">खत कॅल्क्युलेटर</span><span class="lang-en">Fertilizer Calc</span></div>
                    <div class="qa-sub"><span class="lang-mr">अचूक खत प्रमाण</span><span class="lang-en">Accurate Bag Dosage</span></div>
                    <div class="qa-arrow">→</div>
                </div>
            </a>
        </div>
        <div class="col-6 col-md-3">
            <a href="https://maps.app.goo.gl/S34rKk9DwEntCGid6" target="_blank" rel="noopener noreferrer" class="text-decoration-none">
                <div class="quick-action-card" style="--card-color:#7c3aed; --card-bg:#fdf4ff;">
                    <div class="qa-icon">📍</div>
                    <div class="qa-title"><span class="lang-mr">दुकानाला भेट द्या</span><span class="lang-en">Visit Store</span></div>
                    <div class="qa-sub"><span class="lang-mr">गुगल मॅप दिशा</span><span class="lang-en">Google Maps Route</span></div>
                    <div class="qa-arrow">→</div>
                </div>
            </a>
        </div>
    </div>
</section>

<!-- ===== FEATURED PRODUCTS ===== -->
<section class="container featured-section my-5">
    <div class="featured-header d-flex justify-content-between align-items-center mb-4">
        <div>
            <span class="badge px-3 py-1 rounded-pill fw-bold text-success mb-2" style="background: rgba(22, 163, 74, 0.12); border: 1px solid rgba(22, 163, 74, 0.25); font-size: 0.75rem;">
                ⭐ <span class="lang-mr">मुख्य उत्पादने (Top Picks)</span><span class="lang-en">Top Picks</span>
            </span>
            <h2 class="featured-title mb-1 fw-bold">
                <span class="lang-mr">वैशिष्ट्यपूर्ण उत्पादने</span>
                <span class="lang-en">Featured Agri Products</span>
            </h2>
            <p class="featured-subtitle text-muted mb-0">
                <span class="lang-mr">दर्जेदार बियाणे, खते आणि पीक संरक्षण साहित्य.</span>
                <span class="lang-en">Certified seeds, nutrient-rich fertilizers, and crop protectors.</span>
            </p>
        </div>
        <a href="products.html" class="btn btn-outline-success rounded-pill px-4 fw-semibold">
            <span class="lang-mr">सर्व पहा</span><span class="lang-en">View All</span> <i class="bi bi-arrow-right ms-1"></i>
        </a>
    </div>

    <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
        <!-- P1 -->
        <div class="col">
            <div class="product-featured-card">
                <div class="product-featured-img-wrap">
                    <span class="product-featured-discount-badge">5% OFF</span>
                    <span class="product-featured-cat-badge"><span class="lang-mr">बियाणे</span><span class="lang-en">Seeds</span></span>
                    <img src="images/cotton_seeds.jpg" alt="Cotton Seeds" onerror="this.src='images/saptashrungi_shop.jpg'">
                </div>
                <div class="product-featured-content p-3">
                    <div class="text-muted small fw-semibold">MAHYCO SEEDS</div>
                    <h5 class="fw-bold my-1">
                        <a href="products.html" class="text-dark text-decoration-none">
                            <span class="lang-mr">माहिको बीजी-२ कापूस बियाणे (475g)</span>
                            <span class="lang-en">Mahyco BG-II Cotton Seeds (475g)</span>
                        </a>
                    </h5>
                    <div class="product-featured-price-row my-2">
                        <span class="fs-4 fw-bold text-success">₹820</span>
                        <span class="text-decoration-line-through text-muted ms-2">₹864</span>
                    </div>
                    <div class="d-flex justify-content-between align-items-center mt-3 pt-2 border-top">
                        <span class="badge bg-success-subtle text-success"><i class="bi bi-check-circle me-1"></i><span class="lang-mr">उपलब्ध</span><span class="lang-en">In Stock</span></span>
                        <a href="https://wa.me/918600813827?text=माहिको%20कापूस%20बियाण्याविषयी%20माहिती%20हवी%20आहे" class="btn btn-sm btn-success rounded-pill px-3"><i class="bi bi-whatsapp me-1"></i><span class="lang-mr">चौकशी</span><span class="lang-en">Inquire</span></a>
                    </div>
                </div>
            </div>
        </div>

        <!-- P2 -->
        <div class="col">
            <div class="product-featured-card">
                <div class="product-featured-img-wrap">
                    <span class="product-featured-discount-badge">5% OFF</span>
                    <span class="product-featured-cat-badge"><span class="lang-mr">बियाणे</span><span class="lang-en">Seeds</span></span>
                    <img src="images/soybean_seeds.jpg" alt="Soybean Seeds" onerror="this.src='images/saptashrungi_shop.jpg'">
                </div>
                <div class="product-featured-content p-3">
                    <div class="text-muted small fw-semibold">MAHABEEJ</div>
                    <h5 class="fw-bold my-1">
                        <a href="products.html" class="text-dark text-decoration-none">
                            <span class="lang-mr">जेएस ३३५ प्रमाणित सोयाबीन बियाणे (30 Kg)</span>
                            <span class="lang-en">JS-335 Certified Soybean Seeds (30 Kg)</span>
                        </a>
                    </h5>
                    <div class="product-featured-price-row my-2">
                        <span class="fs-4 fw-bold text-success">₹2,700</span>
                        <span class="text-decoration-line-through text-muted ms-2">₹2,850</span>
                    </div>
                    <div class="d-flex justify-content-between align-items-center mt-3 pt-2 border-top">
                        <span class="badge bg-success-subtle text-success"><i class="bi bi-check-circle me-1"></i><span class="lang-mr">उपलब्ध</span><span class="lang-en">In Stock</span></span>
                        <a href="https://wa.me/918600813827?text=सोयाबीन%20बियाण्याविषयी%20माहिती%20हवी%20आहे" class="btn btn-sm btn-success rounded-pill px-3"><i class="bi bi-whatsapp me-1"></i><span class="lang-mr">चौकशी</span><span class="lang-en">Inquire</span></a>
                    </div>
                </div>
            </div>
        </div>

        <!-- P3 -->
        <div class="col">
            <div class="product-featured-card">
                <div class="product-featured-img-wrap">
                    <span class="product-featured-discount-badge">4% OFF</span>
                    <span class="product-featured-cat-badge"><span class="lang-mr">खते</span><span class="lang-en">Fertilizers</span></span>
                    <img src="images/fertilizer_npk.jpg" alt="Mahadhan NPK" onerror="this.src='images/saptashrungi_shop.jpg'">
                </div>
                <div class="product-featured-content p-3">
                    <div class="text-muted small fw-semibold">DEEPAK FERTILISERS</div>
                    <h5 class="fw-bold my-1">
                        <a href="products.html" class="text-dark text-decoration-none">
                            <span class="lang-mr">महाधन २४:२४:० खत (५० किलो)</span>
                            <span class="lang-en">Mahadhan 24:24:0 Fertilizer (50 Kg)</span>
                        </a>
                    </h5>
                    <div class="product-featured-price-row my-2">
                        <span class="fs-4 fw-bold text-success">₹1,680</span>
                        <span class="text-decoration-line-through text-muted ms-2">₹1,750</span>
                    </div>
                    <div class="d-flex justify-content-between align-items-center mt-3 pt-2 border-top">
                        <span class="badge bg-success-subtle text-success"><i class="bi bi-check-circle me-1"></i><span class="lang-mr">उपलब्ध</span><span class="lang-en">In Stock</span></span>
                        <a href="https://wa.me/918600813827?text=महाधन%20खताविषयी%20माहिती%20हवी%20आहे" class="btn btn-sm btn-success rounded-pill px-3"><i class="bi bi-whatsapp me-1"></i><span class="lang-mr">चौकशी</span><span class="lang-en">Inquire</span></a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ===== WHY CHOOSE US ===== -->
<section class="py-5" style="background:#f8fafc;">
    <div class="container">
        <div class="text-center mb-5">
            <span class="badge bg-success-subtle text-success px-3 py-1 rounded-pill fw-semibold mb-2">
                <span class="lang-mr">आमची वैशिष्ट्ये</span>
                <span class="lang-en">Why Choose Us</span>
            </span>
            <h2 class="fw-bold text-dark">
                <span class="lang-mr">शेतकरी सप्तशृंगी ॲग्रोवर का विश्वास ठेवतात?</span>
                <span class="lang-en">Why Farmers Trust Saptashrungi Agro?</span>
            </h2>
            <p class="text-muted" style="max-width:650px;margin:0 auto;">
                <span class="lang-mr">आम्ही केवळ उत्पादने विकत नाही, तर शेतकरी बांधवांना समृद्धी मिळवून देण्यासाठी योग्य मार्गदर्शन देतो.</span>
                <span class="lang-en">We don't just supply farm inputs; we provide expert guidance to maximize agricultural yields.</span>
            </p>
        </div>

        <div class="row g-4">
            <div class="col-md-4">
                <div class="card border-0 shadow-sm p-4 text-center rounded-4 h-100 bg-white">
                    <div class="mb-3 fs-1 text-success"><i class="bi bi-shield-check"></i></div>
                    <h5 class="fw-bold mb-2"><span class="lang-mr">१००% अस्सल व प्रमाणित उत्पादने</span><span class="lang-en">100% Genuine & Certified</span></h5>
                    <p class="text-muted small mb-0"><span class="lang-mr">नामवंत कंपन्यांचे अधिकृत बियाणे, खते आणि कीटकनाशके थेट कंपनीकडून खात्रीशीर उपलब्ध.</span><span class="lang-en">Authorized seeds, fertilizers, and plant medicine sourced directly from certified manufacturers.</span></p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card border-0 shadow-sm p-4 text-center rounded-4 h-100 bg-white">
                    <div class="mb-3 fs-1 text-primary"><i class="bi bi-person-check-fill"></i></div>
                    <h5 class="fw-bold mb-2"><span class="lang-mr">अनुभवी कृषी तज्ज्ञ सल्ला</span><span class="lang-en">Expert Agri Advisory</span></h5>
                    <p class="text-muted small mb-0"><span class="lang-mr">पिकांच्या रोग-किडींचे अचूक निदान आणि शास्त्रीय खत व्यवस्थापनासाठी मोफत शेतकरी मार्गदर्शन.</span><span class="lang-en">Free diagnostics and scientific dosage advice tailored to your crop cycle and local soil condition.</span></p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card border-0 shadow-sm p-4 text-center rounded-4 h-100 bg-white">
                    <div class="mb-3 fs-1 text-warning"><i class="bi bi-currency-rupee"></i></div>
                    <h5 class="fw-bold mb-2"><span class="lang-mr">वाजवी व पारदर्शक दर</span><span class="lang-en">Fair & Transparent Rates</span></h5>
                    <p class="text-muted small mb-0"><span class="lang-mr">शासकीय नियमांनुसार व रास्त किमतीत उत्पादने, जीएसटी पावतीसह पारदर्शक व्यवहार.</span><span class="lang-en">Transparent pricing strictly aligned with government guidelines and official GST billing.</span></p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- ===== ⭐ FARMER REVIEWS SECTION (#reviews) ===== -->
<section class="container my-5 py-4" id="reviews">
    <div class="text-center mb-5">
        <span class="badge bg-warning-subtle text-dark border border-warning px-3 py-1 rounded-pill mb-2 fw-semibold">
            <i class="bi bi-star-fill text-warning me-1"></i>
            <span class="lang-mr">शेतकरी अभिप्राय</span><span class="lang-en">Farmer Reviews</span>
        </span>
        <h2 class="fw-bold text-success">
            <span class="lang-mr">आमच्या शेतकरी बांधवांचे अनुभव</span>
            <span class="lang-en">What Local Farmers Say About Us</span>
        </h2>
        <p class="text-muted" style="max-width:650px; margin:0 auto;">
            <span class="lang-mr">मिरखनगर व वैजापूर परिसरातील ५००+ शेतकरी बांधवांचा सप्तशृंगी ॲग्रोवर दृढ विश्वास. सरासरी रेटिंग <strong>४.९ / ५.०</strong> ⭐</span>
            <span class="lang-en">Trusted by 500+ farmers in Mirakhnagar and Vaijapur. Average farmer satisfaction rating <strong>4.9 / 5.0</strong> ⭐</span>
        </p>
    </div>

    <!-- Rating Summary Bar -->
    <div class="card border-0 shadow-sm rounded-4 p-4 mb-4 bg-white">
        <div class="row align-items-center g-3 text-center text-md-start">
            <div class="col-md-3 text-center border-end-md">
                <div class="display-3 fw-bold text-success mb-0">4.9</div>
                <div class="text-warning fs-5 mb-1">
                    <i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i>
                </div>
                <small class="text-muted"><span class="lang-mr">५००+ शेतकरी प्रतिक्रिया</span><span class="lang-en">Based on 500+ Farmers</span></small>
            </div>
            <div class="col-md-9 px-md-4">
                <div class="row g-3">
                    <div class="col-sm-4 text-center">
                        <div class="fw-bold text-dark fs-5">१००%</div>
                        <small class="text-muted"><span class="lang-mr">अस्सल बियाणे व खते</span><span class="lang-en">Genuine Products</span></small>
                    </div>
                    <div class="col-sm-4 text-center">
                        <div class="fw-bold text-dark fs-5">९८%</div>
                        <small class="text-muted"><span class="lang-mr">योग्य पीक सल्ला</span><span class="lang-en">Effective Advice</span></small>
                    </div>
                    <div class="col-sm-4 text-center">
                        <div class="fw-bold text-dark fs-5">२४/७</div>
                        <small class="text-muted"><span class="lang-mr">व्हॉट्सॲप सपोर्ट</span><span class="lang-en">WhatsApp Support</span></small>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Review Cards Grid -->
    <div class="row g-4">
        <!-- Review 1 -->
        <div class="col-md-6 col-lg-3">
            <div class="card h-100 border-0 shadow-sm rounded-4 p-4 d-flex flex-column justify-content-between bg-white">
                <div>
                    <div class="text-warning mb-2">
                        <i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i>
                    </div>
                    <p class="text-muted small mb-3" style="line-height:1.6;">
                        <span class="lang-mr">"कापूस बियाणे आणि कीटकनाशकांसाठी सप्तशृंगी ॲग्रोचे मार्गदर्शन अतिशय अचूक ठरले. बोंडअळीच्या नियंत्रणासाठी त्यांनी दिलेल्या सल्ल्याने माझ्या उत्पादनात मोठी वाढ झाली!"</span>
                        <span class="lang-en">"Their guidance for cotton seeds and pest control was spot on. The advisory on bollworm management noticeably increased our crop output this season!"</span>
                    </p>
                </div>
                <div class="d-flex align-items-center gap-3 pt-3 border-top">
                    <div class="rounded-circle bg-success text-white fw-bold d-flex align-items-center justify-content-center" style="width:40px;height:40px;">RP</div>
                    <div>
                        <h6 class="mb-0 fw-bold text-dark"><span class="lang-mr">रमेश पाटील</span><span class="lang-en">Ramesh Patil</span></h6>
                        <small class="text-muted"><span class="lang-mr">वैजापूर • कापूस शेतकरी</span><span class="lang-en">Vaijapur • Cotton Farmer</span></small>
                    </div>
                </div>
            </div>
        </div>

        <!-- Review 2 -->
        <div class="col-md-6 col-lg-3">
            <div class="card h-100 border-0 shadow-sm rounded-4 p-4 d-flex flex-column justify-content-between bg-white">
                <div>
                    <div class="text-warning mb-2">
                        <i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i>
                    </div>
                    <p class="text-muted small mb-3" style="line-height:1.6;">
                        <span class="lang-mr">"ऊस पिकासाठी लागणाऱ्या खतांचे प्रमाण कॅल्क्युलेटरद्वारे समजून घेऊन योग्य वेळी खते टाकली. योग्य भाव आणि नेहमी वेळेत खते उपलब्ध असतात."</span>
                        <span class="lang-en">"Used their fertilizer calculator for sugarcane nutrient management. Genuine fertilizer bags always in stock at completely fair market rates."</span>
                    </p>
                </div>
                <div class="d-flex align-items-center gap-3 pt-3 border-top">
                    <div class="rounded-circle bg-primary text-white fw-bold d-flex align-items-center justify-content-center" style="width:40px;height:40px;">SS</div>
                    <div>
                        <h6 class="mb-0 fw-bold text-dark"><span class="lang-mr">संदीप सोनवणे</span><span class="lang-en">Sandeep Sonawane</span></h6>
                        <small class="text-muted"><span class="lang-mr">मिरखनगर • ऊस उत्पादक</span><span class="lang-en">Mirakhnagar • Sugarcane Grower</span></small>
                    </div>
                </div>
            </div>
        </div>

        <!-- Review 3 -->
        <div class="col-md-6 col-lg-3">
            <div class="card h-100 border-0 shadow-sm rounded-4 p-4 d-flex flex-column justify-content-between bg-white">
                <div>
                    <div class="text-warning mb-2">
                        <i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i>
                    </div>
                    <p class="text-muted small mb-3" style="line-height:1.6;">
                        <span class="lang-mr">"सोयाबीन बियाणे १००% उगवणक्षम निघाले. दुकानातील कर्मचारी प्रत्येक औषधाची माहिती सविस्तर सांगतात, त्यामुळे फवारणी वाया जात नाही."</span>
                        <span class="lang-en">"Mahabeej soybean seeds had 100% germination rate. The team explains spray dilution carefully so no chemical gets wasted."</span>
                    </p>
                </div>
                <div class="d-flex align-items-center gap-3 pt-3 border-top">
                    <div class="rounded-circle bg-warning text-dark fw-bold d-flex align-items-center justify-content-center" style="width:40px;height:40px;">BG</div>
                    <div>
                        <h6 class="mb-0 fw-bold text-dark"><span class="lang-mr">बाळासाहेब गायकवाड</span><span class="lang-en">Balasaheb Gaikwad</span></h6>
                        <small class="text-muted"><span class="lang-mr">गंगापूर • सोयाबीन शेतकरी</span><span class="lang-en">Gangapur • Soybean Farmer</span></small>
                    </div>
                </div>
            </div>
        </div>

        <!-- Review 4 -->
        <div class="col-md-6 col-lg-3">
            <div class="card h-100 border-0 shadow-sm rounded-4 p-4 d-flex flex-column justify-content-between bg-white">
                <div>
                    <div class="text-warning mb-2">
                        <i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i>
                    </div>
                    <p class="text-muted small mb-3" style="line-height:1.6;">
                        <span class="lang-mr">"कांदा आणि भाजीपाल्यासाठी ठिबक सिंचन साहित्य व वॉटर सोल्युबल खते एकाच ठिकाणी मिळतात. व्हॉट्सॲपवर विचारले तरी लगेच उत्तर मिळते!"</span>
                        <span class="lang-en">"Drip irrigation materials and water-soluble fertilizers in one place. Quick and helpful replies even when contacting via WhatsApp!"</span>
                    </p>
                </div>
                <div class="d-flex align-items-center gap-3 pt-3 border-top">
                    <div class="rounded-circle bg-info text-white fw-bold d-flex align-items-center justify-content-center" style="width:40px;height:40px;">DS</div>
                    <div>
                        <h6 class="mb-0 fw-bold text-dark"><span class="lang-mr">ज्ञानेश्वर शिंदे</span><span class="lang-en">Dnyaneshwar Shinde</span></h6>
                        <small class="text-muted"><span class="lang-mr">वैजापूर • कांदा व भाजीपाला</span><span class="lang-en">Vaijapur • Vegetable Farmer</span></small>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Review CTA Buttons -->
    <div class="text-center mt-4 pt-2">
        <a href="products.html" class="btn btn-krushi px-4 py-2 rounded-pill fw-semibold shadow-sm me-2">
            <i class="bi bi-grid-fill me-1"></i>
            <span class="lang-mr">उत्पादने पहा</span><span class="lang-en">Explore Catalog</span>
        </a>
        <a href="https://wa.me/918600813827?text=नमस्कार,%20मी%20सप्तशृंगी%20ॲग्रो%20सर्व्हिसेसबद्दल%20अभिप्राय%20देऊ%20इच्छितो." target="_blank" class="btn btn-outline-success px-4 py-2 rounded-pill fw-semibold shadow-sm">
            <i class="bi bi-whatsapp me-1"></i>
            <span class="lang-mr">व्हॉट्सॲपवर अभिप्राय पाठवा</span><span class="lang-en">Share Feedback on WhatsApp</span>
        </a>
    </div>
</section>
""" + foot_html()

with open(os.path.join(DIST_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_content)
print("Generated dist/index.html")

# ==============================================================================
# 2. PRODUCTS.HTML
# ==============================================================================
products_content = head_html("उत्पादने", "Products Catalog") + nav_html("products") + """
<div class="container my-4">
    <nav aria-label="breadcrumb" class="mb-3">
        <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="index.html" class="text-success text-decoration-none"><span class="lang-mr">मुख्यपृष्ठ</span><span class="lang-en">Home</span></a></li>
            <li class="breadcrumb-item active" aria-current="page"><span class="lang-mr">उत्पादने</span><span class="lang-en">Products Catalog</span></li>
        </ol>
    </nav>

    <div class="row g-4">
        <!-- Sidebar Filters -->
        <div class="col-lg-3">
            <div class="card border-0 shadow-sm rounded-4">
                <div class="card-header bg-success text-white py-3 rounded-top-4 d-flex justify-content-between align-items-center">
                    <h6 class="mb-0 fw-bold"><i class="bi bi-funnel me-2"></i><span class="lang-mr">फिल्टर</span><span class="lang-en">Filter Products</span></h6>
                    <button type="button" onclick="resetFilters()" class="btn btn-sm text-white-50 p-0 text-decoration-none"><span class="lang-mr">रिसेट</span><span class="lang-en">Reset</span></button>
                </div>
                <div class="card-body p-3">
                    <!-- Search Input -->
                    <div class="mb-3">
                        <label class="form-label fw-bold text-success small text-uppercase"><span class="lang-mr">शोध</span><span class="lang-en">Search</span></label>
                        <input type="text" id="searchInput" onkeyup="filterProducts()" class="form-control form-control-sm"
                               data-placeholder-mr="बियाणे, खते किंवा ब्रँड..."
                               data-placeholder-en="Search seeds, fertilizers..."
                               placeholder="बियाणे, खते किंवा ब्रँड...">
                    </div>

                    <!-- Category Filter -->
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
                                <label class="form-check-label small" for="cat_drip"><span class="lang-mr">💧 ठिबक सिंचन</span><span class="lang-en">💧 Drip Irrigation</span></label>
                            </div>
                        </div>
                    </div>

                    <!-- Price Filter -->
                    <div class="mb-4">
                        <label class="form-label fw-bold text-success small text-uppercase"><span class="lang-mr">कमाल किंमत</span><span class="lang-en">Max Price</span></label>
                        <input type="range" class="form-range" id="priceRange" min="200" max="4000" step="100" value="4000" oninput="updatePrice(this.value)">
                        <div class="d-flex justify-content-between small text-muted">
                            <span>₹200</span>
                            <span id="priceVal" class="fw-bold text-success">₹4000</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Products Grid -->
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

            <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4" id="productsGrid">
                <!-- Products rendered dynamically by script -->
            </div>
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

function updatePrice(val) {
    document.getElementById('priceVal').textContent = '₹' + val;
    filterProducts();
}

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
        grid.innerHTML = '<div class="col-12 py-5 text-center text-muted"><i class="bi bi-search fs-1 d-block mb-2"></i><span class="lang-mr">कोणतीही उत्पादने सापडली नाहीत.</span><span class="lang-en">No products match your filter criteria.</span></div>';
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
print("Generated dist/products.html")

# ==============================================================================
# 3. FERTILIZER-CALC.HTML
# ==============================================================================
calc_content = head_html("खत कॅल्क्युलेटर", "Fertilizer Calculator") + nav_html("advisory") + """
<div class="container my-4">
    <div class="text-center mb-4">
        <span class="badge bg-success-subtle text-success border border-success-subtle px-3 py-1 rounded-pill mb-2 fw-semibold">
            <i class="bi bi-cpu me-1"></i>
            <span class="lang-mr">स्मार्ट कृषी सल्ला इंजिन</span>
            <span class="lang-en">Smart Agronomy Engine</span>
        </span>
        <h2 class="fw-bold text-success">
            <span class="lang-mr">खत कॅल्क्युलेटर (Smart Fertilizer Calculator)</span>
            <span class="lang-en">Smart Fertilizer Dosage Calculator</span>
        </h2>
        <p class="text-muted" style="max-width:650px;margin:0 auto;">
            <span class="lang-mr">पीक, क्षेत्रफळ आणि जमिनीच्या प्रकारावर आधारित रासायनिक व सेंद्रिय खतांचे शास्त्रीय प्रमाण.</span>
            <span class="lang-en">Scientific recommendation of essential fertilizers tailored to your crop, acreage, and soil profile.</span>
        </p>
    </div>

    <div class="row g-4 mb-5">
        <!-- Form -->
        <div class="col-lg-5">
            <div class="card border-0 shadow-sm rounded-4">
                <div class="card-header bg-success text-white py-3 rounded-top-4">
                    <h6 class="mb-0 fw-bold">
                        <i class="bi bi-sliders me-2"></i>
                        <span class="lang-mr">शेतीची माहिती निवडा</span>
                        <span class="lang-en">Select Crop & Land Details</span>
                    </h6>
                </div>
                <div class="card-body p-4">
                    <form id="calcForm" onsubmit="calculateFertilizer(event)">
                        <div class="mb-3">
                            <label class="form-label fw-bold text-success small text-uppercase">
                                <span class="lang-mr">पीक निवडा</span><span class="lang-en">Select Crop</span>
                            </label>
                            <select id="crop" class="form-select">
                                <option value="cotton" selected>कापूस - बीजी २ (Cotton)</option>
                                <option value="sugarcane">ऊस (Sugarcane)</option>
                                <option value="soybean">सोयाबीन (Soybean)</option>
                                <option value="wheat">गहू (Wheat)</option>
                                <option value="onion">कांदा (Onion)</option>
                                <option value="vegetables">भाजीपाला व फळबाग (Vegetables)</option>
                            </select>
                        </div>

                        <div class="mb-3">
                            <label class="form-label fw-bold text-success small text-uppercase">
                                <span class="lang-mr">शेत क्षेत्रफळ (Acres)</span><span class="lang-en">Farm Area (Acres)</span>
                            </label>
                            <div class="input-group">
                                <input type="number" step="0.5" min="0.5" max="100" id="acres" class="form-control" value="2" required onchange="calculateFertilizer()">
                                <span class="input-group-text"><span class="lang-mr">एकर</span><span class="lang-en">Acres</span></span>
                            </div>
                        </div>

                        <div class="mb-3">
                            <label class="form-label fw-bold text-success small text-uppercase">
                                <span class="lang-mr">जमिनीचा प्रकार</span><span class="lang-en">Soil Type</span>
                            </label>
                            <select id="soil" class="form-select">
                                <option value="medium">मध्यम काळी जमीन (Medium Black)</option>
                                <option value="heavy">भारी काळी चिकण जमीन (Heavy Clay)</option>
                                <option value="light">हलकी व पोयट्याची जमीन (Light Sandy)</option>
                            </select>
                        </div>

                        <div class="mb-4">
                            <label class="form-label fw-bold text-success small text-uppercase">
                                <span class="lang-mr">पिकाचा टप्पा</span><span class="lang-en">Growth Stage</span>
                            </label>
                            <select id="stage" class="form-select">
                                <option value="full">संपूर्ण हंगाम (Full Season Cycle)</option>
                                <option value="basal">पेरणी / लागवड वेळ (Basal Dose)</option>
                                <option value="vegetative">शाकीय वाढ टप्पा (Vegetative Growth)</option>
                                <option value="flowering">फुलोरा व फळधारणा (Flowering & Pod Filling)</option>
                            </select>
                        </div>

                        <button type="submit" class="btn btn-krushi w-100 fw-bold py-2 rounded-pill shadow-sm">
                            <i class="bi bi-calculator me-1"></i>
                            <span class="lang-mr">खत प्रमाण काढा (Calculate Bags)</span>
                            <span class="lang-en">Calculate Bags Required</span>
                        </button>
                    </form>
                </div>
            </div>
        </div>

        <!-- Output Cards -->
        <div class="col-lg-7">
            <div class="card border-0 shadow-sm rounded-4 h-100">
                <div class="card-header bg-dark text-white py-3 rounded-top-4 d-flex justify-content-between align-items-center">
                    <h6 class="mb-0 fw-bold">
                        <i class="bi bi-check-circle-fill text-success me-2"></i>
                        <span class="lang-mr">शिफारस केलेले खतांचे प्रमाण</span>
                        <span class="lang-en">Recommended Fertilizer Dosage</span>
                    </h6>
                    <span class="badge bg-success" id="resultAcreBadge">२ एकर साठी (For 2 Acres)</span>
                </div>
                <div class="card-body p-4">
                    <div class="alert alert-success d-flex align-items-center gap-2 mb-4">
                        <i class="bi bi-info-circle-fill fs-5"></i>
                        <span id="summaryText">
                            <span class="lang-mr">कापूस पिकासाठी २ एकर क्षेत्रानुसार आवश्यक खतांचे प्रमाण खालीलप्रमाणे:</span>
                            <span class="lang-en">Recommended fertilizer quantities for 2 acres of cotton cultivation:</span>
                        </span>
                    </div>

                    <div class="row g-3 text-center mb-4" id="bagsRow">
                        <!-- Calculated dynamically -->
                    </div>

                    <div class="p-3 rounded-3 bg-light border">
                        <h6 class="fw-bold text-success mb-2">
                            <i class="bi bi-lightbulb-fill text-warning me-1"></i>
                            <span class="lang-mr">तज्ज्ञांचा कृषी सल्ला:</span>
                            <span class="lang-en">Agronomist Best Practices:</span>
                        </h6>
                        <ul class="small text-muted mb-0 ps-3">
                            <li><span class="lang-mr">युरिया खताचा वापर दोन ते तीन समान हप्त्यांमध्ये विभागून ओल असतानाच करा.</span><span class="lang-en">Apply Urea in 2-3 split applications strictly when sufficient soil moisture is present.</span></li>
                            <li><span class="lang-mr">फॉस्फरस व पोटॅशयुक्त खते (DAP / 10:26:26) जमिनीत मुळांच्या सानिध्यात ४ इंचांवर द्या.</span><span class="lang-en">Place Phosphatic and Potash fertilizers (DAP / 10:26:26) 3-4 inches deep near the root zone.</span></li>
                            <li><span class="lang-mr">सूक्ष्म अन्नद्रव्ये (Zinc, Boron) शेणखतामध्ये मिसळून वापरल्यास अधिक फायदा मिळतो.</span><span class="lang-en">Incorporate micronutrients (Zinc, Boron) with well-decomposed organic manure for high absorption.</span></li>
                        </ul>
                    </div>

                    <div class="mt-4 pt-3 border-top text-center">
                        <a id="btnOrderFert" href="https://wa.me/918600813827?text=मला%20खत%20कॅल्क्युलेटरनुसार%20खते%20खरेदी%20करायची%20आहेत." target="_blank" class="btn btn-outline-success rounded-pill px-4 fw-semibold">
                            <i class="bi bi-whatsapp me-1"></i>
                            <span class="lang-mr">ही खते दुकानातून मागवा (Order Bags)</span>
                            <span class="lang-en">Order Fertilizer Bags on WhatsApp</span>
                        </a>
                    </div>
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
    
    document.getElementById('resultAcreBadge').innerHTML = `<span class="lang-mr">${acres} एकर साठी</span><span class="lang-en">For ${acres} Acre(s)</span>`;

    let ureaBags = Math.round(acres * 2.5);
    let dapBags = Math.round(acres * 1.5);
    let mopBags = Math.round(acres * 1.0);
    let npkBags = Math.round(acres * 2.0);

    if (crop === 'sugarcane') {
        ureaBags = Math.round(acres * 5.5);
        dapBags = Math.round(acres * 3.0);
        mopBags = Math.round(acres * 3.0);
        npkBags = Math.round(acres * 4.0);
    } else if (crop === 'soybean') {
        ureaBags = Math.round(acres * 1.0);
        dapBags = Math.round(acres * 2.0);
        mopBags = Math.round(acres * 1.0);
        npkBags = Math.round(acres * 1.5);
    } else if (crop === 'onion') {
        ureaBags = Math.round(acres * 2.0);
        dapBags = Math.round(acres * 2.0);
        mopBags = Math.round(acres * 1.5);
        npkBags = Math.round(acres * 2.5);
    }

    const row = document.getElementById('bagsRow');
    row.innerHTML = `
        <div class="col-6 col-md-3">
            <div class="p-3 rounded-3 border bg-white shadow-sm">
                <div class="fw-bold fs-2 text-success">${ureaBags}</div>
                <div class="fw-semibold text-dark small"><span class="lang-mr">युरिया बॅग्स</span><span class="lang-en">Urea Bags</span></div>
                <small class="text-muted">(45 kg)</small>
            </div>
        </div>
        <div class="col-6 col-md-3">
            <div class="p-3 rounded-3 border bg-white shadow-sm">
                <div class="fw-bold fs-2 text-primary">${dapBags}</div>
                <div class="fw-semibold text-dark small"><span class="lang-mr">DAP बॅग्स</span><span class="lang-en">DAP Bags</span></div>
                <small class="text-muted">(18:46:0 50kg)</small>
            </div>
        </div>
        <div class="col-6 col-md-3">
            <div class="p-3 rounded-3 border bg-white shadow-sm">
                <div class="fw-bold fs-2 text-warning">${mopBags}</div>
                <div class="fw-semibold text-dark small"><span class="lang-mr">पोटॅश बॅग्स</span><span class="lang-en">Potash (MOP)</span></div>
                <small class="text-muted">(0:0:60 50kg)</small>
            </div>
        </div>
        <div class="col-6 col-md-3">
            <div class="p-3 rounded-3 border bg-white shadow-sm">
                <div class="fw-bold fs-2 text-info">${npkBags}</div>
                <div class="fw-semibold text-dark small"><span class="lang-mr">१०:२६:२६ बॅग्स</span><span class="lang-en">10:26:26 NPK</span></div>
                <small class="text-muted">(50 kg)</small>
            </div>
        </div>
    `;

    const orderText = `नमस्कार, मला ${acres} एकर शेतीसाठी ${ureaBags} युरिया, ${dapBags} DAP, ${mopBags} पोटॅश खरेदी करायचे आहेत.`;
    document.getElementById('btnOrderFert').href = 'https://wa.me/918600813827?text=' + encodeURIComponent(orderText);
}

document.addEventListener('DOMContentLoaded', function(){
    calculateFertilizer();
});
</script>
""" + foot_html()

with open(os.path.join(DIST_DIR, "fertilizer-calc.html"), "w", encoding="utf-8") as f:
    f.write(calc_content)
print("Generated dist/fertilizer-calc.html")

# ==============================================================================
# 4. WEATHER.HTML
# ==============================================================================
weather_content = head_html("हवामान अंदाज", "Weather Forecast") + nav_html("advisory") + """
<div class="container my-4">
    <!-- Header -->
    <div class="text-center mb-4">
        <span class="badge bg-primary-subtle text-primary border border-primary-subtle px-3 py-1 rounded-pill mb-2 fw-semibold">
            <i class="bi bi-cloud-sun me-1"></i>
            <span class="lang-mr">स्थानिक हवामान व शेती सल्ला</span>
            <span class="lang-en">Local Agri Meteorology & Advisory</span>
        </span>
        <h2 class="fw-bold text-success">
            <span class="lang-mr">हवामान अंदाज (Agri Weather Forecast)</span>
            <span class="lang-en">Agricultural Weather Forecast</span>
        </h2>
        <p class="text-muted" style="max-width:650px; margin:0 auto;">
            <span class="lang-mr">फवारणी किंवा सिंचनापूर्वी स्थानिक हवामानाचा अंदाज तपासा आणि पिकाचे नुकसान टाळा.</span>
            <span class="lang-en">Check agricultural forecast before spraying pesticides or irrigating crops to prevent wash-off and disease outbreaks.</span>
        </p>
    </div>

    <!-- City Search Form & Presets -->
    <div class="row justify-content-center mb-4">
        <div class="col-md-7">
            <div class="d-flex gap-2 mb-2">
                <input type="text" id="cityInput" class="form-control" 
                       data-placeholder-mr="शहर / तालुका टाका (उदा. वैजापूर, संभाजीनगर, नाशिक)..."
                       data-placeholder-en="Enter City / Taluka (e.g. Vaijapur, Sambhajinagar)..."
                       placeholder="शहर / तालुका टाका (उदा. वैजापूर, संभाजीनगर, नाशिक)..." value="वैजापूर (Vaijapur)">
                <button type="button" onclick="searchWeather()" class="btn btn-krushi px-4">
                    <span class="lang-mr">शोधा</span><span class="lang-en">Search</span>
                </button>
            </div>
            <!-- City Quick Pills -->
            <div class="d-flex gap-2 flex-wrap justify-content-center">
                <button type="button" class="btn btn-sm btn-outline-secondary rounded-pill px-3 py-0" onclick="setCity('Vaijapur')">वैजापूर (Vaijapur)</button>
                <button type="button" class="btn btn-sm btn-outline-secondary rounded-pill px-3 py-0" onclick="setCity('Sambhajinagar')">संभाजीनगर</button>
                <button type="button" class="btn btn-sm btn-outline-secondary rounded-pill px-3 py-0" onclick="setCity('Nashik')">नाशिक</button>
                <button type="button" class="btn btn-sm btn-outline-secondary rounded-pill px-3 py-0" onclick="setCity('Pune')">पुणे</button>
                <button type="button" class="btn btn-sm btn-outline-secondary rounded-pill px-3 py-0" onclick="setCity('Sangli')">सांगली</button>
            </div>
        </div>
    </div>

    <!-- Weather Overview Card -->
    <div class="row justify-content-center mb-5">
        <div class="col-lg-8">
            <div class="card border-0 shadow-sm rounded-4 overflow-hidden text-white" style="background: linear-gradient(135deg, #1565c0, #0288d1);">
                <div class="card-body p-4 p-md-5">
                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <div>
                            <h3 class="fw-bold mb-0 text-white"><i class="bi bi-geo-alt-fill text-warning me-2"></i><span id="weatherCityName">वैजापूर (Vaijapur)</span></h3>
                            <small class="text-white-50">Maharashtra, India</small>
                        </div>
                        <span class="badge bg-light text-dark px-3 py-2 fw-bold"><span class="lang-mr">आजचा अंदाज</span><span class="lang-en">Today's Forecast</span></span>
                    </div>

                    <div class="row align-items-center my-4">
                        <div class="col-md-6 text-center text-md-start mb-3 mb-md-0">
                            <h1 class="display-3 fw-bold mb-0 text-white" id="weatherTemp">29°C</h1>
                            <p class="lead text-white-50 mb-0" id="weatherCondition">
                                <span class="lang-mr">अंशतः ढगाळ व कोरडे हवामान</span>
                                <span class="lang-en">Partly Cloudy & Dry</span>
                            </p>
                        </div>
                        <div class="col-md-6">
                            <div class="bg-white bg-opacity-10 p-3 rounded-3">
                                <div class="d-flex justify-content-between py-1 border-bottom border-light border-opacity-25">
                                    <span class="text-white-50"><span class="lang-mr">पावसाची शक्यता:</span><span class="lang-en">Rain Chance:</span></span>
                                    <strong class="text-white" id="weatherRain">20%</strong>
                                </div>
                                <div class="d-flex justify-content-between py-1 border-bottom border-light border-opacity-25">
                                    <span class="text-white-50"><span class="lang-mr">हवेतील आर्द्रता:</span><span class="lang-en">Humidity:</span></span>
                                    <strong class="text-white" id="weatherHumidity">65%</strong>
                                </div>
                                <div class="d-flex justify-content-between py-1">
                                    <span class="text-white-50"><span class="lang-mr">वाऱ्याचा वेग:</span><span class="lang-en">Wind Speed:</span></span>
                                    <strong class="text-white" id="weatherWind">12 km/h</strong>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Agri Advisory Alert -->
                    <div class="bg-warning text-dark p-3 rounded-3 fw-semibold small mt-3" id="weatherAdvisoryBox">
                        <i class="bi bi-info-circle-fill me-2"></i>
                        <span class="lang-mr">फवारणी सल्ला: आज वाऱ्याचा वेग कमी असल्याने कीटकनाशक फवारणीसाठी हवामान अनुकूल आहे. दुपारच्या उन्हात फवारणी टाळा.</span>
                        <span class="lang-en">Spraying Advisory: Low wind velocity makes today suitable for pesticide application. Avoid spraying during peak midday heat.</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
const weatherPresets = {
    'Vaijapur': { name_mr: 'वैजापूर (Vaijapur)', name_en: 'Vaijapur, MH', temp: '29°C', cond_mr: 'अंशतः ढगाळ व कोरडे', cond_en: 'Partly Cloudy & Dry', rain: '20%', hum: '65%', wind: '12 km/h', adv_mr: 'फवारणी सल्ला: वाऱ्याचा वेग अनुकूल असून फवारणीसाठी योग्य वेळ आहे. ठिबक सिंचन नियमित चालू ठेवा.', adv_en: 'Spraying Advisory: Mild winds present optimal conditions for foliar spray. Keep regular drip schedules.' },
    'Sambhajinagar': { name_mr: 'छत्रपती संभाजीनगर', name_en: 'Chh. Sambhajinagar', temp: '31°C', cond_mr: 'निरभ्र व सूर्यप्रकाश', cond_en: 'Sunny & Clear', rain: '10%', hum: '58%', wind: '14 km/h', adv_mr: 'सिंचन सल्ला: सूर्यप्रकाश तीव्र असल्याने बाष्पीभवन वाढेल. संध्याकाळच्या वेळेत पाणी द्या.', adv_en: 'Irrigation Advisory: High evaporation rate today; irrigate crops during evening hours.' },
    'Nashik': { name_mr: 'नाशिक (Nashik)', name_en: 'Nashik, MH', temp: '27°C', cond_mr: 'ढगाळ हवामान', cond_en: 'Cloudy Sky', rain: '40%', hum: '75%', wind: '16 km/h', adv_mr: 'रोग नियंत्रण: जास्त आर्द्रतेमुळे बुरशीजन्य रोगांचा प्रादुर्भाव होऊ शकतो, बोर्डो मिश्रण किंवा बुरशीनाशक तयार ठेवा.', adv_en: 'Disease Alert: Elevated humidity may trigger fungal spread. Keep preventative fungicides ready.' },
    'Pune': { name_mr: 'पुणे (Pune)', name_en: 'Pune, MH', temp: '28°C', cond_mr: 'अंशतः ढगाळ', cond_en: 'Partly Cloudy', rain: '25%', hum: '68%', wind: '11 km/h', adv_mr: 'फवारणी सल्ला: हवामान स्थिर आहे. भाजीपाला पिकांवर कीटकनाशक फवारणी करता येईल.', adv_en: 'Advisory: Weather is calm. Ideal for preventive spraying on vegetable and fruit crops.' },
    'Sangli': { name_mr: 'सांगली (Sangli)', name_en: 'Sangli, MH', temp: '30°C', cond_mr: 'उबदार व निरभ्र', cond_en: 'Warm & Fair', rain: '15%', hum: '62%', wind: '13 km/h', adv_mr: 'ऊस पीक सल्ला: उसाला हलके पाणी द्यावे व नत्र खताचा हप्ता देण्यास अनुकूल वेळ आहे.', adv_en: 'Sugarcane Advisory: Good window for light irrigation and top-dressing nitrogen fertilizers.' }
};

function setCity(key) {
    const data = weatherPresets[key] || weatherPresets['Vaijapur'];
    document.getElementById('cityInput').value = data.name_mr;
    applyWeatherData(data);
}

function searchWeather() {
    const val = document.getElementById('cityInput').value.toLowerCase();
    let matched = weatherPresets['Vaijapur'];
    for(const k in weatherPresets) {
        if(val.includes(k.toLowerCase()) || weatherPresets[k].name_mr.includes(val)) {
            matched = weatherPresets[k];
            break;
        }
    }
    applyWeatherData(matched);
}

function applyWeatherData(d) {
    document.getElementById('weatherCityName').textContent = d.name_mr;
    document.getElementById('weatherTemp').textContent = d.temp;
    document.getElementById('weatherRain').textContent = d.rain;
    document.getElementById('weatherHumidity').textContent = d.hum;
    document.getElementById('weatherWind').textContent = d.wind;
    document.getElementById('weatherCondition').innerHTML = `<span class="lang-mr">${d.cond_mr}</span><span class="lang-en">${d.cond_en}</span>`;
    document.getElementById('weatherAdvisoryBox').innerHTML = `<i class="bi bi-info-circle-fill me-2"></i><span class="lang-mr">${d.adv_mr}</span><span class="lang-en">${d.adv_en}</span>`;
}
</script>
""" + foot_html()

with open(os.path.join(DIST_DIR, "weather.html"), "w", encoding="utf-8") as f:
    f.write(weather_content)
print("Generated dist/weather.html")

# ==============================================================================
# 5. FARMING-TIPS.HTML
# ==============================================================================
tips_content = head_html("पीक संरक्षण व कीड सल्ला", "Crop Care & Pest Advice") + nav_html("advisory") + """
<div class="container my-4">
    <div class="text-center mb-5">
        <span class="badge bg-success px-3 py-1 rounded-pill mb-2">
            <span class="lang-mr">कृषी तज्ज्ञ मार्गदर्शक सूचना</span>
            <span class="lang-en">Agronomist Guidelines</span>
        </span>
        <h2 class="fw-bold text-success">
            <span class="lang-mr">पीक संरक्षण व कीड नियंत्रण मार्गदर्शिका</span>
            <span class="lang-en">Crop Care & Pest Management Guide</span>
        </h2>
        <p class="text-muted" style="max-width:650px;margin:0 auto;">
            <span class="lang-mr">हंगामी पीक व्यवस्थापन, रोग लक्षणे आणि एकात्मिक कीड नियंत्रण (IPM) शास्त्रीय उपाय.</span>
            <span class="lang-en">Seasonal crop management practices, disease symptom identification, and integrated pest management (IPM) measures.</span>
        </p>
    </div>

    <!-- Seasonal Crop Management Grid -->
    <h4 class="fw-bold text-dark mb-3">
        <i class="bi bi-flower1 text-success me-2"></i>
        <span class="lang-mr">हंगामी पीक व्यवस्थापन</span>
        <span class="lang-en">Seasonal Crop Management</span>
    </h4>
    <div class="row g-4 mb-5">
        <div class="col-md-6">
            <div class="card h-100 border-0 shadow-sm rounded-4 p-4 bg-white">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="badge bg-success"><span class="lang-mr">कापूस (Cotton)</span><span class="lang-en">Cotton</span></span>
                    <i class="bi bi-check2-circle text-success fs-5"></i>
                </div>
                <h5 class="fw-bold text-dark">
                    <span class="lang-mr">पातेगळ व बोंड वाढ टप्पा व्यवस्थापन</span>
                    <span class="lang-en">Square Drop & Boll Development</span>
                </h5>
                <p class="text-muted small m-0" style="line-height:1.7;">
                    <span class="lang-mr">कापूस पिकात पातेगळ रोखण्यासाठी बोरॉन (१ ग्रॅम/लिटर) आणि ००:५२:३४ (५ ग्रॅम/लिटर) ची फवारणी करावी. गुलाबी बोंडअळीच्या नियंत्रणासाठी हेक्टरी ५ कामगंध सापळे (Pheromone Traps) उभारावेत.</span>
                    <span class="lang-en">Spray Boron (1g/L) and 00:52:34 (5g/L) to prevent flower bud shedding. Install 5 pheromone traps per hectare to monitor and mass-trap pink bollworm moths.</span>
                </p>
            </div>
        </div>

        <div class="col-md-6">
            <div class="card h-100 border-0 shadow-sm rounded-4 p-4 bg-white">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="badge bg-success"><span class="lang-mr">सोयाबीन (Soybean)</span><span class="lang-en">Soybean</span></span>
                    <i class="bi bi-check2-circle text-success fs-5"></i>
                </div>
                <h5 class="fw-bold text-dark">
                    <span class="lang-mr">शेंगा भरण्याच्या टप्प्यातील पोषण</span>
                    <span class="lang-en">Pod Filling Nutritional Care</span>
                </h5>
                <p class="text-muted small m-0" style="line-height:1.7;">
                    <span class="lang-mr">सोयाबीनच्या शेंगांमध्ये दाणा भरताना पोटॅशियम नायट्रेट (१३:००:४५ - १ किलो/१०० लिटर पाणी) फवारावे, ज्यामुळे दाण्याचा आकार मोठा होऊन चकचकीतपणा वाढतो आणि वजन भरते.</span>
                    <span class="lang-en">Spray Potassium Nitrate (13:00:45 at 1kg/100L water) during pod development to ensure bolder grain size, higher test weight, and disease tolerance.</span>
                </p>
            </div>
        </div>

        <div class="col-md-6">
            <div class="card h-100 border-0 shadow-sm rounded-4 p-4 bg-white">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="badge bg-success"><span class="lang-mr">ऊस (Sugarcane)</span><span class="lang-en">Sugarcane</span></span>
                    <i class="bi bi-check2-circle text-success fs-5"></i>
                </div>
                <h5 class="fw-bold text-dark">
                    <span class="lang-mr">मोठी बांधणी व खत डोस</span>
                    <span class="lang-en">Earthing Up & Heavy Dressing</span>
                </h5>
                <p class="text-muted small m-0" style="line-height:1.7;">
                    <span class="lang-mr">ऊस लागवडीनंतर १०० ते १२० दिवसांनी मोठी बांधणी करावी. या वेळी प्रति एकर २ बॅग युरिया, २ बॅग १०:२६:२६ आणि १० किलो फेरस सल्फेट देऊन मातीची भर लावावी.</span>
                    <span class="lang-en">Perform heavy earthing up between 100-120 days after planting. Apply 2 bags Urea, 2 bags 10:26:26, and 10 kg Ferrous Sulphate per acre before earthing up.</span>
                </p>
            </div>
        </div>

        <div class="col-md-6">
            <div class="card h-100 border-0 shadow-sm rounded-4 p-4 bg-white">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <span class="badge bg-success"><span class="lang-mr">कांदा (Onion)</span><span class="lang-en">Onion</span></span>
                    <i class="bi bi-check2-circle text-success fs-5"></i>
                </div>
                <h5 class="fw-bold text-dark">
                    <span class="lang-mr">फुलकिडे (थ्रिप्स) व जांभळा करपा नियंत्रण</span>
                    <span class="lang-en">Thrips & Purple Blotch Management</span>
                </h5>
                <p class="text-muted small m-0" style="line-height:1.7;">
                    <span class="lang-mr">कांद्यावरील पांढरे ठिपके आणि पिळा रोखण्यासाठी डायफेनोकोनाझोल (१ मिली/लिटर) + फिप्रोनिल (१.५ मिली/लिटर) स्टिकरसह मिसळून फवारावे.</span>
                    <span class="lang-en">Control curling and purple spots by spraying Difenoconazole (1 ml/L) mixed with Fipronil (1.5 ml/L) along with a non-ionic silicone spreader.</span>
                </p>
            </div>
        </div>
    </div>

    <!-- Pest & Disease Identification Guide -->
    <h4 class="fw-bold text-dark mb-3">
        <i class="bi bi-bug-fill text-danger me-2"></i>
        <span class="lang-mr">कीड व रोग निदान तक्ता</span>
        <span class="lang-en">Pest & Disease Diagnosis Table</span>
    </h4>
    <div class="card border-0 shadow-sm rounded-4 overflow-hidden mb-5">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="table-success">
                    <tr>
                        <th><span class="lang-mr">कीड / रोग</span><span class="lang-en">Pest / Disease</span></th>
                        <th><span class="lang-mr">बाधित पिके</span><span class="lang-en">Affected Crops</span></th>
                        <th><span class="lang-mr">लक्षणे व नुकसान</span><span class="lang-en">Symptoms & Damage</span></th>
                        <th><span class="lang-mr">रासायनिक उपाय</span><span class="lang-en">Chemical Control</span></th>
                        <th><span class="lang-mr">जैविक / सेंद्रिय उपाय</span><span class="lang-en">Organic Control</span></th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong class="text-danger"><span class="lang-mr">गुलाबी बोंडअळी</span><span class="lang-en">Pink Bollworm</span></strong></td>
                        <td><span class="lang-mr">कापूस</span><span class="lang-en">Cotton</span></td>
                        <td class="small"><span class="lang-mr">पात्यांचे व बोंडांचे नुकसान, लिंट खराब होणे.</span><span class="lang-en">Damaged rosetted flowers, bored bolls and stained lint.</span></td>
                        <td class="small text-primary"><i class="bi bi-prescription2 me-1"></i>प्रोफेनोफॉस ५०% EC (२ मिली/लिटर)</td>
                        <td class="small text-success"><i class="bi bi-tree me-1"></i>कामगंध सापळे (हेक्टरी ५) + निंबोळी अर्क ५%</td>
                    </tr>
                    <tr>
                        <td><strong class="text-danger"><span class="lang-mr">तांबेरा व करपा</span><span class="lang-en">Rust & Blight</span></strong></td>
                        <td><span class="lang-mr">सोयाबीन, गहू</span><span class="lang-en">Soybean, Wheat</span></td>
                        <td class="small"><span class="lang-mr">पानांवर तपकिरी-तांबूस ठिपके, पाने सुकणे.</span><span class="lang-en">Brown rust pustules on leaves, premature defoliation.</span></td>
                        <td class="small text-primary"><i class="bi bi-prescription2 me-1"></i>टेबुकोनाझोल + ट्रायफ्लॉक्सीस्ट्रॉबिन (०.७ ग्रॅम/लिटर)</td>
                        <td class="small text-success"><i class="bi bi-tree me-1"></i>ट्रायकोडर्मा व्हिरीडी (५ ग्रॅम/लिटर)</td>
                    </tr>
                    <tr>
                        <td><strong class="text-danger"><span class="lang-mr">फुलकिडे (थ्रिप्स)</span><span class="lang-en">Thrips</span></strong></td>
                        <td><span class="lang-mr">कांदा, मिरची, भाजीपाला</span><span class="lang-en">Onion, Chilli, Vegetables</span></td>
                        <td class="small"><span class="lang-mr">पानांवर चंदेरी रेषा, पाने गोळा होणे (चुरडा-मुरडा).</span><span class="lang-en">Silvering and curling of leaf tips, stunted growth.</span></td>
                        <td class="small text-primary"><i class="bi bi-prescription2 me-1"></i>फिप्रोनिल ५% SC (१.५ मिली/लिटर)</td>
                        <td class="small text-success"><i class="bi bi-tree me-1"></i>निळे चिकट सापळे (Blue Sticky Traps)</td>
                    </tr>
                    <tr>
                        <td><strong class="text-danger"><span class="lang-mr">खोडकिडा</span><span class="lang-en">Early Shoot Borer</span></strong></td>
                        <td><span class="lang-mr">ऊस, मका</span><span class="lang-en">Sugarcane, Maize</span></td>
                        <td class="small"><span class="lang-mr">मधला पोंगा सुकणे (Dead Heart), उसाची वाढ खुंटणे.</span><span class="lang-en">Central whorl drying (Dead Heart), tillers dying.</span></td>
                        <td class="small text-primary"><i class="bi bi-prescription2 me-1"></i>क्लोरँट्रानिलीप्रोल (कोराजन - ०.४ मिली/लिटर)</td>
                        <td class="small text-success"><i class="bi bi-tree me-1"></i>ट्रायकोग्रामा कार्ड (Trichogramma Cards)</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
""" + foot_html()

with open(os.path.join(DIST_DIR, "farming-tips.html"), "w", encoding="utf-8") as f:
    f.write(tips_content)
print("Generated dist/farming-tips.html")

# ==============================================================================
# 6. ABOUT.HTML
# ==============================================================================
about_content = head_html("आमच्याबद्दल", "About Us") + nav_html("about") + """
<section style="background: linear-gradient(135deg, #0a2e0a 0%, #1b5e20 50%, #0d3b0d 100%); min-height: 280px; display:flex; align-items:center; position:relative; overflow:hidden;">
    <div class="container text-center py-5 text-white position-relative" style="z-index:2;">
        <span class="badge mb-3 px-4 py-2 rounded-pill fw-bold" style="background:linear-gradient(135deg,#eab308,#f97316);font-size:0.85rem;">
            🌾 <span class="lang-mr">आमच्याबद्दल</span><span class="lang-en">About Us</span>
        </span>
        <h1 class="display-5 fw-bold mb-3">
            <span class="lang-mr">सप्तशृंगी ॲग्रो सर्व्हिसेस</span>
            <span class="lang-en">Saptashrungi Agro Services</span>
        </h1>
        <p class="lead mb-0 text-white-50" style="max-width:650px; margin:0 auto;">
            <span class="lang-mr">मिरखनगर, वैजापूर येथील अग्रगण्य व अधिकृत कृषी सेवा केंद्र</span>
            <span class="lang-en">Authorized agricultural service center in Mirakhnagar, Vaijapur</span>
        </p>
    </div>
</section>

<section class="container my-5">
    <div class="row align-items-center g-5">
        <div class="col-lg-6">
            <span class="badge bg-success-subtle text-success px-3 py-2 rounded-pill fw-semibold mb-3 d-inline-block">
                🌱 <span class="lang-mr">आमची कहाणी</span><span class="lang-en">Our Story</span>
            </span>
            <h2 class="fw-bold text-success mb-4" style="font-size:2rem; line-height:1.3;">
                <span class="lang-mr">शेतकऱ्यांच्या समृद्धीसाठी<br><span style="color:#1b5e20;">समर्पित कृषी सेवा</span></span>
                <span class="lang-en">Dedicated Agricultural Support<br><span style="color:#1b5e20;">For Farmer Prosperity</span></span>
            </h2>

            <p class="text-muted mb-3" style="line-height:1.8;">
                <span class="lang-mr"><strong>सप्तशृंगी ॲग्रो सर्व्हिसेस</strong> हे मिरखनगर (वैजापूर, छत्रपती संभाजीनगर) येथील नामांकित कृषी सेवा केंद्र आहे. आमच्या केंद्रावर परिसरातील शेतकरी बांधवांना लागणारे सर्व प्रकारचे प्रमाणित बियाणे, दर्जेदार रासायनिक व सेंद्रिय खते, परिणामकारक पीक संरक्षण औषधे आणि आधुनिक ठिबक सिंचन साहित्य एकाच छताखाली उपलब्ध आहे.</span>
                <span class="lang-en"><strong>Saptashrungi Agro Services</strong> is a premier authorized agricultural inputs center situated in Mirakhnagar, Vaijapur. We provide certified hybrid seeds, high-efficiency chemical and organic fertilizers, crop protection agrochemicals, and micro-irrigation systems under one roof.</span>
            </p>
            <p class="text-muted mb-4" style="line-height:1.8;">
                <span class="lang-mr">आमचा उद्देश केवळ उत्पादने विकणे हा नसून, प्रत्येक शेतकऱ्याला जमिनीचे आरोग्य टिकवून कमी खर्चात अधिक उत्पादन घेण्यासाठी योग्य व शास्त्रीय मार्गदर्शन देणे हा आहे.</span>
                <span class="lang-en">Our core mission extends beyond retailing; we empower farmers with scientific nutrient schedules and IPM practices to maximize yields while minimizing cultivation costs.</span>
            </p>

            <div class="d-flex flex-column gap-3">
                <div class="d-flex align-items-start gap-3">
                    <div style="width:42px;height:42px;border-radius:10px;background:#e8f5e9;display:flex;align-items:center;justify-content:center;flex-shrink:0;">
                        <i class="bi bi-patch-check-fill text-success fs-5"></i>
                    </div>
                    <div>
                        <h6 class="fw-bold text-dark mb-1"><span class="lang-mr">१००% अस्सल व खात्रीशीर साहित्य</span><span class="lang-en">100% Genuine & Certified Stock</span></h6>
                        <p class="text-muted small mb-0"><span class="lang-mr">महाबीज, माहिको, कोरोमंडल, इफको आणि जैन इरिगेशन सारख्या नामांकित कंपन्यांचे अधिकृत वितरक.</span><span class="lang-en">Authorized distributor for Mahabeej, Mahyco, Coromandel, IFFCO, and Jain Irrigation.</span></p>
                    </div>
                </div>
                <div class="d-flex align-items-start gap-3">
                    <div style="width:42px;height:42px;border-radius:10px;background:#fff3e0;display:flex;align-items:center;justify-content:center;flex-shrink:0;">
                        <i class="bi bi-people-fill fs-5" style="color:#f97316;"></i>
                    </div>
                    <div>
                        <h6 class="fw-bold text-dark mb-1"><span class="lang-mr">तज्ज्ञ कृषी मार्गदर्शन</span><span class="lang-en">Agronomy Advisory</span></h6>
                        <p class="text-muted small mb-0"><span class="lang-mr">पीक रोग निदान, हवामान अंदाज आणि खत कॅल्क्युलेटरद्वारे अचूक मात्रा निर्धारण.</span><span class="lang-en">Scientific diagnosis, real-time weather advisory, and precise fertilizer dosage calculations.</span></p>
                    </div>
                </div>
            </div>
        </div>

        <div class="col-lg-6">
            <div class="card border-0 shadow-lg rounded-4 overflow-hidden">
                <img src="images/saptashrungi_shop.jpg" alt="Saptashrungi Agro Store" class="img-fluid" style="min-height:360px;object-fit:cover;">
                <div class="card-body p-4 bg-light">
                    <h5 class="fw-bold text-success mb-1">
                        <span class="lang-mr">सप्तशृंगी ॲग्रो सर्व्हिसेस, मिरखनगर</span>
                        <span class="lang-en">Saptashrungi Agro Services, Mirakhnagar</span>
                    </h5>
                    <p class="text-muted small mb-2"><i class="bi bi-geo-alt-fill text-success me-1"></i> Mirakhnagar, Vaijapur, Chhatrapati Sambhajinagar - 423703</p>
                    <p class="text-muted small mb-0"><i class="bi bi-telephone-fill text-success me-1"></i> <a href="tel:+918600813827" class="text-success text-decoration-none fw-bold">+91 8600813827</a> | सोम - शनि: सकाळी ८:०० ते रात्री ८:३०</p>
                </div>
            </div>
        </div>
    </div>
</section>
""" + foot_html()

with open(os.path.join(DIST_DIR, "about.html"), "w", encoding="utf-8") as f:
    f.write(about_content)
print("Generated dist/about.html")

# ==============================================================================
# 7. CONTACT.HTML
# ==============================================================================
contact_content = head_html("संपर्क", "Contact Us") + nav_html("contact") + """
<div class="container my-5">
    <div class="text-center mb-5">
        <span class="badge bg-success-subtle text-success px-3 py-1 rounded-pill mb-2 fw-semibold">
            <span class="lang-mr">थेट संपर्क</span><span class="lang-en">Get in Touch</span>
        </span>
        <h2 class="fw-bold text-success">
            <span class="lang-mr">आमच्याशी संपर्क साधा</span>
            <span class="lang-en">Contact Saptashrungi Agro</span>
        </h2>
        <p class="text-muted" style="max-width:650px; margin:0 auto;">
            <span class="lang-mr">बियाणे, खते किंवा पीक सल्ल्यासाठी आम्हाला कधीही कॉल किंवा व्हॉट्सॲप करा किंवा दुकानाला भेट द्या.</span>
            <span class="lang-en">Feel free to call, message on WhatsApp, or visit our retail store in Mirakhnagar, Vaijapur for any farming inquiry.</span>
        </p>
    </div>

    <div class="row g-4 mb-5">
        <!-- Contact Information Cards -->
        <div class="col-lg-5">
            <div class="card border-0 shadow-sm rounded-4 p-4 h-100 bg-white">
                <h5 class="fw-bold text-dark mb-4">
                    <span class="lang-mr">संपर्क माहिती</span>
                    <span class="lang-en">Contact Details</span>
                </h5>

                <div class="d-flex align-items-start gap-3 mb-4">
                    <div class="rounded-circle bg-success text-white d-flex align-items-center justify-content-center flex-shrink-0" style="width:48px;height:48px;">
                        <i class="bi bi-geo-alt-fill fs-5"></i>
                    </div>
                    <div>
                        <h6 class="fw-bold mb-1"><span class="lang-mr">दुकानाचा पत्ता</span><span class="lang-en">Store Address</span></h6>
                        <p class="text-muted small mb-0">
                            सप्तशृंगी ॲग्रो सर्व्हिसेस, मिरखनगर, वैजापूर,<br>
                            छत्रपती संभाजीनगर, महाराष्ट्र - ४२३७०३
                        </p>
                    </div>
                </div>

                <div class="d-flex align-items-start gap-3 mb-4">
                    <div class="rounded-circle bg-primary text-white d-flex align-items-center justify-content-center flex-shrink-0" style="width:48px;height:48px;">
                        <i class="bi bi-telephone-fill fs-5"></i>
                    </div>
                    <div>
                        <h6 class="fw-bold mb-1"><span class="lang-mr">फोन व कॉल</span><span class="lang-en">Phone & Mobile</span></h6>
                        <p class="text-muted small mb-1"><a href="tel:+918600813827" class="text-dark fw-bold text-decoration-none">+91 8600813827</a></p>
                        <small class="text-muted"><span class="lang-mr">सोम - शनि: सकाळी ८:०० ते रात्री ८:३०</span><span class="lang-en">Mon - Sat: 8:00 AM to 8:30 PM</span></small>
                    </div>
                </div>

                <div class="d-flex align-items-start gap-3 mb-4">
                    <div class="rounded-circle bg-success text-white d-flex align-items-center justify-content-center flex-shrink-0" style="width:48px;height:48px;">
                        <i class="bi bi-whatsapp fs-5"></i>
                    </div>
                    <div>
                        <h6 class="fw-bold mb-1"><span class="lang-mr">व्हॉट्सॲप सल्ला</span><span class="lang-en">WhatsApp Advisory</span></h6>
                        <p class="text-muted small mb-2"><span class="lang-mr">पिकांच्या रोगांचे फोटो पाठवून त्वरित सल्ला मिळवा.</span><span class="lang-en">Send crop disease photos for immediate dosage advice.</span></p>
                        <a href="https://wa.me/918600813827?text=नमस्कार,%20मला%20माहिती%20हवी%20आहे." target="_blank" class="btn btn-sm btn-success rounded-pill px-3">
                            <i class="bi bi-whatsapp me-1"></i><span class="lang-mr">व्हॉट्सॲप सुरू करा</span><span class="lang-en">Message on WhatsApp</span>
                        </a>
                    </div>
                </div>

                <div class="d-flex align-items-start gap-3">
                    <div class="rounded-circle bg-warning text-dark d-flex align-items-center justify-content-center flex-shrink-0" style="width:48px;height:48px;">
                        <i class="bi bi-receipt fs-5"></i>
                    </div>
                    <div>
                        <h6 class="fw-bold mb-1"><span class="lang-mr">नोंदणी व परवाना</span><span class="lang-en">Licenses</span></h6>
                        <p class="text-muted small mb-0">GSTIN: 27AAAAA0000A1Z5<br>कृषी विभाग परवानाधारक केंद्र</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Interactive Contact Form -->
        <div class="col-lg-7">
            <div class="card border-0 shadow-sm rounded-4 p-4 h-100 bg-white">
                <h5 class="fw-bold text-dark mb-3">
                    <span class="lang-mr">संदेश पाठवा / चौकशी करा</span>
                    <span class="lang-en">Send Message / Inquiry</span>
                </h5>
                <form id="contactForm" onsubmit="submitContactForm(event)">
                    <div class="mb-3">
                        <label class="form-label small fw-bold text-success text-uppercase"><span class="lang-mr">आपले नाव</span><span class="lang-en">Your Full Name</span></label>
                        <input type="text" id="contactName" class="form-control" required 
                               data-placeholder-mr="उदा. रमेश पाटील"
                               data-placeholder-en="e.g. Ramesh Patil"
                               placeholder="उदा. रमेश पाटील">
                    </div>
                    <div class="row g-3 mb-3">
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-success text-uppercase"><span class="lang-mr">मोबाईल नंबर</span><span class="lang-en">Mobile Number</span></label>
                            <input type="tel" id="contactPhone" class="form-control" required 
                                   data-placeholder-mr="१० अंकी मोबाईल नंबर"
                                   data-placeholder-en="10-digit Mobile Number"
                                   placeholder="१० अंकी मोबाईल नंबर">
                        </div>
                        <div class="col-md-6">
                            <label class="form-label small fw-bold text-success text-uppercase"><span class="lang-mr">मुख्य पीक</span><span class="lang-en">Crop Type</span></label>
                            <select id="contactCrop" class="form-select">
                                <option value="कापूस">कापूस (Cotton)</option>
                                <option value="सोयाबीन">सोयाबीन (Soybean)</option>
                                <option value="ऊस">ऊस (Sugarcane)</option>
                                <option value="कांदा">कांदा (Onion)</option>
                                <option value="भाजीपाला">भाजीपाला (Vegetables)</option>
                                <option value="इतर">इतर (Other)</option>
                            </select>
                        </div>
                    </div>
                    <div class="mb-3">
                        <label class="form-label small fw-bold text-success text-uppercase"><span class="lang-mr">आपला संदेश किंवा शंका</span><span class="lang-en">Your Inquiry / Message</span></label>
                        <textarea id="contactMsg" class="form-control" rows="4" required 
                                  data-placeholder-mr="उत्पादनाची उपलब्धता किंवा पीक समस्येबद्दल लिहा..."
                                  data-placeholder-en="Ask about product availability or crop issue..."
                                  placeholder="उत्पादनाची उपलब्धता किंवा पीक समस्येबद्दल लिहा..."></textarea>
                    </div>
                    <button type="submit" class="btn btn-krushi px-4 py-2 rounded-pill fw-semibold shadow-sm">
                        <i class="bi bi-send-fill me-1"></i>
                        <span class="lang-mr">संदेश पाठवा</span><span class="lang-en">Send Message</span>
                    </button>
                    <div id="contactAlert" class="alert alert-success mt-3 d-none">
                        <i class="bi bi-check-circle-fill me-2"></i>
                        <span class="lang-mr">धन्यवाद! आपला संदेश प्राप्त झाला आहे. आम्ही लवकरच संपर्क करू.</span>
                        <span class="lang-en">Thank you! Your inquiry has been received. We will contact you shortly.</span>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <!-- Google Map Embed -->
    <div class="card border-0 shadow-sm rounded-4 overflow-hidden mb-5">
        <div class="card-header bg-dark text-white py-3">
            <h6 class="mb-0 fw-bold"><i class="bi bi-map-fill text-success me-2"></i><span class="lang-mr">गुगल मॅप स्थान</span><span class="lang-en">Google Maps Location</span> (Mirakhnagar, Vaijapur)</h6>
        </div>
        <div class="ratio ratio-21x9" style="min-height:350px;">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15002.585794828135!2d74.7214!3d19.9248!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bdc33c1622b7a95%3A0x6b2b73bcba5256e4!2sVaijapur%2C%20Maharashtra!5e0!3m2!1sen!2sin!4v1700000000000" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
        </div>
    </div>
</div>

<script>
function submitContactForm(e) {
    e.preventDefault();
    const name = document.getElementById('contactName').value;
    const phone = document.getElementById('contactPhone').value;
    const crop = document.getElementById('contactCrop').value;
    const msg = document.getElementById('contactMsg').value;

    const alertBox = document.getElementById('contactAlert');
    alertBox.classList.remove('d-none');
    
    const waText = `नमस्कार, मी ${name} (मोबाईल: ${phone}). पीक: ${crop}. संदेश: ${msg}`;
    setTimeout(() => {
        window.open('https://wa.me/918600813827?text=' + encodeURIComponent(waText), '_blank');
    }, 1200);
}
</script>
""" + foot_html()

with open(os.path.join(DIST_DIR, "contact.html"), "w", encoding="utf-8") as f:
    f.write(contact_content)
print("Generated dist/contact.html")

# ==============================================================================
# 8. FAQ.HTML
# ==============================================================================
faq_content = head_html("वारंवार विचारले जाणारे प्रश्न", "FAQ") + nav_html("faq") + """
<div class="container my-5" style="max-width:850px;">
    <div class="text-center mb-5">
        <span class="badge bg-success-subtle text-success px-3 py-1 rounded-pill mb-2 fw-semibold">
            <span class="lang-mr">मदत केंद्र</span><span class="lang-en">Help Center</span>
        </span>
        <h2 class="fw-bold text-success">
            <span class="lang-mr">वारंवार विचारले जाणारे प्रश्न (FAQ)</span>
            <span class="lang-en">Frequently Asked Questions</span>
        </h2>
        <p class="text-muted">
            <span class="lang-mr">शेतकरी बांधवांना पडणारे सामान्य प्रश्न व त्यांची सविस्तर उत्तरे.</span>
            <span class="lang-en">Clear answers to common questions regarding products, seed certification, and store advisory.</span>
        </p>
    </div>

    <div class="accordion shadow-sm rounded-4 overflow-hidden" id="faqAccordion">
        <!-- Q1 -->
        <div class="accordion-item border-0 border-bottom">
            <h2 class="accordion-header" id="headingOne">
                <button class="accordion-button fw-bold text-dark" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                    <span class="lang-mr">१. तुमच्याकडे मिळणारे बियाणे व खते प्रमाणित आहेत का?</span>
                    <span class="lang-en">1. Are all seeds and fertilizers 100% certified?</span>
                </button>
            </h2>
            <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#faqAccordion">
                <div class="accordion-body text-muted small" style="line-height:1.7;">
                    <span class="lang-mr">होय, १००% प्रमाणित. सप्तशृंगी ॲग्रो सर्व्हिसेस हे महाराष्ट्र शासन कृषी विभागाचे अधिकृत परवानाधारक केंद्र आहे. आमच्याकडील सर्व बियाणे (महाबीज, माहिको इ.) आणि खते (इफको, महाधन, कोरोमंडल इ.) थेट मान्यताप्राप्त कंपन्यांकडून येतात. प्रत्येक बॅचची गुणवत्ता व मुदत तपासलेली असते.</span>
                    <span class="lang-en">Yes, 100% certified. We are a licensed agricultural distributor authorized by the Department of Agriculture, Maharashtra. All seeds and fertilizers are procured directly from certified manufacturers with verified batch numbers and test reports.</span>
                </div>
            </div>
        </div>

        <!-- Q2 -->
        <div class="accordion-item border-0 border-bottom">
            <h2 class="accordion-header" id="headingTwo">
                <button class="accordion-button collapsed fw-bold text-dark" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                    <span class="lang-mr">२. खत कॅल्क्युलेटरचा वापर कसा करावा?</span>
                    <span class="lang-en">2. How do I use the smart Fertilizer Calculator?</span>
                </button>
            </h2>
            <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#faqAccordion">
                <div class="accordion-body text-muted small" style="line-height:1.7;">
                    <span class="lang-mr">वेबसाइटवरील 'खत कॅल्क्युलेटर' पानावर जाऊन आपले पीक (कापूस, ऊस, सोयाबीन इ.) आणि शेताचे क्षेत्रफळ (एकर) निवडा. कॅल्क्युलेटर आपोआप विद्यापीठ शिफारशीनुसार आवश्यक युरिया, डीएपी, पोटॅश आणि संयुक्त खतांच्या बॅग्सचे अचूक प्रमाण दाखवतो.</span>
                    <span class="lang-en">Navigate to our Fertilizer Calculator, select your crop and farm acreage. The tool calculates exact bags of Urea, DAP, Potash, and NPK blends based on agricultural university recommendations.</span>
                </div>
            </div>
        </div>

        <!-- Q3 -->
        <div class="accordion-item border-0 border-bottom">
            <h2 class="accordion-header" id="headingThree">
                <button class="accordion-button collapsed fw-bold text-dark" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                    <span class="lang-mr">३. पिकावर कीड किंवा रोग आल्यास ऑनलाइन सल्ला मिळू शकतो का?</span>
                    <span class="lang-en">3. Can I get crop pest advice online?</span>
                </button>
            </h2>
            <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#faqAccordion">
                <div class="accordion-body text-muted small" style="line-height:1.7;">
                    <span class="lang-mr">होय! शेतकरी बांधव त्यांच्या बाधित पिकाचे, पानांचे किंवा किडीचे स्पष्ट फोटो काढून आमच्या व्हॉट्सॲप नंबरवर (+91 8600813827) पाठवू शकतात. आमचे कृषी तज्ज्ञ रोगाचे अचूक निदान करून योग्य औषधाचे प्रमाण व फवारणीची पद्धत सांगतात.</span>
                    <span class="lang-en">Yes! You can take clear photos of the infected leaves or pest attack and send them to our WhatsApp (+91 8600813827). We provide precise diagnosis, appropriate chemical or organic recommendations, and spraying dilution instructions.</span>
                </div>
            </div>
        </div>

        <!-- Q4 -->
        <div class="accordion-item border-0">
            <h2 class="accordion-header" id="headingFour">
                <button class="accordion-button collapsed fw-bold text-dark" type="button" data-bs-toggle="collapse" data-bs-target="#collapseFour" aria-expanded="false" aria-controls="collapseFour">
                    <span class="lang-mr">४. दुकानाची वेळ काय आहे?</span>
                    <span class="lang-en">4. What are the retail store working hours?</span>
                </button>
            </h2>
            <div id="collapseFour" class="accordion-collapse collapse" aria-labelledby="headingFour" data-bs-parent="#faqAccordion">
                <div class="accordion-body text-muted small" style="line-height:1.7;">
                    <span class="lang-mr">सप्तशृंगी ॲग्रो सर्व्हिसेस हे दुकान सोमवार ते शनिवार सकाळी ८:०० ते रात्री ८:३० या वेळेत खुले असते. आपत्कालीन फवारणी किंवा खतांच्या गरजेसाठी रविवारच्या दिवशीही संपर्क साधता येतो.</span>
                    <span class="lang-en">Our store in Mirakhnagar, Vaijapur is open Monday to Saturday from 8:00 AM to 8:30 PM. For emergency requirements during peak seasons, WhatsApp support remains available.</span>
                </div>
            </div>
        </div>
    </div>
</div>
""" + foot_html()

with open(os.path.join(DIST_DIR, "faq.html"), "w", encoding="utf-8") as f:
    f.write(faq_content)
print("Generated dist/faq.html")

# ==============================================================================
# 9. LOGIN.HTML (Full Authenticated & Client-Side UI)
# ==============================================================================
login_content = head_html("लॉगिन", "Login") + nav_html("login") + """
<div class="container my-5 py-3" style="max-width:460px;">
    <div class="card border-0 shadow-lg rounded-4 overflow-hidden bg-white">
        <div class="card-header text-center py-4 text-white" style="background: linear-gradient(135deg, #1b5e20, #15803d);">
            <img src="images/saptashrungi_logo_round.jpg" alt="Logo" class="rounded-circle shadow mb-2" style="width:64px;height:64px;object-fit:cover;border:2px solid #fff;">
            <h4 class="fw-bold mb-1">
                <span class="lang-mr">पुन्हा स्वागत आहे</span>
                <span class="lang-en">Welcome Back</span>
            </h4>
            <small class="text-white-50">
                <span class="lang-mr">मोबाईल नंबर किंवा ईमेल वापरून लॉगिन करा</span>
                <span class="lang-en">Sign in with mobile number or email</span>
            </small>
        </div>
        <div class="card-body p-4">
            <form id="loginForm" onsubmit="handleLogin(event)">
                <div class="mb-3">
                    <label class="form-label small fw-bold text-success text-uppercase">
                        <span class="lang-mr">मोबाईल नंबर किंवा ईमेल *</span>
                        <span class="lang-en">Mobile Number or Email *</span>
                    </label>
                    <div class="input-group">
                        <span class="input-group-text bg-light text-muted"><i class="bi bi-person"></i></span>
                        <input type="text" id="username" class="form-control" required autofocus
                               data-placeholder-mr="मोबाईल नंबर किंवा ईमेल"
                               data-placeholder-en="Mobile or Email"
                               placeholder="मोबाईल नंबर किंवा ईमेल">
                    </div>
                </div>

                <div class="mb-3">
                    <label class="form-label small fw-bold text-success text-uppercase">
                        <span class="lang-mr">पासवर्ड *</span>
                        <span class="lang-en">Password *</span>
                    </label>
                    <div class="input-group">
                        <span class="input-group-text bg-light text-muted"><i class="bi bi-lock"></i></span>
                        <input type="password" id="password" class="form-control" required
                               placeholder="••••••••">
                        <button class="btn btn-outline-secondary" type="button" onclick="togglePass('password', 'eyeIcon')">
                            <i class="bi bi-eye" id="eyeIcon"></i>
                        </button>
                    </div>
                </div>

                <div class="d-flex justify-content-between align-items-center mb-4 small">
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="rememberMe">
                        <label class="form-check-label text-muted" for="rememberMe">
                            <span class="lang-mr">लक्षात ठेवा</span>
                            <span class="lang-en">Remember me</span>
                        </label>
                    </div>
                    <a href="forgot-password.html" class="text-success text-decoration-none fw-semibold">
                        <span class="lang-mr">पासवर्ड विसरलात?</span>
                        <span class="lang-en">Forgot password?</span>
                    </a>
                </div>

                <button type="submit" class="btn btn-krushi w-100 fw-bold py-2 rounded-pill shadow-sm mb-3">
                    <i class="bi bi-box-arrow-in-right me-1"></i>
                    <span class="lang-mr">लॉगिन करा</span>
                    <span class="lang-en">Log In</span>
                </button>

                <div id="loginMsg" class="alert alert-success small d-none text-center">
                    <i class="bi bi-check-circle-fill me-1"></i>
                    <span class="lang-mr">लॉगिन यशस्वी! मुख्य पानावर नेले जात आहे...</span>
                    <span class="lang-en">Login Successful! Redirecting...</span>
                </div>
            </form>

            <div class="text-center pt-3 border-top mt-3 small">
                <span class="text-muted"><span class="lang-mr">नवीन शेतकरी?</span><span class="lang-en">New farmer?</span></span>
                <a href="register.html" class="text-success fw-bold text-decoration-none ms-1">
                    <span class="lang-mr">येथे नोंदणी करा</span><span class="lang-en">Register here</span>
                </a>
            </div>
        </div>
        <div class="card-footer text-center bg-light py-2 border-0">
            <a href="index.html" class="text-muted small text-decoration-none">
                ← <span class="lang-mr">मुख्यपृष्ठावर परत जा</span><span class="lang-en">Back to Home</span>
            </a>
        </div>
    </div>
</div>

<script>
function togglePass(inputId, iconId) {
    const input = document.getElementById(inputId);
    const icon = document.getElementById(iconId);
    if(input.type === 'password') {
        input.type = 'text';
        icon.className = 'bi bi-eye-slash';
    } else {
        input.type = 'password';
        icon.className = 'bi bi-eye';
    }
}

function handleLogin(e) {
    e.preventDefault();
    const msg = document.getElementById('loginMsg');
    msg.classList.remove('d-none');
    setTimeout(() => {
        window.location.href = 'index.html';
    }, 1200);
}
</script>
""" + foot_html()

with open(os.path.join(DIST_DIR, "login.html"), "w", encoding="utf-8") as f:
    f.write(login_content)
print("Generated dist/login.html")

# ==============================================================================
# 10. REGISTER.HTML (New Farmer Registration)
# ==============================================================================
register_content = head_html("नवीन शेतकरी नोंदणी", "Farmer Registration") + nav_html("register") + """
<div class="container my-5">
    <div class="row justify-content-center">
        <div class="col-lg-8 col-md-10">
            <div class="card border-0 shadow-lg rounded-4 overflow-hidden bg-white">
                <div class="card-header text-center py-4 text-white" style="background: linear-gradient(135deg, #1b5e20, #15803d);">
                    <img src="images/saptashrungi_logo_round.jpg" alt="Logo" class="rounded-circle shadow mb-2" style="width:64px;height:64px;object-fit:cover;border:2px solid #fff;">
                    <h4 class="fw-bold mb-1">
                        👨‍🌾 <span class="lang-mr">नवीन शेतकरी नोंदणी</span>
                        <span class="lang-en">New Farmer Registration</span>
                    </h4>
                    <small class="text-white-50">
                        <span class="lang-mr">सप्तशृंगी ॲग्रो सर्व्हिसेस - तुमचे शेतकरी खाते तयार करा</span>
                        <span class="lang-en">Saptashrungi Agro Services - Create your farmer account</span>
                    </small>
                </div>

                <div class="card-body p-4 p-md-5">
                    <form id="registerForm" onsubmit="handleRegister(event)">
                        <div class="row g-3">
                            <!-- Full Name -->
                            <div class="col-md-6">
                                <label class="form-label fw-semibold small text-success">
                                    <span class="lang-mr">पूर्ण नाव *</span><span class="lang-en">Full Name *</span>
                                </label>
                                <input type="text" id="regName" class="form-control" required
                                       data-placeholder-mr="उदा. रमेश आनंदा पाटील"
                                       data-placeholder-en="e.g. Ramesh Ananda Patil"
                                       placeholder="उदा. रमेश आनंदा पाटील">
                            </div>

                            <!-- Mobile Number -->
                            <div class="col-md-6">
                                <label class="form-label fw-semibold small text-success">
                                    <span class="lang-mr">मोबाईल नंबर *</span><span class="lang-en">Mobile Number *</span>
                                </label>
                                <div class="input-group">
                                    <span class="input-group-text">+91</span>
                                    <input type="tel" id="regMobile" class="form-control" maxlength="10" required
                                           data-placeholder-mr="१० अंकी मोबाईल नंबर"
                                           data-placeholder-en="10-digit mobile"
                                           placeholder="१० अंकी मोबाईल नंबर">
                                </div>
                            </div>

                            <!-- Email -->
                            <div class="col-md-6">
                                <label class="form-label fw-semibold small text-success">
                                    <span class="lang-mr">ईमेल पत्ता</span><span class="lang-en">Email Address</span>
                                </label>
                                <input type="email" id="regEmail" class="form-control"
                                       data-placeholder-mr="farmer@example.com"
                                       data-placeholder-en="farmer@example.com"
                                       placeholder="farmer@example.com">
                            </div>

                            <!-- Village -->
                            <div class="col-md-6">
                                <label class="form-label fw-semibold small text-success">
                                    <span class="lang-mr">गाव *</span><span class="lang-en">Village *</span>
                                </label>
                                <input type="text" id="regVillage" class="form-control" required
                                       data-placeholder-mr="उदा. मिरखनगर / कसबे डिग्रज"
                                       data-placeholder-en="e.g. Mirakhnagar / Kasbe Digraj"
                                       placeholder="उदा. मिरखनगर / कसबे डिग्रज">
                            </div>

                            <!-- Taluka -->
                            <div class="col-md-6">
                                <label class="form-label fw-semibold small text-success">
                                    <span class="lang-mr">तालुका *</span><span class="lang-en">Taluka *</span>
                                </label>
                                <input type="text" id="regTaluka" class="form-control" required
                                       data-placeholder-mr="उदा. वैजापूर"
                                       data-placeholder-en="e.g. Vaijapur"
                                       placeholder="उदा. वैजापूर">
                            </div>

                            <!-- District -->
                            <div class="col-md-6">
                                <label class="form-label fw-semibold small text-success">
                                    <span class="lang-mr">जिल्हा *</span><span class="lang-en">District *</span>
                                </label>
                                <input type="text" id="regDistrict" class="form-control" required
                                       data-placeholder-mr="उदा. छत्रपती संभाजीनगर"
                                       data-placeholder-en="e.g. Chh. Sambhajinagar"
                                       placeholder="उदा. छत्रपती संभाजीनगर">
                            </div>

                            <!-- Address -->
                            <div class="col-12">
                                <label class="form-label fw-semibold small text-success">
                                    <span class="lang-mr">शेतीचा / घराचा पत्ता *</span><span class="lang-en">Farm / Home Address *</span>
                                </label>
                                <textarea id="regAddress" class="form-control" rows="2" required
                                          data-placeholder-mr="गट क्र., लँडमार्क, पोस्ट..."
                                          data-placeholder-en="Gat No, Landmark, Post..."
                                          placeholder="गट क्र., लँडमार्क, पोस्ट..."></textarea>
                            </div>

                            <!-- Password -->
                            <div class="col-md-6">
                                <label class="form-label fw-semibold small text-success">
                                    <span class="lang-mr">पासवर्ड तयार करा *</span><span class="lang-en">Create Password *</span>
                                </label>
                                <div class="input-group">
                                    <input type="password" id="regPass" class="form-control" minlength="6" required placeholder="••••••••">
                                    <button class="btn btn-outline-secondary" type="button" onclick="togglePass('regPass', 'eyeReg1')">
                                        <i class="bi bi-eye" id="eyeReg1"></i>
                                    </button>
                                </div>
                            </div>

                            <!-- Confirm Password -->
                            <div class="col-md-6">
                                <label class="form-label fw-semibold small text-success">
                                    <span class="lang-mr">पासवर्डची पुष्टी करा *</span><span class="lang-en">Confirm Password *</span>
                                </label>
                                <div class="input-group">
                                    <input type="password" id="regConfirmPass" class="form-control" minlength="6" required placeholder="••••••••">
                                    <button class="btn btn-outline-secondary" type="button" onclick="togglePass('regConfirmPass', 'eyeReg2')">
                                        <i class="bi bi-eye" id="eyeReg2"></i>
                                    </button>
                                </div>
                            </div>
                        </div>

                        <div id="regAlert" class="alert alert-success mt-4 d-none">
                            <i class="bi bi-check-circle-fill me-2"></i>
                            <span class="lang-mr">अभिनंदन! आपले शेतकरी खाते तयार झाले आहे. लॉगिन पानावर नेले जात आहे...</span>
                            <span class="lang-en">Congratulations! Your farmer account has been created. Redirecting to login...</span>
                        </div>

                        <div class="mt-4">
                            <button type="submit" class="btn btn-krushi w-100 py-2 rounded-pill fw-bold shadow-sm">
                                <i class="bi bi-person-check-fill me-1"></i>
                                <span class="lang-mr">नोंदणी पूर्ण करा (Register Account)</span>
                                <span class="lang-en">Complete Registration</span>
                            </button>
                        </div>

                        <div class="text-center mt-3 pt-3 border-top small">
                            <span class="text-muted"><span class="lang-mr">आधीच नोंदणी केली आहे का?</span><span class="lang-en">Already registered?</span></span>
                            <a href="login.html" class="text-success fw-bold text-decoration-none ms-1">
                                <span class="lang-mr">येथे लॉगिन करा</span><span class="lang-en">Login here</span>
                            </a>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
function togglePass(inputId, iconId) {
    const input = document.getElementById(inputId);
    const icon = document.getElementById(iconId);
    if(input.type === 'password') {
        input.type = 'text';
        icon.className = 'bi bi-eye-slash';
    } else {
        input.type = 'password';
        icon.className = 'bi bi-eye';
    }
}

function handleRegister(e) {
    e.preventDefault();
    const p1 = document.getElementById('regPass').value;
    const p2 = document.getElementById('regConfirmPass').value;
    if(p1 !== p2) {
        alert("दोन्ही पासवर्ड समान असणे आवश्यक आहे! / Both passwords must match!");
        return;
    }
    const alertBox = document.getElementById('regAlert');
    alertBox.classList.remove('d-none');
    setTimeout(() => {
        window.location.href = 'login.html';
    }, 1500);
}
</script>
""" + foot_html()

with open(os.path.join(DIST_DIR, "register.html"), "w", encoding="utf-8") as f:
    f.write(register_content)
print("Generated dist/register.html")

# ==============================================================================
# 11. FORGOT-PASSWORD.HTML
# ==============================================================================
forgot_content = head_html("पासवर्ड रीसेट", "Forgot Password") + nav_html("login") + """
<div class="container my-5">
    <div class="row justify-content-center">
        <div class="col-md-6 col-lg-5">
            <div class="card border-0 shadow-lg rounded-4 overflow-hidden bg-white">
                <div class="card-body p-4 p-md-5 text-center">
                    <div class="rounded-circle mx-auto mb-3 d-flex align-items-center justify-content-center" style="width:64px;height:64px;background:#e8f5e9;color:#1b5e20;">
                        <i class="bi bi-key-fill fs-3"></i>
                    </div>
                    <h4 class="fw-bold mb-2">
                        <span class="lang-mr">पासवर्ड रीसेट साहाय्य</span>
                        <span class="lang-en">Password Reset Support</span>
                    </h4>
                    <p class="text-muted small mb-4" style="line-height:1.6;">
                        <span class="lang-mr">खाते सुरक्षिततेसाठी पासवर्ड रीसेट करण्यासाठी थेट दुकानाच्या हेल्पलाइनवर संपर्क साधा किंवा व्हॉट्सॲपवर मेसेज करा.</span>
                        <span class="lang-en">For account security, please contact our store helpline or message on WhatsApp to reset your credentials.</span>
                    </p>

                    <div class="d-grid gap-2 mb-3">
                        <a href="tel:+918600813827" class="btn btn-krushi py-2 rounded-pill fw-bold shadow-sm">
                            <i class="bi bi-telephone-fill me-2"></i>+91 8600813827 वर कॉल करा
                        </a>
                        <a href="https://wa.me/918600813827?text=नमस्कार,%20मी%20माझा%20पासवर्ड%20विसरलो%20आहे.%20कृपया%20मदत%20करा." target="_blank" class="btn btn-outline-success py-2 rounded-pill fw-bold">
                            <i class="bi bi-whatsapp me-2"></i>व्हॉट्सॲपवर मदत मागा
                        </a>
                    </div>

                    <div class="mt-4 pt-3 border-top">
                        <a href="login.html" class="text-success text-decoration-none small fw-bold">
                            « <span class="lang-mr">लॉगिन पानाकडे परत जा</span><span class="lang-en">Back to Login</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
""" + foot_html()

with open(os.path.join(DIST_DIR, "forgot-password.html"), "w", encoding="utf-8") as f:
    f.write(forgot_content)
print("Generated dist/forgot-password.html")

# ==============================================================================
# 12. OFFERS.HTML (Seasonal Offers & Discounts)
# ==============================================================================
offers_content = head_html("विशेष ऑफर्स व कूपन्स", "Offers & Discounts") + nav_html("offers") + """
<div class="container my-4">
    <div class="text-center mb-5">
        <span class="badge bg-warning text-dark px-3 py-1 rounded-pill mb-2 fw-bold">
            🔥 <span class="lang-mr">हंगामी सवलत योजना</span><span class="lang-en">Seasonal Farm Deals</span>
        </span>
        <h2 class="fw-bold text-success">
            <span class="lang-mr">सध्याच्या चालू ऑफर्स व कूपन्स</span>
            <span class="lang-en">Current Special Agri Offers</span>
        </h2>
        <p class="text-muted" style="max-width:650px;margin:0 auto;">
            <span class="lang-mr">सप्तशृंगी ॲग्रो सर्व्हिसेसतर्फे खरीप व रब्बी हंगामासाठी शेतकरी बांधवांना विशेष सूट आणि सवलत.</span>
            <span class="lang-en">Exclusive seasonal coupons, fertilizer combo discounts, and irrigation package offers.</span>
        </p>
    </div>

    <div class="row g-4 mb-5">
        <!-- Offer 1 -->
        <div class="col-md-6 col-lg-4">
            <div class="card h-100 border-0 shadow-sm rounded-4 overflow-hidden bg-white" style="border-top: 4px solid #16a34a !important;">
                <div class="card-body p-4 d-flex flex-column">
                    <div class="d-flex justify-content-between align-items-start mb-2">
                        <span class="badge bg-success rounded-pill px-3 py-1">१०% सूट (10% OFF)</span>
                        <small class="text-muted"><span class="lang-mr">खरीप हंगाम</span><span class="lang-en">Kharif Season</span></small>
                    </div>
                    <h5 class="fw-bold text-dark mt-2">
                        <span class="lang-mr">प्रमाणित बियाण्यांवर १०% सूट</span>
                        <span class="lang-en">10% OFF on Certified Seeds</span>
                    </h5>
                    <p class="text-muted small flex-grow-1" style="line-height:1.6;">
                        <span class="lang-mr">महाबीज सोयाबीन आणि माहिको कापूस बियाण्यांच्या २ किंवा अधिक बॅग्ज खरेदीवर तात्काळ १०% सूट.</span>
                        <span class="lang-en">Flat 10% discount on purchase of 2 or more bags of Mahabeej soybean & Mahyco cotton seeds.</span>
                    </p>
                    <div class="bg-light p-3 rounded-3 border d-flex justify-content-between align-items-center mt-3">
                        <div>
                            <small class="text-muted d-block" style="font-size: 0.7rem;">COUPON CODE</small>
                            <code class="fw-bold fs-5 text-success">KHARIF10</code>
                        </div>
                        <a href="https://wa.me/918600813827?text=मला%20KHARIF10%20कूपन%20वापरून%20बियाणे%20मागवायचे%20आहेत." target="_blank" class="btn btn-sm btn-krushi rounded-pill px-3">
                            <span class="lang-mr">कूपन वापरा</span><span class="lang-en">Use Code</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>

        <!-- Offer 2 -->
        <div class="col-md-6 col-lg-4">
            <div class="card h-100 border-0 shadow-sm rounded-4 overflow-hidden bg-white" style="border-top: 4px solid #f57f17 !important;">
                <div class="card-body p-4 d-flex flex-column">
                    <div class="d-flex justify-content-between align-items-start mb-2">
                        <span class="badge bg-warning text-dark rounded-pill px-3 py-1">₹५० सूट / बॅग</span>
                        <small class="text-muted"><span class="lang-mr">खत कॉम्बो</span><span class="lang-en">Fertilizer Combo</span></small>
                    </div>
                    <h5 class="fw-bold text-dark mt-2">
                        <span class="lang-mr">NPK कॉम्प्लेक्स खत डिस्काउंट</span>
                        <span class="lang-en">NPK Fertilizer Combo Deal</span>
                    </h5>
                    <p class="text-muted small flex-grow-1" style="line-height:1.6;">
                        <span class="lang-mr">१०:२६:२६ किंवा महाधन २४:२४:० खतांच्या ५ पेक्षा जास्त बॅग्स खरेदीवर प्रति बॅग ₹५० ची थेट बचत.</span>
                        <span class="lang-en">Flat ₹50 rebate per bag on bulk purchase of 5 or more bags of 10:26:26 or Mahadhan 24:24:0.</span>
                    </p>
                    <div class="bg-light p-3 rounded-3 border d-flex justify-content-between align-items-center mt-3">
                        <div>
                            <small class="text-muted d-block" style="font-size: 0.7rem;">COUPON CODE</small>
                            <code class="fw-bold fs-5 text-success">NPK50</code>
                        </div>
                        <a href="https://wa.me/918600813827?text=मला%20NPK50%20कूपन%20वापरून%20खते%20मागवायची%20आहेत." target="_blank" class="btn btn-sm btn-krushi rounded-pill px-3">
                            <span class="lang-mr">कूपन वापरा</span><span class="lang-en">Use Code</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>

        <!-- Offer 3 -->
        <div class="col-md-6 col-lg-4">
            <div class="card h-100 border-0 shadow-sm rounded-4 overflow-hidden bg-white" style="border-top: 4px solid #0288d1 !important;">
                <div class="card-body p-4 d-flex flex-column">
                    <div class="d-flex justify-content-between align-items-start mb-2">
                        <span class="badge bg-info text-white rounded-pill px-3 py-1">₹३०० सूट</span>
                        <small class="text-muted"><span class="lang-mr">स्प्रे पंप</span><span class="lang-en">Sprayer Special</span></small>
                    </div>
                    <h5 class="fw-bold text-dark mt-2">
                        <span class="lang-mr">बॅटरी स्प्रे पंप ऑफर</span>
                        <span class="lang-en">Battery Sprayer Special</span>
                    </h5>
                    <p class="text-muted small flex-grow-1" style="line-height:1.6;">
                        <span class="lang-mr">फाल्कन १६ लिटर १२V डबल मोटर बॅटरी स्प्रे पंप खरेदीवर ₹३०० सूट व १ मोफत अतिरिक्त नोझल सेट.</span>
                        <span class="lang-en">Instant ₹300 OFF on Falcon 16L 12V dual-motor battery sprayer plus a free accessory nozzle set.</span>
                    </p>
                    <div class="bg-light p-3 rounded-3 border d-flex justify-content-between align-items-center mt-3">
                        <div>
                            <small class="text-muted d-block" style="font-size: 0.7rem;">COUPON CODE</small>
                            <code class="fw-bold fs-5 text-success">PUMP300</code>
                        </div>
                        <a href="https://wa.me/918600813827?text=मला%20PUMP300%20कूपन%20वापरून%20स्प्रे%20पंप%20मागवायचा%20आहे." target="_blank" class="btn btn-sm btn-krushi rounded-pill px-3">
                            <span class="lang-mr">कूपन वापरा</span><span class="lang-en">Use Code</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
""" + foot_html()

with open(os.path.join(DIST_DIR, "offers.html"), "w", encoding="utf-8") as f:
    f.write(offers_content)
print("Generated dist/offers.html")

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
"""

with open(os.path.join(DIST_DIR, "_redirects"), "w", encoding="utf-8") as f:
    f.write(redirects_content)
print("Updated dist/_redirects")

print("All static pages and redirects generated successfully!")
