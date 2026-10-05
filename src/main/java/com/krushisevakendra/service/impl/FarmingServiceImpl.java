package com.krushisevakendra.service.impl;

import com.krushisevakendra.dto.FertilizerCalcDto;
import com.krushisevakendra.service.FarmingService;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.*;

@Service
public class FarmingServiceImpl implements FarmingService {

    @Override
    public FertilizerCalcDto calculateFertilizer(String crop, Double acres, String soilType, String stage) {
        if (acres == null || acres <= 0) acres = 1.0;
        if (crop == null || crop.isBlank()) crop = "sugarcane";

        FertilizerCalcDto dto = new FertilizerCalcDto();
        dto.setCrop(crop);
        dto.setFarmAreaAcres(acres);
        dto.setSoilType(soilType != null ? soilType : "Medium Black");
        dto.setCropStage(stage != null ? stage : "Full Season");

        // Base recommended N-P-K per acre in kg (Standard agronomic guidelines)
        double nPerAcre = 100.0;
        double pPerAcre = 50.0;
        double kPerAcre = 50.0;
        String complexName = "Mahadhan 24:24:0 NPK";

        List<String> schedule = new ArrayList<>();
        List<String> micronutrients = new ArrayList<>();

        switch (crop.toLowerCase()) {
            case "sugarcane", "ऊस" -> {
                nPerAcre = 160.0;
                pPerAcre = 68.0;
                kPerAcre = 68.0;
                complexName = "Coromandel Gromor 10:26:26 (50 Kg)";
                schedule.add("Basal Dose (लागवड वेळ): 10% N, 50% P, 50% K (NPK 10:26:26 + Neem Cake)");
                schedule.add("Tillering Stage (६-८ आठवडे): 40% N (Urea split in 2 applications)");
                schedule.add("Grand Growth / Earthing Up (मोठी बांधणी): 40% N, 50% P, 50% K");
                schedule.add("Maturity (पक्वता): Stop Nitrogen, light irrigation");
                micronutrients.add("Ferrous Sulphate (हिरकास) - 10 kg/acre for chlorosis control");
                micronutrients.add("Zinc Sulphate (झिंक) - 10 kg/acre during earthing up");
            }
            case "cotton", "कापूस" -> {
                nPerAcre = 60.0;
                pPerAcre = 30.0;
                kPerAcre = 30.0;
                complexName = "Mahadhan 24:24:0 Complex (50 Kg)";
                schedule.add("Basal Dose (पेरणीच्या वेळी): 20% N + Full P + Full K (Mahadhan 24:24:0 + MOP)");
                schedule.add("Square / Branching (३०-३५ दिवस): 40% N (Urea)");
                schedule.add("Flowering & Boll formation (६०-७० दिवस): 40% N (Urea) + 13:00:45 spray");
                micronutrients.add("Magnesium Sulphate - 10 kg/acre (prevents leaf reddening / लाल्या रोग)");
                micronutrients.add("Boron (20%) - 200g/acre foliar spray during flowering");
            }
            case "soybean", "सोयाबीन" -> {
                nPerAcre = 12.0; // Legume crop fixes atmospheric N
                pPerAcre = 30.0;
                kPerAcre = 16.0;
                complexName = "Single Super Phosphate (SSP 50 Kg)";
                schedule.add("Basal Dose (पेरणीच्या वेळी): 100% N, P, K through SSP + DAP/Urea + MOP");
                schedule.add("Flowering Stage (३०-३५ दिवस): 19:19:19 water soluble spray (5g/L)");
                schedule.add("Pod Filling (५०-५५ दिवस): 00:52:34 + Micronutrient spray");
                micronutrients.add("Sulphur 90% WG / Powder - 10 kg/acre (crucial for soybean oil content)");
                micronutrients.add("Rhizobium & PSB Bio-fertilizer seed treatment before sowing");
            }
            case "wheat", "गहू" -> {
                nPerAcre = 48.0;
                pPerAcre = 24.0;
                kPerAcre = 16.0;
                complexName = "IFFCO 12:32:16 Complex (50 Kg)";
                schedule.add("Basal (पेरणी): 50% N + Full P + Full K");
                schedule.add("Crown Root Initiation (२१ दिवस): 50% N (Urea top dress after first irrigation)");
                micronutrients.add("Zinc Sulphate 21% - 10 kg/acre in deficient soils");
            }
            case "onion", "कांदा" -> {
                nPerAcre = 40.0;
                pPerAcre = 20.0;
                kPerAcre = 25.0;
                complexName = "Coromandel 10:26:26 (50 Kg)";
                schedule.add("Basal (पुनर्लागवड): 33% N + Full P + 50% K");
                schedule.add("Vegetative Growth (३० दिवस): 33% N (Urea)");
                schedule.add("Bulb Development (४५-५० दिवस): 34% N + 50% K (MOP + 00:00:50 spray)");
                micronutrients.add("Bensulf / Sulphur 90% - 10 kg/acre (improves pungency & storage life)");
            }
            default -> { // Vegetables / General
                nPerAcre = 50.0;
                pPerAcre = 25.0;
                kPerAcre = 25.0;
                complexName = "Mahadhan 24:24:0 NPK (50 Kg)";
                schedule.add("Basal: 40% N + Full P + Full K");
                schedule.add("Vegetative & Fruit set: Split remaining N in 2 doses");
                micronutrients.add("Grade 2 Micronutrient liquid spray @ 2.5 ml/L");
            }
        }

        // Adjust for soil type
        if ("Light / Sandy Soil".equalsIgnoreCase(soilType)) {
            nPerAcre *= 1.15; // Light soils leach N faster
            kPerAcre *= 1.10;
        } else if ("Heavy Black Clay".equalsIgnoreCase(soilType)) {
            pPerAcre *= 1.10; // High P-fixation in clay
        }

        double totalN = nPerAcre * acres;
        double totalP = pPerAcre * acres;
        double totalK = kPerAcre * acres;

        dto.setRequiredN(round(totalN));
        dto.setRequiredP(round(totalP));
        dto.setRequiredK(round(totalK));

        // Calculation Method 1: Straight Fertilizers
        // Urea (46% N, 45kg bag = 20.7 kg N/bag)
        double ureaBags = totalN / 20.7;
        // SSP (16% P2O5, 50kg bag = 8.0 kg P/bag)
        double sspBags = totalP / 8.0;
        // MOP (60% K2O, 50kg bag = 30.0 kg K/bag)
        double mopBags = totalK / 30.0;

        dto.setUreaBags(round(ureaBags));
        dto.setSspBags(round(sspBags));
        dto.setMopBags(round(mopBags));

        // Calculation Method 2: Complex Fertilizer Strategy
        dto.setComplexFertilizerName(complexName);
        double complexBags = totalP / 13.0; // average 50kg bag P contribution
        double nFromComplex = complexBags * 5.0;
        double kFromComplex = complexBags * 13.0;
        double remainingN = Math.max(0, totalN - nFromComplex);
        double remainingK = Math.max(0, totalK - kFromComplex);

        dto.setComplexBags(round(complexBags));
        dto.setSupplementaryUreaBags(round(remainingN / 20.7));
        dto.setSupplementaryMopBags(round(remainingK / 30.0));

        // Estimated cost (approx: Urea ~₹266/bag, SSP ~₹450/bag, MOP ~₹1700/bag, Complex ~₹1750/bag)
        double cost = (dto.getComplexBags() * 1750.0) + 
                      (dto.getSupplementaryUreaBags() * 266.50) + 
                      (dto.getSupplementaryMopBags() * 1700.0);
        dto.setEstimatedTotalCost(BigDecimal.valueOf(cost).setScale(2, RoundingMode.HALF_UP));

        dto.setApplicationSchedule(schedule);
        dto.setMicronutrientAdvice(micronutrients);

        return dto;
    }

    @Override
    public Map<String, Object> getWeatherForecast(String city) {
        if (city == null || city.isBlank()) city = "Sangli";

        Map<String, Object> weather = new LinkedHashMap<>();
        weather.put("city", city);
        weather.put("temperature", "28°C");
        weather.put("condition", "Partly Cloudy / अंशतः ढगाळ");
        weather.put("humidity", "74%");
        weather.put("windSpeed", "14 km/h");
        weather.put("rainChance", "30% (Light showers expected in evening)");
        weather.put("forecastDays", Arrays.asList(
                Map.of("day", "Today", "dayMr", "आज", "temp", "28°C", "icon", "bi-cloud-sun", "rain", "30%"),
                Map.of("day", "Tomorrow", "dayMr", "उद्या", "temp", "29°C", "icon", "bi-cloud-rain", "rain", "65%"),
                Map.of("day", "Thursday", "dayMr", "गुरुवार", "temp", "27°C", "icon", "bi-cloud-lightning-rain", "rain", "80%"),
                Map.of("day", "Friday", "dayMr", "शुक्रवार", "temp", "30°C", "icon", "bi-sun", "rain", "15%"),
                Map.of("day", "Saturday", "dayMr", "शनिवार", "temp", "31°C", "icon", "bi-sun", "rain", "10%")
        ));
        weather.put("agriAdvisory", "Favorable conditions for foliar sprays until afternoon. Ensure drainage channels in heavy soil fields before upcoming showers.");
        weather.put("agriAdvisoryMr", "दुपारपर्यंत कीटकनाशक फवारणीसाठी हवामान अनुकूल राहील. आगामी पावसाच्या अंदाजामुळे शेतातील पाण्याचा निचरा व्यवस्था तपासावी.");
        return weather;
    }

    @Override
    public List<Map<String, Object>> getCropCareTips() {
        return List.of(
                Map.of(
                        "crop", "Sugarcane (ऊस)",
                        "title", "Earthing-up & Micronutrient Drenching",
                        "titleMr", "मोठी बांधणी व सूक्ष्मअन्नद्रव्ये व्यवस्थापन",
                        "description", "Perform earthing up between 120-130 days to prevent lodging. Apply Ferrous + Zinc sulphate along with FYM around root zones.",
                        "descriptionMr", "ऊस लोळू नये म्हणून १२० ते १३० दिवसांत मोठी बांधणी करा. मुळांजवळ शेणखतासोबत फेरस व झिंक सल्फेट द्यावे."
                ),
                Map.of(
                        "crop", "Cotton (कापूस)",
                        "title", "Pink Bollworm Pheromone Traps",
                        "titleMr", "गुलाबी बोंडअळी कामगंध सापळे",
                        "description", "Install 5-8 pheromone traps per acre at 45 days after sowing to monitor and disrupt male moth population.",
                        "descriptionMr", "कापूस पेरणीनंतर ४५ दिवसांनी एकरी ५ ते ८ कामगंध सापळे लावावेत जेणेकरून बोंडअळीचा प्रादुर्भाव वेळीच रोखता येईल."
                ),
                Map.of(
                        "crop", "Soybean (सोयाबीन)",
                        "title", "Girdle Beetle & Semilooper Management",
                        "titleMr", "चक्रीभुंगा आणि उंटअळी नियंत्रण",
                        "description", "Spray Ampligo @ 80 ml/acre or Coragen @ 60 ml/acre when early girdle beetle ring-cuts appear on stems.",
                        "descriptionMr", "चक्रीभुंग्याचे कट दिसताच अँप्लिगो ८० मिली किंवा कोराजन ६० मिली प्रति एकर १५० लिटर पाण्यातून फवारणी करावी."
                ),
                Map.of(
                        "crop", "Grapes & Pomegranate (द्राक्ष आणि डाळिंब)",
                        "title", "Canopy Management & Drip Fertigation",
                        "titleMr", "कॅनोपी व्यवस्थापन व ठिबक फर्टीगेशन",
                        "description", "Maintain leaf area index and deliver 00:52:34 with Magnesium through drip system during flowering to maximize fruit set.",
                        "descriptionMr", "फुलोरा अवस्थेत ००:५२:३४ आणि मॅग्नेशियम सल्फेट ठिबकद्वारे द्यावे जेणेकरून फुलांची गळ थांबून सेटिंग चांगली होईल."
                )
        );
    }

    @Override
    public List<Map<String, Object>> getPestManagementTips() {
        return List.of(
                Map.of(
                        "pestName", "Fall Armyworm / लष्करी अळी (Spodoptera)",
                        "affectedCrops", "Maize, Sugarcane, Sorghum",
                        "symptoms", "Pin-holes on whorl leaves, extensive ragged feeding with sawdust-like frass.",
                        "chemicalControl", "Spray Emamectin Benzoate 5% SG @ 0.5g/L or Ampligo @ 0.5ml/L targeting leaf whorls.",
                        "organicControl", "Apply Neem oil (10,000 ppm) @ 2ml/L + Metarhizium anisopliae bio-insecticide."
                ),
                Map.of(
                        "pestName", "Thrips & Sucking Pests / थ्रिप्स व तुडतुडे",
                        "affectedCrops", "Cotton, Onion, Chilli, Grapes",
                        "symptoms", "Curling of leaves, silver patches on leaf undersides, stunted shoot growth.",
                        "chemicalControl", "Spray Dimethoate 30% EC (Rogor) @ 1.5ml/L or Acetamiprid 20% SP @ 0.5g/L.",
                        "organicControl", "Install Blue and Yellow sticky traps @ 20/acre + spray Dashparni Ark @ 5ml/L."
                ),
                Map.of(
                        "pestName", "Downy Mildew & Fungal Blight / करपा व भुरी रोग",
                        "affectedCrops", "Grapes, Tomato, Soybean, Pomegranate",
                        "symptoms", "Yellowish-brown angular spots on foliage, white fungal growth under leaf surface.",
                        "chemicalControl", "Spray Metalaxyl + Mancozeb @ 2.5g/L or Azoxystrobin @ 1ml/L.",
                        "organicControl", "Trichoderma viride bio-fungicide @ 5g/L preventive spray."
                )
        );
    }

    @Override
    public List<Map<String, Object>> getCropRecommendations(String soilType, String season, String waterAvailability) {
        List<Map<String, Object>> list = new ArrayList<>();
        list.add(Map.of(
                "crop", "Soybean (सोयाबीन)",
                "suitability", "Highly Recommended (उत्कृष्ट)",
                "duration", "95 - 105 Days",
                "profitMargin", "₹35,000 - ₹45,000 / Acre",
                "recommendedVariety", "JS 335, Phule Sangam (KDS 726)",
                "seedRate", "25 - 30 Kg / Acre"
        ));
        list.add(Map.of(
                "crop", "Sugarcane (ऊस - अडसाली/सुरू)",
                "suitability", "High Yielding (शाश्वत नफा)",
                "duration", "12 - 15 Months",
                "profitMargin", "₹90,000 - ₹1,30,000 / Acre",
                "recommendedVariety", "Co 86032 (Nira), CoM 0265 (Phule 265)",
                "seedRate", "25,000 - 30,000 eye buds / Acre"
        ));
        list.add(Map.of(
                "crop", "Cotton (कापूस - बीजी II)",
                "suitability", "Recommended for well-drained soils",
                "duration", "150 - 180 Days",
                "profitMargin", "₹40,000 - ₹60,000 / Acre",
                "recommendedVariety", "Mahyco Bollgard II, Ajit 155",
                "seedRate", "2 Packets (950g) / Acre"
        ));
        return list;
    }

    private double round(double val) {
        return Math.round(val * 100.0) / 100.0;
    }
}
