from proekt_futbol.repositories.transfers_service import transfer_player, list_transfers_by_player
from proekt_futbol.repositories.players_service import get_players_by_club


def route(data):

    intent = data["intent"]

    if intent == "transfer_player":
        return transfer_player(
            data["player"],
            data["from"],
            data["to"],
            data["date"]
        )

    elif intent == "show_transfers_player":

        transfers = list_transfers_by_player(data["player"])

        if not transfers:
            return "Няма трансфери."

        result = ""
        for t in transfers:
            result += f"{t[0]} -> {t[1]} ({t[2]})\n"

        return result

    elif intent == "show_players_club":

        players = get_players_by_club(data["club"])

        if not players:
            return "Няма играчи."

        result = ""
        for p in players:
            result += f"{p[0]} | {p[1]} | №{p[2]}\n"

        return result

    else:
        return "Неразпозната команда."