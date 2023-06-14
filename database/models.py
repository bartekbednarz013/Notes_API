from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .config import Base, engine


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    notes = relationship("NoteModel", back_populates="author", cascade="all,delete")


class NoteModel(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("users.id"))
    text = Column(String, index=True)
    author = relationship("UserModel", back_populates="notes")


Base.metadata.create_all(engine)
