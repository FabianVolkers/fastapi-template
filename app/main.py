# from typing import Optional

from fastapi import Depends, FastAPI

import crud
import models
import schemas
from db.database import engine
from routers import windbox, wireguard

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(wireguard.router)
app.include_router(windbox.router)


@app.get("/")
def read_root():
    return {"Wind": "Box"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}
