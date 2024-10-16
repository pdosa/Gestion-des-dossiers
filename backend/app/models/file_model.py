from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
    pass


class Document(Base):
    __tablename__ = "documents"
    document_id = Column(Integer, primary_key=True, index=True)
    dossier_id = Column(Integer, ForeignKey("dossiers.id"))
    file_name = Column(String(255), nullable=False)
    file_path = Column(String(255), nullable=False)
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    dossier = relationship("Dossier", back_populates="documents")