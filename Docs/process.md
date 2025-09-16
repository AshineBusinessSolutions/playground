# IAM Business Process Flow – DevSecOps Integration

This flow shows how IAM integrates into the DevSecOps lifecycle during onboarding, access management, CI/CD operations, and offboarding.

```mermaid
flowchart TD
    HR[HR System] -->|New Hire Event| IAM1[Trigger IAM API]
    IAM1 --> IAM2[Provision Role-Based Access]
    IAM2 --> Tools[External Tools: GitHub, Jira, SonarQube]

    Dev[Developer/Employee] -->|Login| IAM3[Authentication]
    IAM3 --> IAM4[Access Validation]

    Pipeline[CI/CD Pipeline] -->|Request Token| IAM5[Issue Short-Lived Token]
    IAM5 --> SecTools[Security Tools: SonarQube, Vulnerability Scanners]

    IAM6[Offboarding Event] -->|Revoke Access| Tools
    IAM6 --> IAM4
