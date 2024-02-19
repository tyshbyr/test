from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from app.repositories import users as crud
from app.schemas import users as schemas
from app.db.depends import get_db


router = APIRouter()


@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)
