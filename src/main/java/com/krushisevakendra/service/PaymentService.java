package com.krushisevakendra.service;

import com.krushisevakendra.entity.Order;
import com.krushisevakendra.entity.Payment;
import com.krushisevakendra.entity.Udhari;
import com.krushisevakendra.entity.User;
import com.krushisevakendra.enums.PaymentMethod;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

public interface PaymentService {
    Payment recordPayment(User user, Udhari udhari, Order order, BigDecimal amount, PaymentMethod method, String transactionId, String remarks);
    Optional<Payment> getPaymentById(Long id);
    Page<Payment> getUserPayments(Long userId, Pageable pageable);
    List<Payment> getUdhariPayments(Long udhariId);
    Page<Payment> getAllPaymentsPaged(Pageable pageable);
    Page<Payment> searchPayments(String query, Pageable pageable);
    List<Payment> getRecentPayments();
    List<Object[]> getPaymentTotalsByMethod();
    BigDecimal getPaymentsTotalBetween(LocalDateTime start, LocalDateTime end);
}
