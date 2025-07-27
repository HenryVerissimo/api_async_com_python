from pydantic import ValidationError

from src.schemas import UserCreate
from src.database.mysql.repositories import UsersRepository


class UsersController:
    def __init__(self) -> None:
        self.repository = UsersRepository()

    async def create_user(self, data: dict) -> dict:
        try:
            UserCreate(**data)
            response = await self.repository.Insert_user(data)
            return {"body": {"data": response}, "status": 201}

        except ValidationError as error:
            return {"body": {"error": str(error)}, "status": 400}

        except Exception as error:
            return {"body": {"error": str(error)}, "status": 500}
