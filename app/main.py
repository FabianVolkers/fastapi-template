# from typing import Optional

from fastapi import FastAPI
import uvicorn
from alembic.config import Config
from alembic import command
import os
from app.routers import windbox, wireguard

# import crud
# import models
# import schemas


# models.Base.metadata.create_all(bind=engine)


def create_app():
    app = FastAPI()

    app.include_router(wireguard.router)
    app.include_router(windbox.router)

    @app.get("/")
    def read_root():
        return {"Wind": "Box"}

    return app
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
    #     return {"item_id": item_id, "q": q}


def run():
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)


def setup_db():
    alembic_cfg = Config(f"{os.getcwd()}/alembic.ini")
    command.upgrade(alembic_cfg, "head")


def test():
    # pytest
    import subprocess
    subprocess.call(["pytest", "tests/"])


def lint():
    # flake 8 app tests
    import subprocess
    subprocess.call(["flake8", "app", "tests"])


app = create_app()
