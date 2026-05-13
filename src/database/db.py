import sqlite3

DB_NAME = "football.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def execute(query, params=()):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)

    conn.commit()
    conn.close()


def fetch_all(query, params=()):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)

    rows = cursor.fetchall()

    conn.close()

    return rows


def fetch_one(query, params=()):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)

    row = cursor.fetchone()

    conn.close()

    return row