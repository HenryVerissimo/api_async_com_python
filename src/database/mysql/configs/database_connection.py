from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
    AsyncEngine,
)

from typing import AsyncGenerator, Optional
from decouple import config
from contextlib import asynccontextmanager


class MySQLConnectionHandler:
    """
    Class responsible for creating and managing asynchronous connections to the MySQL database using SQLAlchemy.
    """

    _engine: Optional[AsyncEngine] = None
    _session_factory: Optional[async_sessionmaker[AsyncSession]] = None

    def __init__(self):
        self._database_uri: str = config("DATABASE_URI", cast=str)
        self._echo_debug: bool = config("ECHO", cast=bool)

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """
        Asynchronous context manager that provides a database session.

        Ensures safe opening and closing of the session.
        """

        async with self.session_factory() as session:
            yield session

    @property
    def session_factory(self) -> async_sessionmaker[AsyncSession]:
        """
        Returns a singleton session factory.

        Creates an asynchronous session factory, ensuring that it is unique.
        """

        if not MySQLConnectionHandler._session_factory:
            MySQLConnectionHandler._session_factory = async_sessionmaker(
                bind=self.engine,
                expire_on_commit=False,
                class_=AsyncSession,
            )

        return MySQLConnectionHandler._session_factory

    @property
    def engine(self) -> AsyncEngine:
        """
        Returns a singleton Engine instance.

        Ensures only Engine is created and reused for all database sessions.
        """

        if not MySQLConnectionHandler._engine:
            MySQLConnectionHandler._engine = create_async_engine(
                self._database_uri,
                echo=self._echo_debug,
            )

        return MySQLConnectionHandler._engine
