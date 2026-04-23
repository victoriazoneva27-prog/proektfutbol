import json
import re

from src.chatbot.handlers_clubs import handle_add_club, handle_list_clubs
from src.chatbot.handlers_matches import handle_select_match, handle_goal


class Router:
    def __init__(self):
        self.handlers = {
            "handle_add_club": handle_add_club,
            "handle_list_clubs": handle_list_clubs,
            "handle_select_match": handle_select_match,
            "handle_goal": handle_goal
        }

        import os

        BASE_DIR = os.path.dirname(__file__)
        path = os.path.join(BASE_DIR, "intents.json")

        with open(path, encoding="utf-8") as f:
            self.intents = json.load(f)
            self.intents = json.load(f)

    def route(self, text):
        text = text.strip()

        for intent_data in self.intents.values():
            patterns = intent_data.get("patterns", [])
            handler_name = intent_data.get("handler")

            for pattern in patterns:
                match = re.fullmatch(pattern, text)
                if match:
                    handler = self.handlers.get(handler_name)

                    if not handler:
                        return "Грешка: handler не съществува"

                    try:
                        result = handler(match.groups())
                        return result if result else "OK"
                    except Exception as e:
                        return f"Грешка: {str(e)}"

        return "Неразпозната команда"


router = Router()