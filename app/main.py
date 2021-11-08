def create_app():
    """Create FastAPI app instance"""
    from fastapi import FastAPI

    from app.routers import windbox, wireguard

    app = FastAPI()

    app.include_router(wireguard.get_wireguard_router())
    app.include_router(windbox.router)

    @app.get("/")
    def read_root():
        return {"Wind": "Box"}

    return app


app = create_app()

"""
Functions for poetry scripts
Run with poetry run <script_name>
Defined scripts can be found in `pyproject.toml`
"""


def run():
    """ Runs the FastAPI app for development using uvicorn"""
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)


def setup_db():
    """Setup or update the database using alembic"""
    import os

    from alembic import command
    from alembic.config import Config

    alembic_cfg = Config(f"{os.getcwd()}/alembic.ini")
    command.upgrade(alembic_cfg, "head")


def test():
    """Run tests using pytest"""
    import subprocess
    subprocess.call(["pytest", "tests/"])


def lint():
    """Lint code using flake8"""
    import subprocess
    subprocess.call(["flake8", "app", "tests"])


def isort():
    """Sort imports using isort"""
    import subprocess
    subprocess.call(["isort", "app", "tests"])


def autopep8():
    """Format code using autopep8"""
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
    """Format code using both isort and autopep8"""
    isort()
    autopep8()


def check_isort():
    """Check if imports are sorted correctly"""
    import subprocess
    subprocess.call(["isort", "app", "tests", "--check"])


def ci():
    """Run style guide checks and tests combined for CI"""
    check_isort()
    lint()
    test()
