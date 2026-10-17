package com.krushisevakendra.controller;

import com.krushisevakendra.dto.ApiResponse;
import com.krushisevakendra.dto.FertilizerCalcDto;
import com.krushisevakendra.dto.PublicProductDto;
import com.krushisevakendra.dto.ReminderDto;
import com.krushisevakendra.entity.Category;
import com.krushisevakendra.entity.Product;
import com.krushisevakendra.service.CategoryService;
import com.krushisevakendra.service.FarmingService;
import com.krushisevakendra.service.NotificationService;
import com.krushisevakendra.service.ProductService;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api")
public class ApiController {

    private final ProductService productService;
    private final CategoryService categoryService;
    private final FarmingService farmingService;
    private final NotificationService notificationService;

    public ApiController(ProductService productService,
                         CategoryService categoryService,
                         FarmingService farmingService,
                         NotificationService notificationService) {
        this.productService = productService;
        this.categoryService = categoryService;
        this.farmingService = farmingService;
        this.notificationService = notificationService;
    }

    @GetMapping("/products")
    public ResponseEntity<ApiResponse<List<PublicProductDto>>> getAllProducts() {
        List<PublicProductDto> products = productService.getAllActiveProducts().stream()
                .map(PublicProductDto::from)
                .toList();
        return ResponseEntity.ok(ApiResponse.ok("Products fetched", products));
    }

    @GetMapping("/products/{id}")
    public ResponseEntity<ApiResponse<PublicProductDto>> getProductById(@PathVariable Long id) {
        return productService.getActiveProductById(id)
                .map(PublicProductDto::from)
                .map(p -> ResponseEntity.ok(ApiResponse.ok("Product found", p)))
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping("/products/barcode/{barcode}")
    public ResponseEntity<ApiResponse<Product>> getProductByBarcode(@PathVariable String barcode) {
        return productService.getProductByBarcode(barcode)
                .map(p -> ResponseEntity.ok(ApiResponse.ok("Product found by barcode", p)))
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping("/products/search")
    public ResponseEntity<ApiResponse<List<PublicProductDto>>> searchProducts(@RequestParam String q) {
        Page<Product> page = productService.searchAndFilter(null, null, null, null, false, q, PageRequest.of(0, 8));
        List<PublicProductDto> products = page.getContent().stream()
                .map(PublicProductDto::from)
                .toList();
        return ResponseEntity.ok(ApiResponse.ok("Search results", products));
    }

    @GetMapping("/categories")
    public ResponseEntity<ApiResponse<List<Category>>> getCategories() {
        return ResponseEntity.ok(ApiResponse.ok("Active categories", categoryService.getAllActiveCategories()));
    }

    @GetMapping("/farming/weather")
    public ResponseEntity<ApiResponse<Map<String, Object>>> getWeather(@RequestParam(defaultValue = "Sangli") String city) {
        return ResponseEntity.ok(ApiResponse.ok("Weather forecast", farmingService.getWeatherForecast(city)));
    }

    @GetMapping("/farming/fertilizer-calc")
    public ResponseEntity<ApiResponse<FertilizerCalcDto>> calculateFertilizer(
            @RequestParam(defaultValue = "sugarcane") String crop,
            @RequestParam(defaultValue = "1.0") Double acres,
            @RequestParam(defaultValue = "Medium Black") String soilType,
            @RequestParam(defaultValue = "Full Season") String stage) {
        return ResponseEntity.ok(ApiResponse.ok("Calculation result", farmingService.calculateFertilizer(crop, acres, soilType, stage)));
    }

    @PostMapping("/admin/reminders/send")
    public ResponseEntity<ApiResponse<String>> sendReminder(@RequestBody ReminderDto reminderDto) {
        try {
            notificationService.sendReminder(reminderDto);
            return ResponseEntity.ok(ApiResponse.ok("Reminder recorded successfully."));
        } catch (UnsupportedOperationException exception) {
            return ResponseEntity.status(HttpStatus.SERVICE_UNAVAILABLE)
                    .body(ApiResponse.error(exception.getMessage()));
        }
    }
}
