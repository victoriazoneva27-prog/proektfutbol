from src.database.init_db import init_database
init_database()
from src.ui.chatbot_gui import ChatGUI

if __name__ == "__main__":
    ChatGUI().run()