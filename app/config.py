import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Windbox Config API"
    admin_email: str = "admin@example.com"
    items_per_user: int = 50
    sqlalchemy_database_url: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///./config.db"
        )


settings = Settings()
