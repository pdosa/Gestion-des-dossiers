from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
    pass


class Dossier(Base):
    __tablename__ = "dossiers"
    id_dossier = Column(Integer, primary_key=True, index=True)
    titre = Column(String(255), nullable=False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    statut = Column(String(50), default="En attente")

    user = relationship("User", back_populates="dossiers")
    documents = relationship("Document", back_populates="dossier")
    factures = relationship("Facture", back_populates="dossier")