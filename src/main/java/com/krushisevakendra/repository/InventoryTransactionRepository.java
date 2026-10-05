package com.krushisevakendra.repository;

import com.krushisevakendra.entity.InventoryTransaction;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface InventoryTransactionRepository extends JpaRepository<InventoryTransaction, Long> {
    List<InventoryTransaction> findByProductIdOrderByTransactionDateDesc(Long productId);
    Page<InventoryTransaction> findAllByOrderByTransactionDateDesc(Pageable pageable);
}
