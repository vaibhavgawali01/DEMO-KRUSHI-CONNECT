package com.krushisevakendra.repository;

import com.krushisevakendra.entity.OrderItem;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface OrderItemRepository extends JpaRepository<OrderItem, Long> {
    List<OrderItem> findByOrderId(Long orderId);

    @Query("SELECT oi.product.id, oi.product.name, SUM(oi.quantity), SUM(oi.total) " +
           "FROM OrderItem oi JOIN oi.order o " +
           "WHERE o.orderStatus <> 'CANCELLED' " +
           "GROUP BY oi.product.id, oi.product.name " +
           "ORDER BY SUM(oi.quantity) DESC")
    List<Object[]> findTopSellingProducts();
}
