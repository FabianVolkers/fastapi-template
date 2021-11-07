from sqlalchemy import Column, Integer, String

from app.db.database import Base


class Windbox(Base):
    __tablename__ = "windboxes"

    id = Column(Integer, primary_key=True, index=True)
    hostname = Column(String)
