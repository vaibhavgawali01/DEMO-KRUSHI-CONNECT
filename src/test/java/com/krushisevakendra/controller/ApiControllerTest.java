package com.krushisevakendra.controller;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.krushisevakendra.entity.Category;
import com.krushisevakendra.entity.Product;
import com.krushisevakendra.service.CategoryService;
import com.krushisevakendra.service.FarmingService;
import com.krushisevakendra.service.NotificationService;
import com.krushisevakendra.service.ProductService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.http.HttpStatus;

import java.math.BigDecimal;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

class ApiControllerTest {

    private ProductService productService;
    private ApiController controller;
    private final ObjectMapper objectMapper = new ObjectMapper();

    @BeforeEach
    void setUp() {
        productService = mock(ProductService.class);
        controller = new ApiController(
                productService,
                mock(CategoryService.class),
                mock(FarmingService.class),
                mock(NotificationService.class)
        );
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
