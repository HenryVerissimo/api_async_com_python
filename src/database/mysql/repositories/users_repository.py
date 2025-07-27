from src.database.mysql.configs import MySQLConnectionHandler
from src.database.mysql.models import User


class UsersRepository:
    async def Insert_user(self, data: dict) -> dict:
        async with MySQLConnectionHandler().get_session() as session:
            try:
                new_user = User(
                    name=data["name"],
                    age=data["age"],
                    email=data["email"],
                )

                await new_user.set_password_hash(data["password"])
                session.add(new_user)
                await session.commit()
                return data

            except Exception as error:
                print(3)
                await session.rollback()
                raise Exception(f"Error: {error}")
