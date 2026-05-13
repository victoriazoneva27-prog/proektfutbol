from src.repositories import leagues_repo
from src.repositories import clubs_repo


def create_league(
        league_name,
        season
):

    league = leagues_repo.get_league(
        league_name,
        season
    )

    if league:
        return "Лигата вече съществува"

    leagues_repo.create_league(
        league_name,
        season
    )

    return (
        f"Създадена лига: "
        f"{league_name} "
        f"{season}"
    )


def add_team_to_league(
        club_name,
        league_name,
        season
):

    club = clubs_repo.get_club_by_name(
        club_name
    )

    if not club:
        return "Клубът не съществува"

    league = leagues_repo.get_league(
        league_name,
        season
    )

    if not league:
        return "Лигата не съществува"

    exists = leagues_repo.team_exists_in_league(
        league[0],
        club[0]
    )

    if exists:
        return "Отборът вече е в лигата"

    leagues_repo.add_team_to_league(
        league[0],
        club[0]
    )

    return (
        f"{club_name} е добавен "
        f"в {league_name}"
    )


def remove_team_from_league(
        club_name,
        league_name,
        season
):

    club = clubs_repo.get_club_by_name(
        club_name
    )

    if not club:
        return "Клубът не съществува"

    league = leagues_repo.get_league(
        league_name,
        season
    )

    if not league:
        return "Лигата не съществува"

    leagues_repo.remove_team_from_league(
        league[0],
        club[0]
    )

    return (
        f"{club_name} е премахнат "
        f"от {league_name}"
    )


def show_teams(
        league_name,
        season
):

    league = leagues_repo.get_league(
        league_name,
        season
    )

    if not league:
        return "Лигата не съществува"

    teams = leagues_repo.get_teams_in_league(
        league[0]
    )

    if not teams:
        return "Няма отбори"

    text = (
        f"ОТБОРИ В "
        f"{league_name} "
        f"{season}\n\n"
    )

    for t in teams:

        text += (
            f"{t[0]}. "
            f"{t[1]}\n"
        )

    return text


def generate_schedule(
        league_name,
        season
):

    league = leagues_repo.get_league(
        league_name,
        season
    )

    if not league:
        return "Лигата не съществува"

    teams = leagues_repo.get_teams_in_league(
        league[0]
    )

    if len(teams) < 2:
        return "Няма достатъчно отбори"

    round_no = 1

    for i in range(len(teams)):

        for j in range(i + 1, len(teams)):

            leagues_repo.create_match(
                league[0],
                round_no,
                teams[i][0],
                teams[j][0]
            )

            round_no += 1

    return "Програмата е генерирана"


def show_round(
        round_no,
        league_name,
        season
):

    league = leagues_repo.get_league(
        league_name,
        season
    )

    if not league:
        return "Лигата не съществува"

    matches = leagues_repo.get_round_matches(
        league[0],
        round_no
    )

    if not matches:
        return "Няма мачове"

    text = (
        f"КРЪГ {round_no}\n\n"
    )

    for m in matches:

        text += (
            f"Мач #{m[0]} | "
            f"{m[1]} vs {m[2]} | "
            f"{m[3]}:{m[4]} | "
            f"{m[5]}\n"
        )

    return text


def show_matches(
        league_name,
        season
):

    league = leagues_repo.get_league(
        league_name,
        season
    )

    if not league:
        return "Лигата не съществува"

    matches = leagues_repo.get_all_matches(
        league[0]
    )

    if not matches:
        return "Няма мачове"

    text = ""

    for m in matches:

        text += (
            f"#{m[0]} | "
            f"Кръг {m[1]} | "
            f"{m[2]} vs {m[3]} | "
            f"{m[4]}:{m[5]} | "
            f"{m[6]}\n"
        )

    return text