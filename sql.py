import sqlite3

with sqlite3.connect("cdf.db") as connection:

    c = connection.cursor()
    # c.execute("DROP TABLE posts")
    c.execute("CREATE TABLE user(username TEXT,email TEXT,password TEXT, confirm TEXT)")
    c.execute('INSERT INTO user VALUES("cynthia", "cynthia@gmail.com", "chepkemoi@23", "chepkemoi@23")')
    
