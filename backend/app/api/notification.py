from fastapi import APIRouter


notif=APIRouter(prefix="/Documents",tags=["Documents"])

from fastapi import APIRouter,Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.notification_model import Notification
from app.models.user_model import User
from app.schemas.responseModel.notification_response import NotificationCreate, NotificationResponse
from app.core.token_validation import get_current_active

from db.db_connection import bd_connection_v1




# Envoyer une notification
@notif.post("/notifications/")
def send_notification(notification: NotificationCreate, db: Session = Depends(bd_connection_v1), current_user: User = Depends(get_current_active)):
    new_notification = Notification(
        message=notification.message, user_id=current_user.id
    )
    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)
    return new_notification

# Obtenir les notifications de l'utilisateur connecté
@notif.get("/notifications/")
def get_notifications(db: Session = Depends(bd_connection_v1), current_user: User = Depends(get_current_active)):
    notifications = db.query(Notification).filter(Notification.user_id == current_user.id).all()
    return notifications

# Marquer une notification comme lue
@notif.put("/notifications/{notification_id}/read")
def mark_as_read(notification_id: int, db: Session = Depends(bd_connection_v1), current_user: User = Depends(get_current_active)):
    notification = db.query(Notification).filter(Notification.id == notification_id, Notification.user_id == current_user.id).first()
    if not notification:
        raise HTTPException(status_code=404, detail="Notification non trouvée")
    notification.is_read = True
    db.commit()
    return {"message": "Notification marquée comme lue"}