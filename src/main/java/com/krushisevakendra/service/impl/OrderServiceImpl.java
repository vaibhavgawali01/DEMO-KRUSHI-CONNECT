package com.krushisevakendra.service.impl;

import com.krushisevakendra.dto.CartDto;
import com.krushisevakendra.dto.CartItemDto;
import com.krushisevakendra.dto.CheckoutDto;
import com.krushisevakendra.entity.Order;
import com.krushisevakendra.entity.OrderItem;
import com.krushisevakendra.entity.Product;
import com.krushisevakendra.entity.User;
import com.krushisevakendra.enums.*;
import com.krushisevakendra.exception.InsufficientStockException;
import com.krushisevakendra.exception.ResourceNotFoundException;
import com.krushisevakendra.repository.OrderRepository;
import com.krushisevakendra.repository.ProductRepository;
import com.krushisevakendra.service.*;
import org.springframework.context.annotation.Lazy;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.Year;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Service
@Transactional
public class OrderServiceImpl implements OrderService {

    private final OrderRepository orderRepository;
    private final ProductRepository productRepository;
    private final InventoryService inventoryService;
    private final UdhariService udhariService;
    private final PaymentService paymentService;
    private final NotificationService notificationService;

    public OrderServiceImpl(OrderRepository orderRepository,
                            ProductRepository productRepository,
                            InventoryService inventoryService,
                            @Lazy UdhariService udhariService,
                            @Lazy PaymentService paymentService,
                            @Lazy NotificationService notificationService) {
        this.orderRepository = orderRepository;
        this.productRepository = productRepository;
        this.inventoryService = inventoryService;
        this.udhariService = udhariService;
        this.paymentService = paymentService;
        this.notificationService = notificationService;
    }

    @Override
    public Order createOrder(User user, CartDto cart, CheckoutDto checkoutDto) {
        if (cart == null || cart.getItems().isEmpty()) {
            throw new IllegalArgumentException("Cart is empty / कार्ट रिकामे आहे");
        }

        // Validate stock for all items
        for (CartItemDto item : cart.getItems()) {
            Product product = productRepository.findById(item.getProductId())
                    .orElseThrow(() -> new ResourceNotFoundException("Product not found: " + item.getProductId()));
            if (product.getStockQuantity() < item.getQuantity()) {
                throw new InsufficientStockException("Insufficient stock for " + product.getName() + 
                        ". Available: " + product.getStockQuantity() + ", in cart: " + item.getQuantity());
            }
        }

        Order order = new Order();
        String currentYear = String.valueOf(Year.now().getValue());
        String randomSeq = UUID.randomUUID().toString().substring(0, 5).toUpperCase();
        order.setOrderNumber("KSK-" + currentYear + "-" + randomSeq);
        order.setUser(user);
        order.setSubtotal(cart.getSubtotal());
        order.setDiscount(cart.getDiscountAmount());
        order.setGst(cart.getTotalGst());
        order.setTotal(cart.getGrandTotal());
        order.setPaymentMethod(checkoutDto.getPaymentMethod());
        order.setDeliveryAddress(checkoutDto.getDeliveryAddress() + ", " + 
                (checkoutDto.getVillage() != null ? checkoutDto.getVillage() : ""));
        order.setNotes(checkoutDto.getNotes());
        order.setCreatedAt(LocalDateTime.now());
        order.setOrderStatus(OrderStatus.CONFIRMED);

        if (checkoutDto.getPaymentMethod() == PaymentMethod.UDHARI) {
            order.setPaymentStatus(PaymentStatus.PENDING);
        } else if (checkoutDto.getPaymentMethod() == PaymentMethod.CASH) {
            order.setPaymentStatus(PaymentStatus.PENDING); // Paid on delivery/pickup
        } else {
            order.setPaymentStatus(PaymentStatus.PAID);
        }

        Order savedOrder = orderRepository.save(order);

        // Process order items & deduct stock
        for (CartItemDto cartItem : cart.getItems()) {
            Product product = productRepository.findById(cartItem.getProductId()).get();
            OrderItem item = new OrderItem(
                    savedOrder,
                    product,
                    cartItem.getQuantity(),
                    cartItem.getPrice(),
                    cartItem.getItemGst(),
                    cartItem.getItemTotal()
            );
            savedOrder.addOrderItem(item);

            // Deduct stock
            inventoryService.adjustStock(product.getId(), cartItem.getQuantity(), 
                    InventoryTransactionType.ORDER_DEDUCTION, "Order #" + savedOrder.getOrderNumber());
        }

        Order finalOrder = orderRepository.save(savedOrder);

        // If Udhari payment method, record in Udhari ledger
        if (checkoutDto.getPaymentMethod() == PaymentMethod.UDHARI) {
            LocalDate dueDate = LocalDate.now().plusDays(30); // Default 30 days credit period
            udhariService.createUdhariRecord(user, finalOrder, finalOrder.getTotal(), dueDate);
        } else if (order.getPaymentStatus() == PaymentStatus.PAID) {
            paymentService.recordPayment(user, null, finalOrder, finalOrder.getTotal(), 
                    checkoutDto.getPaymentMethod(), 
                    checkoutDto.getUpiTransactionId() != null ? checkoutDto.getUpiTransactionId() : "TXN-" + System.currentTimeMillis(),
                    "Order payment for #" + finalOrder.getOrderNumber());
        }

        // Send confirmation notification
        notificationService.createNotification(user, 
                "Order Placed Successfully / ऑर्डर नोंदवली", 
                "Your order #" + finalOrder.getOrderNumber() + " for ₹" + finalOrder.getTotal() + " has been placed successfully.", 
                NotificationType.IN_APP);

        return finalOrder;
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<Order> getOrderById(Long id) {
        return orderRepository.findById(id);
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<Order> getOrderByNumber(String orderNumber) {
        return orderRepository.findByOrderNumber(orderNumber);
    }

    @Override
    @Transactional(readOnly = true)
    public Page<Order> getUserOrders(Long userId, Pageable pageable) {
        return orderRepository.findByUserIdOrderByCreatedAtDesc(userId, pageable);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Order> getUserOrdersList(Long userId) {
        return orderRepository.findByUserIdOrderByCreatedAtDesc(userId);
    }

    @Override
    @Transactional(readOnly = true)
    public Page<Order> getAllOrdersPaged(Pageable pageable) {
        return orderRepository.findAll(pageable);
    }

    @Override
    @Transactional(readOnly = true)
    public Page<Order> searchOrders(String query, Pageable pageable) {
        if (query == null || query.isBlank()) {
            return orderRepository.findAll(pageable);
        }
        return orderRepository.searchOrders(query.trim(), pageable);
    }

    @Override
    @Transactional(readOnly = true)
    public List<Order> getRecentOrders() {
        return orderRepository.findTop10ByOrderByCreatedAtDesc();
    }

    @Override
    public Order updateOrderStatus(Long orderId, OrderStatus status) {
        Order order = orderRepository.findById(orderId)
                .orElseThrow(() -> new ResourceNotFoundException("Order not found with id: " + orderId));
        order.setOrderStatus(status);
        if (status == OrderStatus.DELIVERED && order.getPaymentMethod() == PaymentMethod.CASH) {
            order.setPaymentStatus(PaymentStatus.PAID);
        }
        Order updated = orderRepository.save(order);

        notificationService.createNotification(order.getUser(),
                "Order Status Updated: " + status.name(),
                "Your order #" + order.getOrderNumber() + " status is now: " + status.getDisplayNameEn() + " (" + status.getDisplayNameMr() + ")",
                NotificationType.IN_APP);

        return updated;
    }

    @Override
    public Order updatePaymentStatus(Long orderId, PaymentStatus status) {
        Order order = orderRepository.findById(orderId)
                .orElseThrow(() -> new ResourceNotFoundException("Order not found with id: " + orderId));
        order.setPaymentStatus(status);
        return orderRepository.save(order);
    }

    @Override
    @Transactional(readOnly = true)
    public BigDecimal getTotalSales() {
        return orderRepository.calculateTotalSales();
    }

    @Override
    @Transactional(readOnly = true)
    public BigDecimal getTodaySales() {
        LocalDateTime startOfDay = LocalDate.now().atStartOfDay();
        LocalDateTime endOfDay = LocalDate.now().atTime(23, 59, 59);
        return orderRepository.calculateSalesBetween(startOfDay, endOfDay);
    }

    @Override
    @Transactional(readOnly = true)
    public BigDecimal getMonthlySales() {
        LocalDateTime startOfMonth = LocalDate.now().withDayOfMonth(1).atStartOfDay();
        LocalDateTime endOfDay = LocalDate.now().atTime(23, 59, 59);
        return orderRepository.calculateSalesBetween(startOfMonth, endOfDay);
    }

    @Override
    @Transactional(readOnly = true)
    public long getOrderCountByStatus(OrderStatus status) {
        return orderRepository.countByOrderStatus(status);
    }

    @Override
    @Transactional(readOnly = true)
    public long getTotalOrderCount() {
        return orderRepository.count();
    }
}
