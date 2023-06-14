from pydantic import BaseModel
from .note import NoteSchema


class UserCreateSchema(BaseModel):
    username: str
    password: str


class UserSchema(BaseModel):
    id: int
    username: str
    notes: list[NoteSchema] = []

    class Config:
        orm_mode = True


class AllUsersSchema(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
