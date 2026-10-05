package com.krushisevakendra.enums;

public enum PaymentStatus {
    PENDING("Pending", "प्रलंबित"),
    PAID("Paid", "यशस्वी"),
    PARTIAL("Partially Paid", "अंशतः भरले"),
    FAILED("Failed", "अयशस्वी");

    private final String displayNameEn;
    private final String displayNameMr;

    PaymentStatus(String displayNameEn, String displayNameMr) {
        this.displayNameEn = displayNameEn;
        this.displayNameMr = displayNameMr;
    }

    public String getDisplayNameEn() {
        return displayNameEn;
    }

    public String getDisplayNameMr() {
        return displayNameMr;
    }
}
