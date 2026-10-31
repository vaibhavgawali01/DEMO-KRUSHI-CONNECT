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
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContext;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.context.HttpSessionSecurityContextRepository;
import org.springframework.web.bind.annotation.*;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.*;

@CrossOrigin(origins = "*", allowedHeaders = "*")
@RestController
@RequestMapping("/api")
public class ApiController {

    private static final Logger log = LoggerFactory.getLogger(ApiController.class);

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
            String address = payload.getOrDefault("address", "Farm Address").trim();
            String village = payload.getOrDefault("village", "Vaijapur").trim();
            String taluka = payload.getOrDefault("taluka", "Vaijapur").trim();
            String district = payload.getOrDefault("district", "Chhatrapati Sambhajinagar").trim();

            if (mobile.isEmpty() || password.isEmpty() || name.isEmpty()) {
                return ResponseEntity.badRequest().headers(noCacheHeaders())
                        .body(ApiResponse.error("Name, mobile number, and password are required."));
            }

            if (!mobile.matches("^[0-9]{10}$")) {
                return ResponseEntity.badRequest().headers(noCacheHeaders())
                        .body(ApiResponse.error("Please enter a valid 10-digit mobile number."));
            }

            if (password.length() < 6) {
                return ResponseEntity.badRequest().headers(noCacheHeaders())
                        .body(ApiResponse.error("Password must be at least 6 characters long."));
            }

            if (email.isEmpty()) {
                email = mobile + "@krushiseva.local";
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
            log.error("Farmer registration error", e);
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).headers(noCacheHeaders())
                    .body(ApiResponse.error("Registration could not be completed. Please check your details and try again."));
        }
    }

    @PostMapping("/auth/login")
    public ResponseEntity<ApiResponse<Map<String, Object>>> loginFarmer(
            @RequestBody Map<String, String> payload,
            HttpServletRequest request,
            HttpServletResponse response) {
        String username = payload.getOrDefault("username", "").trim();
        String password = payload.getOrDefault("password", "");

        if (username.isBlank() || password.isBlank()) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).headers(noCacheHeaders())
                    .body(ApiResponse.error("Username and password are required."));
        }

        Optional<User> userOpt = userRepository.findByEmailOrMobile(username);
        if (userOpt.isPresent()) {
            User u = userOpt.get();
            if (passwordEncoder.matches(password, u.getPasswordHash())) {
                CustomUserDetails userDetails = new CustomUserDetails(u);
                UsernamePasswordAuthenticationToken authentication =
                        new UsernamePasswordAuthenticationToken(userDetails, null, userDetails.getAuthorities());
                SecurityContext context = SecurityContextHolder.createEmptyContext();
                context.setAuthentication(authentication);
                SecurityContextHolder.setContext(context);

                if (request != null) {
                    HttpSession session = request.getSession(true);
                    session.setAttribute(HttpSessionSecurityContextRepository.SPRING_SECURITY_CONTEXT_KEY, context);
                }

                boolean isAdmin = authentication.getAuthorities().stream()
                        .anyMatch(a -> "ROLE_ADMIN".equals(a.getAuthority()));

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
        Authentication auth = SecurityContextHolder.getContext().getAuthentication();
        if (auth == null || !auth.isAuthenticated() || auth.getAuthorities().stream().noneMatch(a -> "ROLE_ADMIN".equals(a.getAuthority()))) {
            return ResponseEntity.status(HttpStatus.FORBIDDEN).headers(noCacheHeaders())
                    .body(ApiResponse.error("Admin authorization required."));
        }

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
        Authentication auth = SecurityContextHolder.getContext().getAuthentication();
        if (auth == null || !auth.isAuthenticated() || auth.getAuthorities().stream().noneMatch(a -> "ROLE_ADMIN".equals(a.getAuthority()))) {
            return ResponseEntity.status(HttpStatus.FORBIDDEN).headers(noCacheHeaders())
                    .body(ApiResponse.error("Admin authorization required."));
        }

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
        Authentication auth = SecurityContextHolder.getContext().getAuthentication();
        if (auth == null || !auth.isAuthenticated() || auth.getAuthorities().stream().noneMatch(a -> "ROLE_ADMIN".equals(a.getAuthority()))) {
            return ResponseEntity.status(HttpStatus.FORBIDDEN).headers(noCacheHeaders())
                    .body(ApiResponse.error("Admin authorization required."));
        }

        try {
            String name = (String) payload.getOrDefault("name", "");
            String mobile = (String) payload.getOrDefault("mobile", "");
            String notes = (String) payload.getOrDefault("notes", "Store purchase");
            String dueDateStr = (String) payload.getOrDefault("dueDate", "");

            BigDecimal amount = BigDecimal.ZERO;
            Object amtObj = payload.get("amount");
            if (amtObj instanceof Number) {
                amount = BigDecimal.valueOf(((Number) amtObj).doubleValue());
            } else if (amtObj instanceof String && !((String) amtObj).isBlank()) {
                try {
                    amount = new BigDecimal(((String) amtObj).trim());
                } catch (NumberFormatException nfe) {
                    return ResponseEntity.badRequest().headers(noCacheHeaders())
                            .body(ApiResponse.error("Invalid transaction amount format."));
                }
            }

            if (amount.compareTo(BigDecimal.ZERO) <= 0) {
                return ResponseEntity.badRequest().headers(noCacheHeaders())
                        .body(ApiResponse.error("Transaction amount must be greater than zero."));
            }

            // Find existing registered farmer
            User user = null;
            if (mobile != null && !mobile.isBlank()) {
                user = userRepository.findByMobile(mobile.trim()).orElse(null);
            }
            if (user == null && name != null && !name.isBlank()) {
                List<User> found = userRepository.findAllCustomers();
                user = found.stream()
                        .filter(u -> u.getName() != null && u.getName().equalsIgnoreCase(name.trim()))
                        .findFirst()
                        .orElse(null);
            }

            // Never auto-create customer with hardcoded credentials!
            if (user == null) {
                return ResponseEntity.status(HttpStatus.NOT_FOUND).headers(noCacheHeaders())
                        .body(ApiResponse.error("Customer not found. Please register the farmer before recording credit dues."));
            }

            LocalDate dueDate = LocalDate.now().plusDays(30);
            if (dueDateStr != null && !dueDateStr.isBlank()) {
                try {
                    dueDate = LocalDate.parse(dueDateStr.trim());
                } catch (Exception ignored) {}
            }

            Udhari record = new Udhari();
            record.setUser(user);
            record.setTotalAmount(amount);
            record.setPaidAmount(BigDecimal.ZERO);
            record.setRemainingAmount(amount);
            record.setDueDate(dueDate);
            record.setStatus(UdhariStatus.ACTIVE);
            record.setNotes(notes != null && !notes.isBlank() ? notes.trim() : "Store credit");
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
            resp.put("dueDate", saved.getDueDate() != null ? saved.getDueDate().toString() : null);
            resp.put("notes", saved.getNotes());
            resp.put("status", saved.getStatus().name());

            return ResponseEntity.status(HttpStatus.CREATED).headers(noCacheHeaders())
                    .body(ApiResponse.ok("Udhari transaction recorded", resp));
        } catch (Exception e) {
            log.error("Failed to add udhari transaction", e);
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).headers(noCacheHeaders())
                    .body(ApiResponse.error("Unable to record transaction. Please verify data and try again."));
        }
    }

    @GetMapping({"/ledger/{identifier}", "/farmer/credit-ledger", "/farmer/ledger"})
    public ResponseEntity<ApiResponse<Map<String, Object>>> getFarmerLedger(
            @PathVariable(required = false) String identifier,
            @RequestParam(required = false) String farmerId,
            @RequestParam(required = false) String mobile,
            @RequestParam(required = false) String name) {

        Authentication auth = SecurityContextHolder.getContext().getAuthentication();
        if (auth == null || !auth.isAuthenticated() || "anonymousUser".equals(auth.getName())) {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).headers(noCacheHeaders())
                    .body(ApiResponse.error("Authentication required to view credit ledger."));
        }

        boolean isAdmin = auth.getAuthorities().stream().anyMatch(a -> "ROLE_ADMIN".equals(a.getAuthority()));
        User currentUser = null;
        if (auth.getPrincipal() instanceof CustomUserDetails userDetails) {
            currentUser = userDetails.getUser();
        } else {
            currentUser = userRepository.findByEmailOrMobile(auth.getName()).orElse(null);
        }

        User targetFarmer;
        String lookup = identifier;
        if (lookup == null || lookup.isBlank() || "{identifier}".equals(lookup)) {
            lookup = farmerId != null ? farmerId : (mobile != null ? mobile : name);
        }

        if (isAdmin) {
            if (lookup != null && !lookup.isBlank()) {
                targetFarmer = findUserByLookup(lookup);
            } else {
                targetFarmer = currentUser;
            }
        } else {
            if (currentUser == null) {
                return ResponseEntity.status(HttpStatus.UNAUTHORIZED).headers(noCacheHeaders())
                        .body(ApiResponse.error("User profile not found."));
            }
            if (lookup != null && !lookup.isBlank()) {
                User requested = findUserByLookup(lookup);
                if (requested != null && !requested.getId().equals(currentUser.getId())) {
                    return ResponseEntity.status(HttpStatus.FORBIDDEN).headers(noCacheHeaders())
                            .body(ApiResponse.error("Access denied. You can only view your own credit ledger."));
                }
            }
            targetFarmer = currentUser;
        }

        if (targetFarmer == null) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).headers(noCacheHeaders())
                    .body(ApiResponse.error("Farmer record not found."));
        }

        List<Udhari> userUdhari = udhariRepository.findByUserIdOrderByCreatedAtDesc(targetFarmer.getId());
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
            t.put("status", u.getStatus() != null ? u.getStatus().name() : "ACTIVE");
            t.put("dueDate", u.getDueDate() != null ? u.getDueDate().toString() : null);
            txns.add(t);
        }

        BigDecimal pendingDue = totalCredit.subtract(totalPaid).max(BigDecimal.ZERO);

        Map<String, Object> data = new HashMap<>();
        data.put("farmerId", "KSK-" + targetFarmer.getMobile());
        data.put("farmerName", targetFarmer.getName());
        data.put("mobile", targetFarmer.getMobile());
        data.put("totalCredit", totalCredit);
        data.put("totalPaid", totalPaid);
        data.put("pendingDue", pendingDue);
        data.put("transactions", txns);

        return ResponseEntity.ok().headers(noCacheHeaders()).body(ApiResponse.ok("Credit ledger fetched", data));
    }

    private User findUserByLookup(String lookup) {
        if (lookup == null || lookup.isBlank()) return null;
        String clean = lookup.replace("KSK-", "").trim();
        Optional<User> byMobile = userRepository.findByMobile(clean);
        if (byMobile.isPresent()) return byMobile.get();
        Optional<User> byEmail = userRepository.findByEmail(lookup.trim());
        if (byEmail.isPresent()) return byEmail.get();
        String search = lookup.trim().toLowerCase();
        return userRepository.findAllCustomers().stream()
                .filter(u -> u.getName() != null && (u.getName().equalsIgnoreCase(lookup.trim()) || u.getName().toLowerCase().contains(search)))
                .findFirst()
                .orElse(null);
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
