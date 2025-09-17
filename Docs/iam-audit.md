# IAM – Audit & Logging

```mermaid
flowchart TB
    subgraph Audit [📝 Audit & Logging Service]
        Collector[Collect Actions]
        LogStore[(Audit Storage)]
        Analyzer[Analyze Logs & Patterns]
    end

    API[🌐 API Gateway] --> Collector
    PolicyEngine[📜 Policy Engine] --> Collector
    TokenService[🔑 Token Service] --> Collector

    Collector --> LogStore
    LogStore --> Analyzer
