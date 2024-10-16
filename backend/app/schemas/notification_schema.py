from datetime import datetime

from pydantic import BaseModel


class NotificationSchema(BaseModel):
    notif_id:int
    user_id:int
    message:str
    is_read:str
    send_at:datetime
    
    
