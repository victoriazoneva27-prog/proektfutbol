import tkinter as tk
from src.chatbot.router import router

class ChatGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Football Chatbot")

        self.text = tk.Text(self.root, height=20)
        self.text.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack(fill="x")
        self.entry.bind("<Return>", self.send)

    def send(self, event):
        user_input = self.entry.get()
        self.text.insert(tk.END, "You: " + user_input + "\n")

        response = router.route(user_input)
        self.text.insert(tk.END, "Bot: " + response + "\n")

        self.entry.delete(0, tk.END)

    def run(self):
        self.root.mainloop()