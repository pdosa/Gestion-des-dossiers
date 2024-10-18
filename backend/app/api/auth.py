from datetime import timedelta
from typing import Annotated

from core.exceptions import incorrect_username_or_password_exceptions, no_access_method, permission_exception
from core.get_user_state import authenticate_user
from core.password_validation import get_password_hash
from core.token_validation import create_access_token, oauth2_scheme, current_user_token, get_current_active_admin
from db.db_connection import bd_connection_v1
from fastapi import (
    APIRouter,
    Depends
)
from fastapi.security import OAuth2PasswordRequestForm
from models.user_model import User
from schemas.responseModel.role_response import UserResponse, Token
from schemas.user_schemas import UserModel
from sqlalchemy.orm import Session

# test connection

auth = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@auth.post("/login",status_code=201)
async def login_for_access_token(
        form_data:Annotated[OAuth2PasswordRequestForm,Depends()],
        db:Session=Depends(bd_connection_v1)
)->Token:
    user=authenticate_user(
        session=db,
        plain_password=form_data.password,
        matricule=int(form_data.username)
    )
    if not user:
        raise incorrect_username_or_password_exceptions
    access_token_expires=timedelta(weeks=4)
    access_token=create_access_token(
        data={"sub":user.matricule},expires_delta=access_token_expires
    )
    return Token(
        access_token=access_token,token_type="bearer"
    )
@auth.post("/create_user",response_model=UserResponse,status_code=201)
def add_user(user_create: UserModel, session: Session = Depends(bd_connection_v1),token:str=Depends(oauth2_scheme)):
    user = current_user_token(token,session)
    if not user:
        raise no_access_method
    user_validate=get_current_active_admin(user)
    if user_validate is None:
        raise permission_exception
    hashed_password=get_password_hash(user_create.password)
    new_user=User(
        matricule=user.matricule,
        username=user_create.username,
        email=user_create.email,
        password=hashed_password,
        role_id=user_create.role_id
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return {"message":"freddy"}

@auth.post("/create_user_user",status_code=201)
def create_user_simple_user(user:UserModel, session:Session=Depends(bd_connection_v1)):
    hashed_password=get_password_hash(user.password)
    new_user=User(
        matricule=user.matricule,
        username=user.username,
        email=user.email,
        password=hashed_password,
        role_id=user.role_id,
        is_active=user.is_active
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return {"message":"user ok"}
