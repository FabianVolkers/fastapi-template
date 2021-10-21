from typing import List, Optional

from pydantic import BaseModel

class WindboxBase(BaseModel):
    hostname: str

class WindboxCreate(WindboxBase):
    pass

class WindboxUpdate(WindboxBase):
    pass

class Windbox(WindboxBase):
    id: int

    class Config:
        orm_mode = True