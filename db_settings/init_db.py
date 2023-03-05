import sqlite3


def main():
    connection = sqlite3.connect('database.bd')
    with open('db_settings/schema.sql') as file:
        connection.executescript(file.read())

    cursor = connection.cursor()

    cursor.execute(
        'INSERT INTO posts (title, content) VALUES (?, ?)',
        ('First Post', 'Connect for the first post'),
    )

    cursor.execute(
        'INSERT INTO posts (title, content) VALUES (?, ?)',
        ('Second post', 'Content for the second post'),
    )

    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
