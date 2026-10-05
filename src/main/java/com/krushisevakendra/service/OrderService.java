package com.krushisevakendra.service;

import com.krushisevakendra.dto.CartDto;
import com.krushisevakendra.dto.CheckoutDto;
import com.krushisevakendra.entity.Order;
import com.krushisevakendra.entity.User;
import com.krushisevakendra.enums.OrderStatus;
import com.krushisevakendra.enums.PaymentStatus;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

import java.math.BigDecimal;
import java.util.List;
import java.util.Optional;

public interface OrderService {
    Order createOrder(User user, CartDto cart, CheckoutDto checkoutDto);
    Optional<Order> getOrderById(Long id);
    Optional<Order> getOrderByNumber(String orderNumber);
    Page<Order> getUserOrders(Long userId, Pageable pageable);
    List<Order> getUserOrdersList(Long userId);
    Page<Order> getAllOrdersPaged(Pageable pageable);
    Page<Order> searchOrders(String query, Pageable pageable);
    List<Order> getRecentOrders();
    Order updateOrderStatus(Long orderId, OrderStatus status);
    Order updatePaymentStatus(Long orderId, PaymentStatus status);
    BigDecimal getTotalSales();
    BigDecimal getTodaySales();
    BigDecimal getMonthlySales();
    long getOrderCountByStatus(OrderStatus status);
    long getTotalOrderCount();
}
