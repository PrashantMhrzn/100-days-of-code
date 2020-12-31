import sqlite3

conn = sqlite3.connect('contacts.db')

c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE contacts(
        first TEXT,
        last TEXT,
        number INTIGER
    )""")

def add_contact(first, last, number):
    with conn:
        c.execute("INSERT INTO contacts VALUES(?,?,?)",(first, last, number))
        print('Contact successfully added') 

def delete_contact(first,last):
    with conn:
        c.execute("""DELETE FROM contacts
        WHERE first = ? AND last = ?
        """,(first, last))
        print('Contact successfully deleted') 

def view_contact(first):
    c.execute("SELECT * FROM contacts WHERE first = ?",(first,))
    print(c.fetchall())

def view_all():
    c.execute("SELECT * FROM contacts")
    print(c.fetchall())
