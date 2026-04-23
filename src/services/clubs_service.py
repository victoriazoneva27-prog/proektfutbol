from src.repositories.clubs_repo import clubs_repo


class ClubsService:
    def add_club(self, name):
        if not name:
            return "Грешка: празно име"

        existing = clubs_repo.get_by_name(name)
        if existing:
            return "Грешка: клубът вече съществува"

        clubs_repo.create(name)
        return "Клуб добавен"

    def list_clubs(self):
        clubs = clubs_repo.get_all()
        if not clubs:
            return "Няма клубове"

        result = []
        for c in clubs:
            result.append(c["name"])

        return "\n".join(result)

    def delete_club(self, name):
        club = clubs_repo.get_by_name(name)
        if not club:
            return "Няма такъв клуб"

        clubs_repo.delete(club["id"])
        return "Клуб изтрит"


clubs_service = ClubsService()