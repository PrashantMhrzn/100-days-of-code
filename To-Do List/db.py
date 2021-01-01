import sqlite3

conn = sqlite3.connect('todo.db')

c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE todo(
        id INTIGER,
        task TEXT
    )
    """)

def add_task(id, task):
    with conn:
        c.execute("INSERT INTO todo VALUES (?,?)",(id ,task))
        c.execute("SELECT * FROM todo")
        print(c.fetchall())

def delete_task(id):
    with conn:
        c.execute("""DELETE FROM todo 
            WHERE id = ?""",(id,))
        c.execute("SELECT * FROM todo")
        print(c.fetchall())

def show_all():
    c.execute("SELECT * FROM todo")
    print(c.fetchall())


if __name__ == '__main__':
    show_all()
