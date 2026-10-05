package com.krushisevakendra.service;

import com.krushisevakendra.dto.ReportFilterDto;

import java.util.Map;

public interface ReportService {
    Map<String, Object> generateSalesReport(ReportFilterDto filter);
    Map<String, Object> generateStockReport();
    Map<String, Object> generateUdhariReport();
    Map<String, Object> generateCustomerPurchasesReport();
    Map<String, Object> generateProfitReport(ReportFilterDto filter);
    String exportReportToCsv(String reportType, ReportFilterDto filter);
}
