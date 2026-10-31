# -*- coding: utf-8 -*-
"""
Syncs generated dist files into Spring Boot templates so both static (Vercel)
and server-rendered (Spring Boot / Supabase) serve the latest features.
"""
import os
import shutil

BASE_DIR = r"c:\Users\HP\OneDrive\Documents\krushi seva"
DIST_DIR = os.path.join(BASE_DIR, "dist")
TEMPLATES_DIR = os.path.join(BASE_DIR, "src", "main", "resources", "templates")

MAPPINGS = {
    # Auth
    os.path.join(DIST_DIR, "register.html"): os.path.join(TEMPLATES_DIR, "auth", "register.html"),
    os.path.join(DIST_DIR, "login.html"): os.path.join(TEMPLATES_DIR, "auth", "login.html"),
    os.path.join(DIST_DIR, "forgot-password.html"): os.path.join(TEMPLATES_DIR, "auth", "forgot-password.html"),

    # Admin
    os.path.join(DIST_DIR, "admin-dashboard.html"): os.path.join(TEMPLATES_DIR, "admin", "dashboard.html"),
    os.path.join(DIST_DIR, "admin-products.html"): os.path.join(TEMPLATES_DIR, "admin", "products.html"),
    os.path.join(DIST_DIR, "admin-product-form.html"): os.path.join(TEMPLATES_DIR, "admin", "product-form.html"),
    os.path.join(DIST_DIR, "admin-customers.html"): os.path.join(TEMPLATES_DIR, "admin", "customers.html"),
    os.path.join(DIST_DIR, "admin-udhari.html"): os.path.join(TEMPLATES_DIR, "admin", "udhari.html"),
    os.path.join(DIST_DIR, "admin-categories.html"): os.path.join(TEMPLATES_DIR, "admin", "categories.html"),
    os.path.join(DIST_DIR, "admin-inventory.html"): os.path.join(TEMPLATES_DIR, "admin", "inventory.html"),
    os.path.join(DIST_DIR, "admin-reports.html"): os.path.join(TEMPLATES_DIR, "admin", "reports.html"),
    os.path.join(DIST_DIR, "admin-backup.html"): os.path.join(TEMPLATES_DIR, "admin", "backup.html"),
    os.path.join(DIST_DIR, "admin-settings.html"): os.path.join(TEMPLATES_DIR, "admin", "settings.html"),

    # Customer / Farmer
    os.path.join(DIST_DIR, "farmer-dashboard.html"): os.path.join(TEMPLATES_DIR, "customer", "dashboard.html"),
    os.path.join(DIST_DIR, "farmer-udhari.html"): os.path.join(TEMPLATES_DIR, "customer", "udhari.html"),
    os.path.join(DIST_DIR, "farmer-profile.html"): os.path.join(TEMPLATES_DIR, "customer", "profile.html"),
    os.path.join(DIST_DIR, "farmer-orders.html"): os.path.join(TEMPLATES_DIR, "customer", "order-history.html"),
    os.path.join(DIST_DIR, "farmer-pay.html"): os.path.join(TEMPLATES_DIR, "customer", "pay.html"),
    os.path.join(DIST_DIR, "farmer-notifications.html"): os.path.join(TEMPLATES_DIR, "customer", "notifications.html"),

    # Public
    os.path.join(DIST_DIR, "index.html"): os.path.join(TEMPLATES_DIR, "public", "index.html"),
    os.path.join(DIST_DIR, "products.html"): os.path.join(TEMPLATES_DIR, "public", "products.html"),
    os.path.join(DIST_DIR, "weather.html"): os.path.join(TEMPLATES_DIR, "public", "weather.html"),
    os.path.join(DIST_DIR, "fertilizer-calc.html"): os.path.join(TEMPLATES_DIR, "public", "fertilizer-calc.html"),
    os.path.join(DIST_DIR, "farming-tips.html"): os.path.join(TEMPLATES_DIR, "public", "farming-tips.html"),
    os.path.join(DIST_DIR, "about.html"): os.path.join(TEMPLATES_DIR, "public", "about.html"),
    os.path.join(DIST_DIR, "contact.html"): os.path.join(TEMPLATES_DIR, "public", "contact.html"),
    os.path.join(DIST_DIR, "faq.html"): os.path.join(TEMPLATES_DIR, "public", "faq.html"),
    os.path.join(DIST_DIR, "offers.html"): os.path.join(TEMPLATES_DIR, "public", "offers.html"),
}

synced = 0
for src, dst in MAPPINGS.items():
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        synced += 1

print(f"Successfully synced {synced} templates from dist to src/main/resources/templates!")
