package com.krushisevakendra.service.impl;

import com.krushisevakendra.dto.UdhariEditDto;
import com.krushisevakendra.dto.UdhariPaymentDto;
import com.krushisevakendra.entity.Order;
import com.krushisevakendra.entity.Payment;
import com.krushisevakendra.entity.Udhari;
import com.krushisevakendra.entity.User;
import com.krushisevakendra.enums.NotificationType;
import com.krushisevakendra.enums.PaymentStatus;
import com.krushisevakendra.enums.UdhariStatus;
import com.krushisevakendra.exception.ResourceNotFoundException;
import com.krushisevakendra.repository.OrderRepository;
import com.krushisevakendra.repository.UdhariRepository;
import com.krushisevakendra.service.NotificationService;
import com.krushisevakendra.service.PaymentService;
import com.krushisevakendra.service.UdhariService;
import org.springframework.context.annotation.Lazy;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

@Service
@Transactional
public class UdhariServiceImpl implements UdhariService {

    private final UdhariRepository udhariRepository;
    private final OrderRepository orderRepository;
    private final PaymentService paymentService;
    private final NotificationService notificationService;

    public UdhariServiceImpl(UdhariRepository udhariRepository,
                             OrderRepository orderRepository,
                             @Lazy PaymentService paymentService,
                             @Lazy NotificationService notificationService) {
        this.udhariRepository = udhariRepository;
        this.orderRepository = orderRepository;
        this.paymentService = paymentService;
        this.notificationService = notificationService;
    }

    @Override
    public Udhari createUdhariRecord(User user, Order order, BigDecimal totalAmount, LocalDate dueDate) {
        Udhari udhari = new Udhari(user, order, totalAmount, dueDate != null ? dueDate : LocalDate.now().plusDays(30));
        udhari.setCreatedAt(LocalDateTime.now());
        udhari.setUpdatedAt(LocalDateTime.now());
        return udhariRepository.save(udhari);
    }

    @Override
    public Udhari updateUdhariRecord(UdhariEditDto dto) {
        Udhari udhari = udhariRepository.findById(dto.getId())
                .orElseThrow(() -> new ResourceNotFoundException("Udhari record not found with id: " + dto.getId()));

        if (dto.getTotalAmount() != null) {
            udhari.setTotalAmount(dto.getTotalAmount());
        }

        if (dto.getPaidAmount() != null) {
            udhari.setPaidAmount(dto.getPaidAmount());
        }

        if (dto.getRemainingAmount() != null) {
            udhari.setRemainingAmount(dto.getRemainingAmount());
        } else if (dto.getTotalAmount() != null && dto.getPaidAmount() != null) {
            BigDecimal rem = dto.getTotalAmount().subtract(dto.getPaidAmount());
            udhari.setRemainingAmount(rem.compareTo(BigDecimal.ZERO) < 0 ? BigDecimal.ZERO : rem);
        }

        if (dto.getDueDate() != null) {
            udhari.setDueDate(dto.getDueDate());
        }

        if (dto.getStatus() != null) {
            udhari.setStatus(dto.getStatus());
        } else {
            udhari.updateStatusBasedOnBalanceAndDate();
        }

        if (dto.getNotes() != null) {
            udhari.setNotes(dto.getNotes());
        }

        if (udhari.getRemainingAmount().compareTo(BigDecimal.ZERO) <= 0) {
            udhari.setStatus(UdhariStatus.PAID_IN_FULL);
            if (udhari.getOrder() != null) {
                udhari.getOrder().setPaymentStatus(PaymentStatus.PAID);
                orderRepository.save(udhari.getOrder());
            }
        }

        udhari.setUpdatedAt(LocalDateTime.now());
        return udhariRepository.save(udhari);
    }

    @Override
    public Payment recordUdhariPayment(UdhariPaymentDto dto) {
        Udhari udhari = udhariRepository.findById(dto.getUdhariId())
                .orElseThrow(() -> new ResourceNotFoundException("Udhari account not found with id: " + dto.getUdhariId()));

        BigDecimal paymentAmt = dto.getAmount();
        if (paymentAmt.compareTo(BigDecimal.ZERO) <= 0) {
            throw new IllegalArgumentException("Payment amount must be greater than zero");
        }

        BigDecimal newPaid = udhari.getPaidAmount().add(paymentAmt);
        BigDecimal newRemaining = udhari.getTotalAmount().subtract(newPaid);

        if (newRemaining.compareTo(BigDecimal.ZERO) <= 0) {
            udhari.setPaidAmount(udhari.getTotalAmount());
            udhari.setRemainingAmount(BigDecimal.ZERO);
            udhari.setStatus(UdhariStatus.PAID_IN_FULL);
            
            // If linked to an order, update order payment status
            if (udhari.getOrder() != null) {
                udhari.getOrder().setPaymentStatus(PaymentStatus.PAID);
                orderRepository.save(udhari.getOrder());
            }
        } else {
            udhari.setPaidAmount(newPaid);
            udhari.setRemainingAmount(newRemaining);
            udhari.updateStatusBasedOnBalanceAndDate();
        }

        udhari.setUpdatedAt(LocalDateTime.now());
        udhariRepository.save(udhari);

        // Record payment entry
        Payment payment = paymentService.recordPayment(
                udhari.getUser(),
                udhari,
                udhari.getOrder(),
                paymentAmt,
                dto.getPaymentMethod(),
                dto.getTransactionId() != null && !dto.getTransactionId().isBlank() ? dto.getTransactionId() : "UDHARI-PAY-" + System.currentTimeMillis(),
                dto.getRemarks() != null ? dto.getRemarks() : "Udhari settlement payment"
        );

        // Notify customer
        notificationService.createNotification(udhari.getUser(),
                "Udhari Payment Received / उधारी जमा पावती",
                "Payment of ₹" + paymentAmt + " received. Remaining balance: ₹" + udhari.getRemainingAmount(),
                NotificationType.IN_APP);

        return payment;
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<Udhari> getUdhariById(Long id) {
        return udhariRepository.findById(id);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Udhari> getUserUdhariList(Long userId) {
        return udhariRepository.findByUserIdOrderByCreatedAtDesc(userId);
    }

    @Override
    @Transactional(readOnly = true)
    public Page<Udhari> getUserUdhariPaged(Long userId, Pageable pageable) {
        return udhariRepository.findByUserIdOrderByCreatedAtDesc(userId, pageable);
    }

    @Override
    @Transactional(readOnly = true)
    public Page<Udhari> getAllUdhariPaged(Pageable pageable) {
        return udhariRepository.findAll(pageable);
    }

    @Override
    @Transactional(readOnly = true)
    public Page<Udhari> searchUdhari(String query, Pageable pageable) {
        if (query == null || query.isBlank()) {
            return udhariRepository.findAll(pageable);
        }
        return udhariRepository.searchUdhari(query.trim(), pageable);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Udhari> getOverdueRecords() {
        return udhariRepository.findOverdueRecords(LocalDate.now());
    }

    @Override
    @Transactional(readOnly = true)
    public BigDecimal getTotalRemainingUdhari() {
        return udhariRepository.calculateTotalRemainingUdhari();
    }

    @Override
    @Transactional(readOnly = true)
    public BigDecimal getTotalUdhariIssued() {
        return udhariRepository.calculateTotalUdhariIssued();
    }

    @Override
    @Transactional(readOnly = true)
    public BigDecimal getTotalUdhariCollected() {
        return udhariRepository.calculateTotalUdhariCollected();
    }

    @Override
    @Transactional(readOnly = true)
    public BigDecimal getUserRemainingUdhari(Long userId) {
        return udhariRepository.calculateUserRemainingUdhari(userId);
    }

    @Override
    @Transactional(readOnly = true)
    public long getOverdueCount() {
        return udhariRepository.countOverdueAccounts();
    }

    @Override
    public Udhari updateDueDate(Long udhariId, LocalDate newDueDate) {
        Udhari udhari = udhariRepository.findById(udhariId)
                .orElseThrow(() -> new ResourceNotFoundException("Udhari record not found with id: " + udhariId));
        udhari.setDueDate(newDueDate);
        udhari.updateStatusBasedOnBalanceAndDate();
        return udhariRepository.save(udhari);
    }

    @Override
    public void updateOverdueStatuses() {
        List<Udhari> overdue = udhariRepository.findOverdueRecords(LocalDate.now());
        for (Udhari u : overdue) {
            u.setStatus(UdhariStatus.OVERDUE);
            udhariRepository.save(u);
        }
    }
}
