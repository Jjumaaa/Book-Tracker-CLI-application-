from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models import Base
from models.book import book_genre

class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    books = relationship('Book', secondary=book_genre, back_populates='genres')

    def __repr__(self):
        return f"<Genre {self.id}: {self.name}>"
