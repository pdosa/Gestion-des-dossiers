from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from backend.app.models.user_model import User
from backend.app.schemas.user_schemas import UserSchema




def create_user(session: Session, user: UserSchema, password: str) -> User | None:
    db_user = User(
        matricule=1,
        username=user.username,
        email=user.email,
        password=password,
        role_id=4,

    )
    session.add(db_user)
    try:
        session.commit()
        session.refresh(db_user)
        print("ok user add")
    except IntegrityError as e:
        session.rollback()
        print(e)
        return None
    return db_user
