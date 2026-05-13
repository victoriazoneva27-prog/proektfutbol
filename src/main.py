from src.chatbot.router import router


def main():

    print("Football Chatbot")
    print("Напиши 'изход' за край")

    while True:

        try:
            user_input = input(">>> ").strip()

            if not user_input:
                continue

            if user_input.lower() == "изход":
                print("Чатботът е спрян")
                break

            response = router.route(user_input)

            print(response)

        except KeyboardInterrupt:
            print("\nЧатботът е спрян")
            break

        except Exception as e:
            print(f"Грешка: {e}")


if __name__ == "__main__":
    main()