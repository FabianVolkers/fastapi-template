import os
from typing import Any

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Windbox Config API"
    admin_email: str = "admin@example.com"
    items_per_user: int = 50
    sqlalchemy_database_url: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///./config.db"
    )

    # feature flags
    flag_api_endpoint_wireguard = False

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return super().__call__(*args, **kwds)


settings = Settings()


class TestSettings(Settings):
    # Test DB
    sqlalchemy_database_url: str = os.getenv(
        "TEST_DATABASE_URL",
        "sqlite:///./config.test.db"
    )

    # Test feature flags
    flag_is_enabled: bool = True
    flag_is_disabled: bool = False

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return super().__call__(*args, **kwds)
