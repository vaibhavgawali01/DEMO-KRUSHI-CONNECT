package com.krushisevakendra.dto;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;

public class FertilizerCalcDto {

    private String crop;
    private Double farmAreaAcres = 1.0;
    private String soilType;
    private String cropStage;

    // Computed Recommendations
    private Double requiredN = 0.0;
    private Double requiredP = 0.0;
    private Double requiredK = 0.0;

    // Commercial Bag Recommendations (Option 1: Straight Fertilizers)
    private Double ureaBags = 0.0;
    private Double sspBags = 0.0;
    private Double mopBags = 0.0;

    // Option 2: Complex Fertilizer Alternative
    private String complexFertilizerName;
    private Double complexBags = 0.0;
    private Double supplementaryUreaBags = 0.0;
    private Double supplementaryMopBags = 0.0;

    private BigDecimal estimatedTotalCost = BigDecimal.ZERO;
    private List<String> applicationSchedule = new ArrayList<>();
    private List<String> micronutrientAdvice = new ArrayList<>();

    public FertilizerCalcDto() {}

    public String getCrop() {
        return crop;
    }

    public void setCrop(String crop) {
        this.crop = crop;
    }

    public Double getFarmAreaAcres() {
        return farmAreaAcres;
    }

    public void setFarmAreaAcres(Double farmAreaAcres) {
        this.farmAreaAcres = farmAreaAcres;
    }

    public String getSoilType() {
        return soilType;
    }

    public void setSoilType(String soilType) {
        this.soilType = soilType;
    }

    public String getCropStage() {
        return cropStage;
    }

    public void setCropStage(String cropStage) {
        this.cropStage = cropStage;
    }

    public Double getRequiredN() {
        return requiredN;
    }

    public void setRequiredN(Double requiredN) {
        this.requiredN = requiredN;
    }

    public Double getRequiredP() {
        return requiredP;
    }

    public void setRequiredP(Double requiredP) {
        this.requiredP = requiredP;
    }

    public Double getRequiredK() {
        return requiredK;
    }

    public void setRequiredK(Double requiredK) {
        this.requiredK = requiredK;
    }

    public Double getUreaBags() {
        return ureaBags;
    }

    public void setUreaBags(Double ureaBags) {
        this.ureaBags = ureaBags;
    }

    public Double getSspBags() {
        return sspBags;
    }

    public void setSspBags(Double sspBags) {
        this.sspBags = sspBags;
    }

    public Double getMopBags() {
        return mopBags;
    }

    public void setMopBags(Double mopBags) {
        this.mopBags = mopBags;
    }

    public String getComplexFertilizerName() {
        return complexFertilizerName;
    }

    public void setComplexFertilizerName(String complexFertilizerName) {
        this.complexFertilizerName = complexFertilizerName;
    }

    public Double getComplexBags() {
        return complexBags;
    }

    public void setComplexBags(Double complexBags) {
        this.complexBags = complexBags;
    }

    public Double getSupplementaryUreaBags() {
        return supplementaryUreaBags;
    }

    public void setSupplementaryUreaBags(Double supplementaryUreaBags) {
        this.supplementaryUreaBags = supplementaryUreaBags;
    }

    public Double getSupplementaryMopBags() {
        return supplementaryMopBags;
    }

    public void setSupplementaryMopBags(Double supplementaryMopBags) {
        this.supplementaryMopBags = supplementaryMopBags;
    }

    public BigDecimal getEstimatedTotalCost() {
        return estimatedTotalCost;
    }

    public void setEstimatedTotalCost(BigDecimal estimatedTotalCost) {
        this.estimatedTotalCost = estimatedTotalCost;
    }

    public List<String> getApplicationSchedule() {
        return applicationSchedule;
    }

    public void setApplicationSchedule(List<String> applicationSchedule) {
        this.applicationSchedule = applicationSchedule;
    }

    public List<String> getMicronutrientAdvice() {
        return micronutrientAdvice;
    }

    public void setMicronutrientAdvice(List<String> micronutrientAdvice) {
        this.micronutrientAdvice = micronutrientAdvice;
    }
}
