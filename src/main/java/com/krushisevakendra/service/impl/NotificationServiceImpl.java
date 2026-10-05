package com.krushisevakendra.service.impl;

import com.krushisevakendra.dto.ReminderDto;
import com.krushisevakendra.entity.Notification;
import com.krushisevakendra.entity.User;
import com.krushisevakendra.enums.NotificationType;
import com.krushisevakendra.exception.ResourceNotFoundException;
import com.krushisevakendra.repository.NotificationRepository;
import com.krushisevakendra.repository.UserRepository;
import com.krushisevakendra.service.NotificationService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.List;

@Service
@Transactional
public class NotificationServiceImpl implements NotificationService {

    private static final Logger log = LoggerFactory.getLogger(NotificationServiceImpl.class);

    private final NotificationRepository notificationRepository;
    private final UserRepository userRepository;

    public NotificationServiceImpl(NotificationRepository notificationRepository, UserRepository userRepository) {
        this.notificationRepository = notificationRepository;
        this.userRepository = userRepository;
    }

    @Override
    public Notification createNotification(User user, String title, String message, NotificationType type) {
        Notification notification = new Notification(user, title, message, type);
        notification.setSentAt(LocalDateTime.now());
        notification.setIsRead(false);
        return notificationRepository.save(notification);
    }

    @Override
    public boolean sendReminder(ReminderDto reminderDto) {
        User user = userRepository.findById(reminderDto.getUserId())
                .orElseThrow(() -> new ResourceNotFoundException("Customer not found with id: " + reminderDto.getUserId()));

        NotificationType type = reminderDto.getType() != null ? reminderDto.getType() : NotificationType.WHATSAPP;
        String message = reminderDto.getMessage();

        // Pluggable channel dispatch abstraction
        switch (type) {
            case SMS -> log.info("[SMS GATEWAY] Sending SMS to {}: {}", user.getMobile(), message);
            case WHATSAPP -> log.info("[WHATSAPP API] Dispatching WhatsApp message to {}: {}", user.getMobile(), message);
            case EMAIL -> log.info("[EMAIL SERVICE] Dispatching Email to {}: {}", user.getEmail(), message);
            case IN_APP -> log.info("[IN-APP ALERT] Creating in-app notification for User: {}", user.getName());
        }

        // Save in-app record for customer dashboard
        String title = type == NotificationType.WHATSAPP ? "WhatsApp Payment Reminder" :
                       type == NotificationType.SMS ? "SMS Payment Reminder" : "Payment Due Reminder";

        createNotification(user, title, message, type);
        return true;
    }

    @Override
    @Transactional(readOnly = true)
    public List<Notification> getUserNotifications(Long userId) {
        return notificationRepository.findByUserIdOrderBySentAtDesc(userId);
    }

    @Override
    @Transactional(readOnly = true)
    public Page<Notification> getUserNotificationsPaged(Long userId, Pageable pageable) {
        return notificationRepository.findByUserIdOrderBySentAtDesc(userId, pageable);
    }

    @Override
    @Transactional(readOnly = true)
    public long getUnreadCount(Long userId) {
        return notificationRepository.countByUserIdAndIsReadFalse(userId);
    }

    @Override
    public void markAsRead(Long notificationId) {
        notificationRepository.findById(notificationId).ifPresent(n -> {
            n.setIsRead(true);
            notificationRepository.save(n);
        });
    }

    @Override
    public void markAllAsRead(Long userId) {
        List<Notification> notifications = notificationRepository.findByUserIdOrderBySentAtDesc(userId);
        for (Notification n : notifications) {
            n.setIsRead(true);
        }
        notificationRepository.saveAll(notifications);
    }
}
