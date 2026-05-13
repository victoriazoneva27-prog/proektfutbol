from src.repositories import matches_repo
from src.repositories import players_repo
from src.repositories import clubs_repo


def set_result(
        match_id,
        home_goals,
        away_goals
):

    match = matches_repo.get_match_by_id(
        match_id
    )

    if not match:
        return "Мачът не съществува"

    matches_repo.set_result(
        match_id,
        home_goals,
        away_goals
    )

    return (
        f"Резултатът е записан: "
        f"{home_goals}:{away_goals}"
    )


def add_goal(
        match_id,
        player_name,
        club_name,
        minute
):

    if minute < 1 or minute > 120:
        return "Невалидна минута"

    player = players_repo.get_player_by_name(
        player_name
    )

    if not player:
        return "Играчът не съществува"

    club = clubs_repo.get_club_by_name(
        club_name
    )

    if not club:
        return "Клубът не съществува"

    matches_repo.add_goal(
        match_id,
        player[0],
        club[0],
        minute
    )

    return (
        f"Гол: "
        f"{player_name} "
        f"({minute} мин)"
    )


def add_card(
        match_id,
        player_name,
        club_name,
        card_type,
        minute
):

    if minute < 1 or minute > 120:
        return "Невалидна минута"

    if card_type not in ["Y", "R"]:
        return "Невалиден картон"

    player = players_repo.get_player_by_name(
        player_name
    )

    if not player:
        return "Играчът не съществува"

    club = clubs_repo.get_club_by_name(
        club_name
    )

    if not club:
        return "Клубът не съществува"

    matches_repo.add_card(
        match_id,
        player[0],
        club[0],
        minute,
        card_type
    )

    return (
        f"Картон "
        f"{card_type} "
        f"за {player_name}"
    )


def show_events(match_id):

    events = matches_repo.get_match_events(
        match_id
    )

    text = "СЪБИТИЯ:\n\n"

    text += "ГОЛОВЕ:\n"

    for g in events["goals"]:
        text += f"{g[0]} мин\n"

    text += "\nКАРТОНИ:\n"

    for c in events["cards"]:
        text += f"{c[0]} мин - {c[1]}\n"

    return text


def show_match(match_id):

    match = matches_repo.get_match_by_id(
        match_id
    )

    if not match:
        return "Мачът не съществува"

    return (
        f"Мач #{match[0]} | "
        f"{match[3]}:{match[4]} | "
        f"{match[5]}"
    )


def show_results():

    matches = matches_repo.get_all_matches()

    text = ""

    for m in matches:

        text += (
            f"#{m[0]} | "
            f"{m[1]} vs {m[2]} | "
            f"{m[3]}:{m[4]} | "
            f"{m[5]}\n"
        )

    return text