from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


# Schéma pour créer un dossier
class NotificationCreate(BaseModel):
    message: str

# Schéma pour afficher un dossier
class NotificationResponse(BaseModel):
    id_notif: int
    user_id: int
    message: str
    is_read: str
    send_at: datetime

    class Config:
        orm_mode = True