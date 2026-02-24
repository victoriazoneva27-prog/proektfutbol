from db import execute, fetch_all, fetch_one
from clubs import find_club_by_name
from datetime import datetime

VALID_POSITIONS = {"GK", "DF", "MF", "FW"}


def validate_position(position):
    if position not in VALID_POSITIONS:
        raise ValueError("Позицията трябва да е една от: GK, DF, MF, FW")


def validate_number(number):
    if not (1 <= number <= 99):
        raise ValueError("Номерът трябва да е между 1 и 99")


def validate_birth_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Датата трябва да е във формат YYYY-MM-DD")

def add_player(full_name, birth_date, nationality,
               position, number, club_name):

    if not full_name.strip():
        raise ValueError("Името не може да е празно")

    validate_birth_date(birth_date)
    validate_position(position)
    validate_number(number)

    club = find_club_by_name(club_name)
    if not club:
        raise ValueError("Клубът не съществува")

    club_id = club[0]

    sql = """
    INSERT INTO players
    (name, birth_date, nationality, position, number, club_id)
    VALUES (?, ?, ?, ?, ?, ?)
    """

    return execute(sql, (
        full_name.strip(),
        birth_date,
        nationality,
        position,
        number,
        club_id
    ))

def list_players():
    sql = """
    SELECT p.id, p.name, p.position, p.number, p.status, c.name
    FROM players p
    JOIN clubs c ON p.club_id = c.id
    ORDER BY p.id
    """
    return fetch_all(sql)


def list_players_by_club(club_name):
    sql = """
    SELECT p.id, p.name, p.position, p.number, p.status
    FROM players p
    JOIN clubs c ON p.club_id = c.id
    WHERE c.name = ?
    """
    return fetch_all(sql, (club_name,))


def find_player_by_name(name):
    sql = "SELECT id FROM players WHERE name = ?"
    return fetch_one(sql, (name,))

def update_player(player_id, position=None, number=None, status=None):
    fields = []
    values = []

    if position:
        validate_position(position)
        fields.append("position=?")
        values.append(position)

    if number:
        validate_number(number)
        fields.append("number=?")
        values.append(number)

    if status:
        fields.append("status=?")
        values.append(status)

    if not fields:
        raise ValueError("Няма подадени стойности за обновяване")

    sql = f"UPDATE players SET {', '.join(fields)} WHERE id=?"
    values.append(player_id)

    return execute(sql, tuple(values))

def delete_player(player_name):
    player = find_player_by_name(player_name)
    if not player:
        raise ValueError("Играчът не съществува")

    sql = "DELETE FROM players WHERE id=?"
    return execute(sql, (player[0],))