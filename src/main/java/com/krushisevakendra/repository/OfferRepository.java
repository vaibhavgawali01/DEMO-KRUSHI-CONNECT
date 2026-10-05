package com.krushisevakendra.repository;

import com.krushisevakendra.entity.Offer;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface OfferRepository extends JpaRepository<Offer, Long> {
    Optional<Offer> findByCouponCodeAndActiveTrue(String couponCode);
    List<Offer> findByActiveTrueOrderByCreatedAtDesc();
}
