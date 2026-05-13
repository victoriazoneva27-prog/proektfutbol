from src.repositories import transfers_repo
from src.repositories import players_repo
from src.repositories import clubs_repo


def transfer_player(
        player_name,
        from_club_name,
        to_club_name,
        transfer_date
):

    player = players_repo.get_player_by_name(
        player_name
    )

    if not player:
        return "Играчът не съществува"

    from_club = clubs_repo.get_club_by_name(
        from_club_name
    )

    if not from_club:
        return "Изходящият клуб не съществува"

    to_club = clubs_repo.get_club_by_name(
        to_club_name
    )

    if not to_club:
        return "Новият клуб не съществува"

    if player[2] != from_club[0]:
        return "Играчът не е в този клуб"

    transfers_repo.add_transfer(
        player[0],
        from_club[0],
        to_club[0],
        transfer_date
    )

    players_repo.update_player_club(
        player[0],
        to_club[0]
    )

    return (
        f"Трансфер успешен:\n"
        f"{player_name}\n"
        f"{from_club_name} -> {to_club_name}\n"
        f"{transfer_date}"
    )


def show_transfers(
        player_name
):

    player = players_repo.get_player_by_name(
        player_name
    )

    if not player:
        return "Играчът не съществува"

    transfers = transfers_repo.get_transfers_by_player(
        player[0]
    )

    if not transfers:
        return "Няма трансфери"

    text = (
        f"ТРАНСФЕРИ НА "
        f"{player_name}\n\n"
    )

    for t in transfers:

        text += (
            f"{t[0]} | "
            f"{t[1]} -> {t[2]}\n"
        )

    return text


def show_club_transfers(
        club_name
):

    club = clubs_repo.get_club_by_name(
        club_name
    )

    if not club:
        return "Клубът не съществува"

    transfers = transfers_repo.get_transfers_by_club(
        club[0]
    )

    if not transfers:
        return "Няма трансфери"

    text = (
        f"ТРАНСФЕРИ НА "
        f"{club_name}\n\n"
    )

    for t in transfers:

        text += (
            f"{t[0]} | "
            f"{t[1]} | "
            f"{t[2]} -> {t[3]}\n"
        )

    return text