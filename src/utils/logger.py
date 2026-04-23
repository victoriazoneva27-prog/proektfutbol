from datetime import datetime

def log(text):
    with open("commands.log", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {text}\n")