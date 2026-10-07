package com.krushisevakendra.controller;

import com.krushisevakendra.dto.UserRegistrationDto;
import com.krushisevakendra.entity.Role;
import com.krushisevakendra.entity.User;
import com.krushisevakendra.enums.RoleName;
import com.krushisevakendra.repository.RoleRepository;
import com.krushisevakendra.repository.UserRepository;
import com.krushisevakendra.security.CustomUserDetails;
import com.krushisevakendra.service.UserService;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.validation.Valid;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.web.context.HttpSessionSecurityContextRepository;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.ArrayList;
import java.util.List;

@Controller
public class AuthController {

    private final UserService userService;
    private final UserRepository userRepository;
    private final RoleRepository roleRepository;

    public AuthController(UserService userService, UserRepository userRepository, RoleRepository roleRepository) {
        this.userService = userService;
        this.userRepository = userRepository;
        this.roleRepository = roleRepository;
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
    public String adminSwitch() {
        return "redirect:/login";
    }

    @GetMapping("/farmer-switch")
    public String farmerSwitch() {
        return "redirect:/login";
    }
}
