# Mini Library System

A command-line library management system written in Python. Users can register, log in, browse and search books, and borrow or return them. Admins can also add new books to the catalogue.

## Problem Statement

Small libraries, college clubs, and school reading rooms often track books and borrowers on paper or in scattered spreadsheets. This makes it hard to know which books are available, who has borrowed what, and who is allowed to manage the catalogue. Records get lost, books go missing, and searching for a title takes far longer than it should.

This project solves that with a simple, lightweight system that:

- keeps a single, searchable catalogue of books and their availability
- tracks borrowing and returning against individual user accounts
- separates what admins (who manage books) and members (who borrow them) can do

## Features

- **User accounts**: register and log in with a username and password
- **Role-based access**: two roles, `admin` and `member`
- **Browse books**: view the full catalogue with ID, title, author, and availability status
- **Search**: find books by a title keyword
- **Borrow and return**: members check books out and return them by Book ID
- **Admin tools**: admins can add new books to the database

## Project Structure

```
.
├── main.py     # Entry point: menus and user interaction loop
├── db.py       # Database setup and table creation
├── auth.py     # Registration and login logic
├── books.py    # Fetch, search, and add books
└── loans.py    # Borrow and return logic
```

## Requirements

- Python 3.8 or higher
- No external libraries required (add any here if your modules use them)

## Getting Started

1. **Clone or download** the project:
   ```bash
   git clone <your-repo-url>
   cd <project-folder>
   ```

2. **Run the program**:
   ```bash
   python main.py
   ```

The database tables are created automatically on first run.

## Usage

### Before login

```
=== Mini Library System ===
1. Register
2. Login
3. Exit
```

### After login

```
--- Main Menu (member) ---
1. View All Books
2. Search Books
3. Borrow Book
4. Return Book
6. Logout
```

Admins also see option **5. Add Book (Admin Only)**.

### Example flow

1. Choose `1` to register a new user with the role `admin` or `member`.
2. Choose `2` to log in.
3. Choose `1` to view all books and note the ID of the one you want.
4. Choose `3` and enter the Book ID to borrow it.
5. Choose `4` and enter the Book ID to return it.

## Roles

| Role     | View / Search | Borrow / Return | Add Books |
|----------|:-------------:|:---------------:|:---------:|
| `member` | Yes           | Yes             | No        |
| `admin`  | Yes           | Yes             | Yes       |

## Known Limitations and Future Improvements

- Anyone can register as `admin`; restrict this in a real deployment
- Non-numeric input for Book ID is not handled yet
- Passwords should be hashed if they are not already
- Possible additions: due dates and fines, delete/edit books, loan history per user

## Author

Built as a learning project. Feel free to fork it and make it your own.

## License

Add a license of your choice (for example, MIT).
