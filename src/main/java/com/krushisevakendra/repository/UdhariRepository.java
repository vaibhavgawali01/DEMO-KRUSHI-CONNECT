package com.krushisevakendra.repository;

import com.krushisevakendra.entity.Udhari;
import com.krushisevakendra.enums.UdhariStatus;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.List;

@Repository
public interface UdhariRepository extends JpaRepository<Udhari, Long> {

    List<Udhari> findByUserIdOrderByCreatedAtDesc(Long userId);

    Page<Udhari> findByUserIdOrderByCreatedAtDesc(Long userId, Pageable pageable);

    List<Udhari> findByStatus(UdhariStatus status);

    @Query("SELECT u FROM Udhari u WHERE u.status != com.krushisevakendra.enums.UdhariStatus.PAID_IN_FULL AND u.dueDate < :today")
    List<Udhari> findOverdueRecords(@Param("today") LocalDate today);

    @Query("SELECT u FROM Udhari u WHERE " +
           "LOWER(u.user.name) LIKE LOWER(CONCAT('%', :query, '%')) OR " +
           "u.user.mobile LIKE CONCAT('%', :query, '%') OR " +
           "LOWER(u.user.village) LIKE LOWER(CONCAT('%', :query, '%'))")
    Page<Udhari> searchUdhari(@Param("query") String query, Pageable pageable);

    @Query("SELECT COALESCE(SUM(u.remainingAmount), 0) FROM Udhari u WHERE u.status != com.krushisevakendra.enums.UdhariStatus.PAID_IN_FULL")
    BigDecimal calculateTotalRemainingUdhari();

    @Query("SELECT COALESCE(SUM(u.totalAmount), 0) FROM Udhari u")
    BigDecimal calculateTotalUdhariIssued();

    @Query("SELECT COALESCE(SUM(u.paidAmount), 0) FROM Udhari u")
    BigDecimal calculateTotalUdhariCollected();

    @Query("SELECT COALESCE(SUM(u.remainingAmount), 0) FROM Udhari u WHERE u.user.id = :userId AND u.status != com.krushisevakendra.enums.UdhariStatus.PAID_IN_FULL")
    BigDecimal calculateUserRemainingUdhari(@Param("userId") Long userId);

    @Query("SELECT COUNT(u) FROM Udhari u WHERE u.status = com.krushisevakendra.enums.UdhariStatus.OVERDUE")
    long countOverdueAccounts();
}
