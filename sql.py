import sqlite3

with sqlite3.connect("sample.db") as connection:

    c = connection.cursor()
    # c.execute("DROP TABLE posts")
    c.execute("CREATE TABLE posts(title TEXT, description TEXT)")
    c.execute('INSERT INTO posts VALUES("Good","I\'M GOOD")')
    c.execute('INSERT INTO posts VALUES("well","I\'M well")')
    c.execute('INSERT INTO posts VALUES("well","I\'M well")')
