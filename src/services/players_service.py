from src.database.db import db


class PlayersService:

    def add_player(self, name, club_name, position, number):
        if position not in ["GK", "DF", "MF", "FW"]:
            return "Невалидна позиция"

        club = db.fetch_one(
            "SELECT id FROM clubs WHERE name=?",
            (club_name,)
        )

        if not club:
            return "Клубът не съществува"

        db.execute(
            """
            INSERT INTO players(full_name, club_id, position, number)
            VALUES (?, ?, ?, ?)
            """,
            (name, club["id"], position, number)
        )

        return "Играч добавен"

    def get_players_by_club(self, club_name):
        club = db.fetch_one(
            "SELECT id FROM clubs WHERE name=?",
            (club_name,)
        )

        if not club:
            return "Клубът не съществува"

        players = db.fetch_all(
            "SELECT * FROM players WHERE club_id=?",
            (club["id"],)
        )

        if not players:
            return "Няма играчи"

        return "\n".join([p["full_name"] for p in players])

    def delete_player(self, name):
        db.execute(
            "DELETE FROM players WHERE full_name=?",
            (name,)
        )
        return "Играч изтрит"


players_service = PlayersService()