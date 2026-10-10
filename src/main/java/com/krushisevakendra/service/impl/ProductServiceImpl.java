package com.krushisevakendra.service.impl;

import com.krushisevakendra.dto.ProductDto;
import com.krushisevakendra.entity.Category;
import com.krushisevakendra.entity.Product;
import com.krushisevakendra.enums.InventoryTransactionType;
import com.krushisevakendra.exception.ResourceNotFoundException;
import com.krushisevakendra.repository.CategoryRepository;
import com.krushisevakendra.repository.ProductRepository;
import com.krushisevakendra.service.InventoryService;
import com.krushisevakendra.service.ProductService;
import org.springframework.context.annotation.Lazy;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.math.BigDecimal;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Service
@Transactional
public class ProductServiceImpl implements ProductService {

    private final ProductRepository productRepository;
    private final CategoryRepository categoryRepository;
    private final InventoryService inventoryService;
    private final Path uploadDirectory;

    public ProductServiceImpl(ProductRepository productRepository, 
                              CategoryRepository categoryRepository,
                              @Lazy InventoryService inventoryService,
                              @Value("${app.upload.dir:uploads}") String uploadDirectory) {
        this.productRepository = productRepository;
        this.categoryRepository = categoryRepository;
        this.inventoryService = inventoryService;
        this.uploadDirectory = Paths.get(uploadDirectory).toAbsolutePath().normalize()
                .resolve("products");
    }

    @Override
    @Transactional(readOnly = true)
    public List<Product> getAllActiveProducts() {
        return productRepository.findByStatus("ACTIVE");
    }

    @Override
    @Transactional(readOnly = true)
    public List<Product> getFeaturedProducts() {
        return productRepository.findTop8ByStatusOrderByRatingDesc("ACTIVE");
    }

    @Override
    @Transactional(readOnly = true)
    public List<Product> getProductsByCategory(Long categoryId) {
        return productRepository.findByCategoryIdAndStatus(categoryId, "ACTIVE");
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<Product> getProductById(Long id) {
        return productRepository.findById(id);
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<Product> getProductByBarcode(String barcode) {
        return productRepository.findByBarcode(barcode);
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<Product> getProductBySku(String sku) {
        return productRepository.findBySku(sku);
    }

    @Override
    @Transactional(readOnly = true)
    public Page<Product> searchAndFilter(Long categoryId, String company, Double minPrice, Double maxPrice, boolean inStockOnly, String keyword, Pageable pageable) {
        String trimmedCompany = (company != null && !company.isBlank() && !"ALL".equalsIgnoreCase(company)) ? company.trim() : null;
        String trimmedKeyword = (keyword != null && !keyword.isBlank()) ? keyword.trim() : null;

        return productRepository.filterProducts(categoryId, trimmedCompany, minPrice, maxPrice, inStockOnly, "ACTIVE", trimmedKeyword, pageable);
    }

    @Override
    @Transactional(readOnly = true)
    public Page<Product> getAllProductsPaged(Pageable pageable) {
        return productRepository.findAll(pageable);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Product> getAllProducts() {
        return productRepository.findAll();
    }

    @Override
    public Product saveProduct(ProductDto dto) {
        Category category = categoryRepository.findById(dto.getCategoryId())
                .orElseThrow(() -> new ResourceNotFoundException("Category not found with id: " + dto.getCategoryId()));

        Product product = new Product();
        mapDtoToProduct(dto, product, category);
        product.setCreatedAt(LocalDateTime.now());
        product.setUpdatedAt(LocalDateTime.now());

        Product saved = productRepository.save(product);

        if (saved.getStockQuantity() > 0) {
            inventoryService.recordTransaction(saved, InventoryTransactionType.STOCK_IN, saved.getStockQuantity(), "Initial Stock Entry");
        }

        return saved;
    }

    @Override
    public Product updateProduct(Long id, ProductDto dto) {
        Product product = productRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Product not found with id: " + id));

        Category category = categoryRepository.findById(dto.getCategoryId())
                .orElseThrow(() -> new ResourceNotFoundException("Category not found with id: " + dto.getCategoryId()));

        int oldStock = product.getStockQuantity() != null ? product.getStockQuantity() : 0;
        int newStock = dto.getStockQuantity() != null ? dto.getStockQuantity() : 0;

        mapDtoToProduct(dto, product, category);
        product.setUpdatedAt(LocalDateTime.now());

        Product updated = productRepository.save(product);

        if (newStock != oldStock) {
            int diff = newStock - oldStock;
            InventoryTransactionType type = diff > 0 ? InventoryTransactionType.STOCK_IN : InventoryTransactionType.ADJUSTMENT;
            inventoryService.recordTransaction(updated, type, Math.abs(diff), "Stock Adjustment in Product Edit");
        }

        return updated;
    }

    @Override
    public void deleteProduct(Long id) {
        if (!productRepository.existsById(id)) {
            throw new ResourceNotFoundException("Product not found with id: " + id);
        }
        productRepository.deleteById(id);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Product> getLowStockProducts() {
        return productRepository.findLowStockProducts();
    }

    @Override
    @Transactional(readOnly = true)
    public List<Product> getExpiredProducts() {
        return productRepository.findExpiredProducts(LocalDate.now());
    }

    @Override
    @Transactional(readOnly = true)
    public List<Product> getExpiringSoonProducts(int days) {
        LocalDate today = LocalDate.now();
        LocalDate targetDate = today.plusDays(days);
        return productRepository.findExpiringSoonProducts(today, targetDate);
    }

    @Override
    @Transactional(readOnly = true)
    public List<String> getAllBrands() {
        return productRepository.findAllDistinctCompanies();
    }

    @Override
    @Transactional(readOnly = true)
    public long getTotalProductCount() {
        return productRepository.count();
    }

    @Override
    @Transactional(readOnly = true)
    public BigDecimal getTotalInventoryValue() {
        List<Product> products = productRepository.findAll();
        BigDecimal total = BigDecimal.ZERO;
        for (Product p : products) {
            if (p.getStockQuantity() != null && p.getPrice() != null && p.getStockQuantity() > 0) {
                total = total.add(p.getPrice().multiply(BigDecimal.valueOf(p.getStockQuantity())));
            }
        }
        return total;
    }

    @Override
    @Transactional(readOnly = true)
    public Page<Product> filterAdminProducts(Long categoryId, String status, String stockStatus, String keyword, Pageable pageable) {
        String trimmedStatus = (status != null && !status.isBlank() && !"ALL".equalsIgnoreCase(status)) ? status.trim().toUpperCase() : null;
        String trimmedStock = (stockStatus != null && !stockStatus.isBlank() && !"ALL".equalsIgnoreCase(stockStatus)) ? stockStatus.trim().toUpperCase() : null;
        String trimmedKeyword = (keyword != null && !keyword.isBlank()) ? keyword.trim() : null;

        return productRepository.filterAdminProducts(categoryId, trimmedStatus, trimmedStock, trimmedKeyword, pageable);
    }

    private void mapDtoToProduct(ProductDto dto, Product product, Category category) {
        product.setCategory(category);
        product.setName(dto.getName().trim());
        product.setNameMr(dto.getNameMr() != null ? dto.getNameMr().trim() : null);
        product.setCompany(dto.getCompany().trim());
        product.setSku(dto.getSku() != null && !dto.getSku().isBlank() ? dto.getSku().trim() : "SKU-" + System.currentTimeMillis());
        product.setBarcode(dto.getBarcode() != null && !dto.getBarcode().isBlank() ? dto.getBarcode().trim() : "890" + System.currentTimeMillis());
        product.setPrice(dto.getPrice());
        product.setDiscountPrice(dto.getDiscountPrice());
        product.setGstRate(dto.getGstRate() != null ? dto.getGstRate() : BigDecimal.ZERO);
        product.setDescription(dto.getDescription());
        product.setUsageInstructions(dto.getUsageInstructions());
        if (dto.getImageFile() != null && !dto.getImageFile().isEmpty()) {
            product.setImage(storeProductImage(dto.getImageFile()));
        } else if (dto.getExistingImage() != null && !dto.getExistingImage().isBlank()) {
            product.setImage(dto.getExistingImage());
        } else if (product.getImage() == null) {
            product.setImage("product_default.jpg");
        }
        product.setStockQuantity(dto.getStockQuantity());
        product.setMinimumStock(dto.getMinimumStock());
        product.setBatchNumber(dto.getBatchNumber());
        product.setExpiryDate(dto.getExpiryDate());
        if (dto.getStatus() != null) {
            product.setStatus(dto.getStatus());
        }
    }

    private String storeProductImage(MultipartFile imageFile) {
        String originalFilename = imageFile.getOriginalFilename();
        String extension = originalFilename == null || !originalFilename.contains(".")
                ? ""
                : originalFilename.substring(originalFilename.lastIndexOf('.') + 1).toLowerCase();
        String contentType = imageFile.getContentType();
        boolean supportedImage = switch (extension) {
            case "jpg", "jpeg" -> "image/jpeg".equals(contentType);
            case "png" -> "image/png".equals(contentType);
            case "gif" -> "image/gif".equals(contentType);
            case "webp" -> "image/webp".equals(contentType);
            default -> false;
        };
        if (!supportedImage) {
            throw new IllegalArgumentException("Choose a valid JPG, PNG, GIF, or WebP image.");
        }

        String storedFilename = UUID.randomUUID() + "." + extension;
        try {
            Files.createDirectories(uploadDirectory);
            Path destination = uploadDirectory.resolve(storedFilename).normalize();
            if (!destination.getParent().equals(uploadDirectory)) {
                throw new IllegalArgumentException("Invalid image filename.");
            }
            imageFile.transferTo(destination);
        } catch (IOException exception) {
            throw new IllegalStateException("Could not save the product image.", exception);
        }
        return "/uploads/products/" + storedFilename;
    }
}
