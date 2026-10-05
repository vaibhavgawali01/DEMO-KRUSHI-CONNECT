package com.krushisevakendra.service.impl;

import com.krushisevakendra.dto.CustomerUpdateDto;
import com.krushisevakendra.dto.UserRegistrationDto;
import com.krushisevakendra.entity.Role;
import com.krushisevakendra.entity.User;
import com.krushisevakendra.enums.RoleName;
import com.krushisevakendra.exception.ResourceNotFoundException;
import com.krushisevakendra.repository.RoleRepository;
import com.krushisevakendra.repository.UserRepository;
import com.krushisevakendra.service.UserService;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.Collections;
import java.util.List;
import java.util.Optional;

@Service
@Transactional
public class UserServiceImpl implements UserService {

    private final UserRepository userRepository;
    private final RoleRepository roleRepository;
    private final PasswordEncoder passwordEncoder;

    public UserServiceImpl(UserRepository userRepository, RoleRepository roleRepository, PasswordEncoder passwordEncoder) {
        this.userRepository = userRepository;
        this.roleRepository = roleRepository;
        this.passwordEncoder = passwordEncoder;
    }

    @Override
    public User registerCustomer(UserRegistrationDto dto) {
        if (userRepository.existsByEmail(dto.getEmail().trim())) {
            throw new IllegalArgumentException("Email is already registered / हा ईमेल आधीच नोंदणीकृत आहे");
        }
        if (userRepository.existsByMobile(dto.getMobile().trim())) {
            throw new IllegalArgumentException("Mobile number is already registered / हा मोबाईल नंबर आधीच नोंदणीकृत आहे");
        }

        Role customerRole = roleRepository.findByName(RoleName.ROLE_CUSTOMER)
                .orElseGet(() -> roleRepository.save(new Role(RoleName.ROLE_CUSTOMER)));

        User user = new User();
        user.setName(dto.getName().trim());
        user.setMobile(dto.getMobile().trim());
        user.setEmail(dto.getEmail().trim());
        user.setAddress(dto.getAddress().trim());
        user.setVillage(dto.getVillage().trim());
        user.setTaluka(dto.getTaluka().trim());
        user.setDistrict(dto.getDistrict().trim());
        user.setPasswordHash(passwordEncoder.encode(dto.getPassword()));
        user.setStatus("ACTIVE");
        user.setCreatedAt(LocalDateTime.now());
        user.setRoles(Collections.singleton(customerRole));

        return userRepository.save(user);
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<User> findById(Long id) {
        return userRepository.findById(id);
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<User> findByEmail(String email) {
        return userRepository.findByEmail(email);
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<User> findByMobile(String mobile) {
        return userRepository.findByMobile(mobile);
    }

    @Override
    @Transactional(readOnly = true)
    public Optional<User> findByEmailOrMobile(String identifier) {
        return userRepository.findByEmailOrMobile(identifier);
    }

    @Override
    public User updateProfile(Long userId, User userDetails) {
        User user = userRepository.findById(userId)
                .orElseThrow(() -> new ResourceNotFoundException("User not found with id: " + userId));

        user.setName(userDetails.getName());
        user.setAddress(userDetails.getAddress());
        user.setVillage(userDetails.getVillage());
        user.setTaluka(userDetails.getTaluka());
        user.setDistrict(userDetails.getDistrict());

        if (userDetails.getPasswordHash() != null && !userDetails.getPasswordHash().isBlank()) {
            user.setPasswordHash(passwordEncoder.encode(userDetails.getPasswordHash()));
        }

        return userRepository.save(user);
    }

    @Override
    public User updateCustomerByAdmin(CustomerUpdateDto dto) {
        User user = userRepository.findById(dto.getId())
                .orElseThrow(() -> new ResourceNotFoundException("Customer not found with id: " + dto.getId()));

        if (dto.getName() != null && !dto.getName().isBlank()) {
            user.setName(dto.getName().trim());
        }
        if (dto.getMobile() != null && !dto.getMobile().isBlank()) {
            user.setMobile(dto.getMobile().trim());
        }
        if (dto.getEmail() != null && !dto.getEmail().isBlank()) {
            user.setEmail(dto.getEmail().trim());
        }
        if (dto.getAddress() != null) {
            user.setAddress(dto.getAddress().trim());
        }
        if (dto.getVillage() != null) {
            user.setVillage(dto.getVillage().trim());
        }
        if (dto.getTaluka() != null) {
            user.setTaluka(dto.getTaluka().trim());
        }
        if (dto.getDistrict() != null) {
            user.setDistrict(dto.getDistrict().trim());
        }
        if (dto.getStatus() != null && !dto.getStatus().isBlank()) {
            user.setStatus(dto.getStatus().trim().toUpperCase());
        }

        return userRepository.save(user);
    }

    @Override
    public User updateStatus(Long userId, String status) {
        User user = userRepository.findById(userId)
                .orElseThrow(() -> new ResourceNotFoundException("User not found with id: " + userId));
        user.setStatus(status);
        return userRepository.save(user);
    }

    @Override
    @Transactional(readOnly = true)
    public List<User> getAllCustomers() {
        return userRepository.findAllCustomers();
    }

    @Override
    @Transactional(readOnly = true)
    public Page<User> searchCustomers(String query, Pageable pageable) {
        if (query == null || query.isBlank()) {
            return userRepository.searchCustomers("", pageable);
        }
        return userRepository.searchCustomers(query.trim(), pageable);
    }

    @Override
    @Transactional(readOnly = true)
    public long getCustomerCount() {
        return userRepository.countCustomers();
    }
}
