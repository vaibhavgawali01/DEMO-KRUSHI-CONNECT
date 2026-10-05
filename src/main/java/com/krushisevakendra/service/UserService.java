package com.krushisevakendra.service;

import com.krushisevakendra.dto.CustomerUpdateDto;
import com.krushisevakendra.dto.UserRegistrationDto;
import com.krushisevakendra.entity.User;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

import java.util.List;
import java.util.Optional;

public interface UserService {
    User registerCustomer(UserRegistrationDto dto);
    Optional<User> findById(Long id);
    Optional<User> findByEmail(String email);
    Optional<User> findByMobile(String mobile);
    Optional<User> findByEmailOrMobile(String identifier);
    User updateProfile(Long userId, User userDetails);
    User updateCustomerByAdmin(CustomerUpdateDto dto);
    User updateStatus(Long userId, String status);
    List<User> getAllCustomers();
    Page<User> searchCustomers(String query, Pageable pageable);
    long getCustomerCount();
}
