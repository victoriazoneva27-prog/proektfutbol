from db import initialize_database
from clubs import add_club, get_all_clubs, update_club, delete_club

from chatbot.nlu import parse_command
from chatbot.router import route


def show_menu():
    print("\n--- FOOTBALL MANAGER ---")
    print("1. Добави клуб")
    print("2. Покажи всички клубове")
    print("3. Обнови клуб")
    print("4. Изтрий клуб")
    print("5. Чатбот")
    print("0. Изход")


def run_chatbot():

    print("\n--- CHATBOT ---")
    print("Примерни команди:")
    print("Трансфер Иван Петров от Левски в Лудогорец 2026-03-10")
    print("Покажи трансфери на Иван Петров")
    print("exit за изход")

    while True:

        text = input(">> ")

        if text.lower() == "exit":
            break

        data = parse_command(text)

        result = route(data)

        print(result)


def main():

    initialize_database()

    while True:

        show_menu()

        choice = input("Избери опция: ")

        if choice == "1":

            name = input("Име на клуб: ")
            city = input("Град: ")

            add_club(name, city)

        elif choice == "2":

            clubs = get_all_clubs()

            print("\n--- Списък с клубове ---")

            for club in clubs:
                print(f"ID: {club[0]}, Име: {club[1]}, Град: {club[2]}")

        elif choice == "3":

            club_id = int(input("ID на клуба: "))
            new_name = input("Ново име: ")
            new_city = input("Нов град: ")

            update_club(club_id, new_name, new_city)

        elif choice == "4":

            club_id = int(input("ID на клуба: "))

            delete_club(club_id)

        elif choice == "5":

            run_chatbot()

        elif choice == "0":

            print("Изход...")
            break

        else:

            print("Невалидна опция!")


if __name__ == "__main__":
    main()