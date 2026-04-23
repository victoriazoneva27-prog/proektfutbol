from src.repositories.leagues_repo import leagues_repo
from src.repositories.clubs_repo import clubs_repo

class LeaguesService:
    def create(self, name, season):
        leagues_repo.create_league(name, season)
        return "Лига създадена"

    def add_team(self, league_name, season, club_name):
        league = leagues_repo.get_league(league_name, season)
        club = clubs_repo.get_by_name(club_name)

        if not league or not club:
            return "Грешка"

        leagues_repo.add_team(league["id"], club["id"])
        return "Добавен"

leagues_service = LeaguesService()