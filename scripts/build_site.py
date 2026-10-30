# -*- coding: utf-8 -*-
import os
import shutil

BASE_DIR = r"c:\Users\HP\OneDrive\Documents\krushi seva"
DIST_DIR = os.path.join(BASE_DIR, "dist")
STATIC_DIR = os.path.join(BASE_DIR, "src", "main", "resources", "static")

# 1. Ensure asset directories are mirrored
for folder in ["css", "js", "images", "videos"]:
    src = os.path.join(STATIC_DIR, folder)
    dst = os.path.join(DIST_DIR, folder)
    if os.path.exists(src):
        shutil.copytree(src, dst, dirs_exist_ok=True)

def head_html(title_mr, title_en):
    return f"""<!DOCTYPE html>
<html lang="mr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title_mr} | {title_en} - सप्तशृंगी ॲग्रो सर्व्हिसेस (Saptashrungi Agro Services)</title>
    <meta name="description" content="Saptashrungi Agro Services - Certified Agricultural Products, Seeds, Fertilizers, Pesticides, Drip Irrigation and Farming Advisory in Mirakhnagar, Vaijapur.">
    <meta name="theme-color" content="#16a34a">
    <link rel="icon" type="image/jpeg" href="images/saptashrungi_logo_round.jpg">

    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/tabler-icons.min.css">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Noto+Sans+Devanagari:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Custom Theme CSS -->
    <link href="css/custom.css" rel="stylesheet">
    <link href="css/dark-mode.css" rel="stylesheet">
    <link href="css/ui-polish.css" rel="stylesheet">
    <link href="css/login-page.css" rel="stylesheet">

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" defer></script>
    <script src="js/premium.js" defer></script>
</head>
<body>
"""

def nav_html(active="home"):
    def act(p):
        return " active fw-bold" if p == active else ""

    return f"""
<nav class="navbar navbar-expand-lg navbar-dark navbar-krushi sticky-top">
    <div class="container-fluid px-3 px-sm-4 px-xl-5">
        <!-- Brand -->
        <a class="navbar-brand-custom" href="index.html">
            <img class="brand-logo" src="images/saptashrungi_logo_round.jpg" alt="Logo">
            <div>
                <span class="brand-text-primary">
                    <span class="lang-mr">सप्तशृंगी ॲग्रो सर्व्हिसेस</span>
                    <span class="lang-en">Saptashrungi Agro Services</span>
                </span>
                <span class="brand-text-secondary d-none d-sm-block">
                    <span class="lang-mr">आपल्या शेतीसाठी योग्य मार्गदर्शन</span>
                    <span class="lang-en">Quality Agricultural Guidance</span>
                </span>
            </div>
        </a>

        <!-- Mobile Language Switcher -->
        <div class="d-flex align-items-center d-lg-none ms-auto me-2">
            <div class="btn-group btn-group-sm rounded-pill border shadow-sm p-1" style="background:#f8fafc;">
                <button type="button" onclick="setLang('mr')" class="btn btn-sm btn-success text-white rounded-pill px-2 py-1 fw-bold btn-lang-mr" style="font-size:0.75rem;">🌾 मराठी</button>
                <button type="button" onclick="setLang('en')" class="btn btn-sm btn-light text-dark rounded-pill px-2 py-1 fw-bold btn-lang-en" style="font-size:0.75rem;">Eng</button>
            </div>
        </div>

        <button class="navbar-toggler border-0 me-2" type="button" data-bs-toggle="collapse" data-bs-target="#navbarMain" aria-controls="navbarMain" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarMain">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0 ms-lg-4 gap-lg-2 gap-xl-3">
                <li class="nav-item">
                    <a class="nav-link nav-link-custom px-lg-3{act('home')}" href="index.html">
                        <i class="bi bi-house-door me-1"></i>
                        <span class="lang-mr">मुख्यपृष्ठ</span><span class="lang-en">Home</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link nav-link-custom px-lg-3{act('products')}" href="products.html">
                        <i class="bi bi-grid me-1"></i>
                        <span class="lang-mr">उत्पादने</span><span class="lang-en">Products</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link nav-link-custom px-lg-3" href="index.html#reviews">
                        <i class="bi bi-star-fill text-warning me-1"></i>
                        <span class="lang-mr">अभिप्राय (Reviews)</span><span class="lang-en">Reviews</span>
                    </a>
                </li>

                <!-- Farming Advisory Dropdown -->
                <li class="nav-item dropdown">
                    <a class="nav-link nav-link-custom px-lg-3 dropdown-toggle{act('advisory')}" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        <i class="bi bi-cloud-sun text-success me-1"></i>
                        <span class="lang-mr">कृषी सल्लागार</span><span class="lang-en">Farming Advisory</span>
                    </a>
                    <ul class="dropdown-menu shadow border-0 rounded-3 mt-1 p-1">
                        <li>
                            <a class="dropdown-item rounded-2 py-2" href="fertilizer-calc.html">
                                <i class="bi bi-calculator me-2 text-success"></i>
                                <span class="lang-mr">खत कॅल्क्युलेटर</span><span class="lang-en">Fertilizer Calculator</span>
                            </a>
                        </li>
                        <li>
                            <a class="dropdown-item rounded-2 py-2" href="weather.html">
                                <i class="bi bi-cloud-rain me-2 text-primary"></i>
                                <span class="lang-mr">हवामान अंदाज</span><span class="lang-en">Weather Forecast</span>
                            </a>
                        </li>
                        <li>
                            <a class="dropdown-item rounded-2 py-2" href="farming-tips.html">
                                <i class="bi bi-journal-text me-2 text-warning"></i>
                                <span class="lang-mr">पीक संरक्षण व कीड सल्ला</span><span class="lang-en">Crop Care & Pest Advice</span>
                            </a>
                        </li>
                    </ul>
                </li>

                <li class="nav-item">
                    <a class="nav-link nav-link-custom px-lg-3{act('about')}" href="about.html">
                        <span class="lang-mr">आमच्याबद्दल</span><span class="lang-en">About Us</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link nav-link-custom px-lg-3{act('contact')}" href="contact.html">
                        <span class="lang-mr">संपर्क</span><span class="lang-en">Contact</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link nav-link-custom px-lg-3{act('faq')}" href="faq.html">
                        <span class="lang-mr">वारंवार विचारले जाणारे प्रश्न</span><span class="lang-en">FAQ</span>
                    </a>
                </li>
            </ul>

            <!-- Desktop Language Switcher & Login -->
            <div class="d-flex align-items-center gap-2 mt-3 mt-lg-0">
                <div class="btn-group btn-group-sm rounded-pill border shadow-sm p-1 d-none d-lg-flex" style="background:#f8fafc;">
                    <button type="button" onclick="setLang('mr')" class="btn btn-sm btn-success text-white rounded-pill px-3 py-1 fw-bold btn-lang-mr" style="font-size:0.8rem;">🌾 मराठी</button>
                    <button type="button" onclick="setLang('en')" class="btn btn-sm btn-light text-dark rounded-pill px-3 py-1 fw-bold btn-lang-en" style="font-size:0.8rem;">Eng</button>
                </div>

                <a href="login.html" class="btn btn-sm btn-outline-light rounded-pill px-3 py-1 fw-semibold">
                    <i class="bi bi-person-circle me-1"></i>
                    <span class="lang-mr">लॉगिन</span><span class="lang-en">Login</span>
                </a>
            </div>
        </div>
    </div>
</nav>
"""

def foot_html():
    return """
<footer class="footer-krushi pt-5 pb-4 mt-5">
    <div class="container-fluid px-3 px-sm-4 px-xl-5">
        <div class="row g-4 mb-4">
            <!-- Brand -->
            <div class="col-lg-4 col-md-6">
                <div class="d-flex align-items-center gap-3 mb-3">
                    <img src="images/saptashrungi_logo_round.jpg" alt="Logo" class="rounded-circle shadow" style="width:52px;height:52px;object-fit:cover;border:2px solid #22c55e;">
                    <div>
                        <h5 class="fw-bold text-white mb-0">
                            <span class="lang-mr">सप्तशृंगी ॲग्रो सर्व्हिसेस</span>
                            <span class="lang-en">Saptashrungi Agro Services</span>
                        </h5>
                        <small class="text-success fw-semibold">Mirakhnagar, Vaijapur</small>
                    </div>
                </div>
                <p class="small text-white-50" style="line-height:1.6;">
                    <span class="lang-mr">मिरखनगर, वैजापूर येथील अग्रगण्य व अधिकृत कृषी सेवा केंद्र. १००% प्रमाणित बियाणे, खते, कीटकनाशके आणि आधुनिक ठिबक सिंचन साहित्य रास्त दरात उपलब्ध.</span>
                    <span class="lang-en">Leading authorized agricultural retail center in Mirakhnagar, Vaijapur. Providing 100% certified seeds, fertilizers, crop protection and modern drip irrigation at fair rates.</span>
                </p>
                <div class="d-flex gap-2">
                    <a href="https://wa.me/918600813827" target="_blank" class="btn btn-sm btn-success rounded-circle" style="width:36px;height:36px;display:flex;align-items:center;justify-content:center;"><i class="bi bi-whatsapp"></i></a>
                    <a href="tel:+918600813827" class="btn btn-sm btn-primary rounded-circle" style="width:36px;height:36px;display:flex;align-items:center;justify-content:center;"><i class="bi bi-telephone-fill"></i></a>
                    <a href="https://maps.app.goo.gl/S34rKk9DwEntCGid6" target="_blank" class="btn btn-sm btn-danger rounded-circle" style="width:36px;height:36px;display:flex;align-items:center;justify-content:center;"><i class="bi bi-geo-alt-fill"></i></a>
                </div>
            </div>

            <!-- Categories -->
            <div class="col-lg-2 col-md-6 col-6">
                <h6 class="text-white fw-bold mb-3">
                    <span class="lang-mr">उत्पादने वर्गवारी</span>
                    <span class="lang-en">Categories</span>
                </h6>
                <ul class="list-unstyled d-flex flex-column gap-2 small" style="color:rgba(200,230,201,0.75);">
                    <li><a href="products.html?cat=seeds" class="text-decoration-none text-light"><span class="lang-mr">🌾 बियाणे (Seeds)</span><span class="lang-en">🌾 Seeds</span></a></li>
                    <li><a href="products.html?cat=fertilizers" class="text-decoration-none text-light"><span class="lang-mr">🧪 खते (Fertilizers)</span><span class="lang-en">🧪 Fertilizers</span></a></li>
                    <li><a href="products.html?cat=pesticides" class="text-decoration-none text-light"><span class="lang-mr">🐛 कीटकनाशके (Pesticides)</span><span class="lang-en">🐛 Pesticides</span></a></li>
                    <li><a href="products.html?cat=tools" class="text-decoration-none text-light"><span class="lang-mr">🔧 शेती अवजारे (Farm Tools)</span><span class="lang-en">🔧 Farm Tools</span></a></li>
                    <li><a href="products.html?cat=drip" class="text-decoration-none text-light"><span class="lang-mr">💧 ठिबक सिंचन (Drip)</span><span class="lang-en">💧 Drip Irrigation</span></a></li>
                </ul>
            </div>

            <!-- Advisory -->
            <div class="col-lg-3 col-md-6 col-6">
                <h6 class="text-white fw-bold mb-3">
                    <span class="lang-mr">कृषी साधने</span>
                    <span class="lang-en">Agri Tools</span>
                </h6>
                <ul class="list-unstyled d-flex flex-column gap-2 small" style="color:rgba(200,230,201,0.75);">
                    <li><a href="fertilizer-calc.html" class="text-decoration-none text-light"><i class="bi bi-calculator me-1 text-success"></i><span class="lang-mr">खत कॅल्क्युलेटर</span><span class="lang-en">Fertilizer Calculator</span></a></li>
                    <li><a href="weather.html" class="text-decoration-none text-light"><i class="bi bi-cloud-sun me-1 text-primary"></i><span class="lang-mr">हवामान अंदाज</span><span class="lang-en">Weather Forecast</span></a></li>
                    <li><a href="farming-tips.html" class="text-decoration-none text-light"><i class="bi bi-journal-text me-1 text-warning"></i><span class="lang-mr">पीक सल्ला व कीड नियंत्रण</span><span class="lang-en">Crop Care & Pest Advice</span></a></li>
                    <li><a href="index.html#reviews" class="text-decoration-none text-light"><i class="bi bi-star-fill me-1 text-warning"></i><span class="lang-mr">शेतकरी अभिप्राय (Reviews)</span><span class="lang-en">Farmer Reviews</span></a></li>
                    <li><a href="faq.html" class="text-decoration-none text-light"><i class="bi bi-question-circle me-1 text-info"></i><span class="lang-mr">वारंवार विचारले जाणारे प्रश्न</span><span class="lang-en">FAQ</span></a></li>
                </ul>
            </div>

            <!-- Address & Contact -->
            <div class="col-lg-3 col-md-6">
                <h6 class="text-white fw-bold mb-3">
                    <span class="lang-mr">📍 दुकानाचा पत्ता</span>
                    <span class="lang-en">📍 Shop Location</span>
                </h6>
                <div class="d-flex flex-column gap-2 small" style="color:rgba(200,230,201,0.75);">
                    <div><i class="bi bi-geo-alt-fill text-success me-1"></i> Mirakhnagar, Vaijapur, Chhatrapati Sambhajinagar - 423703</div>
                    <div><i class="bi bi-telephone-fill text-success me-1"></i> <a href="tel:+918600813827" class="text-white text-decoration-none fw-bold">+91 8600813827</a></div>
                    <div><i class="bi bi-clock-fill text-success me-1"></i> <span class="lang-mr">सोम - शनि: सकाळी ८:०० ते रात्री ८:३०</span><span class="lang-en">Mon - Sat: 8:00 AM to 8:30 PM</span></div>
                    <div><i class="bi bi-receipt text-success me-1"></i> GSTIN: 27AAAAA0000A1Z5</div>
                </div>
            </div>
        </div>

        <!-- Clean Footer Bottom without payment badges -->
        <div class="footer-bottom text-center pt-3 border-top border-secondary border-opacity-25">
            <div style="color:rgba(200,230,201,0.55);font-size:0.85rem;">
                &copy; 2026 <strong class="text-white">Saptashrungi Agro Services</strong>. <span class="lang-mr">शेतकऱ्यांच्या सेवेसाठी सदैव तत्पर.</span><span class="lang-en">Serving Farmers, Supporting Better Farming.</span>
            </div>
        </div>
    </div>

    <!-- Universal Bilingual Switcher Engine -->
    <script>
        function setLang(lang) {
            document.documentElement.setAttribute('lang', lang);
            localStorage.setItem('site_lang', lang);
            
            var isMr = (lang === 'mr');
            document.querySelectorAll('.btn-lang-mr').forEach(function(b){
                b.className = isMr ? 'btn btn-sm btn-success text-white rounded-pill px-3 py-1 fw-bold btn-lang-mr' : 'btn btn-sm btn-light text-dark rounded-pill px-3 py-1 fw-bold btn-lang-mr';
            });
            document.querySelectorAll('.btn-lang-en').forEach(function(b){
                b.className = !isMr ? 'btn btn-sm btn-success text-white rounded-pill px-3 py-1 fw-bold btn-lang-en' : 'btn btn-sm btn-light text-dark rounded-pill px-3 py-1 fw-bold btn-lang-en';
            });

            document.querySelectorAll('[data-placeholder-mr]').forEach(function(el){
                el.placeholder = isMr ? el.getAttribute('data-placeholder-mr') : el.getAttribute('data-placeholder-en');
            });

            window.dispatchEvent(new CustomEvent('languagechange', { detail: { lang: lang } }));
        }
        document.addEventListener('DOMContentLoaded', function(){
            var savedLang = localStorage.getItem('site_lang') || 'mr';
            setLang(savedLang);
        });
    </script>
</footer>
</body>
</html>
"""

print("Base templates initialized.")
