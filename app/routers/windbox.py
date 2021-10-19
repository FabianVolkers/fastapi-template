from fastapi import APIRouter, Depends

from typing import List
from dependencies import get_db

from crud import crud_windbox as crud
from schemas.schemas_windbox import Windbox

router = APIRouter(
    prefix="/windbox",
    tags=["windbox"],
    dependencies=[Depends(get_db)]
)

@router.get("/", response_model=List[Windbox])
async def read_windboxes():
    #windboxes = crud.get_windboxes()
    return[{"windbox": "WB0001"}, {"windbox": "WB0002"}]


@router.get("/{id}")
async def read_windbox(id: str):
    windbox = crud.get_windbox(db=get_db(), windbox_id=id)
    return windbox