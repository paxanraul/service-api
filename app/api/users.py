from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.user import UserRegister, UserResponse
from app.services.user_service import create_user_service


router = APIRouter(prefix="/users", tags=["users"])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user_data: UserRegister, db: Session = Depends(get_db)):
    try:
        return create_user_service(user_data, db)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Пользователь с таким email уже существует"
        )
