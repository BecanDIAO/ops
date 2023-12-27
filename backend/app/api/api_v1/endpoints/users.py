from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from app.api.deps import get_db
from app import schemas, crud


router = APIRouter()


@router.get("/")
def read_users(db: Annotated[Session, Depends(get_db)], skip: int = 0, limit: int = 10) -> list[schemas.User]:
    users = crud.get_users(db, skip, limit)
    return users


@router.post("/", response_model=schemas.User)
def create_user(db: Annotated[Session, Depends(get_db)], user: schemas.UserCreate):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)
