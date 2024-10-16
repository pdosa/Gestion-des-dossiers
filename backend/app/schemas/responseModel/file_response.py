from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


# Schéma pour créer un dossier
class FileCreate(BaseModel):
    file_name: str
    file_path: str

# Schéma pour afficher un dossier
class FileResponse(BaseModel):
    document_id: int
    dossier_id: int
    file_name: str
    file_path: str
    updated_at: datetime

    class Config:
        orm_mode = True