from src.repositories import players_repo
from src.repositories import clubs_repo


VALID_POSITIONS = ["GK", "DF", "MF", "FW"]


def add_player(name, club_name, position, number):

    if position not in VALID_POSITIONS:
        return "Невалидна позиция"

    club = clubs_repo.get_club_by_name(club_name)

    if not club:
        return "Клубът не съществува"

    players_repo.add_player(
        name,
        club[0],
        position,
        number
    )

    return "Играчът е добавен"


def show_players(club_name):

    club = clubs_repo.get_club_by_name(club_name)

    if not club:
        return "Клубът не съществува"

    players = players_repo.get_players_by_club(
        club[0]
    )

    text = ""

    for p in players:
        text += f"{p[2]} - {p[0]} ({p[1]})\n"

    return text


def show_all_players():

    players = players_repo.get_all_players()

    text = ""

    for p in players:
        text += (
            f"{p[0]} | "
            f"{p[1]} | "
            f"{p[2]} | "
            f"{p[3]}\n"
        )

    return text


def update_number(name, number):

    players_repo.update_player_number(
        name,
        number
    )

    return "Номерът е сменен"


def update_position(name, position):

    if position not in VALID_POSITIONS:
        return "Невалидна позиция"

    players_repo.update_player_position(
        name,
        position
    )

    return "Позицията е сменена"


def update_status(name, status):

    players_repo.update_player_status(
        name,
        status
    )

    return "Статусът е сменен"


def delete_player(name):

    players_repo.delete_player(name)

    return "Играчът е изтрит"


def find_player(name):

    player = players_repo.get_player_by_name(name)

    if not player:
        return "Играчът не съществува"

    return (
        f"{player[1]} | "
        f"{player[3]} | "
        f"№{player[4]}"
    )