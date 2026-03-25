from src.services.players_service import get_players_by_club, get_club_by_name, get_player_by_name
from src.services.transfers_service import transfer_player, list_transfers_by_player, list_transfers_by_club


def route(intent_data):
    intent = intent_data.get("intent")

    if intent == "show_players_club":
        players = get_players_by_club(intent_data["club_name"])

        if not players:
            return "Няма играчи за този клуб."

        lines = [f"{p[0]} | {p[1]} | №{p[2]} | {p[3]}" for p in players]
        return "\n".join(lines)

    if intent == "transfer_player":
        return transfer_player(
            intent_data["player_name"],
            intent_data["from_club"],
            intent_data["to_club"],
            intent_data["date"],
            intent_data["fee"]
        )

    if intent == "show_transfers_auto":
        target = intent_data["target"]

        player = get_player_by_name(target)
        if player:
            transfers = list_transfers_by_player(target)
            if not transfers:
                return "Няма трансфери за този играч."
            lines = [f"{t[0]} -> {t[1]} | {t[2]} | сума: {t[3]}" for t in transfers]
            return "\n".join(lines)

        club = get_club_by_name(target)
        if club:
            transfers = list_transfers_by_club(target)
            if not transfers:
                return "Няма трансфери за този клуб."
            lines = [f"{t[0]} | {t[1]} -> {t[2]} | {t[3]} | сума: {t[4]}" for t in transfers]
            return "\n".join(lines)

        return "ERROR: Няма играч или клуб с това име."

    return "Неразпозната команда."