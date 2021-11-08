# from typing import Optional

from fastapi import FastAPI

from app.routers import windbox, wireguard

# import crud
# import models
# import schemas


# models.Base.metadata.create_all(bind=engine)


def create_app():
    app = FastAPI()

    app.include_router(wireguard.get_wireguard_router())
    app.include_router(windbox.router)

    @app.get("/")
    def read_root():
        return {"Wind": "Box"}

    return app
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
    #     return {"item_id": item_id, "q": q}


app = create_app()
