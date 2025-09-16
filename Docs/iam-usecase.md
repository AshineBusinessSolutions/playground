# IAM Use Case Diagram – DevSecOps Integration

This diagram shows the main IAM interactions in the Nia project, combining Employees, Admins, CI/CD, and external tools like GitHub, Jira, and SonarQube.

```mermaid
%% Business Use Case Diagram for IAM in DevSecOps

usecaseDiagram
  actor Employee as E
  actor Admin as A
  actor "CI/CD Pipeline" as P
  actor "External Tools\n(GitHub, Jira, SonarQube)" as T

  rectangle IAM {
    usecase "Login & Authentication" as UC1
    usecase "Request Access" as UC2
    usecase "Provision Access" as UC3
    usecase "Revoke/De-provision Access" as UC4
    usecase "Role-Based Access Control" as UC5
    usecase "Token-based Access for CI/CD" as UC6
  }

  E --> UC1
  E --> UC2
  A --> UC3
  A --> UC4
  A --> UC5
  P --> UC6
  UC3 --> T
  UC4 --> T
  UC6 --> T
