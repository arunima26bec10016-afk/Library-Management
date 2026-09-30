# Mini Library Management System

## Overview

A command-line library management system written in Python. An admin can manage books and members, and members can search, borrow, and return books. The program also calculates fines for late returns and shows a simple report of the library's status.

The project is built using only the concepts from the Python Essentials course: variables, operators, input/output, lists, tuples, sets, dictionaries, control flow, functions, modules and packages, and object-oriented programming.

For the problem statement, scope, and target users, see [statement.md](statement.md).

## Features

- Admin login with a password
- Add, view, search, update, and delete books
- Register and view members (Student, Faculty, Other)
- Issue and return books with a borrowing limit per member type
- Fine calculation for books kept more than 14 days (Rs 2 per extra day)
- Library report (titles, copies, issued books, members, fines, out-of-stock books)
- Input validation on every number and text entry

## Functional Requirements

1. **Book Management:** add, view, search, update copies, delete books
2. **Member Management:** register members and view them
3. **Loan Management:** issue books, return books, calculate fines
4. **Reports:** admin summary and a member's borrowed books

## Non-Functional Requirements

1. **Usability:** simple numbered menus and clear messages after every action
2. **Security:** admin features are protected by a password with 3 attempts
3. **Reliability:** all input is validated, so wrong entries (letters instead of numbers, blank text, wrong IDs) do not crash the program
4. **Maintainability:** code is split into separate modules, each with one job, and uses functions and classes
5. **Error handling:** actions return a (success, message) pair, which the menu prints to the user

## Technologies Used

- Python 3.6 or above
- No external libraries needed
- Git and GitHub for version control

## Project Structure

```
library-management-system/
├── main.py              # start the program from here (menus)
├── test_library.py      # tests
├── statement.md
├── README.md
├── docs/                # diagrams, screenshots and project report
└── library/
    ├── __init__.py
    ├── models.py        # Book, Member, Student, Faculty classes
    ├── storage.py       # lists and dictionaries holding the data
    ├── validation.py    # input checking helpers
    ├── books.py         # book functions
    ├── members.py       # member functions
    ├── loans.py         # issue, return, fine
    └── reports.py       # reports
```

## How to Install and Run

1. Install Python 3 from [python.org](https://www.python.org/downloads/)
2. Download the project folder from GitHub and open it in a terminal
3. Run the program:
   ```
   python main.py
   ```

Some sample books and two sample members (ID 1 is a student, ID 2 is a faculty member) are loaded at the start so you can try it right away.

- Admin password: `admin123`

## How to Use

1. Choose **Admin** to manage books and members, or **Member** and enter your member ID.
2. Members can search a book, note its ID, then choose **Borrow a book**.
3. To return a book, enter its ID and the number of days you kept it. If it is more than 14 days, the fine is shown.

## Borrowing Limits

| Member type | Books at a time |
|-------------|-----------------|
| Student     | 3               |
| Faculty     | 5               |
| Other       | 2               |

## Testing

Run the tests with:

```
python test_library.py
```

It checks adding and searching books, issuing and returning, borrowing limits, fine calculation, delete and update rules, and the report. Each test prints PASS or FAIL, followed by a summary count.

## Screenshots

**Admin: books and library report**

![Admin report](docs/screenshots/shot_admin_report.png)

**Member: search and borrow a book**

![Borrow a book](docs/screenshots/shot_borrow.png)

**Member: return a book with a fine**

![Return with fine](docs/screenshots/shot_return_fine.png)

## Limitations and Future Enhancements

- Data is not saved after the program closes (file storage can be added later)
- No graphical interface
- Possible additions: due dates using real dates, book history per member, and password-protected member accounts
