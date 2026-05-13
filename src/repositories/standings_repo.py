from src.database.db import fetch_all, fetch_one


def get_league(
        league_name,
        season
):

    return fetch_one("""
        SELECT id
        FROM leagues
        WHERE LOWER(name)=LOWER(?)
        AND season=?
    """, (
        league_name,
        season
    ))


def get_teams(league_id):

    return fetch_all("""
        SELECT
            clubs.id,
            clubs.name
        FROM league_teams
        JOIN clubs
        ON clubs.id = league_teams.club_id
        WHERE league_teams.league_id=?
    """, (league_id,))


def get_matches(league_id):

    return fetch_all("""
        SELECT
            home_club_id,
            away_club_id,
            home_goals,
            away_goals
        FROM matches
        WHERE league_id=?
        AND status='played'
    """, (league_id,))


def get_top_scorers(
        league_name,
        season
):

    return fetch_all("""
        SELECT
            players.full_name,
            COUNT(goals.id) as goals_count
        FROM goals
        JOIN players
        ON players.id = goals.player_id
        GROUP BY players.full_name
        ORDER BY goals_count DESC
        LIMIT 10
    """)


def best_attack(
        league_name,
        season
):

    team = fetch_one("""
        SELECT
            clubs.name,
            SUM(matches.home_goals)
        FROM matches
        JOIN clubs
        ON clubs.id = matches.home_club_id
        GROUP BY clubs.name
        ORDER BY SUM(matches.home_goals) DESC
        LIMIT 1
    """)

    if not team:
        return "Няма данни"

    return f"Най-добра атака: {team[0]}"


def best_defense(
        league_name,
        season
):

    team = fetch_one("""
        SELECT
            clubs.name,
            SUM(matches.away_goals)
        FROM matches
        JOIN clubs
        ON clubs.id = matches.away_club_id
        GROUP BY clubs.name
        ORDER BY SUM(matches.away_goals) ASC
        LIMIT 1
    """)

    if not team:
        return "Няма данни"

    return f"Най-добра защита: {team[0]}"