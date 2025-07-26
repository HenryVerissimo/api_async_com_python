from sqlmodel import SQLModel, Field
from asyncio import to_thread
from passlib.hash import bcrypt


class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(nullable=False, max_length=100)
    age: int = Field(nullable=False)
    email: str = Field(nullable=False, max_length=100, index=True)
    password_hash: str = Field(nullable=False)

    async def set_password_hash(self, password: str) -> None:
        """convert user password in hash"""

        self.password_hash = await to_thread(bcrypt.hash, password)

    async def verify_password(self, password: str) -> bool:
        """verify that the user's password is true with hashing"""

        return await to_thread(bcrypt.verify, password, self.password_hash)
