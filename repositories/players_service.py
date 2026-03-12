from proekt_futbol.db import get_connection
from datetime import datetime

VALID_POSITIONS = ['GK', 'DF', 'MF', 'FW']

def add_player(full_name, birth_date, nationality, position, number, club_name):
    if position not in VALID_POSITIONS:
        print("Невалидна позиция!")
        return
    if not (1 <= int(number) <= 99):
        print("Невалиден номер!")
        return
    try:
        datetime.strptime(birth_date, "%Y-%m-%d")
    except ValueError:
        print("Невалидна дата на раждане!")
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM clubs WHERE name = ?", (club_name,))
    club = cursor.fetchone()
    if not club:
        print(f"Клубът '{club_name}' не съществува!")
        conn.close()
        return

    club_id = club[0]

    try:
        cursor.execute("""
            INSERT INTO players (full_name, birth_date, nationality, position, number, club_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (full_name, birth_date, nationality, position, number, club_id))
        conn.commit()
        print(f"Играчът {full_name} е добавен успешно в {club_name}.")
    except Exception as e:
        print("Грешка при добавяне:", e)
    finally:
        conn.close()


def get_players_by_club(club_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT full_name, position, number, status
        FROM players
        JOIN clubs ON players.club_id = clubs.id
        WHERE clubs.name = ?
    """, (club_name,))
    players = cursor.fetchall()
    conn.close()
    return players


def update_player_number(full_name, new_number):
    if not (1 <= int(new_number) <= 99):
        print("Невалиден номер!")
        return

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE players SET number = ? WHERE full_name = ?
    """, (new_number, full_name))
    conn.commit()
    conn.close()
    print(f"Номерът на {full_name} е обновен.")


def delete_player(full_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM players WHERE full_name = ?", (full_name,))
    conn.commit()
    conn.close()
    print(f"Играчът {full_name} е изтрит.")