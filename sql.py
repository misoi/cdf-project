import sqlite3

with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
    c.execute("""create TABLE posts(title TEXT, description TEXT)""")
    c.execute('INSERT INTO posts VALUES("Good","I\'M GOOD")')
