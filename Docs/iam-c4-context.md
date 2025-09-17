# IAM in DevSecOps – Context (Flowchart Layout with Shapes)

```mermaid
flowchart LR
    %% People on the left (rounded)
    HR([🧑‍💼 HR System])
    Admin([🛠️ Admin])
    Dev([👩‍💻 Developer])

    %% Core systems in the center (rectangles)
    subgraph NiaProject [🏗️ Nia Project]
        IAM[[🛡️ IAM Service]]
        CICD[[⚙️ CI/CD Pipeline]]
    end

    %% External tools on the right (document shapes)
    GitHub[(📂 GitHub)]
    Jira[(📋 Jira)]
    Sonar[(🔍 SonarQube)]

    %% Relationships
    HR -->|On/Offboarding| IAM
    Dev -->|Login / Request Access| IAM
    Admin -->|Manage Roles| IAM

    IAM -->|Provision / Revoke| GitHub
    IAM -->|Provision / Revoke| Jira
    IAM -->|Provision / Revoke| Sonar

    CICD -->|Request Token| IAM
    IAM -->|Issue Tokens| CICD
    CICD -->|Run Scans| Sonar
