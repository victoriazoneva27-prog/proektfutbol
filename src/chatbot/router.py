import re
import json
import os

from src.chatbot import handlers_clubs
from src.chatbot import handlers_players
from src.chatbot import handlers_transfers
from src.chatbot import handlers_leagues
from src.chatbot import handlers_matches
from src.chatbot import handlers_standings


class Router:

    def __init__(self):

        base_dir = os.path.dirname(os.path.abspath(__file__))
        intents_path = os.path.join(base_dir, "intents.json")

        with open(intents_path, "r", encoding="utf-8") as f:
            self.intents = json.load(f)

        self.handlers = {

            # clubs
            "add_club": handlers_clubs.handle_add_club,
            "list_clubs": handlers_clubs.handle_list_clubs,
            "delete_club": handlers_clubs.handle_delete_club,
            "update_club": handlers_clubs.handle_update_club,
            "find_club": handlers_clubs.handle_find_club,

            # players
            "add_player": handlers_players.handle_add_player,
            "show_players": handlers_players.handle_show_players,
            "show_all_players": handlers_players.handle_show_all_players,
            "delete_player": handlers_players.handle_delete_player,
            "update_number": handlers_players.handle_update_number,
            "update_position": handlers_players.handle_update_position,
            "update_status": handlers_players.handle_update_status,
            "find_player": handlers_players.handle_find_player,

            # transfers
            "transfer_player": handlers_transfers.handle_transfer_player,
            "transfer_player_fee": handlers_transfers.handle_transfer_player_fee,
            "show_transfers_player": handlers_transfers.handle_show_transfers_player,
            "show_transfers_club": handlers_transfers.handle_show_transfers_club,

            # leagues
            "create_league": handlers_leagues.handle_create_league,
            "list_leagues": handlers_leagues.handle_list_leagues,
            "add_team_to_league": handlers_leagues.handle_add_team_to_league,
            "remove_team_from_league": handlers_leagues.handle_remove_team_from_league,
            "show_league_teams": handlers_leagues.handle_show_league_teams,
            "generate_schedule": handlers_leagues.handle_generate_schedule,

            # matches
            "show_round": handlers_matches.handle_show_round,
            "select_match": handlers_matches.handle_select_match,
            "result_match": handlers_matches.handle_result,
            "goal": handlers_matches.handle_goal,
            "own_goal": handlers_matches.handle_own_goal,
            "card": handlers_matches.handle_card,
            "yellow_card": handlers_matches.handle_yellow_card,
            "red_card": handlers_matches.handle_red_card,
            "show_events": handlers_matches.handle_show_events,
            "show_match": handlers_matches.handle_show_match,
            "show_matches": handlers_matches.handle_show_matches,

            # standings
            "show_standings": handlers_standings.handle_show_standings,
            "refresh_standings": handlers_standings.handle_refresh_standings
        }

    def route(self, text):

        text = text.strip()

        for intent, data in self.intents.items():

            for pattern in data["patterns"]:

                match = re.search(pattern, text, re.IGNORECASE)

                if match:

                    handler = self.handlers.get(intent)

                    if not handler:
                        return "Липсва handler"

                    args = match.groups()

                    try:

                        if len(args) == 0:
                            return handler()

                        return handler(*args)

                    except Exception as e:
                        return f"Грешка: {e}"

        return "Командата не е разпозната"


router = Router()