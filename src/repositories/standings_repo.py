from src.database.db import db


class StandingsRepository:
    def get_league(self, league_name, season):
        return db.fetch_one(
            '''
            SELECT * FROM leagues
            WHERE name=? AND season=?
            ''',
            (league_name, season)
        )

    def get_teams(self, league_id):
        return db.fetch_all(
            '''
            SELECT c.id, c.name
            FROM league_teams lt
            JOIN clubs c ON lt.club_id = c.id
            WHERE lt.league_id = ?
            ''',
            (league_id,)
        )

    def get_played_matches(self, league_id):
        return db.fetch_all(
            '''
            SELECT *
            FROM matches
            WHERE league_id = ?
            AND status = 'played'
            AND home_goals IS NOT NULL
            AND away_goals IS NOT NULL
            ''',
            (league_id,)
        )


standings_repo = StandingsRepository()