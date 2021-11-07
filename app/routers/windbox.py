from http import HTTPStatus
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import crud_windbox
from app.dependencies import get_db
from app.schemas.schemas_windbox import Windbox, WindboxCreate, WindboxUpdate

router = APIRouter(
    prefix="/windbox",
    tags=["windbox"],
    dependencies=[Depends(get_db)]
)


@router.get("/", response_model=List[Windbox])
async def read_windboxes(*, db: Session = Depends(get_db)) -> List[Windbox]:
    windboxes = crud_windbox.windbox.get_multi(db)
    return windboxes


@router.post("/", response_model=Windbox)
async def create_windbox(
    *,
    windbox: WindboxCreate,
    db: Session = Depends(get_db)
) -> Windbox:
    return crud_windbox.windbox.create(db, obj_in=windbox)


@router.get("/{id}", response_model=Windbox)
async def read_windbox(
    *, db: Session = Depends(get_db), id: int
) -> Optional[Windbox]:
    windbox = crud_windbox.windbox.get(db, id=id)
    if not windbox:
        raise HTTPException(404)
    return windbox


@router.put("/{id}", response_model=Windbox)
async def update_windbox(
    *,
    id: int,
    windbox: WindboxUpdate,
    db: Session = Depends(get_db)
) -> Windbox:
    current_windbox = crud_windbox.windbox.get(db, id)
    return crud_windbox.windbox.update(
        db, db_obj=current_windbox, obj_in=windbox)


@router.delete("/{id}", response_model=None, status_code=HTTPStatus.NO_CONTENT)
async def delete_windbox(id: int, db: Session = Depends(get_db)):
    return crud_windbox.windbox.remove(db=db, id=id)
