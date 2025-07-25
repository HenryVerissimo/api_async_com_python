from sqlmodel import create_engine, Session
from sqlalchemy.engine import Engine
from typing import Self
from decouple import config


class MySQLConnectionHandler:
    """
    Create and manipulate the connection to the MySQL database.
    """

    _engine: Engine | None = None

    def __init__(self):
        self._database_uri: str = config("DATABASE_URI", cast=str)
        self.session: Session | None = None

    def connect_db(self) -> None:
        """Create the session with the database"""

        self.session = Session(self.engine)

    def close_connection(self) -> None:
        """Close the session with the database"""

        if self.session:
            self.session.close()
            self.session = None

    def __enter__(self) -> Self:
        self.connect_db()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close_connection()

    @property
    def engine(self) -> Engine:
        """
        Returns a singleton Engine instance.

        Ensures only Engine is created and reused for all database sessions.
        """

        if not MySQLConnectionHandler._engine:
            MySQLConnectionHandler._engine = create_engine(self._database_uri)

        return MySQLConnectionHandler._engine
