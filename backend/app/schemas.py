from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict


class Page(BaseModel):
    page: int
    total: int
    skip: int
    limit: int


class UserBase(BaseModel):
    username: str
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False


class UserCreate(UserBase):
    hashed_password: str


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    registered_on: datetime = None
    last_login: datetime | None


class UserOut(Page):
    users: list[User] = []
