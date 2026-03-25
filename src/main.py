from src.database.db import initialize_database
from src.chatbot.nlu import parse_command
from src.chatbot.router import route
from src.utils.logger import log_command


def main():
    initialize_database()

    print("FootballAI Chatbot")
    print("Пиши команда. За изход: изход")
    print("Примери:")
    print("Покажи играчи на Левски")
    print("Трансфер Иван Петров от Левски в Лудогорец 2026-03-10")
    print("Трансфер Иван Петров от Левски в Лудогорец 2026-03-10 сума 50000")
    print("Покажи трансфери на Иван Петров")
    print("Покажи трансфери на Левски")

    while True:
        raw_input_text = input(">> ").strip()

        if raw_input_text.lower() in ["изход", "exit", "quit"]:
            print("Изход.")
            break

        intent_data = parse_command(raw_input_text)
        result = route(intent_data)

        intent = intent_data.get("intent", "unknown")
        params = {k: v for k, v in intent_data.items() if k != "intent"}
        status = "OK" if not str(result).startswith("ERROR:") else "ERROR"

        log_command(raw_input_text, intent, params, status, result)
        print(result)


if __name__ == "__main__":
    main()