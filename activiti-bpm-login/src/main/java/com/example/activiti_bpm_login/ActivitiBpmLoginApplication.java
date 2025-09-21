package com.example.activiti_bpm_login;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import javax.annotation.PostConstruct;


@SpringBootApplication
public class ActivitiBpmLoginApplication
{

	public static void main(String[] args)
	{
		SpringApplication.run(ActivitiBpmLoginApplication.class, args);
	}
	@PostConstruct
	public void printProps() {
		System.out.println("spring.datasource.url=" + System.getProperty("spring.datasource.url"));
	}

}
