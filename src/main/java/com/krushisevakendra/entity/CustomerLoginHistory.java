package com.krushisevakendra.entity;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "customer_login_history")
public class CustomerLoginHistory {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "user_id", nullable = false)
    private User user;

    @Column(name = "logged_in_at", nullable = false)
    private LocalDateTime loggedInAt;

    public CustomerLoginHistory() {}

    public CustomerLoginHistory(User user, LocalDateTime loggedInAt) {
        this.user = user;
        this.loggedInAt = loggedInAt;
    }

    public Long getId() {
        return id;
    }

    public User getUser() {
        return user;
    }

    public LocalDateTime getLoggedInAt() {
        return loggedInAt;
    }
}
