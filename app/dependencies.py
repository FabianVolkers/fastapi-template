from functools import lru_cache

from fastapi.param_functions import Depends

from config import Settings
from db.database import get_session_local


@lru_cache()
def get_settings():
    return Settings()


def get_db(settings: Settings = Depends(get_settings)):
    db = get_session_local(settings.sqlalchemy_database_url)  # SessionLocal()
    try:
        yield db
    finally:
        db.close()
