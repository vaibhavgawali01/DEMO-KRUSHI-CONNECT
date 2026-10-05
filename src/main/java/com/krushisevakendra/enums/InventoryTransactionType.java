package com.krushisevakendra.enums;

public enum InventoryTransactionType {
    STOCK_IN("Stock In / Purchase", "माल जमा / खरेदी"),
    STOCK_OUT("Stock Out / Sale", "माल वजा / विक्री"),
    ORDER_DEDUCTION("Order Deduction", "ऑर्डर वजावट"),
    RETURN("Customer Return", "परतावा"),
    ADJUSTMENT("Inventory Adjustment / Damage", "नुकसान / दुरुस्ती");

    private final String displayNameEn;
    private final String displayNameMr;

    InventoryTransactionType(String displayNameEn, String displayNameMr) {
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
