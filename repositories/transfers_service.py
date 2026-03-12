from proekt_futbol.db import get_connection
from datetime import datetime


def transfer_player(player_name, from_club, to_club, date, fee=None):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        datetime.strptime(date, "%Y-%m-%d")

        cursor.execute("SELECT id, club_id FROM players WHERE full_name = ?", (player_name,))
        player = cursor.fetchone()

        if not player:
            return "Играчът не съществува."

        player_id, current_club = player

        cursor.execute("SELECT id FROM clubs WHERE name = ?", (from_club,))
        from_row = cursor.fetchone()

        cursor.execute("SELECT id FROM clubs WHERE name = ?", (to_club,))
        to_row = cursor.fetchone()

        if not to_row:
            return "Клубът 'към' не съществува."

        from_id = from_row[0] if from_row else None
        to_id = to_row[0]

        if from_id == to_id:
            return "Играчът не може да се трансферира в същия клуб."

        if current_club != from_id:
            return "Играчът не е в посочения клуб."

        cursor.execute("""
        INSERT INTO transfers(player_id, from_club_id, to_club_id, transfer_date, fee)
        VALUES (?, ?, ?, ?, ?)
        """, (player_id, from_id, to_id, date, fee))

        cursor.execute("""
        UPDATE players
        SET club_id = ?
        WHERE id = ?
        """, (to_id, player_id))

        conn.commit()

        return f"Трансфер успешен: {player_name} от {from_club} → {to_club}"

    except Exception as e:
        conn.rollback()
        return f"Грешка: {e}"

    finally:
        conn.close()


def list_transfers_by_player(player_name):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT c1.name, c2.name, t.transfer_date
    FROM transfers t
    JOIN players p ON t.player_id = p.id
    LEFT JOIN clubs c1 ON t.from_club_id = c1.id
    JOIN clubs c2 ON t.to_club_id = c2.id
    WHERE p.full_name = ?
    """, (player_name,))

    result = cursor.fetchall()
    conn.close()

    return result