from functools import lru_cache
from typing import Any, Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Session

from app.config import TestSettings
from app.db.session import get_db_session
from app.dependencies import get_settings
from app.main import app as fa_app
# Base, Order, OrderItem, Product, Store
from app.models import models_windbox  # , models_wireguard


target_metadata = [models_windbox.Base.metadata]

settings = TestSettings()


def override_get_settings():
    return TestSettings()

# @pytest.fixture(scope="session")
# def db() -> Session:
#     db_session = get_session_local(settings.sqlalchemy_database_url)
#     engine = db_session.bind
#     if not database_exists(engine.url):
#         create_database(engine.url)

#     # Loop through base metadata and create tables
#     for m in target_metadata:
#         m.drop_all(bind=engine)
#         m.create_all(bind=engine)

#     return db_session


@pytest.fixture(scope="module")
def cleanup_db(db: Session) -> None:
    for m in target_metadata:
        for table in reversed(m.sorted_tables):
            db.execute(table.delete())


@pytest.fixture(scope="session")
def db() -> Generator:
    database_uri = override_get_settings().sqlalchemy_database_url
    session: Session = get_db_session(database_uri)()
    engine: Engine = session.bind

    # Loop through base metadata and create tables
    for m in target_metadata:
        m.drop_all(bind=engine)
        m.create_all(bind=engine)

    yield session


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(fa_app) as c:
        yield c


@pytest.fixture(scope="module")
@lru_cache
def get_settings_override():
    return TestSettings()


@pytest.fixture(scope="module")
def app_client(
    get_settings_override: Any
) -> Generator[TestClient, None, None]:
    fa_app.dependency_overrides[get_settings] = lambda: get_settings_override
    yield TestClient(fa_app)
