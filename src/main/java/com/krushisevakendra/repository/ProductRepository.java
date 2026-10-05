package com.krushisevakendra.repository;

import com.krushisevakendra.entity.Product;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

@Repository
public interface ProductRepository extends JpaRepository<Product, Long>, JpaSpecificationExecutor<Product> {

    Optional<Product> findByBarcode(String barcode);

    Optional<Product> findBySku(String sku);

    List<Product> findByStatus(String status);

    List<Product> findTop8ByStatusOrderByRatingDesc(String status);

    List<Product> findByCategoryIdAndStatus(Long categoryId, String status);

    @Query("SELECT p FROM Product p WHERE p.status = 'ACTIVE' AND (" +
           "LOWER(p.name) LIKE LOWER(CONCAT('%', :keyword, '%')) OR " +
           "LOWER(p.nameMr) LIKE LOWER(CONCAT('%', :keyword, '%')) OR " +
           "LOWER(p.company) LIKE LOWER(CONCAT('%', :keyword, '%')) OR " +
           "LOWER(p.category.name) LIKE LOWER(CONCAT('%', :keyword, '%')) OR " +
           "p.sku LIKE CONCAT('%', :keyword, '%') OR " +
           "p.barcode LIKE CONCAT('%', :keyword, '%'))")
    Page<Product> searchProducts(@Param("keyword") String keyword, Pageable pageable);

    @Query("SELECT p FROM Product p WHERE " +
           "(:categoryId IS NULL OR p.category.id = :categoryId) AND " +
           "(:company IS NULL OR LOWER(p.company) = LOWER(:company)) AND " +
           "(:minPrice IS NULL OR p.price >= :minPrice) AND " +
           "(:maxPrice IS NULL OR p.price <= :maxPrice) AND " +
           "(:inStockOnly = false OR p.stockQuantity > 0) AND " +
           "(:status IS NULL OR p.status = :status) AND " +
           "(:keyword IS NULL OR (LOWER(p.name) LIKE LOWER(CONCAT('%', :keyword, '%')) OR LOWER(p.company) LIKE LOWER(CONCAT('%', :keyword, '%'))))")
    Page<Product> filterProducts(
            @Param("categoryId") Long categoryId,
            @Param("company") String company,
            @Param("minPrice") Double minPrice,
            @Param("maxPrice") Double maxPrice,
            @Param("inStockOnly") boolean inStockOnly,
            @Param("status") String status,
            @Param("keyword") String keyword,
            Pageable pageable
    );

    @Query("SELECT p FROM Product p WHERE p.stockQuantity <= p.minimumStock AND p.status = 'ACTIVE'")
    List<Product> findLowStockProducts();

    @Query("SELECT p FROM Product p WHERE p.expiryDate IS NOT NULL AND p.expiryDate < :today AND p.status = 'ACTIVE'")
    List<Product> findExpiredProducts(@Param("today") LocalDate today);

    @Query("SELECT p FROM Product p WHERE p.expiryDate IS NOT NULL AND p.expiryDate >= :today AND p.expiryDate <= :targetDate AND p.status = 'ACTIVE'")
    List<Product> findExpiringSoonProducts(@Param("today") LocalDate today, @Param("targetDate") LocalDate targetDate);

    @Query("SELECT DISTINCT p.company FROM Product p WHERE p.status = 'ACTIVE' ORDER BY p.company ASC")
    List<String> findAllDistinctCompanies();

    @Query("SELECT p FROM Product p WHERE " +
           "(:categoryId IS NULL OR p.category.id = :categoryId) AND " +
           "(:status IS NULL OR p.status = :status) AND " +
           "(:stockStatus IS NULL OR " +
           "  (:stockStatus = 'LOW' AND p.stockQuantity <= p.minimumStock) OR " +
           "  (:stockStatus = 'MEDIUM' AND p.stockQuantity > p.minimumStock AND p.stockQuantity <= (p.minimumStock * 3)) OR " +
           "  (:stockStatus = 'ADEQUATE' AND p.stockQuantity > (p.minimumStock * 3))) AND " +
           "(:keyword IS NULL OR (" +
           "  LOWER(p.name) LIKE LOWER(CONCAT('%', :keyword, '%')) OR " +
           "  LOWER(p.nameMr) LIKE LOWER(CONCAT('%', :keyword, '%')) OR " +
           "  LOWER(p.company) LIKE LOWER(CONCAT('%', :keyword, '%')) OR " +
           "  p.sku LIKE CONCAT('%', :keyword, '%') OR " +
           "  p.barcode LIKE CONCAT('%', :keyword, '%')))")
    Page<Product> filterAdminProducts(
            @Param("categoryId") Long categoryId,
            @Param("status") String status,
            @Param("stockStatus") String stockStatus,
            @Param("keyword") String keyword,
            Pageable pageable
    );

    long countByStatus(String status);
}
