# IAM – Token Service

```mermaid
flowchart TB
    subgraph TokenService [🔑 Token Service]
        JWT[JWT Generator]
        OAUTH[OAuth2 Handler]
        TTL[Enforce Expiry]
        Validator[Validate Tokens]
    end

    CICD[⚙️ CI/CD Pipeline] --> OAUTH
    CICD --> JWT

    JWT --> Validator
    Validator --> DB[Identity Store]
