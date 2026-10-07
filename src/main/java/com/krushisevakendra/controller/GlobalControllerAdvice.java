package com.krushisevakendra.controller;

import com.krushisevakendra.dto.CartDto;
import com.krushisevakendra.entity.User;
import com.krushisevakendra.security.SecurityUtil;
import com.krushisevakendra.service.NotificationService;
import jakarta.servlet.http.HttpSession;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ModelAttribute;

@ControllerAdvice
public class GlobalControllerAdvice {

    private final SecurityUtil securityUtil;
    private final NotificationService notificationService;

    public GlobalControllerAdvice(SecurityUtil securityUtil, NotificationService notificationService) {
        this.securityUtil = securityUtil;
        this.notificationService = notificationService;
    }

    @ModelAttribute("currentUser")
    public User getCurrentUser() {
        return securityUtil.getCurrentUser().orElse(null);
    }

    @ModelAttribute("user")
    public User getUser() {
        return securityUtil.getCurrentUser().orElse(null);
    }

    @ModelAttribute("isMasterAdmin")
    public boolean isMasterAdmin() {
        return securityUtil.getCurrentUser()
                .map(u -> "admin@krushiseva.com".equalsIgnoreCase(u.getEmail()))
                .orElse(false);
    }

    @ModelAttribute("isFarmer")
    public boolean isFarmer() {
        return securityUtil.getCurrentUser()
                .map(u -> !"admin@krushiseva.com".equalsIgnoreCase(u.getEmail()))
                .orElse(false);
    }

    @ModelAttribute("unreadNotifsCount")
    public long getUnreadNotifsCount() {
        return securityUtil.getCurrentUserId()
                .map(notificationService::getUnreadCount)
                .orElse(0L);
    }

    @ModelAttribute("cartItemCount")
    public int getCartItemCount(HttpSession session) {
        if (session == null) return 0;
        CartDto cart = (CartDto) session.getAttribute("KRUSHI_CART");
        return cart != null ? cart.getTotalItemCount() : 0;
    }
}
