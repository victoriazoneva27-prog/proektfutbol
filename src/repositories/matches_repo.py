from src.database.db import execute, fetch_all, fetch_one


def get_match_by_id(match_id):

    return fetch_one("""
        SELECT
            id,
            home_club_id,
            away_club_id,
            home_goals,
            away_goals,
            status
        FROM matches
        WHERE id=?
    """, (match_id,))


def set_result(
        match_id,
        home_goals,
        away_goals
):

    execute("""
        UPDATE matches
        SET
            home_goals=?,
            away_goals=?,
            status='played'
        WHERE id=?
    """, (
        home_goals,
        away_goals,
        match_id
    ))


def add_goal(
        match_id,
        player_id,
        club_id,
        minute
):

    execute("""
        INSERT INTO goals(
            match_id,
            player_id,
            club_id,
            minute
        )
        VALUES (?, ?, ?, ?)
    """, (
        match_id,
        player_id,
        club_id,
        minute
    ))


def add_card(
        match_id,
        player_id,
        club_id,
        minute,
        card_type
):

    execute("""
        INSERT INTO cards(
            match_id,
            player_id,
            club_id,
            minute,
            card_type
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        match_id,
        player_id,
        club_id,
        minute,
        card_type
    ))


def get_match_events(match_id):

    goals = fetch_all("""
        SELECT minute
        FROM goals
        WHERE match_id=?
        ORDER BY minute
    """, (match_id,))

    cards = fetch_all("""
        SELECT minute, card_type
        FROM cards
        WHERE match_id=?
        ORDER BY minute
    """, (match_id,))

    return {
        "goals": goals,
        "cards": cards
    }


def get_all_matches():

    return fetch_all("""
        SELECT
            matches.id,
            hc.name,
            ac.name,
            matches.home_goals,
            matches.away_goals,
            matches.status
        FROM matches
        JOIN clubs hc
        ON hc.id = matches.home_club_id
        JOIN clubs ac
        ON ac.id = matches.away_club_id
        ORDER BY matches.id
    """)