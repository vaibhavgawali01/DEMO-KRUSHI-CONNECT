package com.krushisevakendra.service.impl;

import com.krushisevakendra.entity.Order;
import com.krushisevakendra.entity.Payment;
import com.krushisevakendra.entity.Udhari;
import com.krushisevakendra.entity.User;
import com.krushisevakendra.enums.PaymentMethod;
import com.krushisevakendra.repository.PaymentRepository;
import com.krushisevakendra.service.PaymentService;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

@Service
@Transactional
public class PaymentServiceImpl implements PaymentService {

    private final PaymentRepository paymentRepository;

    public PaymentServiceImpl(PaymentRepository paymentRepository) {
        this.paymentRepository = paymentRepository;
    }

    @Override
    public Payment recordPayment(User user, Udhari udhari, Order order, BigDecimal amount, PaymentMethod method, String transactionId, String remarks) {
        Payment payment = new Payment(user, udhari, order, amount, method, transactionId, remarks);
        payment.setPaymentDate(LocalDateTime.now());
        return paymentRepository.save(payment);
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<Payment> getPaymentById(Long id) {
        return paymentRepository.findById(id);
    }

    @Override
    @Transactional(readOnly = true)
    public Page<Payment> getUserPayments(Long userId, Pageable pageable) {
        return paymentRepository.findByUserIdOrderByPaymentDateDesc(userId, pageable);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Payment> getUdhariPayments(Long udhariId) {
        return paymentRepository.findByUdhariIdOrderByPaymentDateDesc(udhariId);
    }

    @Override
    @Transactional(readOnly = true)
    public Page<Payment> getAllPaymentsPaged(Pageable pageable) {
        return paymentRepository.findAll(pageable);
    }

    @Override
    @Transactional(readOnly = true)
    public Page<Payment> searchPayments(String query, Pageable pageable) {
        if (query == null || query.isBlank()) {
            return paymentRepository.findAll(pageable);
        }
        return paymentRepository.searchPayments(query.trim(), pageable);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Payment> getRecentPayments() {
        return paymentRepository.findTop10ByOrderByPaymentDateDesc();
    }

    @Override
    @Transactional(readOnly = true)
    public List<Object[]> getPaymentTotalsByMethod() {
        return paymentRepository.findPaymentTotalsByMethod();
    }

    @Override
    @Transactional(readOnly = true)
    public BigDecimal getPaymentsTotalBetween(LocalDateTime start, LocalDateTime end) {
        return paymentRepository.calculatePaymentsTotalBetween(start, end);
    }
}
