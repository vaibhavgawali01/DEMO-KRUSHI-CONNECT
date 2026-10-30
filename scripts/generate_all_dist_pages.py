# -*- coding: utf-8 -*-
import os
import sys

from build_site import head_html, nav_html, foot_html, DIST_DIR

print("Generating all 14 static pages...")

# 1. INDEX
index_content = head_html("मुख्यपृष्ठ", "Home") + nav_html("home") + """
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

<!-- QUICK ACTION CARDS -->
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

<!-- FEATURED PRODUCTS -->
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

<!-- WHY CHOOSE US -->
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

<!-- REVIEWS (#reviews) -->
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

    <div class="row g-4">
        <div class="col-md-6 col-lg-3">
            <div class="card h-100 border-0 shadow-sm rounded-4 p-4 d-flex flex-column justify-content-between bg-white">
                <div>
                    <div class="text-warning mb-2"><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i></div>
                    <p class="text-muted small mb-3">"कापूस बियाणे आणि कीटकनाशकांसाठी सप्तशृंगी ॲग्रोचे मार्गदर्शन अतिशय अचूक ठरले. उत्पादनात मोठी वाढ झाली!"</p>
                </div>
                <div class="d-flex align-items-center gap-3 pt-3 border-top">
                    <div class="rounded-circle bg-success text-white fw-bold d-flex align-items-center justify-content-center" style="width:40px;height:40px;">RP</div>
                    <div><h6 class="mb-0 fw-bold text-dark">रमेश पाटील</h6><small class="text-muted">वैजापूर • कापूस</small></div>
                </div>
            </div>
        </div>

        <div class="col-md-6 col-lg-3">
            <div class="card h-100 border-0 shadow-sm rounded-4 p-4 d-flex flex-column justify-content-between bg-white">
                <div>
                    <div class="text-warning mb-2"><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i></div>
                    <p class="text-muted small mb-3">"ऊस पिकासाठी खत कॅल्क्युलेटरने योग्य नियोजन केले. योग्य भाव आणि नेहमी वेळेत खते उपलब्ध असतात."</p>
                </div>
                <div class="d-flex align-items-center gap-3 pt-3 border-top">
                    <div class="rounded-circle bg-primary text-white fw-bold d-flex align-items-center justify-content-center" style="width:40px;height:40px;">SS</div>
                    <div><h6 class="mb-0 fw-bold text-dark">संदीप सोनवणे</h6><small class="text-muted">मिरखनगर • ऊस</small></div>
                </div>
            </div>
        </div>

        <div class="col-md-6 col-lg-3">
            <div class="card h-100 border-0 shadow-sm rounded-4 p-4 d-flex flex-column justify-content-between bg-white">
                <div>
                    <div class="text-warning mb-2"><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i></div>
                    <p class="text-muted small mb-3">"सोयाबीन बियाणे १००% उगवणक्षम निघाले. दुकानातील कर्मचारी औषधांची माहिती सविस्तर सांगतात."</p>
                </div>
                <div class="d-flex align-items-center gap-3 pt-3 border-top">
                    <div class="rounded-circle bg-warning text-dark fw-bold d-flex align-items-center justify-content-center" style="width:40px;height:40px;">BG</div>
                    <div><h6 class="mb-0 fw-bold text-dark">बाळासाहेब गायकवाड</h6><small class="text-muted">गंगापूर • सोयाबीन</small></div>
                </div>
            </div>
        </div>

        <div class="col-md-6 col-lg-3">
            <div class="card h-100 border-0 shadow-sm rounded-4 p-4 d-flex flex-column justify-content-between bg-white">
                <div>
                    <div class="text-warning mb-2"><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i><i class="bi bi-star-fill"></i></div>
                    <p class="text-muted small mb-3">"कांदा आणि भाजीपाल्यासाठी ठिबक सिंचन साहित्य एकाच ठिकाणी मिळते. व्हॉट्सॲपवर विचारले तरी लगेच उत्तर मिळते!"</p>
                </div>
                <div class="d-flex align-items-center gap-3 pt-3 border-top">
                    <div class="rounded-circle bg-info text-white fw-bold d-flex align-items-center justify-content-center" style="width:40px;height:40px;">DS</div>
                    <div><h6 class="mb-0 fw-bold text-dark">ज्ञानेश्वर शिंदे</h6><small class="text-muted">वैजापूर • भाजीपाला</small></div>
                </div>
            </div>
        </div>
    </div>
</section>
""" + foot_html()
with open(os.path.join(DIST_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_content)
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

# 10. REGISTER
register_content = head_html("नोंदणी करा", "Register") + nav_html("register") + """
<div class="container my-5" style="max-width:680px;">
    <div class="card border-0 shadow-lg rounded-4 overflow-hidden bg-white">
        <div class="card-header text-center py-4 text-white" style="background: linear-gradient(135deg, #1b5e20, #15803d);">
            <img src="images/saptashrungi_logo_round.jpg" alt="Logo" class="rounded-circle shadow mb-2" style="width:64px;height:64px;object-fit:cover;border:2px solid #fff;">
            <h4 class="fw-bold mb-1">👨‍🌾 नवीन शेतकरी नोंदणी</h4>
            <small class="text-white-50">सप्तशृंगी ॲग्रो सर्व्हिसेस - खाते तयार करा</small>
        </div>
        <div class="card-body p-4">
            <form id="regForm" onsubmit="handleReg(event)">
                <div class="row g-3">
                    <div class="col-md-6"><label class="form-label small fw-bold text-success">पूर्ण नाव *</label><input type="text" id="rName" class="form-control" required placeholder="उदा. रमेश पाटील"></div>
                    <div class="col-md-6"><label class="form-label small fw-bold text-success">मोबाईल नंबर *</label><input type="tel" id="rPhone" class="form-control" required maxlength="10" placeholder="१० अंकी नंबर"></div>
                    <div class="col-md-6"><label class="form-label small fw-bold text-success">गाव *</label><input type="text" id="rVillage" class="form-control" required placeholder="उदा. मिरखनगर"></div>
                    <div class="col-md-6"><label class="form-label small fw-bold text-success">तालुका *</label><input type="text" id="rTaluka" class="form-control" required placeholder="उदा. वैजापूर"></div>
                    <div class="col-12"><label class="form-label small fw-bold text-success">पासवर्ड *</label><input type="password" id="rPass" class="form-control" required placeholder="••••••••"></div>
                </div>
                <button type="submit" class="btn btn-krushi w-100 py-2 rounded-pill fw-bold shadow-sm mt-4">नोंदणी पूर्ण करा</button>
                <div id="regSuccess" class="alert alert-success mt-3 d-none text-center">नोंदणी यशस्वी! लॉगिन केले जात आहे...</div>
            </form>
            <div class="text-center pt-3 border-top mt-3 small"><a href="login.html" class="text-success fw-bold text-decoration-none">आधीच खाते आहे? लॉगिन करा</a></div>
        </div>
    </div>
</div>
<script>
function handleReg(e) {
    e.preventDefault();
    const name = document.getElementById('rName').value;
    localStorage.setItem('user_role', 'farmer');
    localStorage.setItem('user_name', name || 'शेतकरी');
    document.getElementById('regSuccess').classList.remove('d-none');
    setTimeout(() => { window.location.href = 'farmer-dashboard.html'; }, 800);
}
</script>
""" + foot_html()
with open(os.path.join(DIST_DIR, "register.html"), "w", encoding="utf-8") as f:
    f.write(register_content)
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

# 12. LOGIN.HTML (Direct Instant Working Login without demo mode warning)
login_content = head_html("लॉगिन", "Login") + nav_html("login") + """
<div class="container my-5 py-3" style="max-width:460px;">
    <div class="card border-0 shadow-lg rounded-4 overflow-hidden bg-white">
        <div class="card-header text-center py-4 text-white" style="background: linear-gradient(135deg, #1b5e20, #15803d);">
            <img src="images/saptashrungi_logo_round.jpg" alt="Logo" class="rounded-circle shadow mb-2" style="width:64px;height:64px;object-fit:cover;border:2px solid #fff;">
            <h4 class="fw-bold mb-1">
                <span class="lang-mr">सप्तशृंगी ॲग्रो पोर्टल</span>
                <span class="lang-en">Staff & Admin Portal</span>
            </h4>
            <small class="text-white-50">
                <span class="lang-mr">शेतकरी व ॲडमिन सुरक्षित लॉगिन</span>
                <span class="lang-en">Farmer & Staff Portal Access</span>
            </small>
        </div>
        <div class="card-body p-4">
            <!-- Role Selector Pills -->
            <div class="d-flex p-1 bg-light rounded-pill mb-4 border shadow-sm">
                <button type="button" id="tabFarmer" class="btn btn-sm flex-fill rounded-pill fw-bold btn-success text-white shadow-sm" onclick="switchLoginRole('farmer')">
                    🌾 <span class="lang-mr">शेतकरी ग्राहक</span><span class="lang-en">Farmer</span>
                </button>
                <button type="button" id="tabAdmin" class="btn btn-sm flex-fill rounded-pill fw-bold btn-light text-dark" onclick="switchLoginRole('admin')">
                    🛡️ <span class="lang-mr">ॲडमिन पॅनल</span><span class="lang-en">Admin Panel</span>
                </button>
            </div>

            <form id="loginForm" method="GET" action="farmer-dashboard.html" onsubmit="return handleLogin(event)">
                <input type="hidden" id="loginRole" value="farmer">

                <div class="mb-3">
                    <label id="lblUsername" class="form-label small fw-bold text-success text-uppercase">
                        <span class="lang-mr">शेतकरी नाव किंवा मोबाईल नंबर *</span>
                        <span class="lang-en">Farmer Name or Mobile *</span>
                    </label>
                    <div class="input-group">
                        <span class="input-group-text bg-light text-muted"><i class="bi bi-person"></i></span>
                        <input type="text" id="username" class="form-control" required autofocus
                               value="रमेश पाटील (९८२३४५६७८९)"
                               placeholder="उदा. रमेश पाटील किंवा ९८२३४५६७८९">
                    </div>
                </div>

                <div class="mb-3">
                    <label class="form-label small fw-bold text-success text-uppercase">
                        <span class="lang-mr">पासवर्ड *</span>
                        <span class="lang-en">Password</span>
                    </label>
                    <div class="input-group">
                        <span class="input-group-text bg-light text-muted"><i class="bi bi-lock"></i></span>
                        <input type="password" id="password" class="form-control" required value="farmer123"
                               placeholder="••••••••">
                        <button class="btn btn-outline-secondary" type="button" onclick="togglePass('password', 'eyeIcon')">
                            <i class="bi bi-eye" id="eyeIcon"></i>
                        </button>
                    </div>
                </div>

                <div class="d-flex justify-content-between align-items-center mb-4 small">
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="rememberMe" checked>
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

                <button type="submit" id="btnSubmitLogin" class="btn btn-krushi w-100 fw-bold py-2 rounded-pill shadow-sm mb-3">
                    <i class="bi bi-box-arrow-in-right me-1"></i>
                    <span id="btnSubmitText">
                        <span class="lang-mr">शेतकरी खात्यात प्रवेश करा</span>
                        <span class="lang-en">Sign In to Farmer Dashboard</span>
                    </span>
                </button>

                <div id="loginSuccessBox" class="alert alert-success small d-none text-center py-2">
                    <i class="bi bi-check-circle-fill me-1"></i>
                    <span id="loginSuccessText">लॉगिन यशस्वी! डॅशबोर्ड उघडत आहे...</span>
                    <div class="mt-2">
                        <a id="directDashboardBtn" href="farmer-dashboard.html" class="btn btn-sm btn-success text-white px-3 py-1 fw-bold rounded-pill">
                            <span class="lang-mr">येथे क्लिक करा &rarr;</span>
                            <span class="lang-en">Click here &rarr;</span>
                        </a>
                    </div>
                </div>
            </form>

            <!-- 1-Click Direct Demo Access Buttons -->
            <div class="border-top pt-3 mt-3">
                <div class="text-center mb-2">
                    <span class="badge bg-light text-dark border px-3 py-1 rounded-pill small fw-semibold">
                        ⚡ <span class="lang-mr">थेट १-क्लिक प्रवेश (Quick Direct Access)</span>
                        <span class="lang-en">1-Click Direct Access</span>
                    </span>
                </div>
                <div class="d-grid gap-2">
                    <a href="farmer-dashboard.html" onclick="quickLoginFarmer()" class="btn btn-outline-success fw-bold py-2 rounded-pill shadow-sm small text-center">
                        🌾 <span class="lang-mr">थेट शेतकरी डॅशबोर्ड उघडा (Farmer Dashboard)</span>
                        <span class="lang-en">Open Farmer Dashboard Directly</span>
                    </a>
                    <a href="admin-dashboard.html" onclick="quickLoginAdmin()" class="btn btn-outline-dark fw-bold py-2 rounded-pill shadow-sm small text-center">
                        🛡️ <span class="lang-mr">थेट ॲडमिन पॅनल उघडा (Admin Panel)</span>
                        <span class="lang-en">Open Admin Panel Directly</span>
                    </a>
                </div>
            </div>

            <div class="text-center pt-3 border-top mt-3 small">
                <span class="text-muted"><span class="lang-mr">नवीन शेतकरी?</span><span class="lang-en">New farmer?</span></span>
                <a href="register.html" class="text-success fw-bold text-decoration-none ms-1">
                    <span class="lang-mr">येथे नोंदणी करा</span><span class="lang-en">Register here</span>
                </a>
            </div>
        </div>
        <div class="card-footer text-center bg-light py-2 border-0">
            <a href="index.html" class="text-muted small text-decoration-none">
                ← <span class="lang-mr">मुख्यपृष्ठावर परत जा</span><span class="lang-en">Back to Home Page</span>
            </a>
        </div>
    </div>
</div>

<script>
function switchLoginRole(role) {
    const tabF = document.getElementById('tabFarmer');
    const tabA = document.getElementById('tabAdmin');
    const roleInput = document.getElementById('loginRole');
    const form = document.getElementById('loginForm');
    const uInput = document.getElementById('username');
    const pInput = document.getElementById('password');
    const lbl = document.getElementById('lblUsername');
    const btnText = document.getElementById('btnSubmitText');

    roleInput.value = role;

    if (role === 'admin') {
        tabA.className = 'btn btn-sm flex-fill rounded-pill fw-bold btn-success text-white shadow-sm';
        tabF.className = 'btn btn-sm flex-fill rounded-pill fw-bold btn-light text-dark';
        form.action = 'admin-dashboard.html';
        uInput.value = 'admin@krushiseva.com';
        pInput.value = 'admin123';
        lbl.innerHTML = '<span class="lang-mr">ॲडमिन वापरकर्ता नाव / ईमेल *</span><span class="lang-en">Admin Username / Email *</span>';
        btnText.innerHTML = '<span class="lang-mr">ॲडमिन पॅनलमध्ये प्रवेश करा</span><span class="lang-en">Sign In to Admin Panel</span>';
    } else {
        tabF.className = 'btn btn-sm flex-fill rounded-pill fw-bold btn-success text-white shadow-sm';
        tabA.className = 'btn btn-sm flex-fill rounded-pill fw-bold btn-light text-dark';
        form.action = 'farmer-dashboard.html';
        uInput.value = 'रमेश पाटील (९८२३४५६७८९)';
        pInput.value = 'farmer123';
        lbl.innerHTML = '<span class="lang-mr">शेतकरी नाव किंवा मोबाईल नंबर *</span><span class="lang-en">Farmer Name or Mobile *</span>';
        btnText.innerHTML = '<span class="lang-mr">शेतकरी खात्यात प्रवेश करा</span><span class="lang-en">Sign In to Farmer Dashboard</span>';
    }
}

function quickLoginFarmer() {
    localStorage.setItem('user_role', 'farmer');
    localStorage.setItem('user_name', 'रमेश पाटील');
}

function quickLoginAdmin() {
    localStorage.setItem('user_role', 'admin');
    localStorage.setItem('user_name', 'Admin');
}

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
    if (e && e.preventDefault) e.preventDefault();
    const roleInput = document.getElementById('loginRole');
    const uInput = document.getElementById('username');
    const u = (uInput ? uInput.value : '').trim().toLowerCase();
    const alertBox = document.getElementById('loginSuccessBox');
    const textSpan = document.getElementById('loginSuccessText');
    const btn = document.getElementById('btnSubmitLogin');
    const directBtn = document.getElementById('directDashboardBtn');

    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status"></span>Signing in...';
    }

    const currentTabRole = roleInput ? roleInput.value : 'farmer';
    const isAdmin = (currentTabRole === 'admin' || u.includes('admin') || u === 'admin@krushiseva.com' || u === 'staff' || u === 'owner');
    const target = isAdmin ? 'admin-dashboard.html' : 'farmer-dashboard.html';

    if (isAdmin) {
        localStorage.setItem('user_role', 'admin');
        localStorage.setItem('user_name', 'Admin');
        if (textSpan) {
            textSpan.innerHTML = '<span class="lang-mr">लॉगिन यशस्वी! ॲडमिन डॅशबोर्ड उघडत आहे...</span><span class="lang-en">Login Successful! Opening Admin Dashboard...</span>';
        }
        if (directBtn) {
            directBtn.href = 'admin-dashboard.html';
            directBtn.innerHTML = '<span class="lang-mr">ॲडमिन डॅशबोर्ड वर जा &rarr;</span><span class="lang-en">Go to Admin Dashboard &rarr;</span>';
        }
    } else {
        localStorage.setItem('user_role', 'farmer');
        var displayUName = (uInput ? uInput.value : '').replace(/\\s*\\(.*\\)/, '').trim() || 'रमेश पाटील';
        localStorage.setItem('user_name', displayUName);
        if (textSpan) {
            textSpan.innerHTML = '<span class="lang-mr">लॉगिन यशस्वी! शेतकरी डॅशबोर्ड उघडत आहे...</span><span class="lang-en">Login Successful! Opening Farmer Dashboard...</span>';
        }
        if (directBtn) {
            directBtn.href = 'farmer-dashboard.html';
            directBtn.innerHTML = '<span class="lang-mr">शेतकरी डॅशबोर्ड वर जा &rarr;</span><span class="lang-en">Go to Farmer Dashboard &rarr;</span>';
        }
    }

    if (alertBox) {
        alertBox.classList.remove('d-none');
    }

    setTimeout(() => {
        window.location.replace(target);
    }, 200);

    return false;
}
</script>
""" + foot_html()
with open(os.path.join(DIST_DIR, "login.html"), "w", encoding="utf-8") as f:
    f.write(login_content)
print("12. login.html")

# 13. ADMIN DASHBOARD
admin_dash_content = head_html("ॲडमिन डॅशबोर्ड", "Admin Dashboard") + nav_html("dashboard") + """
<div class="container-fluid px-3 px-lg-4 my-4" style="max-width:1400px;">
    <div class="card border-0 shadow-sm rounded-4 text-white p-4 mb-4 overflow-hidden position-relative" style="background: linear-gradient(135deg, #0a2e0a 0%, #1b5e20 60%, #14532d 100%);">
        <div class="row align-items-center g-3 position-relative" style="z-index:2;">
            <div class="col-md-8">
                <span class="badge bg-white bg-opacity-25 text-white px-3 py-1 rounded-pill mb-2 fw-semibold">
                    🌱 <span class="lang-mr">सप्तशृंगी ॲग्रो सर्व्हिसेस, मिरखनगर</span><span class="lang-en">Saptashrungi Agro Services, Mirakhnagar</span>
                </span>
                <h2 class="display-6 fw-bold mb-1"><span class="lang-mr">व्यवस्थापन डॅशबोर्ड</span><span class="lang-en">Admin Management Dashboard</span></h2>
                <p class="text-white-50 small mb-0"><span class="lang-mr">विक्री, इन्व्हेंटरी, शेतकरी खाती आणि दुकानाच्या कामगिरीचा थेट आढावा.</span><span class="lang-en">Live overview of store sales, stock inventory, farmer credit ledgers and orders.</span></p>
            </div>
            <div class="col-md-4 text-md-end">
                <a href="products.html" class="btn btn-light text-success fw-bold px-3 py-2 rounded-pill shadow-sm me-2"><i class="bi bi-grid-fill me-1"></i>उत्पादने पहा</a>
                <button onclick="handleLogout()" class="btn btn-outline-light fw-bold px-3 py-2 rounded-pill"><i class="bi bi-box-arrow-right me-1"></i>लॉगआउट</button>
            </div>
        </div>
    </div>

    <!-- Low Stock Alert Banner -->
    <div class="alert alert-warning border-0 shadow-sm rounded-4 d-flex align-items-center justify-content-between flex-wrap gap-2 mb-4 p-3" style="background:#fffbeb; border-left: 5px solid #f59e0b !important;">
        <div class="d-flex align-items-center gap-3">
            <div style="width:40px;height:40px;border-radius:10px;background:#fef3c7;display:flex;align-items:center;justify-content:center;font-size:1.25rem;">⚠️</div>
            <div>
                <h6 class="fw-bold mb-0 text-dark"><span class="lang-mr">कमी साठा चेतावणी (Low Stock Alert)</span><span class="lang-en">Low Stock Alert</span></h6>
                <small class="text-muted"><span class="lang-mr"><strong>३ उत्पादनांचा</strong> साठा कमी झाला आहे (उदा. फाल्कन बॅटरी पंप, 10:26:26 खत).</span><span class="lang-en"><strong>3 products</strong> are running below safety threshold.</span></small>
            </div>
        </div>
        <a href="products.html" class="btn btn-sm btn-warning fw-bold px-3 py-2 rounded-pill">तपासा &rarr;</a>
    </div>

    <!-- 6 KPI Metric Cards -->
    <div class="row g-3 mb-4">
        <div class="col-sm-6 col-xl-2">
            <div class="card border-0 shadow-sm rounded-4 p-3 bg-white h-100">
                <div class="d-flex justify-content-between align-items-start mb-2"><span class="text-muted small fw-bold">एकूण विक्री</span><div class="rounded-circle d-flex align-items-center justify-content-center" style="width:36px;height:36px;background:#dcfce7;color:#16a34a;"><i class="bi bi-graph-up-arrow"></i></div></div>
                <h4 class="fw-bold text-success mb-1">₹4,85,250</h4>
                <small class="text-success"><i class="bi bi-arrow-up-short"></i>+14.2% चालू वर्ष</small>
            </div>
        </div>
        <div class="col-sm-6 col-xl-2">
            <div class="card border-0 shadow-sm rounded-4 p-3 bg-white h-100">
                <div class="d-flex justify-content-between align-items-start mb-2"><span class="text-muted small fw-bold">एकूण ऑर्डर्स</span><div class="rounded-circle d-flex align-items-center justify-content-center" style="width:36px;height:36px;background:#e0f2fe;color:#0284c7;"><i class="bi bi-bag-check-fill"></i></div></div>
                <h4 class="fw-bold text-primary mb-1">342</h4>
                <small class="text-muted">पावत्या जनरेट</small>
            </div>
        </div>
        <div class="col-sm-6 col-xl-2">
            <div class="card border-0 shadow-sm rounded-4 p-3 bg-white h-100">
                <div class="d-flex justify-content-between align-items-start mb-2"><span class="text-muted small fw-bold">शेतकरी ग्राहक</span><div class="rounded-circle d-flex align-items-center justify-content-center" style="width:36px;height:36px;background:#fef3c7;color:#d97706;"><i class="bi bi-people-fill"></i></div></div>
                <h4 class="fw-bold text-warning mb-1">520+</h4>
                <small class="text-muted">नोंदणीकृत शेतकरी</small>
            </div>
        </div>
        <div class="col-sm-6 col-xl-2">
            <div class="card border-0 shadow-sm rounded-4 p-3 bg-white h-100">
                <div class="d-flex justify-content-between align-items-start mb-2"><span class="text-muted small fw-bold">उधारी बाकी</span><div class="rounded-circle d-flex align-items-center justify-content-center" style="width:36px;height:36px;background:#fee2e2;color:#dc2626;"><i class="bi bi-clock-history"></i></div></div>
                <h4 class="fw-bold text-danger mb-1">₹42,800</h4>
                <small class="text-muted">१२ शेतकऱ्यांकडे</small>
            </div>
        </div>
        <div class="col-sm-6 col-xl-2">
            <div class="card border-0 shadow-sm rounded-4 p-3 bg-white h-100">
                <div class="d-flex justify-content-between align-items-start mb-2"><span class="text-muted small fw-bold">एकूण उत्पादने</span><div class="rounded-circle d-flex align-items-center justify-content-center" style="width:36px;height:36px;background:#f3e8ff;color:#7e22ce;"><i class="bi bi-box-seam-fill"></i></div></div>
                <h4 class="fw-bold text-dark mb-1">128</h4>
                <small class="text-success">१२५ स्टॉकमध्ये</small>
            </div>
        </div>
        <div class="col-sm-6 col-xl-2">
            <div class="card border-0 shadow-sm rounded-4 p-3 bg-white h-100">
                <div class="d-flex justify-content-between align-items-start mb-2"><span class="text-muted small fw-bold">सल्ला विचारणा</span><div class="rounded-circle d-flex align-items-center justify-content-center" style="width:36px;height:36px;background:#dbeafe;color:#2563eb;"><i class="bi bi-whatsapp"></i></div></div>
                <h4 class="fw-bold text-primary mb-1">68</h4>
                <small class="text-muted">आजचे संपर्क</small>
            </div>
        </div>
    </div>

    <!-- Recent Store Invoices & Orders -->
    <div class="card border-0 shadow-sm rounded-4 overflow-hidden bg-white mb-4">
        <div class="card-header bg-white py-3 border-0 d-flex justify-content-between align-items-center">
            <h5 class="fw-bold mb-0 text-dark"><i class="bi bi-receipt text-success me-2"></i>नुकत्याच झालेल्या विक्री पावत्या (Recent Sales)</h5>
            <span class="badge bg-success-subtle text-success px-3 py-1 rounded-pill">Live Billing</span>
        </div>
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="table-light">
                    <tr><th># पावती (Inv)</th><th>शेतकरी नाव</th><th>खरेदी साहित्य</th><th>रक्कम</th><th>स्थिती</th></tr>
                </thead>
                <tbody>
                    <tr><td><span class="fw-bold text-dark">INV-2026-089</span></td><td>रमेश पाटील (वैजापूर)</td><td>माहिको कापूस बियाणे (२ बॅग), ००:५२:३४</td><td class="fw-bold text-success">₹2,450</td><td><span class="badge bg-success-subtle text-success">Paid (रोख)</span></td></tr>
                    <tr><td><span class="fw-bold text-dark">INV-2026-088</span></td><td>संदीप सोनवणे (मिरखनगर)</td><td>महाधन २४:२४:० (४ बॅग्स), युरिया (२)</td><td class="fw-bold text-success">₹7,252</td><td><span class="badge bg-success-subtle text-success">Paid (UPI)</span></td></tr>
                    <tr><td><span class="fw-bold text-dark">INV-2026-087</span></td><td>बाळासाहेब गायकवाड (गंगापूर)</td><td>जेएस ३३५ सोयाबीन (२ बॅग)</td><td class="fw-bold text-warning">₹5,400</td><td><span class="badge bg-warning-subtle text-dark">उधारी (Pending)</span></td></tr>
                    <tr><td><span class="fw-bold text-dark">INV-2026-086</span></td><td>ज्ञानेश्वर शिंदे (वैजापूर)</td><td>जैन ठिबक पाईप (१ बंडल) + ड्रिपर्स</td><td class="fw-bold text-success">₹3,850</td><td><span class="badge bg-success-subtle text-success">Paid (रोख)</span></td></tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
""" + foot_html()
with open(os.path.join(DIST_DIR, "admin-dashboard.html"), "w", encoding="utf-8") as f:
    f.write(admin_dash_content)
print("13. admin-dashboard.html")

# 14. FARMER DASHBOARD
farmer_dash_content = head_html("शेतकरी डॅशबोर्ड", "Farmer Dashboard") + nav_html("dashboard") + """
<div class="container my-4" style="max-width:1240px;">
    <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-3 mb-4">
        <div>
            <h1 class="h3 fw-bold m-0 text-success"><span class="lang-mr">नमस्ते, </span><span class="lang-en">Welcome, </span><span id="farmerDisplayGreet">रमेश पाटील</span> 🌾</h1>
            <p class="text-muted small m-0 mt-1">सप्तशृंगी ॲग्रो ग्राहक खाते • वैजापूर, संभाजीनगर</p>
        </div>
        <div class="d-flex gap-2">
            <a href="products.html" class="btn btn-success rounded-pill px-3 py-2 fw-bold shadow-sm"><i class="bi bi-cart-plus me-1"></i>खरेदी करा</a>
            <button onclick="handleLogout()" class="btn btn-outline-secondary rounded-pill px-3 py-2"><i class="bi bi-box-arrow-right me-1"></i>बाहेर पडा</button>
        </div>
    </div>

    <!-- Outstanding Udhari Passbook Banner Card -->
    <div class="card border-0 shadow-sm rounded-4 mb-4 overflow-hidden p-4" style="background: linear-gradient(135deg, #f0fdf4, #dcfce7); border: 2px solid #bbf7d0 !important;">
        <div class="row align-items-center g-3">
            <div class="col-lg-7">
                <div class="d-flex align-items-center gap-2 mb-2">
                    <span class="badge bg-success text-white px-3 py-1 rounded-pill fw-bold"><i class="bi bi-check-circle-fill me-1"></i>उधारी खातेवही (Credit Passbook)</span>
                    <span class="badge bg-white text-dark border px-2 py-1 small">मुदत: १५ नोव्हेंबर २०२६</span>
                </div>
                <div class="d-flex align-items-baseline gap-3">
                    <h1 class="display-5 fw-bold text-success m-0">₹2,500.00</h1>
                    <span class="fs-6 fw-semibold text-muted">सध्याची बाकी रक्कम</span>
                </div>
                <div class="d-flex flex-wrap gap-2 mt-3">
                    <div class="bg-white px-3 py-2 rounded-3 border shadow-sm small"><span class="text-muted d-block" style="font-size: 11px;">एकूण खरेदी:</span><strong class="text-dark">₹12,500.00</strong></div>
                    <div class="bg-white px-3 py-2 rounded-3 border shadow-sm small"><span class="text-muted d-block" style="font-size: 11px;">आतापर्यंत जमा:</span><strong class="text-success">₹10,000.00</strong></div>
                    <div class="bg-white px-3 py-2 rounded-3 border shadow-sm small"><span class="text-muted d-block" style="font-size: 11px;">शिल्लक बाकी:</span><strong class="text-danger">₹2,500.00</strong></div>
                </div>
            </div>
            <div class="col-lg-5 text-lg-end">
                <a href="https://wa.me/918600813827?text=माझी%20उधारी%20जमा%20करायची%20आहे." target="_blank" class="btn btn-success btn-lg px-4 py-2 rounded-pill fw-bold shadow-sm">
                    <i class="bi bi-whatsapp me-1"></i> UPI ने जमा करा
                </a>
            </div>
        </div>
    </div>

    <!-- Farmer Recent Orders -->
    <div class="card border-0 shadow-sm rounded-4 overflow-hidden bg-white mb-4">
        <div class="card-header bg-white py-3 border-0"><h5 class="fw-bold mb-0 text-dark"><i class="bi bi-clock-history text-success me-2"></i>माझ्या अलीकडील खरेदी (My Purchases)</h5></div>
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="table-light"><tr><th>तारीख</th><th>उत्पादने</th><th>प्रमाण</th><th>रक्कम</th><th>स्थिती</th></tr></thead>
                <tbody>
                    <tr><td>२८ ऑक्टोबर २०२६</td><td>माहिको बीजी-२ कापूस बियाणे</td><td>२ बॅग्स</td><td class="fw-bold text-success">₹1,640</td><td><span class="badge bg-success">वितरित (Delivered)</span></td></tr>
                    <tr><td>१२ ऑक्टोबर २०२६</td><td>महाधन २४:२४:० खत (५० किलो)</td><td>२ बॅग्स</td><td class="fw-bold text-success">₹3,360</td><td><span class="badge bg-success">वितरित (Delivered)</span></td></tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
""" + foot_html()
with open(os.path.join(DIST_DIR, "farmer-dashboard.html"), "w", encoding="utf-8") as f:
    f.write(farmer_dash_content)
print("14. farmer-dashboard.html")

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
/admin/dashboard /admin-dashboard.html 200
/admin /admin-dashboard.html 200
/admin-dashboard /admin-dashboard.html 200
/farmer/dashboard /farmer-dashboard.html 200
/farmer-dashboard /farmer-dashboard.html 200
"""
with open(os.path.join(DIST_DIR, "_redirects"), "w", encoding="utf-8") as f:
    f.write(redirects_content)
print("Updated dist/_redirects")

print("ALL 14 STATIC PAGES GENERATED SUCCESSFULLY!")
