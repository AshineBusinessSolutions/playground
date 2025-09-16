# C4 Context Diagram – IAM in DevSecOps (Nia Project)

This diagram shows how IAM fits into the Nia project’s ecosystem, highlighting users, systems, and external tools.

```mermaid
C4Context
    title Nia Project – IAM Integration (Context View)

    Person(admin, "Admin", "Manages roles, access, and policies")
    Person(dev, "Developer/Employee", "Uses the system for work and requests access")
    Person(hr, "HR System", "Triggers onboarding and offboarding events")

    System_Boundary(nia, "Nia Project") {
        System(iam, "IAM Service", "Identity & Access Management APIs, roles, policies")
        System(cicd, "CI/CD Pipeline", "Build, test, deploy automation with security checks")
    }

    System_Ext(github, "GitHub", "Source code repository and version control")
    System_Ext(jira, "Jira", "Project/task management")
    System_Ext(sonar, "SonarQube", "Static code analysis and vulnerability scanning")

    Rel(hr, iam, "Sends onboarding/offboarding events")
    Rel(dev, iam, "Login, request access")
    Rel(admin, iam, "Defines roles, manages access policies")
    Rel(iam, github, "Provision/revoke access")
    Rel(iam, jira, "Provision/revoke access")
    Rel(iam, sonar, "Provision/revoke access")
    Rel(cicd, iam, "Requests short-lived tokens")
    Rel(iam, cicd, "Issues tokens for secure integration")
    Rel(cicd, sonar, "Runs security scans with IAM-issued tokens")
