from pydantic import BaseModel


class NoteCreateSchema(BaseModel):
    text: str


class NoteSchema(BaseModel):
    id: int
    author_id: int | None
    text: str

    class Config:
        orm_mode = True
