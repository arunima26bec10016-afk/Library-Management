# loans.py
# Issuing and returning books, plus the fine calculation

from library import storage, books, members

ALLOWED_DAYS = 14     # days a member can keep a book
FINE_PER_DAY = 2      # rupees per extra day


def calculate_fine(days_kept):
    if days_kept > ALLOWED_DAYS:
        return (days_kept - ALLOWED_DAYS) * FINE_PER_DAY
    return 0


def issue_book(book_id, member_id):
    book = books.get_book(book_id)
    member = members.get_member(member_id)

    if book is None:
        return (False, "Book ID not found.")
    if member is None:
        return (False, "Member ID not found.")
    if not book.is_available():
        return (False, "No copies of this book are available right now.")
    if book_id in member.borrowed:
        return (False, "This member already has a copy of this book.")
    if not member.can_borrow():
        return (False, f"Borrow limit reached. {member.member_type}s can borrow {member.get_limit()} books.")

    book.available = book.available - 1
    member.borrowed.append(book_id)
    storage.loans.append({"book_id": book_id, "member_id": member_id, "returned": False, "fine": 0})
    return (True, f"'{book.title}' issued to {member.name}. Please return it within {ALLOWED_DAYS} days.")


def return_book(book_id, member_id, days_kept):
    book = books.get_book(book_id)
    member = members.get_member(member_id)

    if book is None:
        return (False, "Book ID not found.")
    if member is None:
        return (False, "Member ID not found.")
    if book_id not in member.borrowed:
        return (False, "This member has not borrowed that book.")

    fine = calculate_fine(days_kept)
    member.borrowed.remove(book_id)
    book.available = book.available + 1

    # update the loan record
    for loan in storage.loans:
        if loan["book_id"] == book_id and loan["member_id"] == member_id and loan["returned"] == False:
            loan["returned"] = True
            loan["fine"] = fine
            break

    if fine > 0:
        return (True, f"Book returned. It is {days_kept - ALLOWED_DAYS} days late, fine to pay: Rs {fine}")
    return (True, "Book returned on time. No fine.")
