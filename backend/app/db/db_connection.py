import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

env_path = Path(__file__).resolve().parents[2] / '.venv' / '.env'
print(env_path)
load_dotenv(dotenv_path=env_path)
database_url = os.getenv('DATABASE_URL')




# Vérifier si la variable a bien été récupérée
if database_url:
    print(f"Database URL: {database_url}")
else:
    print("DATABASE_URL n'a pas été trouvée dans le fichier .env")

engine = create_engine(database_url)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def bd_connection_v1():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


bd_connection_v1()
