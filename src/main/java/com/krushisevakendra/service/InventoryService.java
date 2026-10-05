package com.krushisevakendra.service;

import com.krushisevakendra.entity.InventoryTransaction;
import com.krushisevakendra.entity.Product;
import com.krushisevakendra.enums.InventoryTransactionType;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

import java.util.List;

public interface InventoryService {
    InventoryTransaction recordTransaction(Product product, InventoryTransactionType type, Integer quantity, String reason);
    Product adjustStock(Long productId, Integer quantity, InventoryTransactionType type, String reason);
    Page<InventoryTransaction> getTransactionHistory(Pageable pageable);
    List<InventoryTransaction> getTransactionsForProduct(Long productId);
}
