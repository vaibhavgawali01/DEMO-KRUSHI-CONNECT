package com.krushisevakendra.controller;

import com.krushisevakendra.entity.Order;
import com.krushisevakendra.entity.Payment;
import com.krushisevakendra.entity.User;
import com.krushisevakendra.exception.ResourceNotFoundException;
import com.krushisevakendra.repository.OfferRepository;
import com.krushisevakendra.security.SecurityUtil;
import com.krushisevakendra.service.*;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import java.math.BigDecimal;
import java.util.List;
import java.util.Optional;
import com.krushisevakendra.enums.OrderStatus;

@Controller
@RequestMapping({"/customer", "/farmer"})
public class CustomerController {

    private final UserService userService;
    private final OrderService orderService;
    private final UdhariService udhariService;
    private final PaymentService paymentService;
    private final NotificationService notificationService;
    private final FarmingService farmingService;
    private final OfferRepository offerRepository;
    private final SecurityUtil securityUtil;

    @Value("${app.shop.name}") private String shopName;
    @Value("${app.shop.gstin}") private String shopGstin;
    @Value("${app.shop.address}") private String shopAddress;
    @Value("${app.shop.mobile}") private String shopMobile;
    @Value("${app.shop.email}") private String shopEmail;
    @Value("${app.shop.upi-id}") private String shopUpiId;

    public CustomerController(UserService userService,
                              OrderService orderService,
                              UdhariService udhariService,
                              PaymentService paymentService,
                              NotificationService notificationService,
                              FarmingService farmingService,
                              OfferRepository offerRepository,
                              SecurityUtil securityUtil) {
        this.userService = userService;
        this.orderService = orderService;
        this.udhariService = udhariService;
        this.paymentService = paymentService;
        this.notificationService = notificationService;
        this.farmingService = farmingService;
        this.offerRepository = offerRepository;
        this.securityUtil = securityUtil;
    }

    private User getAuthenticatedCustomer() {
        return securityUtil.getCurrentUser()
                .orElseThrow(() -> new ResourceNotFoundException("Customer not authenticated"));
    }

    @GetMapping({"", "/", "/dashboard"})
    public String dashboard(Model model) {
        User user = getAuthenticatedCustomer();

        BigDecimal remainingUdhari = udhariService.getUserRemainingUdhari(user.getId());
        if (remainingUdhari == null) remainingUdhari = BigDecimal.ZERO;
        
        long unreadNotifs = notificationService.getUnreadCount(user.getId());

        List<Order> allUserOrders = orderService.getUserOrdersList(user.getId());
        BigDecimal totalSpent = BigDecimal.ZERO;
        BigDecimal thisMonthSpent = BigDecimal.ZERO;
        java.time.LocalDate now = java.time.LocalDate.now();

        for (Order o : allUserOrders) {
            if (o.getTotal() != null && o.getOrderStatus() != OrderStatus.CANCELLED) {
                totalSpent = totalSpent.add(o.getTotal());
                if (o.getCreatedAt() != null && o.getCreatedAt().getMonth() == now.getMonth() && o.getCreatedAt().getYear() == now.getYear()) {
                    thisMonthSpent = thisMonthSpent.add(o.getTotal());
                }
            }
        }

        List<com.krushisevakendra.entity.Udhari> userUdhariList = udhariService.getUserUdhariList(user.getId());
        BigDecimal userTotalCredit = BigDecimal.ZERO;
        BigDecimal userTotalPaid = BigDecimal.ZERO;
        java.time.LocalDate earliestDueDate = null;

        for (com.krushisevakendra.entity.Udhari u : userUdhariList) {
            if (u.getTotalAmount() != null) userTotalCredit = userTotalCredit.add(u.getTotalAmount());
            if (u.getPaidAmount() != null) userTotalPaid = userTotalPaid.add(u.getPaidAmount());
            if (u.getRemainingAmount() != null && u.getRemainingAmount().compareTo(BigDecimal.ZERO) > 0 && u.getDueDate() != null) {
                if (earliestDueDate == null || u.getDueDate().isBefore(earliestDueDate)) {
                    earliestDueDate = u.getDueDate();
                }
            }
        }

        BigDecimal creditLimit = BigDecimal.valueOf(15000.00);
        BigDecimal availableCredit = creditLimit.subtract(remainingUdhari).max(BigDecimal.ZERO);

        java.time.format.DateTimeFormatter dateFormatter = java.time.format.DateTimeFormatter.ofPattern("EEEE, MMMM d, yyyy");
        String formattedDate = now.format(dateFormatter);

        model.addAttribute("user", user);
        model.addAttribute("recentOrders", orderService.getUserOrders(user.getId(), PageRequest.of(0, 5)).getContent());
        model.addAttribute("remainingUdhari", remainingUdhari);
        model.addAttribute("userTotalCredit", userTotalCredit);
        model.addAttribute("userTotalPaid", userTotalPaid);
        model.addAttribute("earliestDueDate", earliestDueDate);
        model.addAttribute("creditLimit", creditLimit);
        model.addAttribute("availableCredit", availableCredit);
        model.addAttribute("totalSpent", totalSpent);
        model.addAttribute("thisMonthSpent", thisMonthSpent);
        model.addAttribute("formattedDate", formattedDate);
        model.addAttribute("udhariRecords", userUdhariList);
        model.addAttribute("unreadNotifsCount", unreadNotifs);
        model.addAttribute("recentNotifications", notificationService.getUserNotifications(user.getId()));
        model.addAttribute("activeOffers", offerRepository.findByActiveTrueOrderByCreatedAtDesc());
        model.addAttribute("weather", farmingService.getWeatherForecast(user.getDistrict() != null ? user.getDistrict() : "Sangli"));
        model.addAttribute("shopUpiId", shopUpiId);

        return "customer/dashboard";
    }

    @GetMapping("/orders")
    public String orderHistory(
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size,
            Model model) {
        User user = getAuthenticatedCustomer();
        model.addAttribute("orderPage", orderService.getUserOrders(user.getId(), PageRequest.of(page, size)));
        return "customer/order-history";
    }

    @GetMapping("/orders/{id}")
    public String orderDetails(@PathVariable Long id, Model model) {
        User user = getAuthenticatedCustomer();
        Order order = orderService.getOrderById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Order not found with id: " + id));

        if (!order.getUser().getId().equals(user.getId()) && !securityUtil.isAdmin()) {
            throw new ResourceNotFoundException("Unauthorized order access");
        }

        model.addAttribute("order", order);
        return "customer/order-details";
    }

    @GetMapping("/orders/{id}/invoice")
    public String downloadInvoice(@PathVariable Long id, Model model) {
        User user = getAuthenticatedCustomer();
        Order order = orderService.getOrderById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Order not found with id: " + id));

        if (!order.getUser().getId().equals(user.getId()) && !securityUtil.isAdmin()) {
            throw new ResourceNotFoundException("Unauthorized invoice access");
        }

        model.addAttribute("order", order);
        model.addAttribute("shopName", shopName);
        model.addAttribute("shopGstin", shopGstin);
        model.addAttribute("shopAddress", shopAddress);
        model.addAttribute("shopMobile", shopMobile);
        model.addAttribute("shopEmail", shopEmail);
        model.addAttribute("shopUpiId", shopUpiId);

        return "invoice/invoice";
    }

    @GetMapping("/udhari")
    public String myUdhari(Model model) {
        User user = getAuthenticatedCustomer();
        BigDecimal remaining = udhariService.getUserRemainingUdhari(user.getId());
        List<com.krushisevakendra.entity.Udhari> list = udhariService.getUserUdhariList(user.getId());
        
        BigDecimal userTotalCredit = BigDecimal.ZERO;
        BigDecimal userTotalPaid = BigDecimal.ZERO;
        java.time.LocalDate earliestDueDate = null;

        for (com.krushisevakendra.entity.Udhari u : list) {
            if (u.getTotalAmount() != null) userTotalCredit = userTotalCredit.add(u.getTotalAmount());
            if (u.getPaidAmount() != null) userTotalPaid = userTotalPaid.add(u.getPaidAmount());
            if (u.getRemainingAmount() != null && u.getRemainingAmount().compareTo(BigDecimal.ZERO) > 0 && u.getDueDate() != null) {
                if (earliestDueDate == null || u.getDueDate().isBefore(earliestDueDate)) {
                    earliestDueDate = u.getDueDate();
                }
            }
        }

        model.addAttribute("remainingBalance", remaining != null ? remaining : BigDecimal.ZERO);
        model.addAttribute("userTotalCredit", userTotalCredit);
        model.addAttribute("userTotalPaid", userTotalPaid);
        model.addAttribute("earliestDueDate", earliestDueDate);
        model.addAttribute("udhariList", list);
        model.addAttribute("paymentsList", paymentService.getUserPayments(user.getId(), PageRequest.of(0, 20)).getContent());
        model.addAttribute("shopUpiId", shopUpiId);
        model.addAttribute("shopName", shopName);
        return "customer/udhari";
    }

    @GetMapping("/payments")
    public String paymentHistory(
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "10") int size,
            Model model) {
        User user = getAuthenticatedCustomer();
        model.addAttribute("paymentPage", paymentService.getUserPayments(user.getId(), PageRequest.of(page, size)));
        return "customer/payment-history";
    }

    @GetMapping("/pay")
    public String payNow(Model model) {
        User user = getAuthenticatedCustomer();
        model.addAttribute("user", user);
        return "customer/pay";
    }

    @GetMapping("/payments/{id}/receipt")
    public String paymentReceipt(@PathVariable Long id, Model model) {
        User user = getAuthenticatedCustomer();
        Payment payment = paymentService.getPaymentById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Payment not found with id: " + id));

        if (!payment.getUser().getId().equals(user.getId()) && !securityUtil.isAdmin()) {
            throw new ResourceNotFoundException("Unauthorized receipt access");
        }

        model.addAttribute("payment", payment);
        model.addAttribute("shopName", shopName);
        model.addAttribute("shopGstin", shopGstin);
        model.addAttribute("shopAddress", shopAddress);
        model.addAttribute("shopMobile", shopMobile);
        return "invoice/payment-receipt";
    }

    @GetMapping("/notifications")
    public String notifications(
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "15") int size,
            Model model) {
        User user = getAuthenticatedCustomer();
        model.addAttribute("notificationPage", notificationService.getUserNotificationsPaged(user.getId(), PageRequest.of(page, size)));
        return "customer/notifications";
    }

    @PostMapping("/notifications/{id}/read")
    public String markNotificationRead(@PathVariable Long id) {
        notificationService.markAsRead(id);
        return "redirect:/customer/notifications";
    }

    @PostMapping("/notifications/read-all")
    public String markAllNotificationsRead() {
        User user = getAuthenticatedCustomer();
        notificationService.markAllAsRead(user.getId());
        return "redirect:/customer/notifications";
    }

    @GetMapping("/profile")
    public String profile(Model model) {
        User user = getAuthenticatedCustomer();
        model.addAttribute("user", user);
        return "customer/profile";
    }

    @PostMapping("/profile")
    public String updateProfile(
            @ModelAttribute User userForm,
            RedirectAttributes redirectAttributes) {
        User user = getAuthenticatedCustomer();
        userService.updateProfile(user.getId(), userForm);
        redirectAttributes.addFlashAttribute("successMessage", "Profile updated successfully / माहिती अद्ययावत केली.");
        return "redirect:/customer/profile";
    }
}
