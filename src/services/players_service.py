from src.database.db import get_connection


def get_players_by_club(club_name):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT p.full_name, p.position, p.number, p.status
            FROM players p
            JOIN clubs c ON p.club_id = c.id
            WHERE c.name = ?
            ORDER BY p.full_name
        """, (club_name,))
        return cursor.fetchall()
    finally:
        conn.close()


def get_player_by_name(full_name):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, full_name, club_id
            FROM players
            WHERE full_name = ?
        """, (full_name,))
        return cursor.fetchone()
    finally:
        conn.close()


def get_club_by_name(club_name):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, name
            FROM clubs
            WHERE name = ?
        """, (club_name,))
        return cursor.fetchone()
    finally:
        conn.close()