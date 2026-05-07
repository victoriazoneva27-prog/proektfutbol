from src.services.match_context import MatchContext
from src.services.matches_service import MatchesService

service = MatchesService()


def handle_select_match(match_id):
    MatchContext.set_match(int(match_id))
    return f"Избран мач {match_id}"


def handle_result(home, away, hg, ag):
    match_id = MatchContext.get_match()

    if not match_id:
        return "Няма избран мач"

    return service.set_result(match_id, home, away, int(hg), int(ag))


def handle_goal(player_name, club_name, minute):
    match_id = MatchContext.get_match()

    if not match_id:
        return "Няма избран мач"

    return service.add_goal(match_id, player_name, club_name, int(minute))


def handle_card(player_name, club_name, card_type, minute):
    match_id = MatchContext.get_match()

    if not match_id:
        return "Няма избран мач"

    return service.add_card(match_id, player_name, club_name, card_type, int(minute))


def handle_show_events(match_id=None):
    if not match_id:
        match_id = MatchContext.get_match()

    if not match_id:
        return "Няма избран мач"

    return service.get_events(match_id)