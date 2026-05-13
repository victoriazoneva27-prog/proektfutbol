from src.database.db import execute, fetch_all, fetch_one


def add_club(name):

    execute(
        "INSERT INTO clubs(name) VALUES (?)",
        (name,)
    )


def get_all_clubs():

    return fetch_all("""
        SELECT id, name
        FROM clubs
        ORDER BY name
    """)


def get_club_by_name(name):

    return fetch_one("""
        SELECT id, name
        FROM clubs
        WHERE LOWER(name)=LOWER(?)
    """, (name,))


def delete_club(name):

    execute("""
        DELETE FROM clubs
        WHERE LOWER(name)=LOWER(?)
    """, (name,))


def update_club(old_name, new_name):

    execute("""
        UPDATE clubs
        SET name=?
        WHERE LOWER(name)=LOWER(?)
    """, (
        new_name,
        old_name
    ))