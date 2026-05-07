from src.database.db import db


class MatchesRepo:

    def update_result(self, match_id, hg, ag):
        db.execute("""
            UPDATE matches
            SET home_goals=?, away_goals=?, status='played'
            WHERE id=?
        """, (hg, ag, match_id))

    def insert_goal(self, match_id, player, club, minute):
        db.execute("""
            INSERT INTO goals (match_id, player_id, club_id, minute)
            VALUES (?, ?, ?, ?)
        """, (match_id, 1, 1, minute))

    def insert_card(self, match_id, player, club, card_type, minute):
        db.execute("""
            INSERT INTO cards (match_id, player_id, club_id, minute, card_type)
            VALUES (?, ?, ?, ?, ?)
        """, (match_id, 1, 1, minute, card_type))

    def get_goals(self, match_id):
        return db.fetch_all("SELECT * FROM goals WHERE match_id=?", (match_id,))

    def get_cards(self, match_id):
        return db.fetch_all("SELECT * FROM cards WHERE match_id=?", (match_id,))