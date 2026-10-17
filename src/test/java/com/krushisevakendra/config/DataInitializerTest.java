package com.krushisevakendra.config;

import com.krushisevakendra.entity.Role;
import com.krushisevakendra.entity.User;
import com.krushisevakendra.enums.RoleName;
import com.krushisevakendra.repository.*;
import org.junit.jupiter.api.Test;
import org.springframework.security.crypto.password.PasswordEncoder;

import java.util.Optional;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

class DataInitializerTest {

    @Test
    void doesNotCreateSampleAccountsOrStoreDataWhenDemoSeedingIsDisabled() {
        RoleRepository roleRepository = mock(RoleRepository.class);
        UserRepository userRepository = mock(UserRepository.class);
        CategoryRepository categoryRepository = mock(CategoryRepository.class);
        ProductRepository productRepository = mock(ProductRepository.class);
        OrderRepository orderRepository = mock(OrderRepository.class);
        UdhariRepository udhariRepository = mock(UdhariRepository.class);
        PaymentRepository paymentRepository = mock(PaymentRepository.class);
        NotificationRepository notificationRepository = mock(NotificationRepository.class);
        OfferRepository offerRepository = mock(OfferRepository.class);
        FeedbackRepository feedbackRepository = mock(FeedbackRepository.class);
        PasswordEncoder passwordEncoder = mock(PasswordEncoder.class);

        Role adminRole = new Role(RoleName.ROLE_ADMIN);
        Role customerRole = new Role(RoleName.ROLE_CUSTOMER);
        when(roleRepository.findByName(RoleName.ROLE_ADMIN)).thenReturn(Optional.of(adminRole));
        when(roleRepository.findByName(RoleName.ROLE_CUSTOMER)).thenReturn(Optional.of(customerRole));
        User admin = new User();
        when(userRepository.findByEmail("admin@krushiseva.com")).thenReturn(Optional.of(admin));
        when(userRepository.save(any(User.class))).thenAnswer(invocation -> invocation.getArgument(0));

        DataInitializer initializer = new DataInitializer(
                roleRepository, userRepository, categoryRepository, productRepository,
                orderRepository, udhariRepository, paymentRepository, notificationRepository,
                offerRepository, feedbackRepository, passwordEncoder, "", false);

        initializer.run();

        verify(userRepository).save(admin);
        verify(userRepository, never()).findByEmail("ramesh@patil.com");
        verify(userRepository, never()).findByEmail("suresh@deshmukh.com");
        verify(userRepository, never()).findAll();
        verifyNoInteractions(categoryRepository, productRepository, orderRepository,
                udhariRepository, paymentRepository, notificationRepository,
                offerRepository, feedbackRepository, passwordEncoder);
    }
}
