from sqlalchemy.orm import Session

from models import models_windbox
from schemas import schemas_windbox
#import models, schemas

def get_windbox(db: Session, windbox_id: int):
    return db.query(models_windbox.Windbox).filter(models_windbox.Windbox.id == windbox_id).first()

def create_windbox(db: Session, windbox: schemas_windbox.WindboxCreate):
    db_windbox = models_windbox.Windbox(id=windbox.id)
    db.add(db_windbox)
    db.commit()
    db.refresh(db_windbox)
    return db_windbox