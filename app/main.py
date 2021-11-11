import os

import uvicorn
from alembic import command
from alembic.config import Config
from fastapi import FastAPI

from app.routers import windbox, wireguard


def create_app():
    app = FastAPI()

    app.include_router(wireguard.router)
    app.include_router(windbox.router)

    @app.get("/")
    def read_root():
        return {"Wind": "Box"}

    return app


app = create_app()


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
