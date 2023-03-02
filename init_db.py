import sqlite3

connection = sqlite3.connect('database.bd')

with open('schema.sql') as file:
    connection.executescript(file.read())

cursor = connection.cursor()

cursor.execute(
    "INSERT INTO posts (title, content) VALUES (?, ?)",
    ('First Post', 'Connect for the first post')
)

cursor.execute(
    "INSERT INTO posts (title, content) VALUES (?, ?)",
    ('Second post', 'Content for the second post')
)

connection.commit()
connection.close()
