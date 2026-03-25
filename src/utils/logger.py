from datetime import datetime


def log_command(raw_input_text, intent, params, status, result):
    with open("commands.log", "a", encoding="utf-8") as f:
        f.write(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | "
            f"input={raw_input_text} | "
            f"intent={intent} | "
            f"params={params} | "
            f"status={status} | "
            f"result={result}\n"
        )