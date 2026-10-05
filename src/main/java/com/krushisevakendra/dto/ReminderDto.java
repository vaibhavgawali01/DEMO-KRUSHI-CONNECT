package com.krushisevakendra.dto;

import com.krushisevakendra.enums.NotificationType;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import java.math.BigDecimal;
import java.time.LocalDate;

public class ReminderDto {

    @NotNull(message = "Customer is required")
    private Long userId;

    private Long udhariId;
    private String customerName;
    private String mobile;
    private String email;
    private BigDecimal dueAmount;
    private LocalDate dueDate;

    @NotNull(message = "Notification type is required")
    private NotificationType type = NotificationType.WHATSAPP;

    @NotBlank(message = "Message cannot be empty")
    private String message;

    public ReminderDto() {}

    public Long getUserId() {
        return userId;
    }

    public void setUserId(Long userId) {
        this.userId = userId;
    }

    public Long getUdhariId() {
        return udhariId;
    }

    public void setUdhariId(Long udhariId) {
        this.udhariId = udhariId;
    }

    public String getCustomerName() {
        return customerName;
    }

    public void setCustomerName(String customerName) {
        this.customerName = customerName;
    }

    public String getMobile() {
        return mobile;
    }

    public void setMobile(String mobile) {
        this.mobile = mobile;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public BigDecimal getDueAmount() {
        return dueAmount;
    }

    public void setDueAmount(BigDecimal dueAmount) {
        this.dueAmount = dueAmount;
    }

    public LocalDate getDueDate() {
        return dueDate;
    }

    public void setDueDate(LocalDate dueDate) {
        this.dueDate = dueDate;
    }

    public NotificationType getType() {
        return type;
    }

    public void setType(NotificationType type) {
        this.type = type;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
}
