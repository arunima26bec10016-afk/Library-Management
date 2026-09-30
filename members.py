# members.py
# Everything related to members: add, find, view

from library import storage
from library.models import Member, Student, Faculty


def add_member(name, member_type):
    member_id = storage.next_member_id()
    if member_type == "student":
        member = Student(member_id, name)
    elif member_type == "faculty":
        member = Faculty(member_id, name)
    else:
        member = Member(member_id, name)
    storage.members.append(member)
    return member


def get_member(member_id):
    for member in storage.members:
        if member.member_id == member_id:
            return member
    return None


def view_all():
    if len(storage.members) == 0:
        print("No members registered yet.")
        return
    for member in storage.members:
        member.show()
