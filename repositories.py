from db import execute, fetch_all, fetch_one

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
