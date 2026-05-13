from src.services import matches_service


CURRENT_MATCH = None


def handle_select_match(match_id):

    global CURRENT_MATCH

    CURRENT_MATCH = int(match_id)

    return f"Избран мач {match_id}"


def handle_result(
        home,
        away,
        home_goals,
        away_goals
):

    global CURRENT_MATCH

    if CURRENT_MATCH is None:
        return "Няма избран мач"

    return matches_service.set_result(
        CURRENT_MATCH,
        int(home_goals),
        int(away_goals)
    )


def handle_goal(
        player_name,
        club_name,
        minute
):

    global CURRENT_MATCH

    if CURRENT_MATCH is None:
        return "Няма избран мач"

    return matches_service.add_goal(
        CURRENT_MATCH,
        player_name.strip(),
        club_name.strip(),
        int(minute)
    )


def handle_card(
        player_name,
        club_name,
        card_type,
        minute
):

    global CURRENT_MATCH

    if CURRENT_MATCH is None:
        return "Няма избран мач"

    return matches_service.add_card(
        CURRENT_MATCH,
        player_name.strip(),
        club_name.strip(),
        card_type.strip().upper(),
        int(minute)
    )


def handle_show_events():

    global CURRENT_MATCH

    if CURRENT_MATCH is None:
        return "Няма избран мач"

    return matches_service.show_events(
        CURRENT_MATCH
    )


def handle_show_match(match_id):

    return matches_service.show_match(
        int(match_id)
    )


def handle_show_results():

    return matches_service.show_results()