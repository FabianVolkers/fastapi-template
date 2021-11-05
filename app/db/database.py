from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# from app.config import settings

# SQLALCHEMY_DATABASE_URL = "sqlite:///./config.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# engine = create_engine(
#   settings.sqlalchemy_database_url, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@lru_cache
def get_db_engine(database_url: str) -> Engine:
    engine = create_engine(
        database_url, connect_args={"check_same_thread": False}
    )

    return engine


def get_session_local(database_url: str) -> sessionmaker:
    engine = get_db_engine(database_url)
    SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    return SessionLocal


Base = declarative_base()
