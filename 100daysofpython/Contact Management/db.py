import sqlite3

conn = sqlite3.connect('contacts.db')

c = conn.cursor()

# c.execute("""CREATE TABLE contacts(
#     first TEXT,
#     last TEXT,
#     number INTIGER
# )""")

def add_contact(first, last, number):
    with conn:
        c.execute("INSERT INTO contacts VALUES(?,?,?)",(first, last, number))
        return 'Contact successfully added'

def delete_contact(first,last):
    with conn:
        c.execute("""DELETE FROM contacts
        WHERE first = ? AND last = ?
        """,(first, last))

# def update_contact(ufirst, ulast, unumber, first, last, number):
#     with conn:
#         c.execute("""UPDATE contacts SET first = ? AND last = ? AND number = ?
#         WHERE first = ? AND last = ? AND number = ?
#         """,(ufirst, ulast, unumber ,first, last, number))

def view_contact(first):
    c.execute("SELECT * FROM contacts WHERE first = ?",(first,))
    print(c.fetchall())

def view_all():
    c.execute("SELECT * FROM contacts")
    print(c.fetchall())

view_all()