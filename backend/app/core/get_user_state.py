from fastapi import HTTPException

from fastapi import HTTPException
from models.role_model import Role
from models.user_model import User
from sqlalchemy.orm import Session


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