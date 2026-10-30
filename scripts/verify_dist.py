# -*- coding: utf-8 -*-
import os

DIST_DIR = r"c:\Users\HP\OneDrive\Documents\krushi seva\dist"

files = [
    "index.html", "products.html", "fertilizer-calc.html",
    "weather.html", "farming-tips.html", "about.html",
    "contact.html", "faq.html", "login.html"
]

all_passed = True

for f in files:
    path = os.path.join(DIST_DIR, f)
    with open(path, "r", encoding="utf-8") as fp:
        content = fp.read()
    
    has_lang_mr = 'class="lang-mr"' in content or "class='lang-mr'" in content or ".lang-mr" in content
    has_lang_en = 'class="lang-en"' in content or "class='lang-en'" in content or ".lang-en" in content
    has_set_lang = "function setLang" in content or "setLang(" in content
    
    # Check restrictions:
    has_credit_upi = "Credit & UPI" in content or "Credit &amp; UPI" in content
    has_accepted_badges = "Accepted:" in content and "Udhari" in content

    print(f"Checking {f}:")
    print(f"  - Has lang-mr: {has_lang_mr}")
    print(f"  - Has lang-en: {has_lang_en}")
    print(f"  - Has setLang engine: {has_set_lang}")
    print(f"  - Contains unwanted Credit & UPI: {has_credit_upi}")
    print(f"  - Contains unwanted Accepted badges: {has_accepted_badges}")

    if not (has_lang_mr and has_lang_en and has_set_lang) or has_credit_upi or has_accepted_badges:
        all_passed = False
        print(f"  FAILED checks for {f}!")

if all_passed:
    print("\nALL 9 PAGES PASSED ALL VERIFICATION CHECKS!")
else:
    print("\nSOME CHECKS FAILED!")
