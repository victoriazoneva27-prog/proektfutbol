from datetime import datetime
from src.database.db import get_connection


FREE_WORDS = {"няма", "свободен", "free", "none", ""}


def _validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def _validate_fee(fee):
    if fee is None:
        return True
    try:
        return float(fee) >= 0
    except ValueError:
        return False


def transfer_player(player_name, from_club, to_club, date, fee=None):
    if not _validate_date(date):
        return "ERROR: Невалидна дата. Използвай YYYY-MM-DD."

    if not _validate_fee(fee):
        return "ERROR: Сумата трябва да е число >= 0."

    conn = get_connection()
    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, full_name, club_id
            FROM players
            WHERE full_name = ?
        """, (player_name,))
        player = cursor.fetchone()

        if not player:
            return "ERROR: Играчът не съществува."

        player_id, _, current_club_id = player

        cursor.execute("SELECT id, name FROM clubs WHERE name = ?", (to_club,))
        to_row = cursor.fetchone()
        if not to_row:
            return "ERROR: Клубът 'към' не съществува."

        to_club_id = to_row[0]

        from_club_clean = from_club.strip().lower()
        if from_club_clean in FREE_WORDS:
            from_club_id = None
        else:
            cursor.execute("SELECT id, name FROM clubs WHERE name = ?", (from_club,))
            from_row = cursor.fetchone()
            if not from_row:
                return "ERROR: Клубът 'от' не съществува."
            from_club_id = from_row[0]

        if from_club_id == to_club_id:
            return "ERROR: Отборът 'от' и 'към' не може да са еднакви."

        if current_club_id is None:
            if from_club_clean not in FREE_WORDS:
                return "ERROR: Играчът е без клуб. Използвай 'няма' или 'свободен' за отбор 'от'."
        else:
            if current_club_id != from_club_id:
                return "ERROR: Играчът не е в посочения клуб."

        cursor.execute("""
            INSERT INTO transfers (player_id, from_club_id, to_club_id, transfer_date, fee)
            VALUES (?, ?, ?, ?, ?)
        """, (player_id, from_club_id, to_club_id, date, fee))

        cursor.execute("""
            UPDATE players
            SET club_id = ?
            WHERE id = ?
        """, (to_club_id, player_id))

        conn.commit()
        from_name = from_club if from_club_id is not None else "свободен"
        return f"OK: Трансфер успешен: {player_name} от {from_name} в {to_club} на {date}."

    except Exception as e:
        conn.rollback()
        return f"ERROR: {e}"
    finally:
        conn.close()


def list_transfers_by_player(player_name):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT
                COALESCE(fc.name, 'свободен') AS from_club,
                tc.name AS to_club,
                t.transfer_date,
                COALESCE(t.fee, 0)
            FROM transfers t
            JOIN players p ON p.id = t.player_id
            LEFT JOIN clubs fc ON fc.id = t.from_club_id
            JOIN clubs tc ON tc.id = t.to_club_id
            WHERE p.full_name = ?
            ORDER BY t.transfer_date
        """, (player_name,))
        return cursor.fetchall()
    finally:
        conn.close()


def list_transfers_by_club(club_name):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT
                p.full_name,
                COALESCE(fc.name, 'свободен') AS from_club,
                tc.name AS to_club,
                t.transfer_date,
                COALESCE(t.fee, 0)
            FROM transfers t
            JOIN players p ON p.id = t.player_id
            LEFT JOIN clubs fc ON fc.id = t.from_club_id
            JOIN clubs tc ON tc.id = t.to_club_id
            WHERE fc.name = ? OR tc.name = ?
            ORDER BY t.transfer_date
        """, (club_name, club_name))
        return cursor.fetchall()
    finally:
        conn.close()