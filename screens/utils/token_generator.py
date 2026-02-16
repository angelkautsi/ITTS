import sqlite3


def generate_token(category):
    conn = sqlite3.connect("itts.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM tickets WHERE category=?",
        (category,)
    )

    count = cursor.fetchone()[0]
    conn.close()

    next_number = count + 1

    token = f"BT-{category}-{str(next_number).zfill(3)}"

    return token
