from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.core.security import hash_password
from app.schemas.user import UserCreate

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    hashed = hash_password(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created"}

from app.core.security import verify_password, create_access_token
from app.schemas.user import UserLogin

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        return {"error": "User not found"}

    if not verify_password(user.password, db_user.hashed_password):
        return {"error": "Wrong password"}

    token = create_access_token({"sub": db_user.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }

from app.dependencies.auth import get_current_user
from fastapi import Depends
@router.get("/me")
def get_me(
        current_user=Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "email": current_user.email
    }


