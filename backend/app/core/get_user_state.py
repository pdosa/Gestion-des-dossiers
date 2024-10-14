from typing import Any

from fastapi import HTTPException

from backend.app.core.password_validation import verify_password
from backend.app.models.role_model import Role
from sqlalchemy.orm import Session
from backend.app.models.user_model import User

def find_current_user(session:Session,matricule:int)-> User | None:
    user=(
        session.query(User).filter(
            matricule==User.matricule
        ).first()
    )
    return user

def authenticate_user(session:Session,plain_password:str,matricule:int)->User|None:
    user=find_current_user(session,matricule)
    if not user:
        return None
    if not verify_password(plain_password,user.password):
        return None
    return user

def check_role_user(session:Session,matricule:int):
    user=find_current_user(session,matricule=matricule)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    role=(session.query(Role).filter(
            user.role_id==Role.role_id
        ).first()
    )
    return  role