package com.krushisevakendra.service;

import com.krushisevakendra.dto.FertilizerCalcDto;

import java.util.List;
import java.util.Map;

public interface FarmingService {
    FertilizerCalcDto calculateFertilizer(String crop, Double acres, String soilType, String stage);
    Map<String, Object> getWeatherForecast(String city);
    List<Map<String, Object>> getCropCareTips();
    List<Map<String, Object>> getPestManagementTips();
    List<Map<String, Object>> getCropRecommendations(String soilType, String season, String waterAvailability);
}
