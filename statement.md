# Project Statement

## Problem Statement

Small libraries, like a college club shelf or a department library, often keep track of books and borrowers in notebooks or loose spreadsheets. It becomes hard to know which books are available, who has taken which book, and who owes a fine for returning late. Books get lost, records get mixed up, and searching for a title takes far longer than it should.

## Scope of the Project

**What the project does**

- Keeps a catalogue of books with the number of copies available
- Registers members (students, faculty, or others)
- Issues and returns books, with a borrowing limit for each member type
- Calculates fines for books kept longer than 14 days
- Gives the admin a simple report of the library's status

**What the project does not do (for now)**

- It is a command-line program with no graphical screen
- Data is stored only while the program is running and is not saved to a file or database
- No online payment of fines and no email or SMS reminders

## Target Users

- **Librarian / Admin:** adds and removes books, registers members, and checks reports
- **Members (students and faculty):** search for books, borrow them, and return them

## High-Level Features

1. Admin login protected by a password
2. Book management: add, view, search, update copies, delete
3. Member management: register and view members
4. Book issue and return with borrowing limits (Student: 3, Faculty: 5, Other: 2)
5. Automatic fine calculation (Rs 2 per day after 14 days)
6. Library report: titles, copies, issued books, members, fines collected, out-of-stock books
7. Input validation so wrong entries do not break the program
