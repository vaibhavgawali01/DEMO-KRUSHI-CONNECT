package com.krushisevakendra.controller;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.krushisevakendra.entity.Category;
import com.krushisevakendra.entity.Product;
import com.krushisevakendra.entity.User;
import com.krushisevakendra.repository.UdhariRepository;
import com.krushisevakendra.repository.UserRepository;
import com.krushisevakendra.security.CustomUserDetails;
import com.krushisevakendra.service.*;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.http.HttpStatus;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.context.SecurityContext;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.crypto.password.PasswordEncoder;

import java.math.BigDecimal;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

class ApiControllerTest {

    private ProductService productService;
    private UserService userService;
    private UserRepository userRepository;
    private UdhariRepository udhariRepository;
    private PasswordEncoder passwordEncoder;
    private ApiController controller;
    private final ObjectMapper objectMapper = new ObjectMapper();

    @BeforeEach
    void setUp() {
        productService = mock(ProductService.class);
        userService = mock(UserService.class);
        userRepository = mock(UserRepository.class);
        udhariRepository = mock(UdhariRepository.class);
        passwordEncoder = mock(PasswordEncoder.class);

        controller = new ApiController(
                productService,
                mock(CategoryService.class),
                mock(FarmingService.class),
                mock(NotificationService.class),
                userService,
                mock(UdhariService.class),
                mock(OrderService.class),
                userRepository,
                udhariRepository,
                passwordEncoder
        );
    }

    @AfterEach
    void tearDown() {
        SecurityContextHolder.clearContext();
    }

    @Test
    void productByIdReturnsOnlyActivePublicProductSummary() {
        Product product = createProduct();
        when(productService.getActiveProductById(12L)).thenReturn(Optional.of(product));

        var response = controller.getProductById(12L);

        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertEquals(12L, response.getBody().getData().id());
        assertEquals("Urea", response.getBody().getData().name());
        assertEquals("Fertilizers", response.getBody().getData().category().name());

        JsonNode json = objectMapper.valueToTree(response.getBody().getData());
        assertFalse(json.has("stockQuantity"));
        assertFalse(json.has("minimumStock"));
        assertFalse(json.has("batchNumber"));
        assertFalse(json.has("expiryDate"));
        assertFalse(json.has("barcode"));
        assertFalse(json.has("sku"));
    }

    @Test
    void productByIdReturnsNotFoundWhenProductIsNotActive() {
        when(productService.getActiveProductById(12L)).thenReturn(Optional.empty());

        var response = controller.getProductById(12L);

        assertEquals(HttpStatus.NOT_FOUND, response.getStatusCode());
        verify(productService).getActiveProductById(12L);
        verify(productService, never()).getProductById(12L);
    }

    @Test
    void getAdminStatsRejectsUnauthenticated() {
        var response = controller.getAdminStats();
        assertEquals(HttpStatus.FORBIDDEN, response.getStatusCode());
    }

    @Test
    void addUdhariRejectsUnauthenticated() {
        Map<String, Object> payload = Map.of("amount", 500, "mobile", "9822012345");
        var response = controller.addUdhariTransaction(payload);
        assertEquals(HttpStatus.FORBIDDEN, response.getStatusCode());
    }

    @Test
    void addUdhariRejectsWhenFarmerNotFoundWithoutCreatingAccount() {
        Authentication auth = mock(Authentication.class);
        when(auth.isAuthenticated()).thenReturn(true);
        doReturn(List.of(new SimpleGrantedAuthority("ROLE_ADMIN"))).when(auth).getAuthorities();
        SecurityContext securityContext = mock(SecurityContext.class);
        when(securityContext.getAuthentication()).thenReturn(auth);
        SecurityContextHolder.setContext(securityContext);

        when(userRepository.findByMobile("9999999999")).thenReturn(Optional.empty());
        when(userRepository.findAllCustomers()).thenReturn(Collections.emptyList());

        Map<String, Object> payload = Map.of("amount", 500, "mobile", "9999999999");
        var response = controller.addUdhariTransaction(payload);

        assertEquals(HttpStatus.NOT_FOUND, response.getStatusCode());
        verify(userService, never()).registerCustomer(any());
    }

    @Test
    void getFarmerLedgerRejectsUnauthenticated() {
        var response = controller.getFarmerLedger("9822012345", null, null, null);
        assertEquals(HttpStatus.UNAUTHORIZED, response.getStatusCode());
    }

    @Test
    void getFarmerLedgerForbidsAccessToAnotherFarmersData() {
        User loggedInUser = new User();
        loggedInUser.setId(101L);
        loggedInUser.setMobile("9822011111");
        loggedInUser.setName("Farmer A");
        CustomUserDetails userDetails = new CustomUserDetails(loggedInUser);

        Authentication auth = mock(Authentication.class);
        when(auth.isAuthenticated()).thenReturn(true);
        when(auth.getPrincipal()).thenReturn(userDetails);
        doReturn(List.of(new SimpleGrantedAuthority("ROLE_CUSTOMER"))).when(auth).getAuthorities();
        SecurityContext securityContext = mock(SecurityContext.class);
        when(securityContext.getAuthentication()).thenReturn(auth);
        SecurityContextHolder.setContext(securityContext);

        User otherFarmer = new User();
        otherFarmer.setId(202L);
        otherFarmer.setMobile("9822022222");
        when(userRepository.findByMobile("9822022222")).thenReturn(Optional.of(otherFarmer));

        var response = controller.getFarmerLedger("9822022222", null, null, null);
        assertEquals(HttpStatus.FORBIDDEN, response.getStatusCode());
    }

    @Test
    void getFarmerLedgerAllowsCustomerToViewOwnData() {
        User loggedInUser = new User();
        loggedInUser.setId(101L);
        loggedInUser.setMobile("9822011111");
        loggedInUser.setName("Farmer A");
        CustomUserDetails userDetails = new CustomUserDetails(loggedInUser);

        Authentication auth = mock(Authentication.class);
        when(auth.isAuthenticated()).thenReturn(true);
        when(auth.getPrincipal()).thenReturn(userDetails);
        doReturn(List.of(new SimpleGrantedAuthority("ROLE_CUSTOMER"))).when(auth).getAuthorities();
        SecurityContext securityContext = mock(SecurityContext.class);
        when(securityContext.getAuthentication()).thenReturn(auth);
        SecurityContextHolder.setContext(securityContext);

        when(userRepository.findByMobile("9822011111")).thenReturn(Optional.of(loggedInUser));
        when(udhariRepository.findByUserIdOrderByCreatedAtDesc(101L)).thenReturn(Collections.emptyList());

        var response = controller.getFarmerLedger("9822011111", null, null, null);
        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertNotNull(response.getBody());
        assertEquals("KSK-9822011111", response.getBody().getData().get("farmerId"));
    }

    private Product createProduct() {
        Category category = new Category();
        category.setId(4L);
        category.setName("Fertilizers");
        category.setNameMr("खते");

        Product product = new Product();
        product.setId(12L);
        product.setName("Urea");
        product.setNameMr("युरिया");
        product.setCompany("Example Company");
        product.setPrice(new BigDecimal("500.00"));
        product.setCategory(category);
        product.setStockQuantity(80);
        product.setBatchNumber("BATCH-PRIVATE");
        product.setBarcode("BARCODE-PRIVATE");
        product.setSku("SKU-PRIVATE");
        return product;
    }
}
