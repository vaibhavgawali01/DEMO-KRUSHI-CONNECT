package com.krushisevakendra.service.impl;

import com.krushisevakendra.dto.ReportFilterDto;
import com.krushisevakendra.entity.Order;
import com.krushisevakendra.entity.OrderItem;
import com.krushisevakendra.entity.Product;
import com.krushisevakendra.entity.Udhari;
import com.krushisevakendra.enums.OrderStatus;
import com.krushisevakendra.repository.*;
import com.krushisevakendra.service.ReportService;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;

@Service
@Transactional(readOnly = true)
public class ReportServiceImpl implements ReportService {

    private final OrderRepository orderRepository;
    private final OrderItemRepository orderItemRepository;
    private final ProductRepository productRepository;
    private final UdhariRepository udhariRepository;
    private final UserRepository userRepository;

    public ReportServiceImpl(OrderRepository orderRepository,
                             OrderItemRepository orderItemRepository,
                             ProductRepository productRepository,
                             UdhariRepository udhariRepository,
                             UserRepository userRepository) {
        this.orderRepository = orderRepository;
        this.orderItemRepository = orderItemRepository;
        this.productRepository = productRepository;
        this.udhariRepository = udhariRepository;
        this.userRepository = userRepository;
    }

    @Override
    public Map<String, Object> generateSalesReport(ReportFilterDto filter) {
        LocalDateTime start = filter.getStartDate() != null ? filter.getStartDate().atStartOfDay() : LocalDateTime.now().minusDays(30);
        LocalDateTime end = filter.getEndDate() != null ? filter.getEndDate().atTime(23, 59, 59) : LocalDateTime.now();

        List<Order> orders = orderRepository.findOrdersBetween(start, end);
        BigDecimal totalRevenue = BigDecimal.ZERO;
        BigDecimal totalGst = BigDecimal.ZERO;
        BigDecimal totalDiscount = BigDecimal.ZERO;
        int totalOrders = orders.size();

        Map<String, BigDecimal> dailyTotals = new LinkedHashMap<>();
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy-MM-dd");

        for (Order o : orders) {
            if (o.getOrderStatus() != OrderStatus.CANCELLED) {
                totalRevenue = totalRevenue.add(o.getTotal());
                totalGst = totalGst.add(o.getGst());
                totalDiscount = totalDiscount.add(o.getDiscount());

                String dateKey = o.getCreatedAt().format(dtf);
                dailyTotals.put(dateKey, dailyTotals.getOrDefault(dateKey, BigDecimal.ZERO).add(o.getTotal()));
            }
        }

        Map<String, Object> report = new HashMap<>();
        report.put("orders", orders);
        report.put("totalRevenue", totalRevenue);
        report.put("totalGst", totalGst);
        report.put("totalDiscount", totalDiscount);
        report.put("totalOrders", totalOrders);
        report.put("dailyTotals", dailyTotals);
        report.put("startDate", start.toLocalDate());
        report.put("endDate", end.toLocalDate());
        return report;
    }

    @Override
    public Map<String, Object> generateStockReport() {
        List<Product> allProducts = productRepository.findAll();
        List<Product> lowStock = productRepository.findLowStockProducts();
        List<Product> expired = productRepository.findExpiredProducts(java.time.LocalDate.now());

        BigDecimal totalStockValue = BigDecimal.ZERO;
        int totalQuantity = 0;

        for (Product p : allProducts) {
            if (p.getStockQuantity() != null && p.getPrice() != null) {
                totalQuantity += p.getStockQuantity();
                totalStockValue = totalStockValue.add(p.getPrice().multiply(BigDecimal.valueOf(p.getStockQuantity())));
            }
        }

        Map<String, Object> report = new HashMap<>();
        report.put("products", allProducts);
        report.put("lowStockProducts", lowStock);
        report.put("expiredProducts", expired);
        report.put("totalStockValue", totalStockValue);
        report.put("totalQuantity", totalQuantity);
        return report;
    }

    @Override
    public Map<String, Object> generateUdhariReport() {
        List<Udhari> allUdhari = udhariRepository.findAll();
        List<Udhari> overdue = udhariRepository.findOverdueRecords(java.time.LocalDate.now());

        BigDecimal totalIssued = udhariRepository.calculateTotalUdhariIssued();
        BigDecimal totalCollected = udhariRepository.calculateTotalUdhariCollected();
        BigDecimal totalRemaining = udhariRepository.calculateTotalRemainingUdhari();

        Map<String, Object> report = new HashMap<>();
        report.put("udhariList", allUdhari);
        report.put("overdueList", overdue);
        report.put("totalIssued", totalIssued);
        report.put("totalCollected", totalCollected);
        report.put("totalRemaining", totalRemaining);
        report.put("overdueCount", overdue.size());
        return report;
    }

    @Override
    public Map<String, Object> generateCustomerPurchasesReport() {
        List<Object[]> topProducts = orderItemRepository.findTopSellingProducts();
        Map<String, Object> report = new HashMap<>();
        report.put("topSellingProducts", topProducts);
        report.put("customers", userRepository.findAllCustomers());
        return report;
    }

    @Override
    public Map<String, Object> generateProfitReport(ReportFilterDto filter) {
        Map<String, Object> sales = generateSalesReport(filter);
        BigDecimal totalRevenue = (BigDecimal) sales.get("totalRevenue");

        // Estimated profit margin ~12% gross average for agri inputs
        BigDecimal estimatedMargin = totalRevenue.multiply(BigDecimal.valueOf(0.12)).setScale(2, RoundingMode.HALF_UP);

        Map<String, Object> report = new HashMap<>(sales);
        report.put("estimatedProfit", estimatedMargin);
        report.put("marginPercentage", "12.0%");
        return report;
    }

    @Override
    public String exportReportToCsv(String reportType, ReportFilterDto filter) {
        StringBuilder csv = new StringBuilder();
        if ("sales".equalsIgnoreCase(reportType)) {
            csv.append("Order Number,Date,Customer,Subtotal,Discount,GST,Total,Payment Method,Status\n");
            Map<String, Object> data = generateSalesReport(filter);
            @SuppressWarnings("unchecked")
            List<Order> orders = (List<Order>) data.get("orders");
            for (Order o : orders) {
                csv.append(String.format("\"%s\",\"%s\",\"%s\",%.2f,%.2f,%.2f,%.2f,\"%s\",\"%s\"\n",
                        o.getOrderNumber(),
                        o.getCreatedAt().toString(),
                        o.getUser().getName(),
                        o.getSubtotal(),
                        o.getDiscount(),
                        o.getGst(),
                        o.getTotal(),
                        o.getPaymentMethod().name(),
                        o.getOrderStatus().name()
                ));
            }
        } else if ("stock".equalsIgnoreCase(reportType)) {
            csv.append("Product ID,SKU,Barcode,Name,Company,Category,Stock Quantity,Min Stock,Price,Status\n");
            List<Product> products = productRepository.findAll();
            for (Product p : products) {
                csv.append(String.format("%d,\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",%d,%d,%.2f,\"%s\"\n",
                        p.getId(),
                        p.getSku() != null ? p.getSku() : "",
                        p.getBarcode() != null ? p.getBarcode() : "",
                        p.getName().replace("\"", "'"),
                        p.getCompany(),
                        p.getCategory().getName(),
                        p.getStockQuantity(),
                        p.getMinimumStock(),
                        p.getPrice(),
                        p.getStatus()
                ));
            }
        } else if ("udhari".equalsIgnoreCase(reportType)) {
            csv.append("Udhari ID,Customer,Mobile,Village,Total Amount,Paid Amount,Remaining Balance,Due Date,Status\n");
            List<Udhari> udhariList = udhariRepository.findAll();
            for (Udhari u : udhariList) {
                csv.append(String.format("%d,\"%s\",\"%s\",\"%s\",%.2f,%.2f,%.2f,\"%s\",\"%s\"\n",
                        u.getId(),
                        u.getUser().getName(),
                        u.getUser().getMobile(),
                        u.getUser().getVillage() != null ? u.getUser().getVillage() : "",
                        u.getTotalAmount(),
                        u.getPaidAmount(),
                        u.getRemainingAmount(),
                        u.getDueDate().toString(),
                        u.getStatus().name()
                ));
            }
        }
        return csv.toString();
    }
}
