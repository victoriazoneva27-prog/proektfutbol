from db import initialize_database
from clubs import add_club, get_all_clubs, update_club, delete_club
from repositories.players_service import *

def show_menu():
    print("\n--- FOOTBALL MANAGER ---")
    print("1. Добави клуб")
    print("2. Покажи всички клубове")
    print("3. Обнови клуб")
    print("4. Изтрий клуб")
    print("5. Чатбот за играчи")
    print("0. Изход")


def handle_player_commands():
    print("\n--- Чатбот за играчи ---")
    print("Команди:")
    print("Добави играч <име> <фамилия> в <клуб> позиция <позиция> номер <номер>")
    print("Покажи играчи на <клуб>")
    print("Смени номер на <име> <фамилия> на <номер>")
    print("Изтрий играч <име> <фамилия>")
    print("exit - за изход от чатбота")

    while True:
        command = input(">> ")

        if command.lower() == "exit":
            print("Излизане от чатбот за играчи...")
            break

        try:
            if command.startswith("Добави играч"):
                parts = command.split()
                full_name = parts[2] + " " + parts[3]
                club_name = parts[5]
                position = parts[7]
                number = int(parts[9])

                add_player(full_name, "1998-01-01", "Bulgarian", position, number, club_name)

            elif command.startswith("Покажи играчи на"):
                club_name = command.replace("Покажи играчи на ", "")
                players = get_players_by_club(club_name)

                if players:
                    for p in players:
                        print(f"Име: {p[0]}, Позиция: {p[1]}, Номер: {p[2]}, Статус: {p[3]}")
                else:
                    print("Няма играчи.")

            elif command.startswith("Смени номер на"):
                parts = command.split()
                full_name = parts[3] + " " + parts[4]
                new_number = int(parts[6])
                update_player_number(full_name, new_number)

            elif command.startswith("Изтрий играч"):
                full_name = command.replace("Изтрий играч ", "")
                delete_player(full_name)

            else:
                print("Неразпозната команда.")
        except Exception as e:
            print("Грешка:", e)


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
            handle_player_commands()

        elif choice == "0":
            print("Изход...")
            break

        else:
            print("Невалидна опция!")


if __name__ == "__main__":
    main()