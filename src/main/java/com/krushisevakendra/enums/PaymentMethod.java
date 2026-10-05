package com.krushisevakendra.enums;

public enum PaymentMethod {
    CASH("Cash", "रोख"),
    UPI("UPI / QR Code", "यूपीआय / क्यूआर कोड"),
    BANK_TRANSFER("Bank Transfer / NEFT", "बँक ट्रान्सफर"),
    ONLINE("Online Payment", "ऑनलाइन पेमेंट"),
    UDHARI("Udhari (Credit)", "उधारी (खाते)");

    private final String displayNameEn;
    private final String displayNameMr;

    PaymentMethod(String displayNameEn, String displayNameMr) {
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
