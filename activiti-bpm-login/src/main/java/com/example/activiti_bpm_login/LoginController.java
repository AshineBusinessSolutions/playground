package com.example.activiti_bpm_login;
import org.activiti.api.process.runtime.ProcessRuntime;
import org.activiti.api.process.model.ProcessInstance;
import org.activiti.api.process.model.builders.ProcessPayloadBuilder;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;
@RestController
public class LoginController {
    @Autowired
    private ProcessRuntime processRuntime;

    @PostMapping("/login")
    public ResponseEntity<String> login(@RequestBody Map<String, Object> credentials) {
        String username = (String) credentials.get("username");
        String password = (String) credentials.get("password");

        ProcessInstance pi = processRuntime.start(ProcessPayloadBuilder
                .start()
                .withProcessDefinitionKey("Process_123")
                .withVariable("username", username)
                .withVariable("password", password)
                .build());

        return ResponseEntity.ok("Process started with instance ID: " + pi.getId());
    }
}





