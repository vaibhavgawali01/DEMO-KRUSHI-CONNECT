package com.krushisevakendra.config;

import com.krushisevakendra.entity.CustomerLoginHistory;
import com.krushisevakendra.repository.CustomerLoginHistoryRepository;
import com.krushisevakendra.security.CustomUserDetails;
import com.krushisevakendra.security.CustomUserDetailsService;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.dao.DaoAuthenticationProvider;
import org.springframework.security.config.annotation.authentication.configuration.AuthenticationConfiguration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configurers.HeadersConfigurer;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.AuthenticationSuccessHandler;

import java.time.LocalDateTime;

@Configuration
@EnableWebSecurity
public class SecurityConfig {

    private final CustomUserDetailsService userDetailsService;
    private final CustomerLoginHistoryRepository customerLoginHistoryRepository;

    public SecurityConfig(CustomUserDetailsService userDetailsService,
                          CustomerLoginHistoryRepository customerLoginHistoryRepository) {
        this.userDetailsService = userDetailsService;
        this.customerLoginHistoryRepository = customerLoginHistoryRepository;
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    @Bean
    public DaoAuthenticationProvider authenticationProvider() {
        DaoAuthenticationProvider authProvider = new DaoAuthenticationProvider();
        authProvider.setUserDetailsService(userDetailsService);
        authProvider.setPasswordEncoder(passwordEncoder());
        return authProvider;
    }

    @Bean
    public AuthenticationManager authenticationManager(AuthenticationConfiguration authConfig) throws Exception {
        return authConfig.getAuthenticationManager();
    }

    @Bean
    public AuthenticationSuccessHandler customAuthenticationSuccessHandler() {
        return (request, response, authentication) -> {
            Object principal = authentication.getPrincipal();
            if (principal instanceof CustomUserDetails userDetails
                    && authentication.getAuthorities().stream()
                    .anyMatch(authority -> authority.getAuthority().equals("ROLE_CUSTOMER"))) {
                customerLoginHistoryRepository.save(
                        new CustomerLoginHistory(userDetails.getUser(), LocalDateTime.now()));
            }

            boolean isAdminRole = authentication.getAuthorities().stream()
                    .anyMatch(a -> a.getAuthority().equals("ROLE_ADMIN"));

            if (isAdminRole) {
                response.sendRedirect("/admin/dashboard");
            } else {
                response.sendRedirect("/farmer/dashboard");
            }
        };
    }

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .csrf(csrf -> csrf
                .ignoringRequestMatchers("/h2-console/**", "/api/**")
            )
            .headers(headers -> headers
                .frameOptions(HeadersConfigurer.FrameOptionsConfig::disable) // Needed for H2 console
            )
            .authorizeHttpRequests(auth -> auth
                // Static resources
                .requestMatchers("/css/**", "/js/**", "/images/**", "/uploads/**", "/webjars/**", "/favicon.ico", "/error").permitAll()
                // Public views and pages
                .requestMatchers("/", "/home", "/products/**", "/categories/**", "/offers/**", 
                                 "/farming-tips/**", "/weather/**", "/fertilizer-calculator/**", 
                                 "/crop-care/**", "/about/**", "/contact/**", "/faq/**", 
                                 "/login", "/register", "/forgot-password", "/admin-switch", "/farmer-switch", "/h2-console/**").permitAll()
                // Public REST APIs
                .requestMatchers("/api/auth/**", "/api/products/**", "/api/categories/**", "/api/farming/**", "/api/offers/**").permitAll()
                // Admin-only area (Strictly only ROLE_ADMIN)
                .requestMatchers("/admin", "/admin/**", "/api/admin/**").hasAuthority("ROLE_ADMIN")
                // Customer & Farmer authenticated area
                .requestMatchers("/customer/**", "/farmer/**", "/cart/**", "/checkout/**", "/orders/**",
                                 "/my-udhari/**", "/my-profile/**", "/invoice/**", "/payment-receipt/**").hasAuthority("ROLE_CUSTOMER")
                .anyRequest().authenticated()
            )
            .exceptionHandling(exceptions -> exceptions
                .accessDeniedHandler((request, response, accessDeniedException) -> {
                    org.springframework.security.core.Authentication auth = 
                        org.springframework.security.core.context.SecurityContextHolder.getContext().getAuthentication();
                    if (auth != null && auth.isAuthenticated() && !"anonymousUser".equals(auth.getName())) {
                        boolean isAdmin = auth.getAuthorities().stream()
                                .anyMatch(authority -> authority.getAuthority().equals("ROLE_ADMIN"));
                        response.sendRedirect(isAdmin ? "/admin/dashboard" : "/farmer/dashboard");
                    } else {
                        response.sendRedirect("/login");
                    }
                })
            )
            .formLogin(form -> form
                .loginPage("/login")
                .loginProcessingUrl("/login")
                .usernameParameter("username") // Supports Email or Mobile number
                .passwordParameter("password")
                .successHandler(customAuthenticationSuccessHandler())
                .failureUrl("/login?error=true")
                .permitAll()
            )
            .logout(logout -> logout
                .logoutRequestMatcher(new org.springframework.security.web.util.matcher.AntPathRequestMatcher("/logout"))
                .logoutSuccessUrl("/login?logout=true")
                .invalidateHttpSession(true)
                .clearAuthentication(true)
                .deleteCookies("JSESSIONID")
                .permitAll()
            )
            .rememberMe(remember -> remember
                .key("krushiSevaSecretRememberMeKey2026")
                .tokenValiditySeconds(86400 * 14) // 14 days
                .userDetailsService(userDetailsService)
            );

        return http.build();
    }
}
