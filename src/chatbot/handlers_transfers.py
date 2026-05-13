from src.repositories import transfers_repo
from src.repositories import players_repo
from src.repositories import clubs_repo


def transfer_player(
        player_name,
        from_club,
        to_club,
        transfer_date
):

    player = players_repo.get_player_by_name(
        player_name
    )

    if not player:
        return "Играчът не съществува"

    from_team = clubs_repo.get_club_by_name(
        from_club
    )

    to_team = clubs_repo.get_club_by_name(
        to_club
    )

    if not from_team or not to_team:
        return "Невалиден клуб"

    transfers_repo.add_transfer(
        player[0],
        from_team[0],
        to_team[0],
        transfer_date
    )

    players_repo.update_player_club(
        player[0],
        to_team[0]
    )

    return (
        f"Трансфер: "
        f"{player_name} "
        f"{from_club} -> "
        f"{to_club}"
    )


def show_transfers(player_name):

    player = players_repo.get_player_by_name(
        player_name
    )

    if not player:
        return "Играчът не съществува"

    transfers = transfers_repo.get_transfers_by_player(
        player[0]
    )

    text = ""

    for t in transfers:

        text += (
            f"{t[0]} | "
            f"{t[1]} -> {t[2]}\n"
        )

    return text


def show_club_transfers(club_name):

    club = clubs_repo.get_club_by_name(
        club_name
    )

    if not club:
        return "Клубът не съществува"

    transfers = transfers_repo.get_transfers_by_club(
        club[0]
    )

    text = ""

    for t in transfers:

        text += (
            f"{t[0]} | "
            f"{t[1]}\n"
        )

    return text