package com.krushisevakendra.dto;

import com.krushisevakendra.entity.Product;
import java.io.Serializable;
import java.math.BigDecimal;
import java.math.RoundingMode;

public class CartItemDto implements Serializable {
    private static final long serialVersionUID = 1L;

    private Long productId;
    private String name;
    private String nameMr;
    private String company;
    private String image;
    private BigDecimal price; // Effective unit price (discount price if present)
    private BigDecimal gstRate;
    private Integer quantity;
    private Integer maxStock;

    public CartItemDto() {}

    public CartItemDto(Product product, Integer quantity) {
        this.productId = product.getId();
        this.name = product.getName();
        this.nameMr = product.getNameMr();
        this.company = product.getCompany();
        this.image = product.getImage();
        this.price = product.getEffectivePrice();
        this.gstRate = product.getGstRate() != null ? product.getGstRate() : BigDecimal.ZERO;
        this.quantity = quantity;
        this.maxStock = product.getStockQuantity();
    }

    public BigDecimal getItemSubtotal() {
        return price.multiply(BigDecimal.valueOf(quantity));
    }

    public BigDecimal getItemGst() {
        if (gstRate == null || gstRate.compareTo(BigDecimal.ZERO) == 0) {
            return BigDecimal.ZERO;
        }
        return getItemSubtotal().multiply(gstRate).divide(BigDecimal.valueOf(100), 2, RoundingMode.HALF_UP);
    }

    public BigDecimal getItemTotal() {
        return getItemSubtotal().add(getItemGst());
    }

    public Long getProductId() {
        return productId;
    }

    public void setProductId(Long productId) {
        this.productId = productId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getNameMr() {
        return nameMr;
    }

    public void setNameMr(String nameMr) {
        this.nameMr = nameMr;
    }

    public String getCompany() {
        return company;
    }

    public void setCompany(String company) {
        this.company = company;
    }

    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }

    public BigDecimal getPrice() {
        return price;
    }

    public void setPrice(BigDecimal price) {
        this.price = price;
    }

    public BigDecimal getGstRate() {
        return gstRate;
    }

    public void setGstRate(BigDecimal gstRate) {
        this.gstRate = gstRate;
    }

    public Integer getQuantity() {
        return quantity;
    }

    public void setQuantity(Integer quantity) {
        this.quantity = quantity;
    }

    public Integer getMaxStock() {
        return maxStock;
    }

    public void setMaxStock(Integer maxStock) {
        this.maxStock = maxStock;
    }
}
