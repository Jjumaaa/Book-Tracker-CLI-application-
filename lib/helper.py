from models import session
from models.book import Book
from models.author import Author
from models.genre import Genre

def exit_program():
    print("Goodbye!")
    exit()

def get_all_books():
    books = session.query(Book).all()
    if not books:
        print("No books found.")
    else:
        for book in books:
            author_name = book.author.name if book.author else "Unknown Author"
            genres = ', '.join([genre.name for genre in book.genres])
            print(f"{book.id}: {book.title} by {author_name} | Genres: {genres}")

def create_book():
    title = input("Enter the book title: ")
    author_name = input("Enter the author's name: ")
    genre_names = input("Enter genres (comma-separated): ").split(',')

    author = session.query(Author).filter_by(name=author_name.strip()).first()
    if not author:
        author = Author(name=author_name.strip())
        session.add(author)

    genres = []
    for name in genre_names:
        g = session.query(Genre).filter_by(name=name.strip()).first()
        if not g:
            g = Genre(name=name.strip())
            session.add(g)
        genres.append(g)

    book = Book(title=title, author=author, genres=genres)
    session.add(book)
    session.commit()
    print(f"Book '{title}' added successfully!")

def delete_book():
    get_all_books()
    book_id = input("Enter the ID of the book to delete: ")
    book = session.query(Book).get(book_id)
    if not book:
        print("Book not found.")
    else:
        session.delete(book)
        session.commit()
        print(f"Deleted book '{book.title}'.")
