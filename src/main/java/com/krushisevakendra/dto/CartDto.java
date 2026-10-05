package com.krushisevakendra.dto;

import java.io.Serializable;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class CartDto implements Serializable {
    private static final long serialVersionUID = 1L;

    private List<CartItemDto> items = new ArrayList<>();
    private String couponCode;
    private BigDecimal discountAmount = BigDecimal.ZERO;

    public CartDto() {}

    public void addItem(CartItemDto newItem) {
        Optional<CartItemDto> existing = items.stream()
                .filter(i -> i.getProductId().equals(newItem.getProductId()))
                .findFirst();

        if (existing.isPresent()) {
            CartItemDto item = existing.get();
            int newQty = item.getQuantity() + newItem.getQuantity();
            if (item.getMaxStock() != null && newQty > item.getMaxStock()) {
                newQty = item.getMaxStock();
            }
            item.setQuantity(newQty);
        } else {
            items.add(newItem);
        }
    }

    public void updateQuantity(Long productId, Integer quantity) {
        if (quantity <= 0) {
            removeItem(productId);
            return;
        }
        items.stream()
                .filter(i -> i.getProductId().equals(productId))
                .findFirst()
                .ifPresent(i -> {
                    if (i.getMaxStock() != null && quantity > i.getMaxStock()) {
                        i.setQuantity(i.getMaxStock());
                    } else {
                        i.setQuantity(quantity);
                    }
                });
    }

    public void removeItem(Long productId) {
        items.removeIf(i -> i.getProductId().equals(productId));
    }

    public void clear() {
        items.clear();
        couponCode = null;
        discountAmount = BigDecimal.ZERO;
    }

    public int getTotalItemCount() {
        return items.stream().mapToInt(CartItemDto::getQuantity).sum();
    }

    public BigDecimal getSubtotal() {
        return items.stream()
                .map(CartItemDto::getItemSubtotal)
                .reduce(BigDecimal.ZERO, BigDecimal::add);
    }

    public BigDecimal getTotalGst() {
        return items.stream()
                .map(CartItemDto::getItemGst)
                .reduce(BigDecimal.ZERO, BigDecimal::add);
    }

    public BigDecimal getCgst() {
        return getTotalGst().divide(BigDecimal.valueOf(2), 2, RoundingMode.HALF_UP);
    }

    public BigDecimal getSgst() {
        return getCgst();
    }

    public BigDecimal getGrandTotal() {
        BigDecimal total = getSubtotal().subtract(discountAmount).add(getTotalGst());
        return total.compareTo(BigDecimal.ZERO) < 0 ? BigDecimal.ZERO : total.setScale(2, RoundingMode.HALF_UP);
    }

    public List<CartItemDto> getItems() {
        return items;
    }

    public void setItems(List<CartItemDto> items) {
        this.items = items;
    }

    public String getCouponCode() {
        return couponCode;
    }

    public void setCouponCode(String couponCode) {
        this.couponCode = couponCode;
    }

    public BigDecimal getDiscountAmount() {
        return discountAmount;
    }

    public void setDiscountAmount(BigDecimal discountAmount) {
        this.discountAmount = discountAmount != null ? discountAmount : BigDecimal.ZERO;
    }
}
