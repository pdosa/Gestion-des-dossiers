<<<<<<< HEAD
from pydantic import BaseModel,EmailStr
from backend.app.models.role_model import RoleName
=======
from models.role_model import RoleName
from pydantic import BaseModel, EmailStr
>>>>>>> 50a9ff8e7b4c3915d252ddd8fccd7d07b2486492


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