from src.repositories.transfers_repo import transfers_repo
from src.repositories.players_repo import players_repo
from src.repositories.clubs_repo import clubs_repo

class TransfersService:
    def transfer(self, player_name, from_club, to_club, date):
        p = players_repo.get_by_name(player_name)
        f = clubs_repo.get_by_name(from_club)
        t = clubs_repo.get_by_name(to_club)

        if not p or not t:
            return "Грешка"

        transfers_repo.add(p["id"], f["id"], t["id"], date)
        return "Трансфер записан"

transfers_service = TransfersService()