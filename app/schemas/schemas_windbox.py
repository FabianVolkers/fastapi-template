from typing import List, Optional

from pydantic import BaseModel

# Shared properties
class WindboxBase(BaseModel):
    hostname: str

# Properties to receive on item creation
class WindboxCreate(WindboxBase):
    pass

# Properties to receive on item update
class WindboxUpdate(WindboxBase):
    pass

# Properties shared by models stored in DB
class Windbox(WindboxBase):
    id: int

    class Config:
        orm_mode = True