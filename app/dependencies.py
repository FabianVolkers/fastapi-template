from functools import lru_cache

from fastapi.param_functions import Depends

from app.config import Settings
from app.db.database import get_session_local


@lru_cache()
def get_settings():
    return Settings()


def get_db(settings: Settings = Depends(get_settings)):
    db_session = get_session_local(settings.sqlalchemy_database_url)  # SessionLocal()
    try:
        yield db_session
    finally:
        db_session.remove()
