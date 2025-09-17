# IAM – Policy Engine Components

```mermaid
flowchart TB
    subgraph PolicyEngine [📜 Policy Engine]
        RBAC[RBAC: Role-Based Access Control]
        ABAC[ABAC: Attribute-Based Access Control]
        PDP[Policy Decision Point]
        PEP[Policy Enforcement Point]
        PolicyDB[(Policy Database)]
    end

    API[🌐 API Gateway] --> PEP
    PEP --> PDP
    PDP --> RBAC
    PDP --> ABAC
    PDP --> PolicyDB
    PDP --> TokenService[🔑 Token Service]
    PDP --> Provisioning[⚙️ Provisioning Modules]
