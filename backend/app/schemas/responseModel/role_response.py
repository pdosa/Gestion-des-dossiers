from pydantic import BaseModel,EmailStr
from backend.app.models.role_model import RoleName


class RoleResponse(BaseModel):
    role:RoleName

class UserResponse(BaseModel):
    matricule:str
    email:EmailStr
    username:str
    role:RoleName

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    username:str