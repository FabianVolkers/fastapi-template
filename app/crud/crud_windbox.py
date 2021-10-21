from sqlalchemy.orm import Session

from models.models_windbox import Windbox
from schemas.schemas_windbox import WindboxCreate, WindboxUpdate
#import models, schemas

from crud.base import CRUDBase

class CRUDWindbox(CRUDBase[Windbox, WindboxCreate, WindboxUpdate]):
    pass

windbox = CRUDWindbox(Windbox)

# def get_windbox(db: Session, windbox_id: int):
#     return db.query(Windbox).filter(Windbox.id == windbox_id).first()

# def create_windbox(db: Session, windbox: WindboxCreate):
#     db_windbox = Windbox(id=windbox.id)
#     db.add(db_windbox)
#     db.commit()
#     db.refresh(db_windbox)
#     return db_windbox