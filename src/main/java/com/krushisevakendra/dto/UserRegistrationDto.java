package com.krushisevakendra.dto;

import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Pattern;
import jakarta.validation.constraints.Size;

public class UserRegistrationDto {

    @NotBlank(message = "Full name is required / पूर्ण नाव आवश्यक आहे")
    @Size(min = 3, max = 100, message = "Name must be between 3 and 100 characters")
    private String name;

    @NotBlank(message = "Mobile number is required / मोबाईल नंबर आवश्यक आहे")
    @Pattern(regexp = "^[6-9]\\d{9}$", message = "Please enter a valid 10-digit mobile number")
    private String mobile;

    @NotBlank(message = "Email is required / ईमेल आवश्यक आहे")
    @Email(message = "Please enter a valid email address")
    private String email;

    @NotBlank(message = "Address is required / पत्ता आवश्यक आहे")
    private String address;

    @NotBlank(message = "Village is required / गाव आवश्यक आहे")
    private String village;

    @NotBlank(message = "Taluka is required / तालुका आवश्यक आहे")
    private String taluka;

    @NotBlank(message = "District is required / जिल्हा आवश्यक आहे")
    private String district;

    @NotBlank(message = "Password is required / पासवर्ड आवश्यक आहे")
    @Size(min = 6, message = "Password must be at least 6 characters")
    private String password;

    @NotBlank(message = "Please confirm your password")
    private String confirmPassword;

    public UserRegistrationDto() {}

    public boolean isPasswordMatching() {
        return password != null && password.equals(confirmPassword);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
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

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getConfirmPassword() {
        return confirmPassword;
    }

    public void setConfirmPassword(String confirmPassword) {
        this.confirmPassword = confirmPassword;
    }
}
