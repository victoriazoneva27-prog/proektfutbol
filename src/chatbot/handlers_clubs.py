from src.services.clubs_service import clubs_service

def handle_add_club(params):
    return clubs_service.add_club(params[0])

def handle_list_clubs(params):
    return clubs_service.list_clubs()