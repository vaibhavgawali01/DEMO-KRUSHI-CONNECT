package com.krushisevakendra.dto;

import com.krushisevakendra.entity.Product;

import java.math.BigDecimal;

public record PublicProductDto(
        Long id,
        String name,
        String nameMr,
        String company,
        BigDecimal price,
        BigDecimal discountPrice,
        BigDecimal effectivePrice,
        BigDecimal gstRate,
        String description,
        String usageInstructions,
        String image,
        BigDecimal rating,
        Integer reviewCount,
        CategorySummary category
) {
    public static PublicProductDto from(Product product) {
        return new PublicProductDto(
                product.getId(),
                product.getName(),
                product.getNameMr(),
                product.getCompany(),
                product.getPrice(),
                product.getDiscountPrice(),
                product.getEffectivePrice(),
                product.getGstRate(),
                product.getDescription(),
                product.getUsageInstructions(),
                product.getImage(),
                product.getRating(),
                product.getReviewCount(),
                new CategorySummary(
                        product.getCategory().getId(),
                        product.getCategory().getName(),
                        product.getCategory().getNameMr()
                )
        );
    }

    public record CategorySummary(Long id, String name, String nameMr) {}
}
