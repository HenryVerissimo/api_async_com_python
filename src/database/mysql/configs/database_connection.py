from sqlmodel import create_engine, Session
from sqlalchemy.engine import Engine
from decouple import config


class MySQLConnectionHandler:
    _engine: Engine | None = None

    def __init__(self):
        self._database_uri: str = config("DATABASE_URI", cast=str)
        self.session: Session | None = None

    def connect_db(self):
        """Create session with database"""

        self.session = Session(self.engine)

    def close_connection(self):
        if self.session:
            self.session.close()
            self.session = None

    def __enter__(self):
        self.connect_db()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_connection()

    @property
    def engine(self) -> Engine:
        if not MySQLConnectionHandler._engine:
            MySQLConnectionHandler._engine = create_engine(self._database_uri)

        return MySQLConnectionHandler._engine
