# from typing import List, Optional

from pydantic import BaseModel


class WindboxBase(BaseModel):
    # Shared properties
    hostname: str


class WindboxCreate(WindboxBase):
    # Properties to receive on item creation
    pass


class WindboxUpdate(WindboxBase):
    # Properties to receive on item update
    pass


class Windbox(WindboxBase):
    # Properties shared by models stored in DB
    id: int

    class Config:
        orm_mode = True
