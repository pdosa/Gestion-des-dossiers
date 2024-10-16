from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
    pass



class Facture(Base):
    __tablename__ = "factures"
    id = Column(Integer, primary_key=True, index=True)
    montant = Column(Integer, nullable=False)
    dossier_id = Column(Integer, ForeignKey("dossiers.id"))
    facture_pdf = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    dossier = relationship("Dossier", back_populates="factures")