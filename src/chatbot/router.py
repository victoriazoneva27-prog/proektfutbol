import re
import json
import os

from src.chatbot import handlers_matches
from src.chatbot import handlers_clubs
from src.chatbot import handlers_standings


class Router:
    def __init__(self):

        base_dir = os.path.dirname(os.path.abspath(__file__))
        intents_path = os.path.join(base_dir, "intents.json")

        with open(intents_path, "r", encoding="utf-8") as f:
            self.intents = json.load(f)

        self.handlers = {
            "add_club": handlers_clubs.handle_add_club,
            "list_clubs": handlers_clubs.handle_list_clubs,

            "select_match": handlers_matches.handle_select_match,
            "result_match": handlers_matches.handle_result,
            "goal": handlers_matches.handle_goal,
            "card": handlers_matches.handle_card,
            "show_events": handlers_matches.handle_show_events,

            "show_standings": handlers_standings.handle_show_standings,
        }

    def route(self, text: str):
        text = text.strip()

        for intent, data in self.intents.items():
            for pattern in data["patterns"]:
                match = re.search(pattern, text, re.IGNORECASE)

                if match:
                    handler = self.handlers.get(intent)

                    if not handler:
                        return "Handler липсва"

                    try:
                        return handler(*match.groups())
                    except TypeError:
                        return "Грешен формат на командата"

        return "Командата не е разпозната"


router = Router()