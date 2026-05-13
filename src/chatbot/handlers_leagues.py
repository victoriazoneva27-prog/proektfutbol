from src.services import leagues_service


def handle_create_league(
        league_name,
        season
):

    return leagues_service.create_league(
        league_name.strip(),
        season.strip()
    )


def handle_add_team(
        club_name,
        league_name,
        season
):

    return leagues_service.add_team_to_league(
        club_name.strip(),
        league_name.strip(),
        season.strip()
    )


def handle_remove_team(
        club_name,
        league_name,
        season
):

    return leagues_service.remove_team_from_league(
        club_name.strip(),
        league_name.strip(),
        season.strip()
    )


def handle_show_teams(
        league_name,
        season
):

    return leagues_service.show_teams(
        league_name.strip(),
        season.strip()
    )


def handle_generate_schedule(
        league_name,
        season
):

    return leagues_service.generate_schedule(
        league_name.strip(),
        season.strip()
    )


def handle_show_round(
        round_no,
        league_name,
        season
):

    return leagues_service.show_round(
        int(round_no),
        league_name.strip(),
        season.strip()
    )


def handle_show_matches(
        league_name,
        season
):

    return leagues_service.show_matches(
        league_name.strip(),
        season.strip()
    )