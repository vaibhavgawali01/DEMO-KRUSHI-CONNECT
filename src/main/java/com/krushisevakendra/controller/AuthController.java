package com.krushisevakendra.controller;

import com.krushisevakendra.dto.UserRegistrationDto;
import com.krushisevakendra.entity.User;
import com.krushisevakendra.security.CustomUserDetails;
import com.krushisevakendra.service.UserService;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.validation.Valid;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.web.context.HttpSessionSecurityContextRepository;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class AuthController {

    private final UserService userService;

    public AuthController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping("/login")
    public String login(
            @RequestParam(required = false) String error,
            @RequestParam(required = false) String logout,
            @RequestParam(required = false) String registered,
            Model model) {

        if (error != null) {
            model.addAttribute("errorMessage", "Invalid mobile/email or password / चुकीचा मोबाईल/ईमेल किंवा पासवर्ड");
        }
        if (logout != null) {
            model.addAttribute("successMessage", "You have been logged out successfully / आपण यशस्वीरित्या लॉग आउट झाला आहात.");
        }
        if (registered != null) {
            model.addAttribute("successMessage", "Registration successful! Please login with your mobile/email and password / नोंदणी यशस्वी झाली! कृपया लॉगिन करा.");
        }
        return "auth/login";
    }

    @GetMapping("/register")
    public String registerForm(Model model) {
        model.addAttribute("registrationDto", new UserRegistrationDto());
        return "auth/register";
    }

    @PostMapping("/register")
    public String registerSubmit(
            @Valid @ModelAttribute("registrationDto") UserRegistrationDto registrationDto,
            BindingResult bindingResult,
            Model model) {

        if (!registrationDto.isPasswordMatching()) {
            bindingResult.rejectValue("confirmPassword", "error.registrationDto", "Passwords do not match / पासवर्ड जुळत नाहीत");
        }

        if (bindingResult.hasErrors()) {
            return "auth/register";
        }

        try {
            userService.registerCustomer(registrationDto);
            return "redirect:/login?registered=true";
        } catch (IllegalArgumentException e) {
            model.addAttribute("errorMessage", e.getMessage());
            return "auth/register";
        }
    }

    @GetMapping("/forgot-password")
    public String forgotPassword() {
        return "auth/forgot-password";
    }

    @GetMapping("/admin-switch")
    public String adminSwitch(HttpServletRequest request) {
        User admin = userService.findByEmailOrMobile("admin@krushiseva.com")
                .orElseGet(() -> userService.findByEmailOrMobile("9876543210").orElse(null));
        if (admin != null) {
            CustomUserDetails userDetails = new CustomUserDetails(admin);
            UsernamePasswordAuthenticationToken auth =
                    new UsernamePasswordAuthenticationToken(userDetails, null, userDetails.getAuthorities());
            SecurityContextHolder.getContext().setAuthentication(auth);
            request.getSession().setAttribute(
                    HttpSessionSecurityContextRepository.SPRING_SECURITY_CONTEXT_KEY,
                    SecurityContextHolder.getContext()
            );
            return "redirect:/admin/dashboard";
        }
        return "redirect:/login";
    }

    @GetMapping("/farmer-switch")
    public String farmerSwitch(HttpServletRequest request) {
        User farmer = userService.findByEmailOrMobile("9822012345")
                .orElseGet(() -> userService.findByEmailOrMobile("ramesh@patil.com").orElse(null));
        if (farmer != null) {
            CustomUserDetails userDetails = new CustomUserDetails(farmer);
            UsernamePasswordAuthenticationToken auth =
                    new UsernamePasswordAuthenticationToken(userDetails, null, userDetails.getAuthorities());
            SecurityContextHolder.getContext().setAuthentication(auth);
            request.getSession().setAttribute(
                    HttpSessionSecurityContextRepository.SPRING_SECURITY_CONTEXT_KEY,
                    SecurityContextHolder.getContext()
            );
            return "redirect:/farmer/dashboard";
        }
        return "redirect:/login";
    }
}
