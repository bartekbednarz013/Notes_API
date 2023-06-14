from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from dependencies import get_db, get_current_user
from schemas.note import NoteSchema, NoteCreateSchema
from database.models import UserModel
from crud.note import create_note, read_all_notes, read_note, delete_note, update_note, read_all_user_notes

router = APIRouter(prefix="/notes", tags=["notes"])


@router.post("", response_model=NoteSchema, status_code=status.HTTP_201_CREATED)
def add_note(
    note: NoteCreateSchema,
    current_user: Annotated[UserModel, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    note = create_note(db, current_user.id, note)
    return note


@router.delete("/{note_id}", response_model=NoteSchema)
def remove_note(
    note_id: str,
    current_user: Annotated[UserModel, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    note = read_note(db, note_id)
    if note.author_id is not current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Cannot delete other user's note.")
    note = delete_note(db, note_id)
    return note


@router.get("", response_model=list[NoteSchema])
def get_all_my_note(
    current_user: Annotated[UserModel, Depends(get_current_user)], db: Annotated[Session, Depends(get_db)]
):
    notes = read_all_user_notes(db, current_user.id)
    if not notes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="You don't have any notes yet.")
    return notes


# @router.get("/all", response_model=list[NoteSchema])
# def get_all_notes(db: Annotated[Session, Depends(get_db)]):
#     notes = read_all_notes(db)
#     if notes == []:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no notes.")
#     return notes


@router.get("/{note_id}")
def get_note(
    note_id: int,
    current_user: Annotated[UserModel, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    note = read_note(db, note_id)
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    if note.author_id is not current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Cannot get other user's note.")
    return note


@router.put("/{note_id}")
async def edit_note(
    note_id: int,
    new_note: NoteCreateSchema,
    current_user: Annotated[UserModel, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    note = read_note(db, note_id)
    if note.author_id is not current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Cannot edit other user's note")
    note = update_note(db, note_id, new_note.text)
    return note
