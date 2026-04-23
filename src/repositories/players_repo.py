from src.database.db import db

class PlayersRepository:
    def create(self, name, club_id):
        return db.execute(
            'INSERT INTO players (full_name, club_id) VALUES (?, ?)',
            (name, club_id)
        )

    def get_by_name(self, name):
        return db.fetch_one(
            'SELECT * FROM players WHERE LOWER(full_name)=LOWER(?)',
            (name,)
        )

players_repo = PlayersRepository()