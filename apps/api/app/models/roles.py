from enum import Enum


class Role(str, Enum):
    OWNER = "owner"
    EDITOR = "editor"
    MEMBER = "member"
    VIEWER = "viewer"