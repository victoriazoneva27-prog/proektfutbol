from src.database.db import db

class LeaguesRepository:
    def create_league(self, name, season):
        return db.execute(
            'INSERT INTO leagues (name, season) VALUES (?, ?)',
            (name, season)
        )

    def get_league(self, name, season):
        return db.fetch_one(
            'SELECT * FROM leagues WHERE name=? AND season=?',
            (name, season)
        )

    def add_team(self, league_id, club_id):
        db.execute(
            'INSERT INTO league_teams (league_id, club_id) VALUES (?, ?)',
            (league_id, club_id)
        )

    def get_teams(self, league_id):
        return db.fetch_all(
            '''
            SELECT c.id, c.name
            FROM league_teams lt
            JOIN clubs c ON lt.club_id = c.id
            WHERE lt.league_id=?
            ''',
            (league_id,)
        )

leagues_repo = LeaguesRepository()