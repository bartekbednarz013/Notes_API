from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.user import AllUsersSchema
from dependencies import get_db
from crud.user import read_all_users, read_user_by_id

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=list[AllUsersSchema])
def get_all_users(db: Session = Depends(get_db)):
    users = read_all_users(db)
    if users == []:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no users.")
    return users


# @router.get("/{user_id}", response_model=UserSchema)
# def get_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = read_user_by_id(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
#     return db_user
