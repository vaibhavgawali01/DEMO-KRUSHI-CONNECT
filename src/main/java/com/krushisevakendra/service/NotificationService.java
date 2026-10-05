package com.krushisevakendra.service;

import com.krushisevakendra.dto.ReminderDto;
import com.krushisevakendra.entity.Notification;
import com.krushisevakendra.entity.User;
import com.krushisevakendra.enums.NotificationType;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

import java.util.List;

public interface NotificationService {
    Notification createNotification(User user, String title, String message, NotificationType type);
    boolean sendReminder(ReminderDto reminderDto);
    List<Notification> getUserNotifications(Long userId);
    Page<Notification> getUserNotificationsPaged(Long userId, Pageable pageable);
    long getUnreadCount(Long userId);
    void markAsRead(Long notificationId);
    void markAllAsRead(Long userId);
}
