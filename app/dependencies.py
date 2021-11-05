from functools import lru_cache
from typing import Generator

from fastapi.param_functions import Depends
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import Session, sessionmaker

from app.config import Settings
from app.db.database import get_session_local
from app.db.session import get_db_session


@lru_cache()
def get_settings() -> Settings:
    return Settings()


def get_db(
    settings: Settings = Depends(get_settings)
) -> Generator[Session, None, None]:
    try:
        db: Session = get_db_session(settings.sqlalchemy_database_url)()
        yield db
    finally:
        db.close()
