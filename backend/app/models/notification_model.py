from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
    pass



class Notification(Base):
    __tablename__ = "notifications"
    id_notif = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    message = Column(String, nullable=False)
    is_read = Column(Boolean, default=False)
    sent_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="notifications")