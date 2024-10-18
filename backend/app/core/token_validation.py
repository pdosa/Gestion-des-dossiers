import os
from _pydatetime import timedelta
from datetime import datetime
from pathlib import Path
from typing import Optional, Annotated

from core.exceptions import credentials_exception, permission_exception
from core.get_user_state import find_current_user
from db.db_connection import bd_connection_v1
from dotenv import load_dotenv
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from models.user_model import User
from sqlalchemy.orm import Session

env_path = Path(__file__).resolve().parents[2] / '.venv' / '.env'
print(env_path)
load_dotenv(dotenv_path=env_path)
secret_key = os.getenv('SECRET_KEY_APP')
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_TIME=4
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data:dict,expires_delta:Optional[timedelta]=None):
    to_encode=data.copy()
    if expires_delta:
        expire=datetime.utcnow()+expires_delta
    else:
        expire=datetime.utcnow()+timedelta(weeks=4)
    to_encode.update({"exp":expire})
    encode_jwt=jwt.encode(to_encode,secret_key,algorithm=ALGORITHM)
    return encode_jwt

def current_user_token(token:Annotated[str,Depends(oauth2_scheme)],db:Session=Depends(bd_connection_v1)):
    try:
        payload=jwt.decode(token,secret_key,algorithms=[ALGORITHM])
        matricule:str=payload.get("sub")
        if matricule is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = find_current_user(db,int(matricule))
    if user is None:
        raise credentials_exception
    return user

def get_current_active(current_user:Annotated[User,Depends(current_user_token)]):
    if current_user is None:
        raise credentials_exception
    return current_user

def get_current_active_admin(current_user:Annotated[User,Depends(current_user_token)]):
    if current_user is None:
        raise credentials_exception
    if current_user.role_id==5:
        raise permission_exception
    return  current_user




