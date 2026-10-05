package com.krushisevakendra.repository;

import com.krushisevakendra.entity.Order;
import com.krushisevakendra.enums.OrderStatus;
import com.krushisevakendra.enums.PaymentStatus;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

@Repository
public interface OrderRepository extends JpaRepository<Order, Long> {

    Optional<Order> findByOrderNumber(String orderNumber);

    Page<Order> findByUserIdOrderByCreatedAtDesc(Long userId, Pageable pageable);

    List<Order> findByUserIdOrderByCreatedAtDesc(Long userId);

    Page<Order> findByOrderStatus(OrderStatus orderStatus, Pageable pageable);

    List<Order> findTop10ByOrderByCreatedAtDesc();

    @Query("SELECT o FROM Order o WHERE " +
           "LOWER(o.orderNumber) LIKE LOWER(CONCAT('%', :query, '%')) OR " +
           "LOWER(o.user.name) LIKE LOWER(CONCAT('%', :query, '%')) OR " +
           "o.user.mobile LIKE CONCAT('%', :query, '%')")
    Page<Order> searchOrders(@Param("query") String query, Pageable pageable);

    @Query("SELECT COALESCE(SUM(o.total), 0) FROM Order o WHERE o.orderStatus != com.krushisevakendra.enums.OrderStatus.CANCELLED")
    BigDecimal calculateTotalSales();

    @Query("SELECT COALESCE(SUM(o.total), 0) FROM Order o WHERE o.orderStatus != com.krushisevakendra.enums.OrderStatus.CANCELLED AND o.createdAt >= :startDate AND o.createdAt <= :endDate")
    BigDecimal calculateSalesBetween(@Param("startDate") LocalDateTime startDate, @Param("endDate") LocalDateTime endDate);

    @Query("SELECT COUNT(o) FROM Order o WHERE o.orderStatus = :status")
    long countByOrderStatus(@Param("status") OrderStatus status);

    @Query("SELECT COUNT(o) FROM Order o WHERE o.paymentStatus = :status")
    long countByPaymentStatus(@Param("status") PaymentStatus status);

    @Query("SELECT o FROM Order o WHERE o.createdAt >= :startDate AND o.createdAt <= :endDate ORDER BY o.createdAt ASC")
    List<Order> findOrdersBetween(@Param("startDate") LocalDateTime startDate, @Param("endDate") LocalDateTime endDate);
}
