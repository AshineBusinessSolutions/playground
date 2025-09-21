package com.example.activiti_bpm_login;
import org.activiti.engine.delegate.DelegateExecution;
import org.activiti.engine.delegate.JavaDelegate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Component;
@Component("loginDelegate")

public class LoginDelegate implements JavaDelegate {
    @Autowired
    private JdbcTemplate jdbcTemplate;

    @Override
    public void execute(DelegateExecution execution) {
        String username = (String) execution.getVariable("username");
        String password = (String) execution.getVariable("password");
        Boolean authenticated = jdbcTemplate.queryForObject("SELECT COUNT(*) FROM users WHERE username=? AND password=? AND enabled=TRUE", new Object[]{username, password}, Integer.class) > 0;
        execution.setVariable("authenticated", authenticated);
    }
}
