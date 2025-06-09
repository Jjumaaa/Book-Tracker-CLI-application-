# models/book.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import Base
from models.book_tag import book_tag

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="books")
    tags = relationship("Tag", secondary=book_tag, back_populates="books")

    def __repr__(self):
        return f"<Book(title='{self.title}')>"
