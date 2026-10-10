package com.krushisevakendra.controller;

import com.krushisevakendra.dto.*;
import com.krushisevakendra.entity.*;
import com.krushisevakendra.enums.*;
import com.krushisevakendra.exception.ResourceNotFoundException;
import com.krushisevakendra.repository.*;
import com.krushisevakendra.service.*;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.io.ByteArrayResource;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Sort;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.List;
import java.util.Map;
import java.util.Optional;

@Controller
@RequestMapping("/admin")
public class AdminController {

    private final ProductService productService;
    private final CategoryService categoryService;
    private final OrderService orderService;
    private final UdhariService udhariService;
    private final PaymentService paymentService;
    private final UserService userService;
    private final InventoryService inventoryService;
    private final ReportService reportService;
    private final NotificationService notificationService;
    private final BackupService backupService;
    private final OfferRepository offerRepository;
    private final FeedbackRepository feedbackRepository;
    private final CustomerLoginHistoryRepository customerLoginHistoryRepository;

    @Value("${app.shop.name}") private String shopName;
    @Value("${app.shop.gstin}") private String shopGstin;
    @Value("${app.shop.address}") private String shopAddress;
    @Value("${app.shop.mobile}") private String shopMobile;
    @Value("${app.shop.email}") private String shopEmail;
    @Value("${app.shop.upi-id}") private String shopUpiId;
    @Value("${app.shop.opening-hours}") private String shopHours;
    @Value("${app.shop.map-url:https://maps.app.goo.gl/S34rKk9DwEntCGid6}") private String shopMapUrl;
    @Value("${app.shop.map-embed-url:https://maps.google.com/maps?q=19.9852957,74.9312239&hl=mr&z=17&output=embed}") private String shopMapEmbedUrl;

    public AdminController(ProductService productService,
                           CategoryService categoryService,
                           OrderService orderService,
                           UdhariService udhariService,
                           PaymentService paymentService,
                           UserService userService,
                           InventoryService inventoryService,
                           ReportService reportService,
                           NotificationService notificationService,
                           BackupService backupService,
                           OfferRepository offerRepository,
                           FeedbackRepository feedbackRepository,
                           CustomerLoginHistoryRepository customerLoginHistoryRepository) {
        this.productService = productService;
        this.categoryService = categoryService;
        this.orderService = orderService;
        this.udhariService = udhariService;
        this.paymentService = paymentService;
        this.userService = userService;
        this.inventoryService = inventoryService;
        this.reportService = reportService;
        this.notificationService = notificationService;
        this.backupService = backupService;
        this.offerRepository = offerRepository;
        this.feedbackRepository = feedbackRepository;
        this.customerLoginHistoryRepository = customerLoginHistoryRepository;
    }

    // 1. Admin Dashboard
    @GetMapping({"", "/", "/dashboard"})
    public String dashboard(Model model) {
        model.addAttribute("totalProducts", productService.getTotalProductCount());
        model.addAttribute("totalCustomers", userService.getCustomerCount());
        model.addAttribute("totalOrders", orderService.getTotalOrderCount());
        model.addAttribute("totalSales", orderService.getTotalSales());
        model.addAttribute("todaySales", orderService.getTodaySales());
        model.addAttribute("monthlySales", orderService.getMonthlySales());
        model.addAttribute("totalRemainingUdhari", udhariService.getTotalRemainingUdhari());
        model.addAttribute("totalUdhariCollected", udhariService.getTotalUdhariCollected());
        model.addAttribute("overdueCount", udhariService.getOverdueCount());
        model.addAttribute("lowStockCount", productService.getLowStockProducts().size());
        model.addAttribute("expiredCount", productService.getExpiredProducts().size());
        model.addAttribute("inventoryValue", productService.getTotalInventoryValue());
        model.addAttribute("recentOrders", orderService.getRecentOrders());
        model.addAttribute("recentPayments", paymentService.getRecentPayments());
        model.addAttribute("overdueUdhariList", udhariService.getOverdueRecords());
        model.addAttribute("lowStockProducts", productService.getLowStockProducts());
        model.addAttribute("pendingOrdersCount", orderService.getOrderCountByStatus(OrderStatus.PENDING));

        return "admin/dashboard";
    }

    // 2. Products Management
    @GetMapping("/products")
    public String listProducts(
            @RequestParam(required = false) Long categoryId,
            @RequestParam(required = false) String status,
            @RequestParam(required = false) String stockStatus,
            @RequestParam(required = false) String keyword,
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "15") int size,
            Model model) {

        model.addAttribute("productPage", productService.filterAdminProducts(categoryId, status, stockStatus, keyword, PageRequest.of(page, size, Sort.by("id").descending())));
        model.addAttribute("categories", categoryService.getAllActiveCategories());
        model.addAttribute("categoryId", categoryId);
        model.addAttribute("status", status);
        model.addAttribute("stockStatus", stockStatus);
        model.addAttribute("keyword", keyword);
        return "admin/products";
    }

    @GetMapping("/products/add")
    public String addProductForm(Model model) {
        model.addAttribute("productDto", new ProductDto());
        model.addAttribute("categories", categoryService.getAllActiveCategories());
        model.addAttribute("isEdit", false);
        return "admin/product-form";
    }

    @PostMapping("/products/add")
    public String addProductSubmit(
            @Valid @ModelAttribute("productDto") ProductDto productDto,
            BindingResult bindingResult,
            Model model,
            RedirectAttributes redirectAttributes) {

        if (bindingResult.hasErrors()) {
            model.addAttribute("categories", categoryService.getAllActiveCategories());
            model.addAttribute("isEdit", false);
            return "admin/product-form";
        }

        try {
            productService.saveProduct(productDto);
        } catch (IllegalArgumentException exception) {
            model.addAttribute("errorMessage", exception.getMessage());
            model.addAttribute("categories", categoryService.getAllActiveCategories());
            model.addAttribute("isEdit", false);
            return "admin/product-form";
        }
        redirectAttributes.addFlashAttribute("successMessage", "Product added successfully / उत्पादन जोडले गेले!");
        return "redirect:/admin/products";
    }

    @GetMapping("/products/{id}/edit")
    public String editProductForm(@PathVariable Long id, Model model) {
        Product product = productService.getProductById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Product not found with id: " + id));

        ProductDto dto = new ProductDto();
        dto.setId(product.getId());
        dto.setCategoryId(product.getCategory().getId());
        dto.setName(product.getName());
        dto.setNameMr(product.getNameMr());
        dto.setCompany(product.getCompany());
        dto.setSku(product.getSku());
        dto.setBarcode(product.getBarcode());
        dto.setPrice(product.getPrice());
        dto.setDiscountPrice(product.getDiscountPrice());
        dto.setGstRate(product.getGstRate());
        dto.setDescription(product.getDescription());
        dto.setUsageInstructions(product.getUsageInstructions());
        dto.setExistingImage(product.getImage());
        dto.setStockQuantity(product.getStockQuantity());
        dto.setMinimumStock(product.getMinimumStock());
        dto.setBatchNumber(product.getBatchNumber());
        dto.setExpiryDate(product.getExpiryDate());
        dto.setStatus(product.getStatus());

        model.addAttribute("productDto", dto);
        model.addAttribute("categories", categoryService.getAllActiveCategories());
        model.addAttribute("isEdit", true);
        return "admin/product-form";
    }

    @PostMapping("/products/{id}/edit")
    public String editProductSubmit(
            @PathVariable Long id,
            @Valid @ModelAttribute("productDto") ProductDto productDto,
            BindingResult bindingResult,
            Model model,
            RedirectAttributes redirectAttributes) {

        if (bindingResult.hasErrors()) {
            model.addAttribute("categories", categoryService.getAllActiveCategories());
            model.addAttribute("isEdit", true);
            return "admin/product-form";
        }

        try {
            productService.updateProduct(id, productDto);
        } catch (IllegalArgumentException exception) {
            model.addAttribute("errorMessage", exception.getMessage());
            model.addAttribute("categories", categoryService.getAllActiveCategories());
            model.addAttribute("isEdit", true);
            return "admin/product-form";
        }
        redirectAttributes.addFlashAttribute("successMessage", "Product updated successfully / उत्पादन अद्ययावत केले!");
        return "redirect:/admin/products";
    }

    @PostMapping("/products/{id}/delete")
    public String deleteProduct(@PathVariable Long id, RedirectAttributes redirectAttributes) {
        productService.deleteProduct(id);
        redirectAttributes.addFlashAttribute("successMessage", "Product deleted / उत्पादन काढले.");
        return "redirect:/admin/products";
    }

    @PostMapping("/products/{id}/adjust-stock")
    public String adjustStock(
            @PathVariable Long id,
            @RequestParam Integer quantity,
            @RequestParam InventoryTransactionType type,
            @RequestParam String reason,
            RedirectAttributes redirectAttributes) {

        inventoryService.adjustStock(id, quantity, type, reason);
        redirectAttributes.addFlashAttribute("successMessage", "Stock updated successfully / साठा अद्ययावत केला.");
        return "redirect:/admin/inventory";
    }

    // 3. Category Management
    @GetMapping("/categories")
    public String listCategories(Model model) {
        model.addAttribute("categories", categoryService.getAllCategories());
        model.addAttribute("categoryDto", new CategoryDto());
        return "admin/categories";
    }

    @PostMapping("/categories/add")
    public String addCategory(
            @Valid @ModelAttribute("categoryDto") CategoryDto categoryDto,
            BindingResult bindingResult,
            RedirectAttributes redirectAttributes) {

        if (bindingResult.hasErrors()) {
            redirectAttributes.addFlashAttribute("errorMessage", "Category name is required");
            return "redirect:/admin/categories";
        }

        categoryService.saveCategory(categoryDto);
        redirectAttributes.addFlashAttribute("successMessage", "Category created / वर्ग जोडला.");
        return "redirect:/admin/categories";
    }

    @PostMapping("/categories/{id}/edit")
    public String editCategory(
            @PathVariable Long id,
            @ModelAttribute CategoryDto categoryDto,
            RedirectAttributes redirectAttributes) {

        categoryService.updateCategory(id, categoryDto);
        redirectAttributes.addFlashAttribute("successMessage", "Category updated / वर्ग अद्ययावत केला.");
        return "redirect:/admin/categories";
    }

    @PostMapping("/categories/{id}/toggle-status")
    public String toggleCategoryStatus(@PathVariable Long id, RedirectAttributes redirectAttributes) {
        categoryService.toggleCategoryStatus(id);
        redirectAttributes.addFlashAttribute("successMessage", "Category status updated.");
        return "redirect:/admin/categories";
    }

    @PostMapping("/categories/{id}/delete")
    public String deleteCategory(@PathVariable Long id, RedirectAttributes redirectAttributes) {
        categoryService.deleteCategory(id);
        redirectAttributes.addFlashAttribute("successMessage", "Category deleted / वर्ग काढला.");
        return "redirect:/admin/categories";
    }

    // 4. Inventory Management & Expiry Tracking
    @GetMapping("/inventory")
    public String inventoryManagement(
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "15") int size,
            Model model) {
        model.addAttribute("products", productService.getAllProducts());
        model.addAttribute("lowStockProducts", productService.getLowStockProducts());
        model.addAttribute("transactionsPage", inventoryService.getTransactionHistory(PageRequest.of(page, size)));
        return "admin/inventory";
    }

    @GetMapping("/expiry-tracking")
    public String expiryTracking(
            @RequestParam(defaultValue = "60") int days,
            Model model) {
        model.addAttribute("expiredProducts", productService.getExpiredProducts());
        model.addAttribute("expiringSoonProducts", productService.getExpiringSoonProducts(days));
        model.addAttribute("selectedDays", days);
        return "admin/expiry-tracking";
    }

    // 5. Customer Management
    @GetMapping("/customers")
    public String listCustomers(
            @RequestParam(required = false) String query,
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "15") int size,
            Model model) {
        model.addAttribute("customerPage", userService.searchCustomers(query, PageRequest.of(page, size)));
        model.addAttribute("query", query);
        model.addAttribute("customerEditDto", new CustomerUpdateDto());
        model.addAttribute("totalCustomers", userService.getCustomerCount());
        model.addAttribute("customerLoginHistory", customerLoginHistoryRepository.findTop100ByOrderByLoggedInAtDesc());
        model.addAttribute("totalCustomerLogins", customerLoginHistoryRepository.count());
        return "admin/customers";
    }

    @GetMapping("/customers/{id}")
    public String customerDetails(@PathVariable Long id, Model model) {
        User customer = userService.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Customer not found with id: " + id));
        List<Udhari> creditRecords = udhariService.getUserUdhariList(id);
        BigDecimal totalCredit = BigDecimal.ZERO;
        BigDecimal totalPaid = BigDecimal.ZERO;
        BigDecimal totalRemaining = BigDecimal.ZERO;
        for (Udhari record : creditRecords) {
            if (record.getTotalAmount() != null) totalCredit = totalCredit.add(record.getTotalAmount());
            if (record.getPaidAmount() != null) totalPaid = totalPaid.add(record.getPaidAmount());
            if (record.getRemainingAmount() != null) totalRemaining = totalRemaining.add(record.getRemainingAmount());
        }

        model.addAttribute("customer", customer);
        model.addAttribute("creditRecords", creditRecords);
        model.addAttribute("totalCredit", totalCredit);
        model.addAttribute("totalPaid", totalPaid);
        model.addAttribute("totalRemaining", totalRemaining);
        model.addAttribute("customerLoginHistory",
                customerLoginHistoryRepository.findTop50ByUserIdOrderByLoggedInAtDesc(id));
        model.addAttribute("totalCustomerLogins", customerLoginHistoryRepository.countByUserId(id));
        CustomerUpdateDto customerEditDto = new CustomerUpdateDto();
        customerEditDto.setId(customer.getId());
        customerEditDto.setName(customer.getName());
        customerEditDto.setMobile(customer.getMobile());
        customerEditDto.setEmail(customer.getEmail());
        customerEditDto.setVillage(customer.getVillage());
        customerEditDto.setTaluka(customer.getTaluka());
        customerEditDto.setDistrict(customer.getDistrict());
        customerEditDto.setAddress(customer.getAddress());
        customerEditDto.setStatus(customer.getStatus());
        model.addAttribute("customerEditDto", customerEditDto);
        return "admin/customer-details";
    }

    @PostMapping("/customers/edit")
    public String editCustomerSubmit(
            @Valid @ModelAttribute("customerEditDto") CustomerUpdateDto customerDto,
            BindingResult bindingResult,
            RedirectAttributes redirectAttributes) {

        if (bindingResult.hasErrors()) {
            redirectAttributes.addFlashAttribute("errorMessage", "Invalid customer details provided / चुकीची माहिती दिली आहे");
            return "redirect:/admin/customers";
        }

        userService.updateCustomerByAdmin(customerDto);
        redirectAttributes.addFlashAttribute("successMessage", "Farmer details updated successfully / शेतकरी माहिती अद्ययावत केली!");
        return "redirect:/admin/customers";
    }

    @PostMapping("/customers/{id}/edit")
    public String editCustomerByIdSubmit(
            @PathVariable Long id,
            @Valid @ModelAttribute("customerEditDto") CustomerUpdateDto customerDto,
            BindingResult bindingResult,
            RedirectAttributes redirectAttributes) {

        customerDto.setId(id);
        if (bindingResult.hasErrors()) {
            redirectAttributes.addFlashAttribute("errorMessage", "Invalid customer details provided");
            return "redirect:/admin/customers/" + id;
        }

        userService.updateCustomerByAdmin(customerDto);
        redirectAttributes.addFlashAttribute("successMessage", "Customer profile updated successfully!");
        return "redirect:/admin/customers/" + id;
    }

    // 6. Orders Management
    @GetMapping("/orders")
    public String listOrders(
            @RequestParam(required = false) String query,
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "15") int size,
            Model model) {
        if (query != null && !query.isBlank()) {
            model.addAttribute("orderPage", orderService.searchOrders(query, PageRequest.of(page, size, Sort.by("id").descending())));
        } else {
            model.addAttribute("orderPage", orderService.getAllOrdersPaged(PageRequest.of(page, size, Sort.by("id").descending())));
        }
        model.addAttribute("query", query);
        return "admin/orders";
    }

    @GetMapping("/orders/{id}")
    public String adminOrderDetails(@PathVariable Long id, Model model) {
        Order order = orderService.getOrderById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Order not found with id: " + id));
        model.addAttribute("order", order);
        model.addAttribute("orderStatuses", OrderStatus.values());
        model.addAttribute("paymentStatuses", PaymentStatus.values());
        return "admin/order-details";
    }

    @PostMapping("/orders/{id}/status")
    public String updateOrderStatus(
            @PathVariable Long id,
            @RequestParam OrderStatus status,
            RedirectAttributes redirectAttributes) {
        orderService.updateOrderStatus(id, status);
        redirectAttributes.addFlashAttribute("successMessage", "Order status updated to " + status.name());
        return "redirect:/admin/orders/" + id;
    }

    @PostMapping("/orders/{id}/payment-status")
    public String updateOrderPaymentStatus(
            @PathVariable Long id,
            @RequestParam PaymentStatus paymentStatus,
            RedirectAttributes redirectAttributes) {
        orderService.updatePaymentStatus(id, paymentStatus);
        redirectAttributes.addFlashAttribute("successMessage", "Payment status updated to " + paymentStatus.name());
        return "redirect:/admin/orders/" + id;
    }

    // 7. Udhari (Credit) Management
    @GetMapping("/udhari")
    public String listUdhari(
            @RequestParam(required = false) String query,
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "15") int size,
            Model model) {
        model.addAttribute("udhariPage", udhariService.searchUdhari(query, PageRequest.of(page, size, Sort.by("id").descending())));
        model.addAttribute("totalRemaining", udhariService.getTotalRemainingUdhari());
        model.addAttribute("totalIssued", udhariService.getTotalUdhariIssued());
        model.addAttribute("totalCollected", udhariService.getTotalUdhariCollected());
        model.addAttribute("overdueList", udhariService.getOverdueRecords());
        model.addAttribute("customers", userService.getAllCustomers());
        model.addAttribute("paymentDto", new UdhariPaymentDto());
        model.addAttribute("udhariEditDto", new UdhariEditDto());
        model.addAttribute("udhariStatuses", UdhariStatus.values());
        model.addAttribute("query", query);
        return "admin/udhari";
    }

    @PostMapping("/udhari/add-credit-customer")
    public String addCreditCustomerSubmit(
            @RequestParam(required = false) Long userId,
            @RequestParam(required = false) String customerName,
            @RequestParam(required = false) String customerMobile,
            @RequestParam(required = false) String customerVillage,
            @RequestParam String itemsDescription,
            @RequestParam BigDecimal totalAmount,
            @RequestParam(required = false, defaultValue = "0") BigDecimal paidAmount,
            @RequestParam(required = false) @org.springframework.format.annotation.DateTimeFormat(iso = org.springframework.format.annotation.DateTimeFormat.ISO.DATE) LocalDate dueDate,
            @RequestParam(required = false) String notes,
            RedirectAttributes redirectAttributes) {

        User customer;
        if (userId != null && userId > 0) {
            customer = userService.findById(userId)
                    .orElseThrow(() -> new ResourceNotFoundException("Customer not found with id: " + userId));
        } else {
            if (customerName == null || customerName.isBlank() || customerMobile == null || customerMobile.isBlank()) {
                redirectAttributes.addFlashAttribute("errorMessage", "कृपया ग्राहकाचे नाव आणि मोबाईल नंबर टाका!");
                return "redirect:/admin/udhari";
            }
            String cleanMobile = customerMobile.replaceAll("[^0-9]", "");
            if (cleanMobile.length() != 10) {
                redirectAttributes.addFlashAttribute("errorMessage", "कृपया वैध १० अंकी मोबाईल नंबर टाका!");
                return "redirect:/admin/udhari";
            }

            Optional<User> existing = userService.findByMobile(cleanMobile);
            if (existing.isPresent()) {
                customer = existing.get();
            } else {
                UserRegistrationDto regDto = new UserRegistrationDto();
                regDto.setName(customerName.trim());
                regDto.setMobile(cleanMobile);
                regDto.setEmail(cleanMobile + "@saptashrungi.local");
                String v = (customerVillage != null && !customerVillage.isBlank()) ? customerVillage.trim() : "Mirakhnagar";
                regDto.setVillage(v);
                regDto.setAddress(v + ", Vaijapur, Chhatrapati Sambhajinagar");
                regDto.setTaluka("Vaijapur");
                regDto.setDistrict("Chhatrapati Sambhajinagar");
                regDto.setPassword("Farmer@123");
                regDto.setConfirmPassword("Farmer@123");
                customer = userService.registerCustomer(regDto);
            }
        }

        String combinedNotes = "";
        if (itemsDescription != null && !itemsDescription.isBlank()) {
            combinedNotes = "वस्तू: " + itemsDescription.trim();
        }
        if (notes != null && !notes.isBlank()) {
            combinedNotes += (combinedNotes.isEmpty() ? "" : " | ") + notes.trim();
        }

        LocalDate due = dueDate != null ? dueDate : LocalDate.now().plusDays(30);
        Udhari udhari = udhariService.createUdhariRecord(customer, null, totalAmount, due);

        BigDecimal paid = paidAmount != null ? paidAmount : BigDecimal.ZERO;
        BigDecimal rem = totalAmount.subtract(paid).max(BigDecimal.ZERO);

        UdhariEditDto editDto = new UdhariEditDto();
        editDto.setId(udhari.getId());
        editDto.setTotalAmount(totalAmount);
        editDto.setPaidAmount(paid);
        editDto.setRemainingAmount(rem);
        editDto.setDueDate(due);
        editDto.setNotes(combinedNotes);
        if (rem.compareTo(BigDecimal.ZERO) == 0) {
            editDto.setStatus(UdhariStatus.PAID_IN_FULL);
        } else if (due.isBefore(LocalDate.now())) {
            editDto.setStatus(UdhariStatus.OVERDUE);
        } else {
            editDto.setStatus(UdhariStatus.ACTIVE);
        }
        udhariService.updateUdhariRecord(editDto);

        redirectAttributes.addFlashAttribute("successMessage", "✅ उधार नेणारा ग्राहक '" + customer.getName() + "' ची ₹" + totalAmount + " ची उधारी (परत देण्याची तारीख: " + due + ") यशस्वीरित्या नोंदवली गेली!");
        return "redirect:/admin/udhari";
    }

    @PostMapping("/udhari/create-or-set")
    public String createOrSetUdhariSubmit(
            @RequestParam Long userId,
            @RequestParam BigDecimal totalAmount,
            @RequestParam(required = false, defaultValue = "0") BigDecimal paidAmount,
            @RequestParam(required = false) @org.springframework.format.annotation.DateTimeFormat(iso = org.springframework.format.annotation.DateTimeFormat.ISO.DATE) LocalDate dueDate,
            @RequestParam(required = false) String notes,
            RedirectAttributes redirectAttributes) {

        User customer = userService.findById(userId)
                .orElseThrow(() -> new ResourceNotFoundException("Customer not found with id: " + userId));

        LocalDate due = dueDate != null ? dueDate : LocalDate.now().plusDays(30);
        Udhari udhari = udhariService.createUdhariRecord(customer, null, totalAmount, due);
        
        if (paidAmount != null && paidAmount.compareTo(BigDecimal.ZERO) > 0) {
            UdhariEditDto editDto = new UdhariEditDto();
            editDto.setId(udhari.getId());
            editDto.setTotalAmount(totalAmount);
            editDto.setPaidAmount(paidAmount);
            editDto.setRemainingAmount(totalAmount.subtract(paidAmount).max(BigDecimal.ZERO));
            editDto.setDueDate(due);
            editDto.setNotes(notes);
            udhariService.updateUdhariRecord(editDto);
        } else if (notes != null && !notes.isBlank()) {
            udhari.setNotes(notes);
            UdhariEditDto editDto = new UdhariEditDto();
            editDto.setId(udhari.getId());
            editDto.setNotes(notes);
            udhariService.updateUdhariRecord(editDto);
        }

        redirectAttributes.addFlashAttribute("successMessage", "Udhari of ₹" + totalAmount + " set successfully for " + customer.getName() + " / उधारी यशस्वीरित्या जोडली गेली!");
        return "redirect:/admin/udhari";
    }

    @PostMapping("/udhari/edit")
    public String editUdhariSubmit(
            @ModelAttribute("udhariEditDto") UdhariEditDto udhariEditDto,
            RedirectAttributes redirectAttributes) {

        if (udhariEditDto.getId() == null) {
            redirectAttributes.addFlashAttribute("errorMessage", "Invalid Udhari ID / अयोग्य उधारी आयडी");
            return "redirect:/admin/udhari";
        }

        udhariService.updateUdhariRecord(udhariEditDto);
        redirectAttributes.addFlashAttribute("successMessage", "Udhari ledger details updated successfully / उधारी खात्याची माहिती अद्ययावत केली!");
        return "redirect:/admin/udhari";
    }

    @PostMapping("/udhari/{id}/edit")
    public String editUdhariByIdSubmit(
            @PathVariable Long id,
            @ModelAttribute("udhariEditDto") UdhariEditDto udhariEditDto,
            RedirectAttributes redirectAttributes) {

        udhariEditDto.setId(id);
        udhariService.updateUdhariRecord(udhariEditDto);
        redirectAttributes.addFlashAttribute("successMessage", "Udhari record updated successfully!");
        return "redirect:/admin/udhari";
    }

    @PostMapping("/udhari/record-payment")
    public String recordUdhariPaymentSubmit(
            @Valid @ModelAttribute("paymentDto") UdhariPaymentDto paymentDto,
            BindingResult bindingResult,
            RedirectAttributes redirectAttributes) {

        if (bindingResult.hasErrors()) {
            redirectAttributes.addFlashAttribute("errorMessage", "Please provide a valid payment amount");
            return "redirect:/admin/udhari";
        }

        paymentService.recordPayment(null, null, null, null, null, null, null); // mapped via udhariService
        udhariService.recordUdhariPayment(paymentDto);
        redirectAttributes.addFlashAttribute("successMessage", "Udhari payment of ₹" + paymentDto.getAmount() + " recorded successfully!");
        return "redirect:/admin/udhari";
    }

    @PostMapping("/udhari/{id}/update-due-date")
    public String updateUdhariDueDate(
            @PathVariable Long id,
            @RequestParam LocalDate newDueDate,
            RedirectAttributes redirectAttributes) {
        udhariService.updateDueDate(id, newDueDate);
        redirectAttributes.addFlashAttribute("successMessage", "Due date updated to " + newDueDate);
        return "redirect:/admin/udhari";
    }

    @PostMapping("/udhari/send-reminder")
    public String sendUdhariReminder(
            @RequestParam Long userId,
            @RequestParam(required = false) Long udhariId,
            @RequestParam NotificationType type,
            @RequestParam String message,
            RedirectAttributes redirectAttributes) {

        ReminderDto dto = new ReminderDto();
        dto.setUserId(userId);
        dto.setUdhariId(udhariId);
        dto.setType(type);
        dto.setMessage(message);

        notificationService.sendReminder(dto);
        redirectAttributes.addFlashAttribute("successMessage", "Reminder sent successfully via " + type.name() + "!");
        return "redirect:/admin/udhari";
    }

    // 8. Payments Management
    @GetMapping("/payments")
    public String listPayments(
            @RequestParam(required = false) String query,
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "15") int size,
            Model model) {
        model.addAttribute("paymentPage", paymentService.searchPayments(query, PageRequest.of(page, size, Sort.by("id").descending())));
        model.addAttribute("query", query);
        model.addAttribute("paymentMethods", paymentService.getPaymentTotalsByMethod());
        return "admin/payments";
    }

    // 9. Reports & Analytics
    @GetMapping("/reports")
    public String reports(
            @ModelAttribute ReportFilterDto filter,
            Model model) {
        model.addAttribute("salesReport", reportService.generateSalesReport(filter));
        model.addAttribute("stockReport", reportService.generateStockReport());
        model.addAttribute("udhariReport", reportService.generateUdhariReport());
        model.addAttribute("profitReport", reportService.generateProfitReport(filter));
        model.addAttribute("customerReport", reportService.generateCustomerPurchasesReport());
        model.addAttribute("filter", filter);
        return "admin/reports";
    }

    @GetMapping("/reports/export/{type}")
    public ResponseEntity<ByteArrayResource> exportReport(
            @PathVariable String type,
            @ModelAttribute ReportFilterDto filter) {
        String csvContent = reportService.exportReportToCsv(type, filter);
        ByteArrayResource resource = new ByteArrayResource(csvContent.getBytes());

        return ResponseEntity.ok()
                .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=" + type + "_report.csv")
                .contentType(MediaType.parseMediaType("text/csv"))
                .contentLength(resource.contentLength())
                .body(resource);
    }

    // 10. Offers Management
    @GetMapping("/offers")
    public String listOffers(Model model) {
        model.addAttribute("offers", offerRepository.findAll());
        model.addAttribute("offerForm", new Offer());
        return "admin/offers";
    }

    @PostMapping("/offers/add")
    public String addOffer(
            @ModelAttribute Offer offer,
            RedirectAttributes redirectAttributes) {
        offer.setCreatedAt(java.time.LocalDateTime.now());
        offerRepository.save(offer);
        redirectAttributes.addFlashAttribute("successMessage", "Offer/Coupon created / ऑफर जोडली गेली.");
        return "redirect:/admin/offers";
    }

    @PostMapping("/offers/{id}/toggle")
    public String toggleOffer(@PathVariable Long id, RedirectAttributes redirectAttributes) {
        offerRepository.findById(id).ifPresent(o -> {
            o.setActive(!Boolean.TRUE.equals(o.getActive()));
            offerRepository.save(o);
        });
        redirectAttributes.addFlashAttribute("successMessage", "Offer status updated.");
        return "redirect:/admin/offers";
    }

    @PostMapping("/offers/{id}/delete")
    public String deleteOffer(@PathVariable Long id, RedirectAttributes redirectAttributes) {
        offerRepository.deleteById(id);
        redirectAttributes.addFlashAttribute("successMessage", "Offer deleted.");
        return "redirect:/admin/offers";
    }

    // 11. Database Backup
    @GetMapping("/backup")
    public String backupDashboard(Model model) {
        model.addAttribute("backupLogs", backupService.getBackupHistory());
        return "admin/backup";
    }

    @PostMapping("/backup/trigger")
    public String triggerBackup(RedirectAttributes redirectAttributes) {
        BackupLog log = backupService.triggerDatabaseBackup();
        redirectAttributes.addFlashAttribute("successMessage", "Database backup generated successfully: " + log.getFileName());
        return "redirect:/admin/backup";
    }

    @GetMapping("/backup/download/{fileName}")
    public ResponseEntity<ByteArrayResource> downloadBackup(@PathVariable String fileName) {
        byte[] data = backupService.getBackupData(fileName);
        ByteArrayResource resource = new ByteArrayResource(data);

        return ResponseEntity.ok()
                .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=" + fileName)
                .contentType(MediaType.APPLICATION_OCTET_STREAM)
                .contentLength(resource.contentLength())
                .body(resource);
    }

    // 12. Settings
    @GetMapping("/settings")
    public String settings(Model model) {
        model.addAttribute("shopName", shopName);
        model.addAttribute("shopGstin", shopGstin);
        model.addAttribute("shopAddress", shopAddress);
        model.addAttribute("shopMobile", shopMobile);
        model.addAttribute("shopEmail", shopEmail);
        model.addAttribute("shopUpiId", shopUpiId);
        model.addAttribute("shopHours", shopHours);
        model.addAttribute("shopMapUrl", shopMapUrl);
        model.addAttribute("shopMapEmbedUrl", shopMapEmbedUrl);
        return "admin/settings";
    }
}
