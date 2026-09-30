# books.py
# Everything related to books: add, view, search, update, delete

from library import storage
from library.models import Book


def add_book(title, author, copies):
    book = Book(storage.next_book_id(), title, author, copies)
    storage.books.append(book)
    return book


def get_book(book_id):
    for book in storage.books:
        if book.book_id == book_id:
            return book
    return None


def view_all():
    if len(storage.books) == 0:
        print("No books in the library yet.")
        return
    for book in storage.books:
        book.show()


def search(keyword):
    # looks in both title and author, ignores capital letters
    keyword = keyword.lower()
    found = []
    for book in storage.books:
        if keyword in book.title.lower() or keyword in book.author.lower():
            found.append(book)
    return found


def update_copies(book_id, new_total):
    book = get_book(book_id)
    if book is None:
        return (False, "Book ID not found.")

    issued = book.total_copies - book.available
    if new_total < issued:
        return (False, f"{issued} copies are issued right now, so the total can't be less than that.")

    book.total_copies = new_total
    book.available = new_total - issued
    return (True, "Number of copies updated.")


def delete_book(book_id):
    book = get_book(book_id)
    if book is None:
        return (False, "Book ID not found.")
    if book.available != book.total_copies:
        return (False, "Some copies are still issued, so this book can't be deleted.")

    storage.books.remove(book)
    return (True, "Book deleted.")
