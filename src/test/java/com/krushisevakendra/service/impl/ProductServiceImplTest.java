package com.krushisevakendra.service.impl;

import com.krushisevakendra.entity.Product;
import com.krushisevakendra.repository.CategoryRepository;
import com.krushisevakendra.repository.ProductRepository;
import com.krushisevakendra.service.InventoryService;
import org.junit.jupiter.api.Test;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertSame;
import static org.mockito.Mockito.*;

class ProductServiceImplTest {

    @Test
    void activeProductLookupFiltersByStatus() {
        ProductRepository productRepository = mock(ProductRepository.class);
        Product expected = new Product();
        when(productRepository.findByIdAndStatus(17L, "ACTIVE")).thenReturn(Optional.of(expected));
        ProductServiceImpl service = new ProductServiceImpl(
                productRepository,
                mock(CategoryRepository.class),
                mock(InventoryService.class),
                "uploads"
        );

        Optional<Product> actual = service.getActiveProductById(17L);

        assertSame(expected, actual.orElseThrow());
        verify(productRepository).findByIdAndStatus(17L, "ACTIVE");
        verify(productRepository, never()).findById(17L);
    }
}
