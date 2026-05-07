from src.services.standings_service import standings_service


def handle_show_standings(league_name, season):
    return standings_service.calculate_table(league_name, season)