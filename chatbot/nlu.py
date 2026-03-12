def parse_command(text):

    if text.startswith("Трансфер"):
        parts = text.split()

        return {
            "intent": "transfer_player",
            "player": parts[1] + " " + parts[2],
            "from": parts[4],
            "to": parts[6],
            "date": parts[7]
        }

    if text.startswith("Покажи трансфери на"):
        name = text.replace("Покажи трансфери на ", "")

        return {
            "intent": "show_transfers_player",
            "player": name
        }

    if text.startswith("Покажи играчи на"):
        club = text.replace("Покажи играчи на ", "")

        return {
            "intent": "show_players_club",
            "club": club
        }

    return {"intent": "unknown"}