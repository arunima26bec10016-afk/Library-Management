# models.py
# The classes used in the project: Book, Member, Student and Faculty


class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = copies
        self.available = copies

    def is_available(self):
        return self.available > 0

    def show(self):
        print(f"ID: {self.book_id} | {self.title} | {self.author} | Available: {self.available}/{self.total_copies}")


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.member_type = "Member"
        self.borrowed = []          # list of book ids this member has right now

    def get_limit(self):
        # how many books a normal member can borrow at once
        return 2

    def can_borrow(self):
        return len(self.borrowed) < self.get_limit()

    def show(self):
        print(f"ID: {self.member_id} | {self.name} | {self.member_type} | Books borrowed: {len(self.borrowed)}/{self.get_limit()}")


class Student(Member):
    def __init__(self, member_id, name):
        super().__init__(member_id, name)
        self.member_type = "Student"

    def get_limit(self):
        return 3


class Faculty(Member):
    def __init__(self, member_id, name):
        super().__init__(member_id, name)
        self.member_type = "Faculty"

    def get_limit(self):
        return 5
