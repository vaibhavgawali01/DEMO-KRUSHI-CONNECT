package com.krushisevakendra.dto;

import com.krushisevakendra.enums.PaymentMethod;
import jakarta.validation.constraints.DecimalMin;
import jakarta.validation.constraints.NotNull;
import java.math.BigDecimal;

public class UdhariPaymentDto {

    @NotNull(message = "Udhari ID is required")
    private Long udhariId;

    @NotNull(message = "Payment amount is required / जमा रक्कम आवश्यक आहे")
    @DecimalMin(value = "1.00", message = "Amount must be at least ₹1.00")
    private BigDecimal amount;

    @NotNull(message = "Payment method is required")
    private PaymentMethod paymentMethod = PaymentMethod.CASH;

    private String transactionId;
    private String remarks;

    public UdhariPaymentDto() {}

    public Long getUdhariId() {
        return udhariId;
    }

    public void setUdhariId(Long udhariId) {
        this.udhariId = udhariId;
    }

    public BigDecimal getAmount() {
        return amount;
    }

    public void setAmount(BigDecimal amount) {
        this.amount = amount;
    }

    public PaymentMethod getPaymentMethod() {
        return paymentMethod;
    }

    public void setPaymentMethod(PaymentMethod paymentMethod) {
        this.paymentMethod = paymentMethod;
    }

    public String getTransactionId() {
        return transactionId;
    }

    public void setTransactionId(String transactionId) {
        this.transactionId = transactionId;
    }

    public String getRemarks() {
        return remarks;
    }

    public void setRemarks(String remarks) {
        this.remarks = remarks;
    }
}
