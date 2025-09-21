package com.example.activiti_bpm_login;  // this is YOUR package!

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;

@Configuration
public class SecurityConfig {

    @Bean
    public UserDetailsService userDetailsService() {
        InMemoryUserDetailsManager manager = new InMemoryUserDetailsManager();
        manager.createUser(
                User.withDefaultPasswordEncoder()
                        .username("admin")
                        .password("admin")
                        .roles("ACTIVITI_USER", "ACTIVITI_ADMIN")
                        .build()
        );
        manager.createUser(
                User.withDefaultPasswordEncoder()
                        .username("user")
                        .password("pass")
                        .roles("ACTIVITI_USER")
                        .build()
        );
        return manager;
    }
}
