package com.krushisevakendra.controller;

import com.krushisevakendra.dto.ApiResponse;
import com.krushisevakendra.dto.FertilizerCalcDto;
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
    public ResponseEntity<ApiResponse<List<Product>>> getAllProducts() {
        return ResponseEntity.ok(ApiResponse.ok("Products fetched", productService.getAllActiveProducts()));
    }

    @GetMapping("/products/{id}")
    public ResponseEntity<ApiResponse<Product>> getProductById(@PathVariable Long id) {
        return productService.getProductById(id)
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
    public ResponseEntity<ApiResponse<List<Product>>> searchProducts(@RequestParam String q) {
        Page<Product> page = productService.searchAndFilter(null, null, null, null, false, q, PageRequest.of(0, 8));
        return ResponseEntity.ok(ApiResponse.ok("Search results", page.getContent()));
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
        boolean sent = notificationService.sendReminder(reminderDto);
        if (sent) {
            return ResponseEntity.ok(ApiResponse.ok("Reminder dispatched successfully"));
        } else {
            return ResponseEntity.badRequest().body(ApiResponse.error("Failed to send reminder"));
        }
    }
}
