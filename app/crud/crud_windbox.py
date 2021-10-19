from sqlalchemy.orm import Session

from .. import models, schemas

def get_windbox(db: Session, windbox_id: int):
    return db.query(models.windbox.Windbox).filter(models.windbox.Windbox.id == windbox_id).first()

def create_windbox(db: Session, windbox: schemas.windbox.WindboxCreate):
    db_windbox = models.windbox.Windbox(id=windbox.id)
    db.add(db_windbox)
    db.commit()
    db.refresh(db_windbox)
    return db_windbox