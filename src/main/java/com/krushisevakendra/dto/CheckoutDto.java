package com.krushisevakendra.dto;

import com.krushisevakendra.enums.PaymentMethod;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;

public class CheckoutDto {

    @NotBlank(message = "Customer name is required / ग्राहकाचे नाव आवश्यक आहे")
    private String customerName;

    @NotBlank(message = "Mobile number is required / मोबाईल नंबर आवश्यक आहे")
    private String mobile;

    @NotBlank(message = "Delivery address is required / पोहोच पत्ता आवश्यक आहे")
    private String deliveryAddress;

    private String village;
    private String taluka;
    private String district;

    @NotNull(message = "Please select a payment method / पेमेंट पद्धत निवडा")
    private PaymentMethod paymentMethod;

    private String notes;
    private String couponCode;
    private String upiTransactionId;

    public CheckoutDto() {}

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

    public String getDeliveryAddress() {
        return deliveryAddress;
    }

    public void setDeliveryAddress(String deliveryAddress) {
        this.deliveryAddress = deliveryAddress;
    }

    public String getVillage() {
        return village;
    }

    public void setVillage(String village) {
        this.village = village;
    }

    public String getTaluka() {
        return taluka;
    }

    public void setTaluka(String taluka) {
        this.taluka = taluka;
    }

    public String getDistrict() {
        return district;
    }

    public void setDistrict(String district) {
        this.district = district;
    }

    public PaymentMethod getPaymentMethod() {
        return paymentMethod;
    }

    public void setPaymentMethod(PaymentMethod paymentMethod) {
        this.paymentMethod = paymentMethod;
    }

    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }

    public String getCouponCode() {
        return couponCode;
    }

    public void setCouponCode(String couponCode) {
        this.couponCode = couponCode;
    }

    public String getUpiTransactionId() {
        return upiTransactionId;
    }

    public void setUpiTransactionId(String upiTransactionId) {
        this.upiTransactionId = upiTransactionId;
    }
}
