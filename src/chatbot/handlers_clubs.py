from src.services import clubs_service


def handle_add_club(name):

    return clubs_service.add_club(
        name.strip()
    )


def handle_list_clubs():

    return clubs_service.list_clubs()


def handle_delete_club(name):

    return clubs_service.delete_club(
        name.strip()
    )


def handle_update_club(
        old_name,
        new_name
):

    return clubs_service.update_club(
        old_name.strip(),
        new_name.strip()
    )


def handle_find_club(name):

    return clubs_service.find_club(
        name.strip()
    )