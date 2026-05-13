from src.database.db import (
    execute,
    fetch_all,
    fetch_one
)


def create_league(
        league_name,
        season
):

    execute("""
        INSERT INTO leagues(
            name,
            season
        )
        VALUES (?, ?)
    """, (
        league_name,
        season
    ))


def get_league(
        league_name,
        season
):

    return fetch_one("""
        SELECT
            id,
            name,
            season
        FROM leagues
        WHERE LOWER(name)=LOWER(?)
        AND season=?
    """, (
        league_name,
        season
    ))


def add_team_to_league(
        league_id,
        club_id
):

    execute("""
        INSERT INTO league_teams(
            league_id,
            club_id
        )
        VALUES (?, ?)
    """, (
        league_id,
        club_id
    ))


def remove_team_from_league(
        league_id,
        club_id
):

    execute("""
        DELETE FROM league_teams
        WHERE league_id=?
        AND club_id=?
    """, (
        league_id,
        club_id
    ))


def team_exists_in_league(
        league_id,
        club_id
):

    return fetch_one("""
        SELECT id
        FROM league_teams
        WHERE league_id=?
        AND club_id=?
    """, (
        league_id,
        club_id
    ))


def get_teams_in_league(
        league_id
):

    return fetch_all("""
        SELECT
            clubs.id,
            clubs.name
        FROM league_teams
        JOIN clubs
        ON clubs.id = league_teams.club_id
        WHERE league_teams.league_id=?
        ORDER BY clubs.name
    """, (league_id,))


def create_match(
        league_id,
        round_no,
        home_club_id,
        away_club_id
):

    execute("""
        INSERT INTO matches(
            league_id,
            round_no,
            home_club_id,
            away_club_id,
            home_goals,
            away_goals,
            status
        )
        VALUES (?, ?, ?, ?, 0, 0, 'scheduled')
    """, (
        league_id,
        round_no,
        home_club_id,
        away_club_id
    ))


def get_round_matches(
        league_id,
        round_no
):

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
        WHERE matches.league_id=?
        AND matches.round_no=?
        ORDER BY matches.id
    """, (
        league_id,
        round_no
    ))


def get_all_matches(
        league_id
):

    return fetch_all("""
        SELECT
            matches.id,
            matches.round_no,
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
        WHERE matches.league_id=?
        ORDER BY matches.round_no
    """, (league_id,))