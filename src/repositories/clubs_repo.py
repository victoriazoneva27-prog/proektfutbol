from src.database.db import db


class ClubsRepository:
    def create(self, name):
        return db.execute(
            'INSERT INTO clubs (name) VALUES (?)',
            (name,)
        )

    def get_by_name(self, name):
        return db.fetch_one(
            'SELECT * FROM clubs WHERE LOWER(name)=LOWER(?)',
            (name,)
        )

    def get_all(self):
        return db.fetch_all(
            'SELECT * FROM clubs'
        )

    def delete(self, club_id):
        db.execute(
            'DELETE FROM clubs WHERE id=?',
            (club_id,)
        )


clubs_repo = ClubsRepository()