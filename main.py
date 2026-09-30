# main.py
# Mini Library Management System - run this file to start the program

from library import storage, books, members, loans, reports
from library.validation import get_text, get_number

ADMIN_PASSWORD = "admin123"


def admin_login():
    attempts = 0
    while attempts < 3:
        password = input("Enter admin password: ")
        if password == ADMIN_PASSWORD:
            return True
        attempts = attempts + 1
        print("Wrong password.")
    print("Too many wrong attempts. Going back to the main menu.")
    return False


def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add a book")
        print("2. Change number of copies")
        print("3. Delete a book")
        print("4. View all books")
        print("5. Register a member")
        print("6. View all members")
        print("7. Library report")
        print("8. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            title = get_text("Book title: ")
            author = get_text("Author: ")
            copies = get_number("Number of copies: ")
            book = books.add_book(title, author, copies)
            print(f"Book added with ID {book.book_id}.")

        elif choice == "2":
            book_id = get_number("Book ID: ")
            new_total = get_number("New total copies: ")
            ok, message = books.update_copies(book_id, new_total)
            print(message)

        elif choice == "3":
            book_id = get_number("Book ID to delete: ")
            ok, message = books.delete_book(book_id)
            print(message)

        elif choice == "4":
            books.view_all()

        elif choice == "5":
            name = get_text("Member name: ")
            print("1. Student  2. Faculty  3. Other")
            kind = get_number("Member type: ")
            if kind == 1:
                member = members.add_member(name, "student")
            elif kind == 2:
                member = members.add_member(name, "faculty")
            else:
                member = members.add_member(name, "other")
            print(f"{member.name} registered as a {member.member_type} with ID {member.member_id}.")

        elif choice == "6":
            members.view_all()

        elif choice == "7":
            reports.print_summary()

        elif choice == "8":
            break

        else:
            print("Invalid choice, try again.")


def member_menu():
    member_id = get_number("Enter your member ID: ")
    member = members.get_member(member_id)
    if member is None:
        print("No member found with that ID.")
        return

    print(f"Welcome, {member.name}!")
    while True:
        print("\n--- Member Menu ---")
        print("1. View all books")
        print("2. Search books")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. My borrowed books")
        print("6. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            books.view_all()

        elif choice == "2":
            keyword = get_text("Enter title or author to search: ")
            results = books.search(keyword)
            if len(results) == 0:
                print("No books found.")
            for book in results:
                book.show()

        elif choice == "3":
            book_id = get_number("Book ID to borrow: ")
            ok, message = loans.issue_book(book_id, member.member_id)
            print(message)

        elif choice == "4":
            book_id = get_number("Book ID to return: ")
            days = get_number("For how many days did you keep it? ", True)
            ok, message = loans.return_book(book_id, member.member_id, days)
            print(message)

        elif choice == "5":
            reports.print_member_books(member.member_id)

        elif choice == "6":
            break

        else:
            print("Invalid choice, try again.")


def main():
    storage.load_sample_data()

    while True:
        print("\n=== Mini Library System ===")
        print("1. Admin")
        print("2. Member")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            if admin_login():
                admin_menu()
        elif choice == "2":
            member_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
