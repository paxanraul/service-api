from sqlalchemy.orm import Session

from app.security import hash_password
from app.repositories.user_repo import get_user_by_email_repo, create_user_repo
from app.models.user import User
from app.schemas.user import UserRegister


def create_user_service(user_data: UserRegister, db: Session) -> User:
    existing = get_user_by_email_repo(user_data.email, db)
    if existing is not None:
        raise ValueError("Такая почта уже зарегистрирована")

    password_hash = hash_password(user_data.password)    

    user = User(
        email=user_data.email,
        password_hash=password_hash,
    )

    return create_user_repo(user, db)
