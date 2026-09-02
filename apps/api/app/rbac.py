from fastapi import Depends

from app.dependencies import get_current_user
from app.models.user import User
from app.models.roles import Role


def require_role(*allowed_roles: Role):
    def role_checker(
        current_user: User = Depends(get_current_user),
    ):
        # Role checking will be connected to
        # project membership when project/team
        # membership tables are implemented.
        return current_user

    return role_checker