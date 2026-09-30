# test_library.py
# Simple tests for the library system. Run with:  python test_library.py

from library import storage, books, members, loans, reports

results = []     # list of (test name, passed or not)


def check(name, condition):
    results.append((name, condition))


def fresh_start():
    # wipe everything and put in one book and two members for each test
    storage.reset_data()
    books.add_book("Python Basics", "Anil Kumar", 2)
    members.add_member("Asha", "student")
    members.add_member("Ravi", "other")


# 1. adding and searching
fresh_start()
check("book gets added", len(storage.books) == 1)
check("search finds book by title", len(books.search("python")) == 1)
check("search finds book by author", len(books.search("ANIL")) == 1)
check("search returns nothing for wrong word", len(books.search("cooking")) == 0)

# 2. issuing
fresh_start()
ok, msg = loans.issue_book(1, 1)
check("issue works", ok == True)
check("available copies go down", books.get_book(1).available == 1)
check("book shows in member list", 1 in members.get_member(1).borrowed)

ok, msg = loans.issue_book(1, 1)
check("same member cannot take same book twice", ok == False)

ok, msg = loans.issue_book(99, 1)
check("wrong book id is rejected", ok == False)

ok, msg = loans.issue_book(1, 99)
check("wrong member id is rejected", ok == False)

# 3. no copies left
fresh_start()
loans.issue_book(1, 1)
loans.issue_book(1, 2)
ok, msg = loans.issue_book(1, 1)
check("cannot issue when no copies left", ok == False)

# 4. borrow limit (normal member = 2 books)
fresh_start()
books.add_book("Book Two", "Author Two", 1)
books.add_book("Book Three", "Author Three", 1)
loans.issue_book(1, 2)
loans.issue_book(2, 2)
ok, msg = loans.issue_book(3, 2)
check("normal member limit of 2 works", ok == False)

# student limit is 3, so the third one should work
fresh_start()
books.add_book("Book Two", "Author Two", 1)
books.add_book("Book Three", "Author Three", 1)
loans.issue_book(1, 1)
loans.issue_book(2, 1)
ok, msg = loans.issue_book(3, 1)
check("student can borrow 3 books", ok == True)

# 5. returning and fines
fresh_start()
loans.issue_book(1, 1)
ok, msg = loans.return_book(1, 1, 5)
check("return works", ok == True)
check("available copies go back up", books.get_book(1).available == 2)
check("no fine within 14 days", loans.calculate_fine(14) == 0)
check("fine after 20 days is 12", loans.calculate_fine(20) == 12)

ok, msg = loans.return_book(1, 1, 3)
check("returning a book not borrowed fails", ok == False)

# 6. delete and update rules
fresh_start()
loans.issue_book(1, 1)
ok, msg = books.delete_book(1)
check("cannot delete an issued book", ok == False)
ok, msg = books.update_copies(1, 0)
check("cannot cut copies below issued count", ok == False)
loans.return_book(1, 1, 2)
ok, msg = books.delete_book(1)
check("can delete once returned", ok == True)

# 7. report
fresh_start()
loans.issue_book(1, 1)
summary = reports.get_summary()
check("report counts issued copies", summary["issued"] == 1)
check("report counts members", summary["members"] == 2)

# show the results
passed = 0
for name, ok in results:
    if ok:
        passed = passed + 1
        print("PASS -", name)
    else:
        print("FAIL -", name)

print()
print(passed, "out of", len(results), "tests passed")
