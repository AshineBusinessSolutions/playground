# C4 Container Diagram – IAM in DevSecOps (Nia Project)

```mermaid
flowchart LR
    %% People
    Admin([🛠️ Admin])
    Dev([👩‍💻 Developer])
    HR([🧑‍💼 HR System])

    %% IAM Service internals
    subgraph IAM [🛡️ IAM Service]
        APIGW[[🌐 API Gateway]]
        Policy[[📜 Policy Engine]]
        Token[[🔑 Token Service]]
        DB[(🗄️ Identity Store)]
        Audit[[📝 Audit & Logging]]
    end

    %% CI/CD Pipeline
    CICD[[⚙️ CI/CD Pipeline]]

    %% External Tools
    GitHub[(📂 GitHub)]
    Jira[(📋 Jira)]
    Sonar[(🔍 SonarQube)]

    %% Relationships
    HR -->|On/Offboarding| APIGW
    Dev -->|Login / Request Access| APIGW
    Admin -->|Manage Roles & Policies| Policy

    APIGW --> Policy
    Policy --> DB
    Policy --> Token
    Policy --> Audit

    Token --> CICD
    CICD --> Sonar

    Policy -->|Provision / Revoke| GitHub
    Policy -->|Provision / Revoke| Jira
    Policy -->|Provision / Revoke| Sonar
