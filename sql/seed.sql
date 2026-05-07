from src.database.db import db


def seed():

    # =========================
    # CLUBS (10 отбора)
    # =========================
    clubs = [
        ("Левски София", "София"),
        ("ЦСКА София", "София"),
        ("Лудогорец", "Разград"),
        ("Ботев Пловдив", "Пловдив"),
        ("Берое", "Стара Загора"),
        ("Славия", "София"),
        ("Черно море", "Варна"),
        ("Локомотив Пловдив", "Пловдив"),
        ("Арда Кърджали", "Кърджали"),
        ("Пирин Благоевград", "Благоевград"),
    ]

    for name, city in clubs:
        db.execute(
            "INSERT OR IGNORE INTO clubs (name, city) VALUES (?, ?)",
            (name, city)
        )

    # =========================
    # PLAYERS (5 на отбор минимум, реални имена)
    # =========================
    players = [
        # Левски
        ("Иван Петров", 1, "FW", 9),
        ("Мартин Георгиев", 1, "DF", 4),
        ("Никола Иванов", 1, "MF", 8),
        ("Даниел Стоянов", 1, "GK", 1),
        ("Симеон Димитров", 1, "MF", 10),

        # ЦСКА
        ("Георги Петров", 2, "FW", 11),
        ("Александър Колев", 2, "MF", 6),
        ("Пламен Николов", 2, "DF", 5),
        ("Иво Христов", 2, "GK", 1),
        ("Тодор Тодоров", 2, "MF", 8),

        # Лудогорец
        ("Кирил Десподов", 3, "FW", 7),
        ("Антон Недялков", 3, "DF", 2),
        ("Светослав Дяков", 3, "MF", 10),
        ("Петър Петров", 3, "GK", 1),
        ("Владимир Стоянов", 3, "FW", 9),

        # Ботев
        ("Иван Василев", 4, "FW", 9),
        ("Асен Чандъров", 4, "MF", 8),
        ("Христо Иванов", 4, "DF", 3),
        ("Димитър Илиев", 4, "GK", 1),
        ("Божидар Краев", 4, "MF", 10),

        # Берое
        ("Станислав Иванов", 5, "FW", 11),
        ("Георги Костадинов", 5, "MF", 6),
        ("Алекс Петров", 5, "DF", 4),
        ("Николай Михайлов", 5, "GK", 1),
        ("Мартин Райнов", 5, "MF", 8),
    ]

    for p in players:
        db.execute(
            """
            INSERT OR IGNORE INTO players
            (full_name, club_id, position, number)
            VALUES (?, ?, ?, ?)
            """,
            p
        )

    # =========================
    # LEAGUE
    # =========================
    db.execute(
        "INSERT OR IGNORE INTO leagues (name, season) VALUES (?, ?)",
        ("Първа лига", "2025/2026")
    )

    league = db.fetch_one(
        "SELECT id FROM leagues WHERE name=? AND season=?",
        ("Първа лига", "2025/2026")
    )

    league_id = league["id"]

    # =========================
    # LEAGUE TEAMS
    # =========================
    for club_id in range(1, 11):
        db.execute(
            "INSERT OR IGNORE INTO league_teams (league_id, club_id) VALUES (?, ?)",
            (league_id, club_id)
        )

    # =========================
    # MATCHES (минимум 5 изиграни)
    # =========================
    matches = [
        (league_id, 1, 1, 2, 2, 1, "played"),
        (league_id, 1, 3, 4, 1, 1, "played"),
        (league_id, 1, 5, 6, 0, 2, "played"),
        (league_id, 1, 7, 8, 3, 0, "played"),
        (league_id, 1, 9, 10, 1, 2, "played"),
        (league_id, 2, 1, 3, None, None, "scheduled"),
        (league_id, 2, 2, 4, None, None, "scheduled"),
    ]

    for m in matches:
        db.execute(
            """
            INSERT OR IGNORE INTO matches
            (league_id, round_no, home_club_id, away_club_id, home_goals, away_goals, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            m
        )

    # =========================
    # GOALS (минимум 5)
    # =========================
    goals = [
        (1, 1, 1, 10),
        (1, 6, 2, 55),
        (2, 11, 3, 33),
        (3, 16, 4, 77),
        (4, 21, 5, 88),
    ]

    for g in goals:
        db.execute(
            """
            INSERT OR IGNORE INTO goals
            (match_id, player_id, club_id, minute)
            VALUES (?, ?, ?, ?)
            """,
            g
        )

    # =========================
    # CARDS (минимум 5)
    # =========================
    cards = [
        (1, 1, 1, 20, "Y"),
        (1, 2, 2, 60, "R"),
        (2, 3, 3, 30, "Y"),
        (3, 4, 4, 70, "Y"),
        (4, 5, 5, 80, "R"),
    ]

    for c in cards:
        db.execute(
            """
            INSERT OR IGNORE INTO cards
            (match_id, player_id, club_id, minute, card_type)
            VALUES (?, ?, ?, ?, ?)
            """,
            c
        )

    # =========================
    # TRANSFERS (минимум 5)
    # =========================
    transfers = [
        (1, 1, 2, "2025-06-01"),
        (2, 3, 4, "2025-06-10"),
        (3, 5, 6, "2025-06-15"),
        (4, 7, 8, "2025-06-20"),
        (5, 9, 10, "2025-06-25"),
    ]

    for t in transfers:
        db.execute(
            """
            INSERT OR IGNORE INTO transfers
            (player_id, from_club_id, to_club_id, transfer_date)
            VALUES (?, ?, ?, ?)
            """,
            t
        )


if __name__ == "__main__":
    seed()