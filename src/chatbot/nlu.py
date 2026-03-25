import re


def parse_command(text):
    text = text.strip()

    transfer_with_fee_pattern = r"^Трансфер\s+(.+?)\s+от\s+(.+?)\s+в\s+(.+?)\s+(\d{4}-\d{2}-\d{2})\s+сума\s+([0-9]+(?:\.[0-9]+)?)$"
    transfer_pattern = r"^Трансфер\s+(.+?)\s+от\s+(.+?)\s+в\s+(.+?)\s+(\d{4}-\d{2}-\d{2})$"
    show_transfers_pattern = r"^Покажи трансфери на\s+(.+)$"
    show_players_club_pattern = r"^Покажи играчи на\s+(.+)$"

    m = re.match(transfer_with_fee_pattern, text, re.IGNORECASE)
    if m:
        return {
            "intent": "transfer_player",
            "player_name": m.group(1).strip(),
            "from_club": m.group(2).strip(),
            "to_club": m.group(3).strip(),
            "date": m.group(4).strip(),
            "fee": m.group(5).strip()
        }

    m = re.match(transfer_pattern, text, re.IGNORECASE)
    if m:
        return {
            "intent": "transfer_player",
            "player_name": m.group(1).strip(),
            "from_club": m.group(2).strip(),
            "to_club": m.group(3).strip(),
            "date": m.group(4).strip(),
            "fee": None
        }

    m = re.match(show_players_club_pattern, text, re.IGNORECASE)
    if m:
        return {
            "intent": "show_players_club",
            "club_name": m.group(1).strip()
        }

    m = re.match(show_transfers_pattern, text, re.IGNORECASE)
    if m:
        return {
            "intent": "show_transfers_auto",
            "target": m.group(1).strip()
        }

    return {
        "intent": "unknown",
        "raw_text": text
    }