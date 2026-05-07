from src.services.players_service import players_service


def handle_add_player(params):
    full_name = params[0]
    club = params[1]
    position = params[2]
    number = int(params[3])

    return players_service.add_player(full_name, club, position, number)


def handle_show_players(params):
    club = params[0]
    return players_service.get_players_by_club(club)


def handle_delete_player(params):
    name = params[0]
    return players_service.delete_player(name)