``markdown
# Work Progress Log for IAM/DevSecOps (Issue #8)
### 🔍 What process Diagram Shows
- **Onboarding:** HR triggers IAM → roles provisioned → tools access granted.  
- **Normal Use:** Developer logs in → IAM validates access.  
- **CI/CD Security:** Pipeline requests token → IAM issues short-lived credentials → tools used in scans.  
- **Offboarding:** IAM revokes access when employee leaves or project ends.  

### 🔍 What iam-c4-context Diagram Shows
- **People:** Admin, Developer, HR.  
- **Core Systems:** IAM Service + CI/CD pipeline inside the Nia boundary.  
- **External Systems:** GitHub, Jira, SonarQube.  
- **Relationships:** IAM provisions access, CI/CD consumes IAM tokens, HR triggers events.  

# Work Progress Log for IAM/DevSecOps (Issue #8)

This log tracks the design and documentation progress for the IAM system integrated with DevSecOps.  
Each step corresponds to a diagram or set of diagrams stored in the `docs/` folder.

---

## ✅ Step 1: Business Use Case Diagram
- File: `docs/iam-usecase.md`
- Purpose: Show IAM interactions from a **business perspective**.
- Highlights:
  - Actors: Employee, Admin, CI/CD Pipeline, External Tools (GitHub, Jira, SonarQube).
  - Use cases: Login, Request Access, Provision, Revoke, Role-based control, Token issuance.
- Status: **Completed**

---

## ✅ Step 2: Business Process Flow
- File: `docs/process.md`
- Purpose: Describe IAM in the **business workflow** (onboarding, provisioning, offboarding, CI/CD integration).
- Highlights:
  - HR triggers onboarding → IAM provisions access.
  - Developers log in → IAM validates access.
  - CI/CD requests tokens → IAM issues short-lived tokens.
  - Offboarding revokes access automatically.
- Status: **Completed**

---

## ✅ Step 3: C4 Context Diagram
- File: `docs/iam-c4-context-flow.md`
- Purpose: Show the **high-level architecture** — how IAM connects with people and systems.
- Highlights:
  - People: HR, Admin, Developer.
  - Core: IAM Service + CI/CD Pipeline.
  - External Systems: GitHub, Jira, SonarQube.
  - Flowchart layout used for clarity (no overlaps).
- Status: **Completed**

---

## ✅ Step 4: C4 Container Diagram
- File: `docs/iam-c4-container.md`
- Purpose: Break IAM into **main subsystems/containers**.
- Highlights:
  - API Gateway.
  - Policy Engine.
  - Identity Store.
  - Token Service.
  - Audit & Logging.
- Status: **Completed**

---

## ✅ Step 5: IAM Component-Level Diagrams
- Purpose: Zoom into each container to show **internal details**.
- Sub-steps:
  - **Step 5a** – API Gateway (`docs/iam-api-components.md`)
    - Endpoints: `/login`, `/register`, `/request-access`, `/provision`, `/revoke`, `/token`.
    - Connects developers, admins, and CI/CD to IAM.
  - **Step 5b** – Policy Engine (`docs/iam-policy-components.md`)
    - Components: PEP (Enforcement), PDP (Decision), RBAC, ABAC, Policy Store.
    - Central brain for enforcing access rules.
  - **Step 5c** – Identity Store (`docs/iam-database.md`)
    - Flowchart view of tables: Users, Roles, Permissions, User ↔ Role mapping, Role ↔ Permission mapping, Audit logs.
    - Tracks identities and their privileges.
  - **Step 5d** – Token Service (`docs/iam-token-service.md`)
    - Modules: JWT Generator, OAuth2 Handler, TTL Expiry, Validator.
    - Issues and validates short-lived tokens for CI/CD.
  - **Step 5e** – Audit & Logging (`docs/iam-audit.md`)
    - Components: Collector, Log Storage, Analyzer.
    - Captures actions for security monitoring and compliance.
- Status: **Completed**

---

# ✅ Current Status
- All business-level and technical diagrams (Context, Container, Components) are **completed**.
- Repository now contains a **full blueprint** for IAM design in DevSecOps.

---

# 🔜 Next Steps (Planned)
- **Step 6: Sequence Diagrams**  
  Show runtime interactions for key flows:
  - User Login.
  - Access Provisioning.
  - CI/CD Token Issuance.
  - Offboarding/Revocation.
- These will demonstrate **how components interact dynamically** beyond the static architecture.


# Work Progress Log for IAM/DevSecOps (Issue #8)

- [x] Step 1: Business Use Case Diagram (`docs/iam-usecase.md`)
- [x] Step 2: Business Process Flow (`docs/process.md`)
- [x] Step 3: C4 Context Diagram (`docs/iam-c4-context-flow.md`)
- [x] Step 4: C4 Container Diagram (`docs/iam-c4-container.md`)
- [x] Step 5a: API Gateway Components (`docs/iam-api-components.md`)
- [x] Step 5b: Policy Engine Components (`docs/iam-policy-components.md`)
- [x] Step 5c: Identity Store Design (`docs/iam-database.md`)
- [x] Step 5d: Token Service Design (`docs/iam-token-service.md`)
- [x] Step 5e: Audit & Logging Design (`docs/iam-audit.md`)