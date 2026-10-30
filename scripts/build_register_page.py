# -*- coding: utf-8 -*-
"""
Builds dist/register.html with complete bilingual support (Marathi/English)
and proper registration flow (does NOT auto-login, redirects cleanly to login.html).
"""
import os
import sys

BASE_DIR = r"c:\Users\HP\OneDrive\Documents\krushi seva"
DIST_DIR = os.path.join(BASE_DIR, "dist")
sys.path.append(os.path.join(BASE_DIR, "scripts"))

from build_site import head_html, nav_html, foot_html

def build_register_page():
    content = head_html("नोंदणी करा", "Register") + nav_html("register") + """
<div class="container my-5" style="max-width: 760px;">
    <div class="card border-0 shadow-lg rounded-4 overflow-hidden bg-white">
        <!-- Header Banner matching authentic Spring Boot template -->
        <div class="card-header text-center py-4 text-white" style="background: linear-gradient(135deg, #1b5e20, #15803d);">
            <img src="images/saptashrungi_logo_round.jpg" alt="Logo" class="rounded-circle shadow mb-2" style="width: 68px; height: 68px; object-fit: cover; border: 3px solid #ffffff;">
            <h4 class="fw-bold mb-1 text-white">
                <span class="lang-mr">👨‍🌾 नवीन शेतकरी नोंदणी</span>
                <span class="lang-en">👨‍🌾 New Farmer Registration</span>
            </h4>
            <small class="text-white-50">
                <span class="lang-mr">सप्तशृंगी ॲग्रो सर्व्हिसेस - तुमचे शेतकरी खाते तयार करा</span>
                <span class="lang-en">Saptashrungi Agro Services - Create your farmer account</span>
            </small>
        </div>

        <div class="card-body p-4 p-md-5">
            <!-- Validation Error Alert -->
            <div id="regErrorBox" class="alert alert-danger d-none align-items-center gap-2 small rounded-3 mb-4">
                <i class="bi bi-exclamation-triangle-fill fs-5 text-danger"></i>
                <div id="regErrorMsg"></div>
            </div>

            <!-- Registration Form -->
            <form id="regForm" onsubmit="return handleReg(event)">
                <div class="row g-3">
                    <!-- Full Name -->
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-success">
                            <span class="lang-mr">पूर्ण नाव *</span>
                            <span class="lang-en">Full Name *</span>
                        </label>
                        <input type="text" id="rName" class="form-control" required
                               data-placeholder-mr="उदा. रमेश आनंदा पाटील"
                               data-placeholder-en="e.g. Ramesh Ananda Patil"
                               placeholder="उदा. रमेश आनंदा पाटील">
                    </div>

                    <!-- Mobile Number -->
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-success">
                            <span class="lang-mr">मोबाईल नंबर (१० अंक) *</span>
                            <span class="lang-en">Mobile Number (10 digits) *</span>
                        </label>
                        <div class="input-group">
                            <span class="input-group-text bg-light text-muted fw-bold">+91</span>
                            <input type="tel" id="rPhone" class="form-control" required maxlength="10" pattern="[0-9]{10}"
                                   data-placeholder-mr="१० अंकी मोबाईल नंबर"
                                   data-placeholder-en="10-digit mobile number"
                                   placeholder="१० अंकी मोबाईल नंबर">
                        </div>
                    </div>

                    <!-- Email -->
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-success">
                            <span class="lang-mr">ईमेल पत्ता (ऐच्छिक)</span>
                            <span class="lang-en">Email Address (Optional)</span>
                        </label>
                        <input type="email" id="rEmail" class="form-control"
                               data-placeholder-mr="उदा. farmer@example.com"
                               data-placeholder-en="e.g. farmer@example.com"
                               placeholder="उदा. farmer@example.com">
                    </div>

                    <!-- Village -->
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-success">
                            <span class="lang-mr">गाव *</span>
                            <span class="lang-en">Village *</span>
                        </label>
                        <input type="text" id="rVillage" class="form-control" required
                               data-placeholder-mr="उदा. मिरखनगर"
                               data-placeholder-en="e.g. Mirakhnagar"
                               placeholder="उदा. मिरखनगर">
                    </div>

                    <!-- Taluka -->
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-success">
                            <span class="lang-mr">तालुका *</span>
                            <span class="lang-en">Taluka *</span>
                        </label>
                        <input type="text" id="rTaluka" class="form-control" required
                               data-placeholder-mr="उदा. वैजापूर"
                               data-placeholder-en="e.g. Vaijapur"
                               placeholder="उदा. वैजापूर">
                    </div>

                    <!-- District -->
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-success">
                            <span class="lang-mr">जिल्हा *</span>
                            <span class="lang-en">District *</span>
                        </label>
                        <input type="text" id="rDistrict" class="form-control" required
                               data-placeholder-mr="उदा. छत्रपती संभाजीनगर"
                               data-placeholder-en="e.g. Chhatrapati Sambhajinagar"
                               placeholder="उदा. छत्रपती संभाजीनगर"
                               value="छत्रपती संभाजीनगर">
                    </div>

                    <!-- Complete Address -->
                    <div class="col-12">
                        <label class="form-label small fw-bold text-success">
                            <span class="lang-mr">शेताचा पत्ता / घराचा पत्ता (ऐच्छिक)</span>
                            <span class="lang-en">Farm Address / Home Address (Optional)</span>
                        </label>
                        <textarea id="rAddress" class="form-control" rows="2"
                                  data-placeholder-mr="उदा. गट क्र., पोस्ट, वैजापूर..."
                                  data-placeholder-en="e.g. Gat No, Post, Vaijapur..."
                                  placeholder="उदा. गट क्र., पोस्ट, वैजापूर..."></textarea>
                    </div>

                    <!-- Password -->
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-success">
                            <span class="lang-mr">पासवर्ड *</span>
                            <span class="lang-en">Password *</span>
                        </label>
                        <input type="password" id="rPass" class="form-control" required minlength="4"
                               data-placeholder-mr="किमान ४ अक्षरे किंवा अंक"
                               data-placeholder-en="At least 4 characters"
                               placeholder="••••••••">
                    </div>

                    <!-- Confirm Password -->
                    <div class="col-md-6">
                        <label class="form-label small fw-bold text-success">
                            <span class="lang-mr">पासवर्डची खात्री करा *</span>
                            <span class="lang-en">Confirm Password *</span>
                        </label>
                        <input type="password" id="rPassConfirm" class="form-control" required minlength="4"
                               data-placeholder-mr="पासवर्ड पुन्हा टाका"
                               data-placeholder-en="Re-enter password"
                               placeholder="••••••••">
                    </div>
                </div>

                <button type="submit" id="btnRegSubmit" class="btn btn-success w-100 py-3 rounded-pill fw-bold shadow-sm mt-4 text-white" style="background:#15803d; border-color:#15803d; font-size:1.05rem;">
                    <i class="bi bi-person-check-fill me-1"></i>
                    <span class="lang-mr">नोंदणी पूर्ण करा</span>
                    <span class="lang-en">Complete Registration</span>
                </button>
            </form>

            <!-- Success Confirmation Card (Shown after registration, NO AUTO LOGIN) -->
            <div id="regSuccessCard" class="d-none text-center py-4">
                <div class="mb-3">
                    <i class="bi bi-check-circle-fill text-success" style="font-size: 4rem;"></i>
                </div>
                <h4 class="fw-bold text-success mb-2">
                    <span class="lang-mr">🎉 अभिनंदन! शेतकरी नोंदणी यशस्वी झाली आहे.</span>
                    <span class="lang-en">🎉 Congratulations! Registration Successful.</span>
                </h4>
                <p class="text-muted mb-4" style="max-width: 520px; margin: 0 auto; line-height: 1.6;">
                    <span class="lang-mr">आपले शेतकरी खाते तयार झाले आहे. आता कृपया आपल्या मोबाईल नंबर आणि पासवर्डचा वापर करून लॉगिन करा.</span>
                    <span class="lang-en">Your farmer account has been created. Now please log in using your registered mobile number and password.</span>
                </p>
                <div class="d-flex justify-content-center gap-3">
                    <a id="regGoToLoginBtn" href="login.html" class="btn btn-success btn-lg px-4 py-2 rounded-pill fw-bold shadow-sm" style="background:#15803d; border-color:#15803d;">
                        <span class="lang-mr">लॉगिन पृष्ठावर जा &rarr;</span>
                        <span class="lang-en">Proceed to Login &rarr;</span>
                    </a>
                </div>
                <small class="text-muted d-block mt-3">
                    <span class="lang-mr">२ सेकंदात लॉगिन पानाकडे रिडायरेक्ट करत आहे...</span>
                    <span class="lang-en">Redirecting to login page in 2 seconds...</span>
                </small>
            </div>

            <!-- Bottom Links -->
            <div class="text-center pt-4 border-top mt-4 small">
                <span class="text-muted">
                    <span class="lang-mr">आधीच नोंदणीकृत आहात का?</span>
                    <span class="lang-en">Already registered?</span>
                </span>
                <a href="login.html" class="text-success fw-bold text-decoration-none ms-1">
                    <span class="lang-mr">लॉगिन करा</span>
                    <span class="lang-en">Sign In here</span>
                </a>
            </div>
        </div>

        <div class="card-footer text-center bg-light py-3 border-0">
            <a href="index.html" class="text-muted small text-decoration-none">
                ← <span class="lang-mr">मुख्यपृष्ठावर परत जा</span><span class="lang-en">Back to Home Page</span>
            </a>
        </div>
    </div>
</div>

<script>
function handleReg(e) {
    if (e && e.preventDefault) e.preventDefault();
    
    var name = document.getElementById('rName').value.trim();
    var phone = document.getElementById('rPhone').value.trim();
    var email = document.getElementById('rEmail').value.trim();
    var village = document.getElementById('rVillage').value.trim();
    var taluka = document.getElementById('rTaluka').value.trim();
    var district = document.getElementById('rDistrict').value.trim();
    var address = document.getElementById('rAddress').value.trim();
    var pass = document.getElementById('rPass').value;
    var passConf = document.getElementById('rPassConfirm').value;
    var errBox = document.getElementById('regErrorBox');
    var errMsg = document.getElementById('regErrorMsg');

    // 1. Validate Phone
    if (phone.length !== 10 || !/^\\d{10}$/.test(phone)) {
        errBox.classList.remove('d-none');
        errBox.classList.add('d-flex');
        errMsg.innerHTML = '<span class="lang-mr">कृपया अचूक १० अंकी मोबाईल नंबर टाका.</span><span class="lang-en">Please enter a valid 10-digit mobile number.</span>';
        window.scrollTo({ top: 0, behavior: 'smooth' });
        return false;
    }

    // 2. Validate Password Match
    if (pass !== passConf) {
        errBox.classList.remove('d-none');
        errBox.classList.add('d-flex');
        errMsg.innerHTML = '<span class="lang-mr">पासवर्ड जुळत नाहीत. कृपया दोन्ही रकान्यात एकच पासवर्ड टाका.</span><span class="lang-en">Passwords do not match. Please verify.</span>';
        window.scrollTo({ top: 0, behavior: 'smooth' });
        return false;
    }

    errBox.classList.add('d-none');
    errBox.classList.remove('d-flex');

    // 3. Save to localStorage (WITHOUT auto-logging in!)
    var newFarmer = {
        name: name,
        phone: phone,
        email: email,
        village: village,
        taluka: taluka,
        district: district,
        address: address,
        registeredAt: new Date().toISOString()
    };
    
    var list = JSON.parse(localStorage.getItem('ksk_registered_farmers') || '[]');
    list.push(newFarmer);
    localStorage.setItem('ksk_registered_farmers', JSON.stringify(list));
    localStorage.setItem('last_registered_phone', phone);
    localStorage.setItem('last_registered_name', name);
    if (village) {
        localStorage.setItem('user_location', village + (district ? ', ' + district : ''));
    }

    // DO NOT set user_role yet! Registration and login are two distinct steps.
    localStorage.removeItem('user_role');

    // 4. Show Success Card and hide Form
    document.getElementById('regForm').classList.add('d-none');
    var successCard = document.getElementById('regSuccessCard');
    successCard.classList.remove('d-none');

    var targetLoginUrl = 'login.html?registered=true&phone=' + encodeURIComponent(phone);
    var loginBtn = document.getElementById('regGoToLoginBtn');
    if (loginBtn) loginBtn.href = targetLoginUrl;

    // 5. Automatically redirect to login page after 2.5 seconds
    setTimeout(function(){
        window.location.href = targetLoginUrl;
    }, 2500);

    return false;
}
</script>
""" + foot_html()
    with open(os.path.join(DIST_DIR, "register.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated dist/register.html with full bilingual support and clean login redirection")

if __name__ == "__main__":
    build_register_page()
