import sqlite3
from config import DB_TYPE, DB_PATH

def get_connection():
    if DB_TYPE == "sqlite":
        conn = sqlite3.connect(DB_PATH)
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn
    else:
        raise ValueError("Unsupported DB_TYPE")

def execute(sql, params=None):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(sql, params or [])
        conn.commit()
        return cursor.rowcount
    except sqlite3.Error as e:
        print("SQL Error:", e)
        return 0
    finally:
        conn.close()

def fetch_all(sql, params=None):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(sql, params or [])
        return cursor.fetchall()
    except sqlite3.Error as e:
        print("SQL Error:", e)
        return []
    finally:
        conn.close()

def fetch_one(sql, params=None):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(sql, params or [])
        return cursor.fetchone()
    except sqlite3.Error as e:
        print("SQL Error:", e)
        return None
    finally:
        conn.close()

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        with open("schema.sql", "r", encoding="utf-8") as f:
            cursor.executescript(f.read())
        conn.commit()
        print("Базата е инициализирана.")
    except Exception as e:
        print("Грешка при инициализация:", e)
    finally:
        conn.close()
