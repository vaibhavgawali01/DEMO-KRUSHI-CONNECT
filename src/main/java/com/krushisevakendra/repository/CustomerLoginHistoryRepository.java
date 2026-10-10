package com.krushisevakendra.repository;

import com.krushisevakendra.entity.CustomerLoginHistory;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CustomerLoginHistoryRepository extends JpaRepository<CustomerLoginHistory, Long> {

    List<CustomerLoginHistory> findTop100ByOrderByLoggedInAtDesc();

    List<CustomerLoginHistory> findTop50ByUserIdOrderByLoggedInAtDesc(Long userId);

    long countByUserId(Long userId);
}
