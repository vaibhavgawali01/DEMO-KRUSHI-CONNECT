package com.krushisevakendra.enums;

public enum NotificationType {
    IN_APP("In-App Notification", "अ‍ॅप सूचना"),
    SMS("SMS Reminder", "एसएमएस"),
    WHATSAPP("WhatsApp Message", "व्हॉट्सअ‍ॅप"),
    EMAIL("Email Alert", "ईमेल");

    private final String displayNameEn;
    private final String displayNameMr;

    NotificationType(String displayNameEn, String displayNameMr) {
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
