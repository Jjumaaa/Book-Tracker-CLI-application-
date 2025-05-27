import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import Base, engine, session
from models.author import Author
from models.genre import Genre
from models.book import Book

Base.metadata.create_all(engine)

author1 = Author(name="G.G Juma")
author2 = Author(name="C.N Kamuthu")

genre1 = Genre(name="Football")
genre2 = Genre(name="Fantasy")

book1 = Book(title="Messi", author=author1)
book1.genres.append(genre1)

book2 = Book(title="World Of Daisies", author=author2)
book2.genres.append(genre2)

session.add_all([author1, author2, genre1, genre2, book1, book2])
session.commit()

print("Database seeded Kabisa!")