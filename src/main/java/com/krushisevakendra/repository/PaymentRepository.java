package com.krushisevakendra.repository;

import com.krushisevakendra.entity.Payment;
import com.krushisevakendra.enums.PaymentMethod;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.List;

@Repository
public interface PaymentRepository extends JpaRepository<Payment, Long> {

    List<Payment> findByUserIdOrderByPaymentDateDesc(Long userId);

    Page<Payment> findByUserIdOrderByPaymentDateDesc(Long userId, Pageable pageable);

    List<Payment> findByUdhariIdOrderByPaymentDateDesc(Long udhariId);

    List<Payment> findTop10ByOrderByPaymentDateDesc();

    @Query("SELECT p FROM Payment p WHERE p.paymentDate >= :startDate AND p.paymentDate <= :endDate ORDER BY p.paymentDate DESC")
    List<Payment> findPaymentsBetween(@Param("startDate") LocalDateTime startDate, @Param("endDate") LocalDateTime endDate);

    @Query("SELECT COALESCE(SUM(p.amount), 0) FROM Payment p WHERE p.paymentDate >= :startDate AND p.paymentDate <= :endDate")
    BigDecimal calculatePaymentsTotalBetween(@Param("startDate") LocalDateTime startDate, @Param("endDate") LocalDateTime endDate);

    @Query("SELECT p.paymentMethod, SUM(p.amount) FROM Payment p GROUP BY p.paymentMethod")
    List<Object[]> findPaymentTotalsByMethod();

    @Query("SELECT p FROM Payment p WHERE " +
           "LOWER(p.user.name) LIKE LOWER(CONCAT('%', :query, '%')) OR " +
           "p.user.mobile LIKE CONCAT('%', :query, '%') OR " +
           "p.transactionId LIKE CONCAT('%', :query, '%')")
    Page<Payment> searchPayments(@Param("query") String query, Pageable pageable);
}
