from pydantic import BaseModel


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    age: int
    email: str
    password: str
    confirm_password: str
