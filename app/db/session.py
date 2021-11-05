from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker


def get_db_session(database_uri: str) -> sessionmaker:

    engine: Engine = create_engine(
        database_uri,
        pool_pre_ping=True,
        connect_args={"check_same_thread": False}
    )

    return sessionmaker(autocommit=False, autoflush=False, bind=engine)
