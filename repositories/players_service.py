from proekt_futbol.db import execute, fetch_all, fetch_one
from proekt_futbol.clubs import find_club_by_name
from datetime import datetime

VALID_POSITIONS = {"GK", "DF", "MF", "FW"}


def validate_player(position, number, birth_date):
    if position not in VALID_POSITIONS:
        raise ValueError("Невалидна позиция. Позволени: GK, DF, MF, FW")

    if not (1 <= int(number) <= 99):
        raise ValueError("Номерът трябва да е между 1 и 99")

    try:
        datetime.strptime(birth_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Датата трябва да е във формат YYYY-MM-DD")



def add_player(full_name, birth_date, nationality, position, number, club_name):
    club = find_club_by_name(club_name)

    if not club:
        print("Клубът не съществува.")
        return

    validate_player(position, number, birth_date)

    sql = """
    INSERT INTO players (club_id, full_name, birth_date, nationality, position, number, status)
    VALUES (?, ?, ?, ?, ?, ?, 'active')
    """

    execute(sql, (club[0], full_name, birth_date, nationality, position, number))
    print("Играчът е добавен успешно.")


def get_players_by_club(club_name):
    club = find_club_by_name(club_name)

    if not club:
        print("Клубът не съществува.")
        return []

    sql = """
    SELECT full_name, position, number, status
    FROM players
    WHERE club_id = ?
    """

    return fetch_all(sql, (club[0],))


def update_player_number(full_name, new_number):
    if not (1 <= int(new_number) <= 99):
        print("Номерът трябва да е между 1 и 99")
        return

    sql = "UPDATE players SET number = ? WHERE full_name = ?"
    execute(sql, (new_number, full_name))
    print("Номерът е обновен.")


def update_player_status(full_name, new_status):
    sql = "UPDATE players SET status = ? WHERE full_name = ?"
    execute(sql, (new_status, full_name))
    print("Статусът е обновен.")


def delete_player(full_name):
    sql = "DELETE FROM players WHERE full_name = ?"
    execute(sql, (full_name,))
    print("Играчът е изтрит.")