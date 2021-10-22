from fastapi import APIRouter, Depends

from typing import Any, List
from dependencies import get_db

from crud import crud_windbox
from dependencies import get_db
from fastapi import APIRouter, Depends
from schemas.schemas_windbox import Windbox

from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/windbox",
    tags=["windbox"],
    dependencies=[Depends(get_db)]
)

@router.get("/", response_model=List[Windbox])
async def read_windboxes(*, db: Session = Depends(get_db)):
    windboxes = crud_windbox.windbox.get_multi(db)
    return windboxes


@router.get("/{id}", response_model=Windbox)
async def read_windbox(*, db: Session = Depends(get_db), id: str) -> Any:
    windbox = crud_windbox.windbox.get(db, id=id)
    return windbox