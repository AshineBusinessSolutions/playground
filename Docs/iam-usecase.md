# IAM Business Flow – DevSecOps

```mermaid
flowchart TD
    E[Employee] -->|Login| IAM1(Login & Authentication)
    E -->|Request Access| IAM2(Request Access)
    A[Admin] -->|Provision Access| IAM3(Provision Access)
    A -->|Revoke Access| IAM4(Revoke/De-provision Access)
    A -->|Define Roles| IAM5(Role-Based Access Control)
    P[CI/CD Pipeline] -->|Token Request| IAM6(Token-based Access for CI/CD)

    IAM3 --> T[External Tools: GitHub, Jira, SonarQube]
    IAM4 --> T
    IAM6 --> T
