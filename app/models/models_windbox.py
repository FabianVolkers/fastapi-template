from app.db.database import Base
from sqlalchemy import Column, Integer, String


class Windbox(Base):
    __tablename__ = "windboxes"

    id = Column(Integer, primary_key=True, index=True)
    hostname = Column(String)
