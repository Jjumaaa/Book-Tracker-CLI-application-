from helper import exit_program, get_all_books, create_book, delete_book

def menu():
    print("\n--- Book Tracker CLI ---")
    print("1. View all books")
    print("2. Add a new book")
    print("3. Delete a book")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("> ").strip()
        if choice == "0":
            exit_program()
        elif choice == "1":
            get_all_books()
        elif choice == "2":
            create_book()
        elif choice == "3":
            delete_book()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
