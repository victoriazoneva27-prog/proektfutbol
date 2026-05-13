from src.database.db import execute, fetch_all, fetch_one


def add_player(
        full_name,
        club_id,
        position,
        number
):

    execute("""
        INSERT INTO players(
            full_name,
            club_id,
            position,
            number
        )
        VALUES (?, ?, ?, ?)
    """, (
        full_name,
        club_id,
        position,
        number
    ))


def get_player_by_name(name):

    return fetch_one("""
        SELECT
            id,
            full_name,
            club_id,
            position,
            number
        FROM players
        WHERE LOWER(full_name)=LOWER(?)
    """, (name,))


def get_players_by_club(club_id):

    return fetch_all("""
        SELECT
            full_name,
            position,
            number
        FROM players
        WHERE club_id=?
        ORDER BY number
    """, (club_id,))


def get_all_players():

    return fetch_all("""
        SELECT
            players.full_name,
            clubs.name,
            players.position,
            players.number
        FROM players
        JOIN clubs
        ON clubs.id = players.club_id
        ORDER BY players.full_name
    """)


def update_player_number(name, number):

    execute("""
        UPDATE players
        SET number=?
        WHERE LOWER(full_name)=LOWER(?)
    """, (
        number,
        name
    ))


def update_player_position(name, position):

    execute("""
        UPDATE players
        SET position=?
        WHERE LOWER(full_name)=LOWER(?)
    """, (
        position,
        name
    ))


def update_player_status(name, status):

    execute("""
        UPDATE players
        SET status=?
        WHERE LOWER(full_name)=LOWER(?)
    """, (
        status,
        name
    ))


def delete_player(name):

    execute("""
        DELETE FROM players
        WHERE LOWER(full_name)=LOWER(?)
    """, (name,))