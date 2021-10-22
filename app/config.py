from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Windbox Config API"
    admin_email: str = "admin@example.com"
    items_per_user: int = 50
    sqlalchemy_database_url: str = "sqlite:///./config.db"


settings = Settings()
