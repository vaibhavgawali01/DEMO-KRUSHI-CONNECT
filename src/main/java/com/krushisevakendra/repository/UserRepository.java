package com.krushisevakendra.repository;

import com.krushisevakendra.entity.User;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {

    Optional<User> findByEmail(String email);

    Optional<User> findByMobile(String mobile);

    @Query("SELECT u FROM User u WHERE u.email = :identifier OR u.mobile = :identifier")
    Optional<User> findByEmailOrMobile(@Param("identifier") String identifier);

    boolean existsByEmail(String email);

    boolean existsByMobile(String mobile);

    @Query("SELECT DISTINCT u FROM User u WHERE (u.email IS NULL OR LOWER(u.email) <> 'admin@krushiseva.com') AND (u.mobile IS NULL OR u.mobile <> '9876543210') ORDER BY u.id DESC")
    List<User> findAllCustomers();

    @Query(value = "SELECT DISTINCT u FROM User u WHERE (u.email IS NULL OR LOWER(u.email) <> 'admin@krushiseva.com') AND (u.mobile IS NULL OR u.mobile <> '9876543210') AND " +
           "(:query IS NULL OR :query = '' OR " +
           "LOWER(u.name) LIKE LOWER(CONCAT('%', :query, '%')) OR " +
           "(u.email IS NOT NULL AND LOWER(u.email) LIKE LOWER(CONCAT('%', :query, '%'))) OR " +
           "(u.mobile IS NOT NULL AND u.mobile LIKE CONCAT('%', :query, '%')) OR " +
           "(u.village IS NOT NULL AND LOWER(u.village) LIKE LOWER(CONCAT('%', :query, '%')))) ORDER BY u.id DESC",
           countQuery = "SELECT COUNT(DISTINCT u) FROM User u WHERE (u.email IS NULL OR LOWER(u.email) <> 'admin@krushiseva.com') AND (u.mobile IS NULL OR u.mobile <> '9876543210') AND " +
           "(:query IS NULL OR :query = '' OR " +
           "LOWER(u.name) LIKE LOWER(CONCAT('%', :query, '%')) OR " +
           "(u.email IS NOT NULL AND LOWER(u.email) LIKE LOWER(CONCAT('%', :query, '%'))) OR " +
           "(u.mobile IS NOT NULL AND u.mobile LIKE CONCAT('%', :query, '%')) OR " +
           "(u.village IS NOT NULL AND LOWER(u.village) LIKE LOWER(CONCAT('%', :query, '%'))))")
    Page<User> searchCustomers(@Param("query") String query, Pageable pageable);

    @Query("SELECT COUNT(DISTINCT u) FROM User u WHERE (u.email IS NULL OR LOWER(u.email) <> 'admin@krushiseva.com') AND (u.mobile IS NULL OR u.mobile <> '9876543210')")
    long countCustomers();
}
