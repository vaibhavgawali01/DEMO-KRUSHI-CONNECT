package com.krushisevakendra.enums;

public enum UdhariStatus {
    ACTIVE("Active / Pending", "चालू / बाकी"),
    OVERDUE("Overdue", "मुदत संपली"),
    PAID_IN_FULL("Paid in Full", "पूर्ण जमा");

    private final String displayNameEn;
    private final String displayNameMr;

    UdhariStatus(String displayNameEn, String displayNameMr) {
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
