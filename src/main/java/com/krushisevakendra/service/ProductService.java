package com.krushisevakendra.service;

import com.krushisevakendra.dto.ProductDto;
import com.krushisevakendra.entity.Product;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

import java.util.List;
import java.util.Optional;

public interface ProductService {
    List<Product> getAllActiveProducts();
    List<Product> getFeaturedProducts();
    List<Product> getProductsByCategory(Long categoryId);
    Optional<Product> getProductById(Long id);
    Optional<Product> getProductByBarcode(String barcode);
    Optional<Product> getProductBySku(String sku);
    Page<Product> searchAndFilter(Long categoryId, String company, Double minPrice, Double maxPrice, boolean inStockOnly, String keyword, Pageable pageable);
    Page<Product> getAllProductsPaged(Pageable pageable);
    List<Product> getAllProducts();
    Product saveProduct(ProductDto dto);
    Product updateProduct(Long id, ProductDto dto);
    void deleteProduct(Long id);
    List<Product> getLowStockProducts();
    List<Product> getExpiredProducts();
    List<Product> getExpiringSoonProducts(int days);
    List<String> getAllBrands();
    long getTotalProductCount();
    java.math.BigDecimal getTotalInventoryValue();
    Page<Product> filterAdminProducts(Long categoryId, String status, String stockStatus, String keyword, Pageable pageable);
}
