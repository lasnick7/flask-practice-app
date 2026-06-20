from database import get_connection, init_database


def seed_quotes():
    init_database()

    connection = get_connection()

    connection.execute("""
        INSERT INTO quotes (text, author)
        VALUES (?, ?)
    """, (
        "Computer science is no more about computers than astronomy is about telescopes.",
        "Edsger Dijkstra",
    ))

    connection.execute("""
        INSERT INTO quotes (text, author)
        VALUES (?, ?)
    """, (
        "To understand recursion you must first understand recursion.",
        "Unknown",
    ))

    connection.execute("""
        INSERT INTO quotes (text, author)
        VALUES (?, ?)
    """, (
        "The limits of my language are the limits of my mind.",
        "Ludwig Wittgenstein",
    ))

    connection.commit()
    connection.close()


if __name__ == "__main__":
    seed_quotes()
    print("Test quotes added successfully.")