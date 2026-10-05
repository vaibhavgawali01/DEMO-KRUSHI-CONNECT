package com.krushisevakendra.service.impl;

import com.krushisevakendra.entity.InventoryTransaction;
import com.krushisevakendra.entity.Product;
import com.krushisevakendra.enums.InventoryTransactionType;
import com.krushisevakendra.exception.InsufficientStockException;
import com.krushisevakendra.exception.ResourceNotFoundException;
import com.krushisevakendra.repository.InventoryTransactionRepository;
import com.krushisevakendra.repository.ProductRepository;
import com.krushisevakendra.service.InventoryService;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.List;

@Service
@Transactional
public class InventoryServiceImpl implements InventoryService {

    private final InventoryTransactionRepository transactionRepository;
    private final ProductRepository productRepository;

    public InventoryServiceImpl(InventoryTransactionRepository transactionRepository, ProductRepository productRepository) {
        this.transactionRepository = transactionRepository;
        this.productRepository = productRepository;
    }

    @Override
    public InventoryTransaction recordTransaction(Product product, InventoryTransactionType type, Integer quantity, String reason) {
        InventoryTransaction tx = new InventoryTransaction(product, type, quantity, reason);
        tx.setTransactionDate(LocalDateTime.now());
        return transactionRepository.save(tx);
    }

    @Override
    public Product adjustStock(Long productId, Integer quantity, InventoryTransactionType type, String reason) {
        Product product = productRepository.findById(productId)
                .orElseThrow(() -> new ResourceNotFoundException("Product not found with id: " + productId));

        int currentStock = product.getStockQuantity() != null ? product.getStockQuantity() : 0;
        int newStock = currentStock;

        if (type == InventoryTransactionType.STOCK_IN || type == InventoryTransactionType.RETURN) {
            newStock = currentStock + quantity;
        } else if (type == InventoryTransactionType.STOCK_OUT || type == InventoryTransactionType.ORDER_DEDUCTION || type == InventoryTransactionType.ADJUSTMENT) {
            if (currentStock < quantity) {
                throw new InsufficientStockException("Insufficient stock for product " + product.getName() + ". Available: " + currentStock + ", Requested: " + quantity);
            }
            newStock = currentStock - quantity;
        }

        product.setStockQuantity(newStock);
        product.setUpdatedAt(LocalDateTime.now());
        Product saved = productRepository.save(product);

        recordTransaction(saved, type, quantity, reason);
        return saved;
    }

    @Override
    @Transactional(readOnly = true)
    public Page<InventoryTransaction> getTransactionHistory(Pageable pageable) {
        return transactionRepository.findAllByOrderByTransactionDateDesc(pageable);
    }

    @Override
    @Transactional(readOnly = true)
    public List<InventoryTransaction> getTransactionsForProduct(Long productId) {
        return transactionRepository.findByProductIdOrderByTransactionDateDesc(productId);
    }
}
