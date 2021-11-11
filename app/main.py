# from typing import Optional
import os

import uvicorn
from alembic import command
from alembic.config import Config
from fastapi import FastAPI

# from flake8.checker
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
    import subprocess
    subprocess.call(["pytest", "tests/"])


def lint():
    import subprocess
    subprocess.call(["flake8", "app", "tests"])


def isort():
    import subprocess
    subprocess.call(["isort", "app", "tests"])


def autopep8():
    import subprocess
    subprocess.call([
        "autopep8",
        "--in-place",
        "--aggressive",
        "--aggressive",
        "--recursive",
        "app",
        "tests"
    ])


def format():
    isort()
    autopep8()


def check_isort():
    import subprocess
    subprocess.call(["isort", "app", "tests", "--check"])


def ci():
    check_isort()
    lint()
    test()


app = create_app()
