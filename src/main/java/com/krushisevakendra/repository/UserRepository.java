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

    @Query("SELECT u FROM User u JOIN u.roles r WHERE r.name = 'ROLE_CUSTOMER'")
    List<User> findAllCustomers();

    @Query("SELECT u FROM User u JOIN u.roles r WHERE r.name = 'ROLE_CUSTOMER' AND " +
           "(LOWER(u.name) LIKE LOWER(CONCAT('%', :query, '%')) OR " +
           "u.mobile LIKE CONCAT('%', :query, '%') OR " +
           "LOWER(u.village) LIKE LOWER(CONCAT('%', :query, '%')))")
    Page<User> searchCustomers(@Param("query") String query, Pageable pageable);

    @Query("SELECT COUNT(u) FROM User u JOIN u.roles r WHERE r.name = 'ROLE_CUSTOMER'")
    long countCustomers();
}
