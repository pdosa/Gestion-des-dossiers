from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column,Integer,String
from enum import Enum
class Base(DeclarativeBase):
    pass

class RoleName(str,Enum):
    secretaire="Secretaire"
    agentTransit="Agent_Transit"
    directorRo="DirectorRo"
    directorPDG="DirectorPDG"
    Admin="Admin"
class Role(Base):
    __tablename__="role"
    role_id=Column(
        Integer,
        primary_key=True,
        index=True
    )
    role_name=Column(
        RoleName.secretaire,
        index=True,
        unique=True,
    )