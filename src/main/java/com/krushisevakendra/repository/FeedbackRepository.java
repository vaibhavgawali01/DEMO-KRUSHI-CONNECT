package com.krushisevakendra.repository;

import com.krushisevakendra.entity.Feedback;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface FeedbackRepository extends JpaRepository<Feedback, Long> {
    List<Feedback> findByProductIdAndStatusOrderByCreatedAtDesc(Long productId, String status);
    Page<Feedback> findByStatusOrderByCreatedAtDesc(String status, Pageable pageable);
    
    @Query("SELECT AVG(f.rating) FROM Feedback f WHERE f.product.id = :productId AND f.status = 'APPROVED'")
    Double calculateAverageRatingForProduct(@Param("productId") Long productId);

    @Query("SELECT COUNT(f) FROM Feedback f WHERE f.product.id = :productId AND f.status = 'APPROVED'")
    long countApprovedByProductId(@Param("productId") Long productId);
}
