package com.krushisevakendra.controller;

import com.krushisevakendra.dto.CartDto;
import com.krushisevakendra.dto.CartItemDto;
import com.krushisevakendra.dto.CheckoutDto;
import com.krushisevakendra.entity.Offer;
import com.krushisevakendra.entity.Order;
import com.krushisevakendra.entity.Product;
import com.krushisevakendra.entity.User;
import com.krushisevakendra.exception.ResourceNotFoundException;
import com.krushisevakendra.repository.OfferRepository;
import com.krushisevakendra.security.SecurityUtil;
import com.krushisevakendra.service.OrderService;
import com.krushisevakendra.service.ProductService;
import jakarta.servlet.http.HttpSession;
import jakarta.validation.Valid;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import org.springframework.beans.factory.annotation.Value;
import com.krushisevakendra.exception.InsufficientStockException;

import java.math.BigDecimal;
import java.util.Optional;

@Controller
@RequestMapping("/cart")
public class CartController {

    private static final String CART_SESSION_KEY = "KRUSHI_CART";

    private final ProductService productService;
    private final OrderService orderService;
    private final OfferRepository offerRepository;
    private final SecurityUtil securityUtil;

    @Value("${app.shop.upi-id}")
    private String shopUpiId;

    public CartController(ProductService productService,
                          OrderService orderService,
                          OfferRepository offerRepository,
                          SecurityUtil securityUtil) {
        this.productService = productService;
        this.orderService = orderService;
        this.offerRepository = offerRepository;
        this.securityUtil = securityUtil;
    }

    private CartDto getOrCreateCart(HttpSession session) {
        CartDto cart = (CartDto) session.getAttribute(CART_SESSION_KEY);
        if (cart == null) {
            cart = new CartDto();
            session.setAttribute(CART_SESSION_KEY, cart);
        }
        return cart;
    }

    @GetMapping
    public String viewCart(HttpSession session, Model model) {
        CartDto cart = getOrCreateCart(session);
        model.addAttribute("cart", cart);
        return "customer/cart";
    }

    @PostMapping("/add")
    public String addToCart(
            @RequestParam Long productId,
            @RequestParam(defaultValue = "1") Integer quantity,
            @RequestParam(required = false) String returnUrl,
            HttpSession session,
            RedirectAttributes redirectAttributes) {

        Product product = productService.getProductById(productId)
                .orElseThrow(() -> new ResourceNotFoundException("Product not found with id: " + productId));

        if (quantity == null || quantity <= 0) {
            redirectAttributes.addFlashAttribute("errorMessage", "Quantity must be greater than zero.");
            return "redirect:" + safeReturnUrl(returnUrl, "/products/" + productId);
        }
        if (!"ACTIVE".equalsIgnoreCase(product.getStatus())) {
            redirectAttributes.addFlashAttribute("errorMessage", "This product is no longer available.");
            return "redirect:" + safeReturnUrl(returnUrl, "/products");
        }
        if (product.getStockQuantity() == null || product.getStockQuantity() < quantity) {
            redirectAttributes.addFlashAttribute("errorMessage", "Insufficient stock available for " + product.getName());
            return "redirect:" + safeReturnUrl(returnUrl, "/products/" + productId);
        }

        CartDto cart = getOrCreateCart(session);
        cart.addItem(new CartItemDto(product, quantity));

        redirectAttributes.addFlashAttribute("successMessage", product.getName() + " added to your cart / कार्टमध्ये जोडले!");
        return "redirect:" + safeReturnUrl(returnUrl, "/cart");
    }

    private String safeReturnUrl(String returnUrl, String fallback) {
        return returnUrl != null && returnUrl.startsWith("/products")
                && !returnUrl.startsWith("//") && !returnUrl.contains("\\")
                ? returnUrl
                : fallback;
    }

    @PostMapping("/update")
    public String updateQuantity(
            @RequestParam Long productId,
            @RequestParam Integer quantity,
            HttpSession session,
            RedirectAttributes redirectAttributes) {

        if (quantity == null || quantity <= 0) {
            redirectAttributes.addFlashAttribute("errorMessage", "Quantity must be greater than zero.");
            return "redirect:/cart";
        }
        CartDto cart = getOrCreateCart(session);
        cart.updateQuantity(productId, quantity);
        return "redirect:/cart";
    }

    @PostMapping("/remove")
    public String removeItem(
            @RequestParam Long productId,
            HttpSession session,
            RedirectAttributes redirectAttributes) {

        CartDto cart = getOrCreateCart(session);
        cart.removeItem(productId);
        redirectAttributes.addFlashAttribute("successMessage", "Item removed from cart / कार्टमधून काढले.");
        return "redirect:/cart";
    }

    @PostMapping("/apply-coupon")
    public String applyCoupon(
            @RequestParam String couponCode,
            HttpSession session,
            RedirectAttributes redirectAttributes) {

        CartDto cart = getOrCreateCart(session);
        if (couponCode == null || couponCode.isBlank()) {
            cart.setCouponCode(null);
            cart.setDiscountAmount(BigDecimal.ZERO);
            return "redirect:/cart";
        }

        cart.setCouponCode(null);
        cart.setDiscountAmount(BigDecimal.ZERO);
        Optional<Offer> offerOpt = offerRepository.findByCouponCodeAndActiveTrue(couponCode.trim().toUpperCase());
        if (offerOpt.isPresent() && offerOpt.get().isValid()) {
            Offer offer = offerOpt.get();
            BigDecimal discount = offer.calculateDiscount(cart.getSubtotal());
            if (discount.compareTo(BigDecimal.ZERO) > 0) {
                cart.setCouponCode(offer.getCouponCode());
                cart.setDiscountAmount(discount);
                redirectAttributes.addFlashAttribute("successMessage", "Coupon applied! Discount: ₹" + discount);
            } else {
                redirectAttributes.addFlashAttribute("errorMessage", "Minimum order amount of ₹" + offer.getMinOrderAmount() + " required for this coupon.");
            }
        } else {
            redirectAttributes.addFlashAttribute("errorMessage", "Invalid or expired coupon code / अमान्य कूपन कोड.");
        }

        return "redirect:/cart";
    }

    @GetMapping("/checkout")
    public String checkoutForm(HttpSession session, Model model) {
        CartDto cart = getOrCreateCart(session);
        if (cart.getItems().isEmpty()) {
            return "redirect:/products";
        }

        CheckoutDto checkoutDto = new CheckoutDto();
        Optional<User> currentUser = securityUtil.getCurrentUser();
        if (currentUser.isPresent()) {
            User user = currentUser.get();
            checkoutDto.setCustomerName(user.getName());
            checkoutDto.setMobile(user.getMobile());
            checkoutDto.setDeliveryAddress(user.getAddress());
            checkoutDto.setVillage(user.getVillage());
            checkoutDto.setTaluka(user.getTaluka());
            checkoutDto.setDistrict(user.getDistrict());
        }

        model.addAttribute("cart", cart);
        model.addAttribute("shopUpiId", shopUpiId);
        model.addAttribute("checkoutDto", checkoutDto);
        return "customer/checkout";
    }

    @PostMapping("/checkout")
    public String processCheckout(
            @Valid @ModelAttribute("checkoutDto") CheckoutDto checkoutDto,
            BindingResult bindingResult,
            HttpSession session,
            Model model,
            RedirectAttributes redirectAttributes) {

        CartDto cart = getOrCreateCart(session);
        if (cart.getItems().isEmpty()) {
            return "redirect:/products";
        }

        if (bindingResult.hasErrors()) {
            model.addAttribute("cart", cart);
            model.addAttribute("shopUpiId", shopUpiId);
            return "customer/checkout";
        }

        User user = securityUtil.getCurrentUser().orElseThrow(() -> new ResourceNotFoundException("Logged in user not found"));

        try {
            Order order = orderService.createOrder(user, cart, checkoutDto);
            cart.clear(); // Clear cart after successful checkout
            redirectAttributes.addFlashAttribute("orderSuccess", true);
            return "redirect:/customer/orders/" + order.getId() + "?success=true";
        } catch (InsufficientStockException | IllegalArgumentException e) {
            model.addAttribute("cart", cart);
            model.addAttribute("checkoutDto", checkoutDto);
            model.addAttribute("shopUpiId", shopUpiId);
            model.addAttribute("errorMessage", e.getMessage());
            return "customer/checkout";
        }
    }
}
