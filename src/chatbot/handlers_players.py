from src.services import players_service


def handle_add_player(
        name,
        club,
        position,
        number
):

    return players_service.add_player(
        name.strip(),
        club.strip(),
        position.strip().upper(),
        int(number)
    )


def handle_show_players(club):

    return players_service.show_players(
        club.strip()
    )


def handle_show_all_players():

    return players_service.show_all_players()


def handle_update_number(
        name,
        number
):

    return players_service.update_number(
        name.strip(),
        int(number)
    )


def handle_update_position(
        name,
        position
):

    return players_service.update_position(
        name.strip(),
        position.strip().upper()
    )


def handle_update_status(
        name,
        status
):

    return players_service.update_status(
        name.strip(),
        status.strip()
    )


def handle_delete_player(name):

    return players_service.delete_player(
        name.strip()
    )


def handle_find_player(name):

    return players_service.find_player(
        name.strip()
    )