import tkinter as tk
from src.chatbot.router import router


class ChatGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Football Bot")

        self.text = tk.Text(self.root)
        self.text.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.entry.bind("<Return>", self.send)

    def send(self, _):
        msg = self.entry.get()
        self.text.insert(tk.END, "You: " + msg + "\n")

        response = router.route(msg)
        self.text.insert(tk.END, "Bot: " + str(response) + "\n")

        self.entry.delete(0, tk.END)

    def run(self):
        self.root.mainloop()