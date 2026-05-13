from src.repositories import clubs_repo


def add_club(name):

    if not name:
        return "Невалидно име"

    club = clubs_repo.get_club_by_name(name)

    if club:
        return "Клубът вече съществува"

    clubs_repo.add_club(name)

    return "Клубът е добавен"


def list_clubs():

    clubs = clubs_repo.get_all_clubs()

    if not clubs:
        return "Няма клубове"

    text = ""

    for club in clubs:
        text += f"{club[0]}. {club[1]}\n"

    return text


def delete_club(name):

    club = clubs_repo.get_club_by_name(name)

    if not club:
        return "Клубът не съществува"

    clubs_repo.delete_club(name)

    return "Клубът е изтрит"


def update_club(old_name, new_name):

    club = clubs_repo.get_club_by_name(old_name)

    if not club:
        return "Клубът не съществува"

    clubs_repo.update_club(old_name, new_name)

    return "Клубът е редактиран"


def find_club(name):

    club = clubs_repo.get_club_by_name(name)

    if not club:
        return "Клубът не съществува"

    return f"{club[0]} - {club[1]}"