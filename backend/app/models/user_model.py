from datetime import datetime

from sqlalchemy import Column, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    matricule: Mapped[int] = mapped_column(
        primary_key=True, index=True
    )
    username: Mapped[str] = mapped_column(
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        unique=True, index=True
    )
    password: Mapped[str]
    role_id: Mapped[int]
    is_active: Mapped[bool] = mapped_column(
        default=False
    )
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
