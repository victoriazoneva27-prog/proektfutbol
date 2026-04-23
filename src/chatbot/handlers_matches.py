from src.services.matches_service import matches_service

def handle_select_match(p):
    return matches_service.select_match(int(p[0]))

def handle_goal(p):
    return matches_service.add_goal(p[0], p[1], int(p[2]))