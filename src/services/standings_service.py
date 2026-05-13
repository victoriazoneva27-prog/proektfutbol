from src.repositories import standings_repo


def calculate_table(
        league_name,
        season
):

    league = standings_repo.get_league(
        league_name,
        season
    )

    if not league:
        return "Лигата не съществува"

    league_id = league[0]

    teams = standings_repo.get_teams(
        league_id
    )

    matches = standings_repo.get_matches(
        league_id
    )

    table = {}

    for t in teams:

        table[t[0]] = {
            "name": t[1],
            "mp": 0,
            "w": 0,
            "d": 0,
            "l": 0,
            "gf": 0,
            "ga": 0,
            "gd": 0,
            "pts": 0
        }

    for m in matches:

        home = m[0]
        away = m[1]
        hg = m[2]
        ag = m[3]

        table[home]["mp"] += 1
        table[away]["mp"] += 1

        table[home]["gf"] += hg
        table[home]["ga"] += ag

        table[away]["gf"] += ag
        table[away]["ga"] += hg

        if hg > ag:

            table[home]["w"] += 1
            table[away]["l"] += 1

            table[home]["pts"] += 3

        elif ag > hg:

            table[away]["w"] += 1
            table[home]["l"] += 1

            table[away]["pts"] += 3

        else:

            table[home]["d"] += 1
            table[away]["d"] += 1

            table[home]["pts"] += 1
            table[away]["pts"] += 1

    for t in table.values():

        t["gd"] = t["gf"] - t["ga"]

    sorted_table = sorted(
        table.values(),
        key=lambda x: (
            -x["pts"],
            -x["gd"],
            -x["gf"],
            x["name"]
        )
    )

    text = ""

    pos = 1

    for t in sorted_table:

        text += (
            f"{pos}. "
            f"{t['name']} | "
            f"MP:{t['mp']} "
            f"W:{t['w']} "
            f"D:{t['d']} "
            f"L:{t['l']} "
            f"GF:{t['gf']} "
            f"GA:{t['ga']} "
            f"GD:{t['gd']} "
            f"PTS:{t['pts']}\n"
        )

        pos += 1

    return text


def refresh_table(
        league_name,
        season
):

    return calculate_table(
        league_name,
        season
    )


def top_scorers(
        league_name,
        season
):

    scorers = standings_repo.get_top_scorers(
        league_name,
        season
    )

    text = ""

    for s in scorers:

        text += (
            f"{s[0]} - "
            f"{s[1]} гола\n"
        )

    return text


def best_attack(
        league_name,
        season
):

    return standings_repo.best_attack(
        league_name,
        season
    )


def best_defense(
        league_name,
        season
):

    return standings_repo.best_defense(
        league_name,
        season
    )