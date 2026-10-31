package com.krushisevakendra.controller;

import com.krushisevakendra.dto.ApiResponse;
import com.krushisevakendra.dto.FertilizerCalcDto;
import com.krushisevakendra.dto.PublicProductDto;
import com.krushisevakendra.dto.ReminderDto;
import com.krushisevakendra.dto.UserRegistrationDto;
import com.krushisevakendra.entity.Category;
import com.krushisevakendra.entity.Product;
import com.krushisevakendra.entity.Udhari;
import com.krushisevakendra.entity.User;
import com.krushisevakendra.enums.UdhariStatus;
import com.krushisevakendra.repository.UdhariRepository;
import com.krushisevakendra.repository.UserRepository;
import com.krushisevakendra.security.CustomUserDetails;
import com.krushisevakendra.service.*;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.*;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.*;

@CrossOrigin(origins = "*", allowedHeaders = "*")
@RestController
@RequestMapping("/api")
public class ApiController {

    private final ProductService productService;
    private final CategoryService categoryService;
    private final FarmingService farmingService;
    private final NotificationService notificationService;
    private final UserService userService;
    private final UdhariService udhariService;
    private final OrderService orderService;
    private final UserRepository userRepository;
    private final UdhariRepository udhariRepository;
    private final PasswordEncoder passwordEncoder;

    public ApiController(ProductService productService,
                         CategoryService categoryService,
                         FarmingService farmingService,
                         NotificationService notificationService,
                         UserService userService,
                         UdhariService udhariService,
                         OrderService orderService,
                         UserRepository userRepository,
                         UdhariRepository udhariRepository,
                         PasswordEncoder passwordEncoder) {
        this.productService = productService;
        this.categoryService = categoryService;
        this.farmingService = farmingService;
        this.notificationService = notificationService;
        this.userService = userService;
        this.udhariService = udhariService;
        this.orderService = orderService;
        this.userRepository = userRepository;
        this.udhariRepository = udhariRepository;
        this.passwordEncoder = passwordEncoder;
    }

    private HttpHeaders noCacheHeaders() {
        HttpHeaders headers = new HttpHeaders();
        headers.set(HttpHeaders.CACHE_CONTROL, "no-cache, no-store, must-revalidate");
        headers.set(HttpHeaders.PRAGMA, "no-cache");
        headers.set(HttpHeaders.EXPIRES, "0");
        return headers;
    }

    // --- 1. User Registration & Auth Endpoints ---

    @PostMapping("/auth/register")
    public ResponseEntity<ApiResponse<Map<String, Object>>> registerFarmer(@RequestBody Map<String, String> payload) {
        try {
            String name = payload.getOrDefault("name", "").trim();
            String mobile = payload.getOrDefault("mobile", "").trim();
            String email = payload.getOrDefault("email", "").trim();
            String password = payload.getOrDefault("password", "");
            String address = payload.getOrDefault("address", "Farm Address");
            String village = payload.getOrDefault("village", "Vaijapur");
            String taluka = payload.getOrDefault("taluka", "Vaijapur");
            String district = payload.getOrDefault("district", "Chhatrapati Sambhajinagar");

            if (mobile.isEmpty() || password.isEmpty()) {
                return ResponseEntity.badRequest().headers(noCacheHeaders())
                        .body(ApiResponse.error("Mobile and password are required."));
            }

            if (email.isEmpty()) {
                email = mobile + "@krushiseva.local";
            }

            if (name.isEmpty()) {
                name = "Farmer " + mobile;
            }

            UserRegistrationDto dto = new UserRegistrationDto();
            dto.setName(name);
            dto.setMobile(mobile);
            dto.setEmail(email);
            dto.setAddress(address.isEmpty() ? "Farm Location" : address);
            dto.setVillage(village.isEmpty() ? "Vaijapur" : village);
            dto.setTaluka(taluka.isEmpty() ? "Vaijapur" : taluka);
            dto.setDistrict(district.isEmpty() ? "Chhatrapati Sambhajinagar" : district);
            dto.setPassword(password);
            dto.setConfirmPassword(password);

            User savedUser = userService.registerCustomer(dto);

            Map<String, Object> resp = new HashMap<>();
            resp.put("id", savedUser.getId());
            resp.put("farmerId", "KSK-" + savedUser.getMobile());
            resp.put("name", savedUser.getName());
            resp.put("mobile", savedUser.getMobile());
            resp.put("email", savedUser.getEmail());
            resp.put("village", savedUser.getVillage());
            resp.put("status", savedUser.getStatus());
            resp.put("role", "ROLE_CUSTOMER");

            return ResponseEntity.status(HttpStatus.CREATED).headers(noCacheHeaders())
                    .body(ApiResponse.ok("Farmer registered successfully", resp));
        } catch (IllegalArgumentException e) {
            return ResponseEntity.status(HttpStatus.CONFLICT).headers(noCacheHeaders())
                    .body(ApiResponse.error(e.getMessage()));
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).headers(noCacheHeaders())
                    .body(ApiResponse.error("Registration failed: " + e.getMessage()));
        }
    }

    @PostMapping("/auth/login")
    public ResponseEntity<ApiResponse<Map<String, Object>>> loginFarmer(@RequestBody Map<String, String> payload) {
        String username = payload.getOrDefault("username", "").trim();
        String password = payload.getOrDefault("password", "");

        Optional<User> userOpt = userRepository.findByEmailOrMobile(username);
        if (userOpt.isPresent()) {
            User u = userOpt.get();
            if (passwordEncoder.matches(password, u.getPasswordHash())) {
                boolean isAdmin = u.getRoles().stream().anyMatch(r -> r.getName().name().equals("ROLE_ADMIN"));
                Map<String, Object> data = new HashMap<>();
                data.put("id", u.getId());
                data.put("farmerId", "KSK-" + u.getMobile());
                data.put("name", u.getName());
                data.put("mobile", u.getMobile());
                data.put("role", isAdmin ? "admin" : "customer");
                data.put("village", u.getVillage());
                return ResponseEntity.ok().headers(noCacheHeaders())
                        .body(ApiResponse.ok("Login successful", data));
            }
        }
        return ResponseEntity.status(HttpStatus.UNAUTHORIZED).headers(noCacheHeaders())
                .body(ApiResponse.error("Invalid credentials"));
    }

    // --- 2. Admin Dashboard Stats & Customer Directory ---

    @GetMapping("/admin/stats")
    public ResponseEntity<ApiResponse<Map<String, Object>>> getAdminStats() {
        long totalUsers = userService.getCustomerCount();
        long totalProducts = productService.getTotalProductCount();
        long totalOrders = orderService.getTotalOrderCount();
        BigDecimal totalSales = orderService.getTotalSales();
        BigDecimal remainingUdhari = udhariService.getTotalRemainingUdhari();

        Map<String, Object> stats = new HashMap<>();
        stats.put("totalUsers", totalUsers);
        stats.put("totalProducts", totalProducts);
        stats.put("totalOrders", totalOrders);
        stats.put("totalSales", totalSales != null ? totalSales : BigDecimal.ZERO);
        stats.put("totalRemainingUdhari", remainingUdhari != null ? remainingUdhari : BigDecimal.ZERO);

        return ResponseEntity.ok().headers(noCacheHeaders())
                .body(ApiResponse.ok("Admin stats fetched", stats));
    }

    @GetMapping("/admin/customers")
    public ResponseEntity<ApiResponse<List<Map<String, Object>>>> getAdminCustomers() {
        List<User> customers = userService.getAllCustomers();
        List<Map<String, Object>> result = new ArrayList<>();
        for (User u : customers) {
            Map<String, Object> item = new HashMap<>();
            item.put("id", u.getId());
            item.put("farmerId", "KSK-" + u.getMobile());
            item.put("name", u.getName());
            item.put("mobile", u.getMobile());
            item.put("email", u.getEmail());
            item.put("village", u.getVillage());
            item.put("taluka", u.getTaluka());
            item.put("status", u.getStatus());
            item.put("createdAt", u.getCreatedAt());
            result.add(item);
        }
        return ResponseEntity.ok().headers(noCacheHeaders())
                .body(ApiResponse.ok("Customers fetched", result));
    }

    // --- 3. Credit Ledger (Udhari) Sync Endpoints ---

    @PostMapping("/admin/udhari/add")
    public ResponseEntity<ApiResponse<Map<String, Object>>> addUdhariTransaction(@RequestBody Map<String, Object> payload) {
        try {
            String name = (String) payload.getOrDefault("name", "Farmer");
            String mobile = (String) payload.getOrDefault("mobile", "");
            String village = (String) payload.getOrDefault("village", "Vaijapur");
            String notes = (String) payload.getOrDefault("notes", "Store purchase");
            String dueDateStr = (String) payload.getOrDefault("dueDate", LocalDate.now().plusDays(30).toString());

            BigDecimal amount = BigDecimal.ZERO;
            Object amtObj = payload.get("amount");
            if (amtObj instanceof Number) {
                amount = BigDecimal.valueOf(((Number) amtObj).doubleValue());
            } else if (amtObj instanceof String) {
                amount = new BigDecimal((String) amtObj);
            }

            // Find or associate user
            User user = null;
            if (mobile != null && !mobile.isBlank()) {
                user = userRepository.findByMobile(mobile.trim()).orElse(null);
            }
            if (user == null && name != null && !name.isBlank()) {
                List<User> found = userRepository.findAllCustomers();
                user = found.stream()
                        .filter(u -> u.getName().equalsIgnoreCase(name.trim()))
                        .findFirst()
                        .orElse(null);
            }

            // If user doesn't exist yet in DB, create one so Udhari is permanently linked
            if (user == null) {
                String safeMobile = (mobile != null && !mobile.isBlank()) ? mobile.trim() : "98" + (System.currentTimeMillis() % 100000000L);
                String safeEmail = safeMobile + "@krushiseva.local";
                UserRegistrationDto newDto = new UserRegistrationDto();
                newDto.setName(name != null && !name.isBlank() ? name.trim() : "Farmer " + safeMobile);
                newDto.setMobile(safeMobile);
                newDto.setEmail(safeEmail);
                newDto.setAddress(village);
                newDto.setVillage(village);
                newDto.setTaluka("Vaijapur");
                newDto.setDistrict("Chhatrapati Sambhajinagar");
                newDto.setPassword("farmer123");
                newDto.setConfirmPassword("farmer123");
                user = userService.registerCustomer(newDto);
            }

            LocalDate dueDate = LocalDate.now().plusDays(30);
            try {
                if (dueDateStr != null && !dueDateStr.isBlank()) {
                    dueDate = LocalDate.parse(dueDateStr);
                }
            } catch (Exception ignored) {}

            Udhari record = new Udhari();
            record.setUser(user);
            record.setTotalAmount(amount);
            record.setPaidAmount(BigDecimal.ZERO);
            record.setRemainingAmount(amount);
            record.setDueDate(dueDate);
            record.setStatus(UdhariStatus.ACTIVE);
            record.setNotes(notes);
            record.setCreatedAt(LocalDateTime.now());
            record.setUpdatedAt(LocalDateTime.now());

            Udhari saved = udhariRepository.save(record);

            Map<String, Object> resp = new HashMap<>();
            resp.put("id", saved.getId());
            resp.put("farmerId", "KSK-" + user.getMobile());
            resp.put("name", user.getName());
            resp.put("mobile", user.getMobile());
            resp.put("village", user.getVillage());
            resp.put("amount", saved.getTotalAmount());
            resp.put("remainingAmount", saved.getRemainingAmount());
            resp.put("dueDate", saved.getDueDate().toString());
            resp.put("notes", saved.getNotes());
            resp.put("status", saved.getStatus().name());

            return ResponseEntity.status(HttpStatus.CREATED).headers(noCacheHeaders())
                    .body(ApiResponse.ok("Udhari transaction recorded", resp));
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).headers(noCacheHeaders())
                    .body(ApiResponse.error("Failed to add udhari: " + e.getMessage()));
        }
    }

    @GetMapping({"/ledger/{identifier}", "/farmer/credit-ledger", "/farmer/ledger"})
    public ResponseEntity<ApiResponse<Map<String, Object>>> getFarmerLedger(
            @PathVariable(required = false) String identifier,
            @RequestParam(required = false) String farmerId,
            @RequestParam(required = false) String mobile,
            @RequestParam(required = false) String name) {

        String lookup = identifier;
        if (lookup == null || lookup.isBlank() || "{identifier}".equals(lookup)) {
            lookup = farmerId != null ? farmerId : (mobile != null ? mobile : name);
        }

        // Try authenticated context if no param
        if (lookup == null || lookup.isBlank()) {
            Authentication auth = SecurityContextHolder.getContext().getAuthentication();
            if (auth != null && auth.getPrincipal() instanceof CustomUserDetails userDetails) {
                lookup = userDetails.getUser().getMobile();
            }
        }

        User farmer = null;
        if (lookup != null && !lookup.isBlank()) {
            String clean = lookup.replace("KSK-", "").trim();
            farmer = userRepository.findByMobile(clean).orElse(null);
            if (farmer == null) {
                farmer = userRepository.findByEmail(lookup).orElse(null);
            }
            if (farmer == null) {
                String search = lookup.toLowerCase();
                List<User> list = userRepository.findAllCustomers();
                farmer = list.stream()
                        .filter(u -> u.getName().toLowerCase().contains(search) || search.contains(u.getName().toLowerCase()))
                        .findFirst()
                        .orElse(null);
            }
        }

        if (farmer == null) {
            Map<String, Object> emptyResp = new HashMap<>();
            emptyResp.put("farmerId", lookup != null ? lookup : "KSK-UNKNOWN");
            emptyResp.put("totalCredit", BigDecimal.ZERO);
            emptyResp.put("totalPaid", BigDecimal.ZERO);
            emptyResp.put("pendingDue", BigDecimal.ZERO);
            emptyResp.put("transactions", Collections.emptyList());
            return ResponseEntity.ok().headers(noCacheHeaders()).body(ApiResponse.ok("No records found", emptyResp));
        }

        List<Udhari> userUdhari = udhariRepository.findByUserIdOrderByCreatedAtDesc(farmer.getId());
        BigDecimal totalCredit = BigDecimal.ZERO;
        BigDecimal totalPaid = BigDecimal.ZERO;
        List<Map<String, Object>> txns = new ArrayList<>();

        for (Udhari u : userUdhari) {
            if (u.getTotalAmount() != null) totalCredit = totalCredit.add(u.getTotalAmount());
            if (u.getPaidAmount() != null) totalPaid = totalPaid.add(u.getPaidAmount());

            Map<String, Object> t = new HashMap<>();
            t.put("id", u.getId());
            t.put("date", u.getCreatedAt() != null ? u.getCreatedAt().toLocalDate().toString() : LocalDate.now().toString());
            t.put("notes", u.getNotes() != null ? u.getNotes() : "कृषी माल उधारी खरेदी");
            t.put("debit", u.getTotalAmount());
            t.put("credit", u.getPaidAmount());
            t.put("balance", u.getRemainingAmount());
            t.put("status", u.getStatus().name());
            t.put("dueDate", u.getDueDate() != null ? u.getDueDate().toString() : null);
            txns.add(t);
        }

        BigDecimal pendingDue = totalCredit.subtract(totalPaid).max(BigDecimal.ZERO);

        Map<String, Object> data = new HashMap<>();
        data.put("farmerId", "KSK-" + farmer.getMobile());
        data.put("farmerName", farmer.getName());
        data.put("mobile", farmer.getMobile());
        data.put("totalCredit", totalCredit);
        data.put("totalPaid", totalPaid);
        data.put("pendingDue", pendingDue);
        data.put("transactions", txns);

        return ResponseEntity.ok().headers(noCacheHeaders()).body(ApiResponse.ok("Credit ledger fetched", data));
    }

    // --- 4. Product & Farming Public Endpoints ---

    @GetMapping("/products")
    public ResponseEntity<ApiResponse<List<PublicProductDto>>> getAllProducts() {
        List<PublicProductDto> products = productService.getAllActiveProducts().stream()
                .map(PublicProductDto::from)
                .toList();
        return ResponseEntity.ok().headers(noCacheHeaders()).body(ApiResponse.ok("Products fetched", products));
    }

    @GetMapping("/products/{id}")
    public ResponseEntity<ApiResponse<PublicProductDto>> getProductById(@PathVariable Long id) {
        return productService.getActiveProductById(id)
                .map(PublicProductDto::from)
                .map(p -> ResponseEntity.ok().headers(noCacheHeaders()).body(ApiResponse.ok("Product found", p)))
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping("/products/barcode/{barcode}")
    public ResponseEntity<ApiResponse<Product>> getProductByBarcode(@PathVariable String barcode) {
        return productService.getProductByBarcode(barcode)
                .map(p -> ResponseEntity.ok().headers(noCacheHeaders()).body(ApiResponse.ok("Product found by barcode", p)))
                .orElse(ResponseEntity.notFound().build());
    }

    @GetMapping("/products/search")
    public ResponseEntity<ApiResponse<List<PublicProductDto>>> searchProducts(@RequestParam String q) {
        Page<Product> page = productService.searchAndFilter(null, null, null, null, false, q, PageRequest.of(0, 8));
        List<PublicProductDto> products = page.getContent().stream()
                .map(PublicProductDto::from)
                .toList();
        return ResponseEntity.ok().headers(noCacheHeaders()).body(ApiResponse.ok("Search results", products));
    }

    @GetMapping("/categories")
    public ResponseEntity<ApiResponse<List<Category>>> getCategories() {
        return ResponseEntity.ok().headers(noCacheHeaders()).body(ApiResponse.ok("Active categories", categoryService.getAllActiveCategories()));
    }

    @GetMapping("/farming/weather")
    public ResponseEntity<ApiResponse<Map<String, Object>>> getWeather(@RequestParam(defaultValue = "Sangli") String city) {
        return ResponseEntity.ok().headers(noCacheHeaders()).body(ApiResponse.ok("Weather forecast", farmingService.getWeatherForecast(city)));
    }

    @GetMapping("/farming/fertilizer-calc")
    public ResponseEntity<ApiResponse<FertilizerCalcDto>> calculateFertilizer(
            @RequestParam(defaultValue = "sugarcane") String crop,
            @RequestParam(defaultValue = "1.0") Double acres,
            @RequestParam(defaultValue = "Medium Black") String soilType,
            @RequestParam(defaultValue = "Full Season") String stage) {
        return ResponseEntity.ok().headers(noCacheHeaders()).body(ApiResponse.ok("Calculation result", farmingService.calculateFertilizer(crop, acres, soilType, stage)));
    }

    @PostMapping("/admin/reminders/send")
    public ResponseEntity<ApiResponse<String>> sendReminder(@RequestBody ReminderDto reminderDto) {
        try {
            notificationService.sendReminder(reminderDto);
            return ResponseEntity.ok().headers(noCacheHeaders()).body(ApiResponse.ok("Reminder recorded successfully."));
        } catch (UnsupportedOperationException exception) {
            return ResponseEntity.status(HttpStatus.SERVICE_UNAVAILABLE).headers(noCacheHeaders())
                    .body(ApiResponse.error(exception.getMessage()));
        }
    }
}
