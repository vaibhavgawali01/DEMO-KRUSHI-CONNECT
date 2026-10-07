package com.krushisevakendra.security;

import com.krushisevakendra.entity.User;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import java.util.Collection;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import com.krushisevakendra.enums.RoleName;
import com.krushisevakendra.entity.Role;

public class CustomUserDetails implements UserDetails {

    private final User user;

    public CustomUserDetails(User user) {
        this.user = user;
    }

    public User getUser() {
        return user;
    }

    public Long getId() {
        return user.getId();
    }

    public String getName() {
        return user.getName();
    }

    public String getMobile() {
        return user.getMobile();
    }

    public String getEmail() {
        return user.getEmail();
    }

    public String getVillage() {
        return user.getVillage();
    }

    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
        Set<SimpleGrantedAuthority> auths = new HashSet<>();
        boolean isMasterAdmin = user.getEmail() != null && "admin@krushiseva.com".equalsIgnoreCase(user.getEmail().trim());

        if (user.getRoles() != null) {
            for (Role role : user.getRoles()) {
                if (role.getName() == RoleName.ROLE_ADMIN) {
                    if (isMasterAdmin) {
                        auths.add(new SimpleGrantedAuthority("ROLE_ADMIN"));
                    }
                } else {
                    auths.add(new SimpleGrantedAuthority(role.getName().name()));
                }
            }
        }
        if (auths.isEmpty() || !isMasterAdmin) {
            auths.add(new SimpleGrantedAuthority("ROLE_CUSTOMER"));
        }
        return auths;
    }

    @Override
    public String getPassword() {
        return user.getPasswordHash();
    }

    @Override
    public String getUsername() {
        return user.getEmail();
    }

    @Override
    public boolean isAccountNonExpired() {
        return true;
    }

    @Override
    public boolean isAccountNonLocked() {
        return !"BLOCKED".equalsIgnoreCase(user.getStatus());
    }

    @Override
    public boolean isCredentialsNonExpired() {
        return true;
    }

    @Override
    public boolean isEnabled() {
        return "ACTIVE".equalsIgnoreCase(user.getStatus());
    }
}
