from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///book_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

from models.author import Author
from models.book import Book
from models.tag import Genre
