from src.repositories.matches_repo import matches_repo
from src.repositories.clubs_repo import clubs_repo
from src.repositories.players_repo import players_repo

class MatchesService:
    def __init__(self):
        self.current_match = None

    def select_match(self, match_id):
        m = matches_repo.get_match(match_id)
        if not m:
            return "Няма мач"
        self.current_match = match_id
        return "Избран мач"

    def add_goal(self, player, club, minute):
        if not self.current_match:
            return "Няма избран мач"

        p = players_repo.get_by_name(player)
        c = clubs_repo.get_by_name(club)

        if not p or not c:
            return "Грешка"

        if minute < 1 or minute > 120:
            return "Невалидна минута"

        matches_repo.add_goal(self.current_match, p["id"], c["id"], minute)
        return "Гол записан"

matches_service = MatchesService()