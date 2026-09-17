from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


def get_all_users_repo(db: Session) -> list[User]:
    statement = select(User)
    users = db.scalars(statement).all()

    return users


def get_user_by_email_repo(user_email: str, db: Session) -> User | None:
    statement = select(User).where(User.email == user_email)
    user = db.scalar(statement)

    return user


def create_user_repo(user: User, db: Session) -> User:
    db.add(user)
    db.commit()
    db.refresh(user)

    return user



