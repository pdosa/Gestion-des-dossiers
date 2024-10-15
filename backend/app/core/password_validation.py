import os
from pathlib import Path
from dotenv import load_dotenv
from passlib.context import CryptContext

env_path = Path(__file__).resolve().parents[2] / '.venv' / '.env'
print(env_path)
load_dotenv(dotenv_path=env_path)
secret_key = os.getenv('SECRET_KEY_APP')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password:str)->str:
    return pwd_context.hash(password)

def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)