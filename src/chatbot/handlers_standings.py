from src.services import standings_service


def handle_show_standings(
        league_name,
        season
):

    return standings_service.calculate_table(
        league_name.strip(),
        season.strip()
    )


def handle_refresh_standings(
        league_name,
        season
):

    return standings_service.refresh_table(
        league_name.strip(),
        season.strip()
    )


def handle_top_scorers(
        league_name,
        season
):

    return standings_service.top_scorers(
        league_name.strip(),
        season.strip()
    )


def handle_best_attack(
        league_name,
        season
):

    return standings_service.best_attack(
        league_name.strip(),
        season.strip()
    )


def handle_best_defense(
        league_name,
        season
):

    return standings_service.best_defense(
        league_name.strip(),
        season.strip()
    )