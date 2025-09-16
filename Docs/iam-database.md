# IAM – Identity Store (Flowchart View)

```mermaid
flowchart TB
    subgraph DB [🗄️ Identity Store]
        USERS[Users Table]
        ROLES[Roles Table]
        PERMS[Permissions Table]
        USER_ROLES[User ↔ Role Mapping]
        ROLE_PERMS[Role ↔ Permission Mapping]
        AUDIT[Audit Logs]
    end

    USERS --> USER_ROLES
    ROLES --> USER_ROLES
    ROLES --> ROLE_PERMS
    PERMS --> ROLE_PERMS
    USERS --> AUDIT