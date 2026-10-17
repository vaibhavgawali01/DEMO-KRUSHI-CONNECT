package com.krushisevakendra.service.impl;

import com.krushisevakendra.dto.FertilizerCalcDto;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatIllegalArgumentException;

class FarmingServiceImplTest {

    private final FarmingServiceImpl farmingService = new FarmingServiceImpl();

    @Test
    void calculatesSugarcaneRecommendationForOneAcre() {
        FertilizerCalcDto result = farmingService.calculateFertilizer(
                "sugarcane", 1.0, "Medium Black", "Full Season");

        assertThat(result.getRequiredN()).isEqualTo(160.0);
        assertThat(result.getRequiredP()).isEqualTo(68.0);
        assertThat(result.getRequiredK()).isEqualTo(68.0);
        assertThat(result.getApplicationSchedule()).hasSize(4);
        assertThat(result.getEstimatedTotalCost()).isNotNegative();
    }

    @Test
    void scalesRecommendationByFarmAreaAndSoilType() {
        FertilizerCalcDto mediumSoil = farmingService.calculateFertilizer(
                "cotton", 2.0, "Medium Black", "Full Season");
        FertilizerCalcDto lightSoil = farmingService.calculateFertilizer(
                "cotton", 2.0, "Light / Sandy Soil", "Full Season");

        assertThat(mediumSoil.getRequiredN()).isEqualTo(120.0);
        assertThat(mediumSoil.getRequiredP()).isEqualTo(60.0);
        assertThat(mediumSoil.getRequiredK()).isEqualTo(60.0);
        assertThat(lightSoil.getRequiredN()).isEqualTo(138.0);
        assertThat(lightSoil.getRequiredP()).isEqualTo(60.0);
        assertThat(lightSoil.getRequiredK()).isEqualTo(66.0);
    }

    @Test
    void acceptsMinimumAndMaximumSupportedAreas() {
        assertThat(farmingService.calculateFertilizer(
                "wheat", 0.25, "Medium Black", "Full Season").getFarmAreaAcres()).isEqualTo(0.25);
        assertThat(farmingService.calculateFertilizer(
                "wheat", 100.0, "Medium Black", "Full Season").getFarmAreaAcres()).isEqualTo(100.0);
    }

    @Test
    void rejectsMissingNonFiniteAndOutOfRangeAreas() {
        assertInvalidArea(null);
        assertInvalidArea(Double.NaN);
        assertInvalidArea(Double.POSITIVE_INFINITY);
        assertInvalidArea(Double.NEGATIVE_INFINITY);
        assertInvalidArea(0.0);
        assertInvalidArea(-1.0);
        assertInvalidArea(0.249);
        assertInvalidArea(100.001);
    }

    @Test
    void rejectsUnsupportedGrowthStagesInsteadOfReturningFullSeasonDose() {
        assertThatIllegalArgumentException()
                .isThrownBy(() -> farmingService.calculateFertilizer(
                        "sugarcane", 1.0, "Medium Black", "Basal Stage"))
                .withMessage("Only full-season fertilizer estimates are currently available.");
        assertThatIllegalArgumentException()
                .isThrownBy(() -> farmingService.calculateFertilizer(
                        "sugarcane", 1.0, "Medium Black", "unknown"))
                .withMessage("Only full-season fertilizer estimates are currently available.");
    }

    private void assertInvalidArea(Double acres) {
        assertThatIllegalArgumentException()
                .isThrownBy(() -> farmingService.calculateFertilizer(
                        "sugarcane", acres, "Medium Black", "Full Season"))
                .withMessage("Farm area must be between 0.25 and 100 acres.");
    }
}
