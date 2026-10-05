package com.krushisevakendra.enums;

public enum OrderStatus {
    PENDING("Pending", "प्रलंबित"),
    CONFIRMED("Confirmed", "मंजूर"),
    PROCESSING("Processing", "प्रक्रियेत"),
    READY("Ready for Pickup/Delivery", "तयार आहे"),
    DELIVERED("Delivered", "पोहोचवले"),
    CANCELLED("Cancelled", "रद्द केले");

    private final String displayNameEn;
    private final String displayNameMr;

    OrderStatus(String displayNameEn, String displayNameMr) {
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
