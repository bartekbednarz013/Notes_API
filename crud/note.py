from sqlalchemy.orm import Session
from database.models import NoteModel
from schemas.note import NoteCreateSchema


def create_note(db: Session, user_id, note: NoteCreateSchema) -> NoteModel:
    note_instance = NoteModel(author_id=user_id, text=note.text)
    db.add(note_instance)
    db.commit()
    db.refresh(note_instance)
    return note_instance


def read_note(db: Session, note_id: int) -> NoteModel:
    return db.query(NoteModel).get(note_id)


def read_all_notes(db: Session) -> list[NoteModel]:
    return db.query(NoteModel).all()


def delete_note(db: Session, note_id: int) -> NoteModel:
    note = db.query(NoteModel).get(note_id)
    db.delete(note)
    db.commit()
    return note


def update_note(db: Session, note_id: int, new_text) -> NoteModel:
    db.query(NoteModel).filter(NoteModel.id == note_id).update({"text": new_text})
    db.commit()
    note = db.query(NoteModel).get(note_id)
    return note


def read_all_user_notes(db: Session, user_id) -> list[NoteModel]:
    return db.query(NoteModel).filter(NoteModel.author_id == user_id).all()
