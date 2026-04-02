from fastapi import HTTPException, Query


def role_required(allowed_roles: list):
    def checker(role: str = Query(...)):
        if role not in allowed_roles:
            raise HTTPException(
                status_code=403,
                detail=f"Access denied. Allowed roles: {allowed_roles}"
            )
        return role

    return checker