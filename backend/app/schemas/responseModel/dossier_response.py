from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


# Schéma pour créer un dossier
class DossierCreate(BaseModel):
    titre: str
    description: str

# Schéma pour afficher un dossier
class DossierResponse(BaseModel):
    id_dossier: int
    titre: str
    description: str
    statut: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True