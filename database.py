import sqlite3
from datetime import datetime


DB_NAME = "itts.db" #this is what we will call out database


def connect_db():
    return sqlite3.connect(DB_NAME)


def initialize_database(): #initialising the database
    conn = connect_db()
    cursor = conn.cursor()

    # Creating users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    """)

    # Creating tickets table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        token TEXT UNIQUE NOT NULL,
        category TEXT NOT NULL,
        priority TEXT NOT NULL,
        department TEXT NOT NULL,
        description TEXT NOT NULL,
        status TEXT NOT NULL,
        assigned_to TEXT,
        date_created DATETIME NOT NULL,
        date_closed DATETIME,
        resolution_time REAL
    )
    """)

    # Check if admin already exists
    cursor.execute("SELECT * FROM users WHERE username = ?", ("admin",))
    admin_exists = cursor.fetchone()

    if not admin_exists:
        cursor.execute("""
        INSERT INTO users (username, password, role)
        VALUES (?, ?, ?)
        """, ("admin", "admin123", "admin"))

        print("Default admin user created.")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    initialize_database()
