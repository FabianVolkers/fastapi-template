from sqlalchemy import Column, Integer

from db.database import Base

class WireguardClientConfig(Base):
    __tablename__ = "wireguard_client_configs"

    id = Column(Integer, primary_key=True, index=True)