# reports.py
# Simple reports for the admin

from library import storage, members, books


def get_summary():
    total_copies = 0
    available = 0
    authors = set()          # a set so the same author isn't counted twice
    out_of_stock = []

    for book in storage.books:
        total_copies = total_copies + book.total_copies
        available = available + book.available
        authors.add(book.author)
        if book.available == 0:
            out_of_stock.append(book.title)

    total_fine = 0
    for loan in storage.loans:
        total_fine = total_fine + loan["fine"]

    summary = {
        "titles": len(storage.books),
        "authors": len(authors),
        "total_copies": total_copies,
        "available": available,
        "issued": total_copies - available,
        "members": len(storage.members),
        "fine_collected": total_fine,
        "out_of_stock": out_of_stock,
    }
    return summary


def print_summary():
    s = get_summary()
    print("\n----- Library Report -----")
    print("Book titles       :", s["titles"])
    print("Different authors :", s["authors"])
    print("Total copies      :", s["total_copies"])
    print("Available copies  :", s["available"])
    print("Issued copies     :", s["issued"])
    print("Members           :", s["members"])
    print("Fine collected    : Rs", s["fine_collected"])
    if len(s["out_of_stock"]) == 0:
        print("Out of stock      : none")
    else:
        print("Out of stock      :", ", ".join(s["out_of_stock"]))


def print_member_books(member_id):
    member = members.get_member(member_id)
    if member is None:
        print("Member ID not found.")
        return
    if len(member.borrowed) == 0:
        print(f"{member.name} has no books right now.")
        return
    print(f"Books with {member.name}:")
    for book_id in member.borrowed:
        book = books.get_book(book_id)
        print(f"  - {book.title} (ID {book.book_id})")
