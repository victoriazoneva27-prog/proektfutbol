from src.database.db import db


def init_database():
    db.execute("""
    CREATE TABLE IF NOT EXISTS clubs (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        city TEXT
    )
    """)

    db.execute("""
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY,
        full_name TEXT,
        club_id INTEGER,
        position TEXT,
        number INTEGER
    )
    """)

    db.execute("""
    CREATE TABLE IF NOT EXISTS leagues (
        id INTEGER PRIMARY KEY,
        name TEXT,
        season TEXT
    )
    """)

    db.execute("""
    CREATE TABLE IF NOT EXISTS league_teams (
        league_id INTEGER,
        club_id INTEGER
    )
    """)

    db.execute("""
    CREATE TABLE IF NOT EXISTS matches (
        id INTEGER PRIMARY KEY,
        league_id INTEGER,
        round_no INTEGER,
        home_club_id INTEGER,
        away_club_id INTEGER,
        home_goals INTEGER,
        away_goals INTEGER,
        status TEXT DEFAULT 'scheduled'
    )
    """)

    db.execute("""
    CREATE TABLE IF NOT EXISTS goals (
        id INTEGER PRIMARY KEY,
        match_id INTEGER,
        player_id INTEGER,
        club_id INTEGER,
        minute INTEGER
    )
    """)

    db.execute("""
    CREATE TABLE IF NOT EXISTS cards (
        id INTEGER PRIMARY KEY,
        match_id INTEGER,
        player_id INTEGER,
        club_id INTEGER,
        minute INTEGER,
        card_type TEXT
    )
    """)

    db.execute("""
    CREATE TABLE IF NOT EXISTS transfers (
        id INTEGER PRIMARY KEY,
        player_id INTEGER,
        from_club_id INTEGER,
        to_club_id INTEGER,
        transfer_date TEXT
    )
    """)


if __name__ == "__main__":
    init_database()