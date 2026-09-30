# storage.py
# All the data lives here while the program is running.
# (Nothing is saved to a file, so it resets when the program closes.)

from library.models import Book, Student, Faculty

books = []       # list of Book objects
members = []     # list of Member objects
loans = []       # list of dictionaries, one for every book issued
counters = {"book": 1, "member": 1}


def next_book_id():
    number = counters["book"]
    counters["book"] = number + 1
    return number


def next_member_id():
    number = counters["member"]
    counters["member"] = number + 1
    return number


def reset_data():
    books.clear()
    members.clear()
    loans.clear()
    counters["book"] = 1
    counters["member"] = 1


def load_sample_data():
    sample_books = [
        ("Python Crash Course", "Eric Matthes", 3),
        ("Automate the Boring Stuff", "Al Sweigart", 2),
        ("Wings of Fire", "A P J Abdul Kalam", 2),
        ("The Alchemist", "Paulo Coelho", 1),
    ]
    for title, author, copies in sample_books:
        books.append(Book(next_book_id(), title, author, copies))

    members.append(Student(next_member_id(), "Riya"))
    members.append(Faculty(next_member_id(), "Prof. Sharma"))
