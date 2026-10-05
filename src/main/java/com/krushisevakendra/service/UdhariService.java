package com.krushisevakendra.service;

import com.krushisevakendra.dto.UdhariEditDto;
import com.krushisevakendra.dto.UdhariPaymentDto;
import com.krushisevakendra.entity.Order;
import com.krushisevakendra.entity.Payment;
import com.krushisevakendra.entity.Udhari;
import com.krushisevakendra.entity.User;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

public interface UdhariService {
    Udhari createUdhariRecord(User user, Order order, BigDecimal totalAmount, LocalDate dueDate);
    Payment recordUdhariPayment(UdhariPaymentDto dto);
    Udhari updateUdhariRecord(UdhariEditDto dto);
    Optional<Udhari> getUdhariById(Long id);
    List<Udhari> getUserUdhariList(Long userId);
    Page<Udhari> getUserUdhariPaged(Long userId, Pageable pageable);
    Page<Udhari> getAllUdhariPaged(Pageable pageable);
    Page<Udhari> searchUdhari(String query, Pageable pageable);
    List<Udhari> getOverdueRecords();
    BigDecimal getTotalRemainingUdhari();
    BigDecimal getTotalUdhariIssued();
    BigDecimal getTotalUdhariCollected();
    BigDecimal getUserRemainingUdhari(Long userId);
    long getOverdueCount();
    Udhari updateDueDate(Long udhariId, LocalDate newDueDate);
    void updateOverdueStatuses();
}
