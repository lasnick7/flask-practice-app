import sqlite3


DATABASE_NAME = "database.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def init_database():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            author TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def get_all_quotes():
    connection = get_connection()

    quotes = connection.execute("""
        SELECT id, text, author, created_at
        FROM quotes
        ORDER BY created_at DESC
    """).fetchall()

    connection.close()

    return quotes


def add_quote(text, author):
    connection = get_connection()

    connection.execute("""
        INSERT INTO quotes (text, author)
        VALUES (?, ?)
    """, (text, author))

    connection.commit()
    connection.close()
    

def delete_quote(quote_id):
    connection = get_connection()

    connection.execute("""
        DELETE FROM quotes
        WHERE id = ?
    """, (quote_id,))

    connection.commit()
    connection.close()