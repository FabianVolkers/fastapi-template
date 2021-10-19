from typing import Optional

from fastapi import Depends, FastAPI

from routers import wireguard

app = FastAPI()

app.include_router(wireguard.router)

@app.get("/")
def read_root():
    return {"Wind": "Box"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}