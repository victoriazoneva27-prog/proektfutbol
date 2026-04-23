from src.repositories.players_repo import players_repo
from src.repositories.clubs_repo import clubs_repo

class PlayersService:
    def add_player(self, name, club_name):
        club = clubs_repo.get_by_name(club_name)
        if not club:
            return "Няма клуб"
        players_repo.create(name, club["id"])
        return "Играч добавен"

players_service = PlayersService()