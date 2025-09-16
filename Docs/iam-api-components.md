# IAM – API Gateway Components

```mermaid
flowchart TB
    subgraph API [🌐 API Gateway]
        LOGIN[/POST /login/]
        REGISTER[/POST /register/]
        ACCESS[/POST /request-access/]
        PROVISION[/POST /provision/]
        REVOKE[/POST /revoke/]
        TOKEN[/POST /token/]
    end

    Dev[👩‍💻 Developer] --> LOGIN
    Dev --> REGISTER
    Dev --> ACCESS

    Admin[🛠️ Admin] --> PROVISION
    Admin --> REVOKE

    CICD[⚙️ CI/CD Pipeline] --> TOKEN

    %% API forwards everything to Policy Engine
    API --> Policy[📜 Policy Engine]
