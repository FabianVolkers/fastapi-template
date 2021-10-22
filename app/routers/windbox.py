from typing import Any, List
from schemas.schemas_windbox import WindboxCreate

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


@router.post("/", response_model=Windbox)
async def create_windbox(
    *,
    windbox: WindboxCreate,
    db: Session = Depends(get_db)
 ) -> Windbox:
    return crud_windbox.windbox.create(db, obj_in=windbox)


@router.put("/{id}", response_model=Windbox)
async def update_windbox(
    *,
    id: str,
    windbox: WindboxUpdate,
    db: Session = Depends(get_db)
  ) -> Windbox:
    current_windbox = crud_windbox.windbox.get(db, id)
    return crud_windbox.windbox.update(
        db, db_obj=current_windbox, obj_in=windbox)
