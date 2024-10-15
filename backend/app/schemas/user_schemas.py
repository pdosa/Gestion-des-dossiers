from pydantic import BaseModel, EmailStr

class UserModel(BaseModel):
    matricule:int
    username:str
    email:EmailStr
    password:str
    role_id:int
    is_active:bool
class UserSchema(BaseModel):
    matricule: str
    username: str
    email: EmailStr
