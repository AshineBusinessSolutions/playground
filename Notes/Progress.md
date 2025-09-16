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

- [x] Step 1: Business Use Case Diagram (iam-usecase.md)
- [x] Step 2: Business Process Flow (process.md)
- [x] Step 3: C4 Context Diagram (iam-c4-context.md)
- [ ] Step 4: C4 Container Diagram.