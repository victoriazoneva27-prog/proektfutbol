from db import execute, fetch_all, fetch_one
from db import execute, fetch_all, fetch_one
from clubs import find_club_by_name
from datetime import datetime


VALID_POSITIONS = {"GK", "DF", "MF", "FW"}

def add_club(name, city=None):
    if not name.strip():
        raise ValueError("Името на клуба не може да е празно.")
    try:
        sql = "INSERT INTO clubs (name, city) VALUES (?, ?)"
        return execute(sql, (name.strip(), city))
    except Exception as e:
        print("Грешка при добавяне:", e)
        return 0

def list_clubs():
    sql = "SELECT id, name, city FROM clubs ORDER BY id"
    return fetch_all(sql)

def get_club_by_id(club_id):
    sql = "SELECT id, name, city FROM clubs WHERE id = ?"
    return fetch_one(sql, (club_id,))

def find_club_by_name(name):
    sql = "SELECT id, name, city FROM clubs WHERE name = ?"
    return fetch_one(sql, (name.strip(),))

def update_club(club_id, name, city=None):
    if not name.strip():
        raise ValueError("Името на клуба не може да е празно.")
    sql = "UPDATE clubs SET name = ?, city = ? WHERE id = ?"
    return execute(sql, (name.strip(), city, club_id))

def delete_club(club_id):
    sql = "DELETE FROM clubs WHERE id = ?"
    return execute(sql, (club_id,))

def validate_player(position, number, birth_date):
    if position not in VALID_POSITIONS:
        raise ValueError("Невалидна позиция. Позволени: GK, DF, MF, FW")

    if not (1 <= int(number) <= 99):
        raise ValueError("Номерът трябва да е между 1 и 99")

    try:
        datetime.strptime(birth_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Датата трябва да е във формат YYYY-MM-DD")


# CREATE
def add_player(full_name, birth_date, nationality, position, number, club_name):
    club = find_club_by_name(club_name)

    if not club:
        print("Клубът не съществува.")
        return

    validate_player(position, number, birth_date)

    sql = """
    INSERT INTO players (club_id, full_name, birth_date, nationality, position, number)
    VALUES (?, ?, ?, ?, ?, ?)
    """

    execute(sql, (club[0], full_name, birth_date, nationality, position, number))
    print("Играчът е добавен успешно.")


# READ + FILTER
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


# UPDATE
def update_player_number(full_name, new_number):
    if not (1 <= int(new_number) <= 99):
        print("Номерът трябва да е между 1 и 99")
        return

    sql = "UPDATE players SET number = ? WHERE full_name = ?"
    execute(sql, (new_number, full_name))
    print("Номерът е обновен.")


# DELETE
def delete_player(full_name):
    sql = "DELETE FROM players WHERE full_name = ?"
    execute(sql, (full_name,))
    print("Играчът е изтрит.")

def add_club(name, city=None):
    if not name.strip():
        raise ValueError("Името на клуба не може да е празно.")
    try:
        sql = "INSERT INTO clubs (name, city) VALUES (?, ?)"
        return execute(sql, (name.strip(), city))
    except Exception as e:
        print("Грешка при добавяне:", e)
        return 0

def list_clubs():
    sql = "SELECT id, name, city FROM clubs ORDER BY id"
    return fetch_all(sql)

def get_club_by_id(club_id):
    sql = "SELECT id, name, city FROM clubs WHERE id = ?"
    return fetch_one(sql, (club_id,))

def find_club_by_name(name):
    sql = "SELECT id, name, city FROM clubs WHERE name = ?"
    return fetch_one(sql, (name.strip(),))

def update_club(club_id, name, city=None):
    if not name.strip():
        raise ValueError("Името на клуба не може да е празно.")
    sql = "UPDATE clubs SET name = ?, city = ? WHERE id = ?"
    return execute(sql, (name.strip(), city, club_id))

def delete_club(club_id):
    sql = "DELETE FROM clubs WHERE id = ?"
    return execute(sql, (club_id,))
