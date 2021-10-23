from app.db.database import Base
from sqlalchemy import Column, Integer


class WireguardClientConfig(Base):
    __tablename__ = "wireguard_client_configs"

    id = Column(Integer, primary_key=True, index=True)
