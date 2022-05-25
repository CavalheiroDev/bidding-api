from typing import Optional, TypedDict


class UserCreatorTypedDict(TypedDict):
    username: str
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    is_superuser: bool
    password: str
