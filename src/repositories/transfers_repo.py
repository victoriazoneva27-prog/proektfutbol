from src.database.db import db

class TransfersRepository:
    def add(self, player_id, from_id, to_id, date):
        db.execute(
            'INSERT INTO transfers (player_id, from_club_id, to_club_id, transfer_date) VALUES (?, ?, ?, ?)',
            (player_id, from_id, to_id, date)
        )

transfers_repo = TransfersRepository()