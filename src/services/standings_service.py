from src.repositories.standings_repo import standings_repo


class StandingsService:
    def calculate_table(self, league_name, season):
        league = standings_repo.get_league(league_name, season)

        if not league:
            return 'Грешка: лигата не съществува.'

        teams = standings_repo.get_teams(league['id'])

        if not teams:
            return 'Грешка: няма отбори в тази лига.'

        table = {}

        for team in teams:
            table[team['id']] = {
                'name': team['name'],
                'MP': 0,
                'W': 0,
                'D': 0,
                'L': 0,
                'GF': 0,
                'GA': 0,
                'GD': 0,
                'PTS': 0
            }

        matches = standings_repo.get_played_matches(league['id'])

        for match in matches:
            home_id = match['home_club_id']
            away_id = match['away_club_id']

            if home_id not in table or away_id not in table:
                continue

            hg = match['home_goals']
            ag = match['away_goals']

            home = table[home_id]
            away = table[away_id]

            home['MP'] += 1
            away['MP'] += 1

            home['GF'] += hg
            home['GA'] += ag

            away['GF'] += ag
            away['GA'] += hg

            if hg > ag:
                home['W'] += 1
                away['L'] += 1

                home['PTS'] += 3

            elif ag > hg:
                away['W'] += 1
                home['L'] += 1

                away['PTS'] += 3

            else:
                home['D'] += 1
                away['D'] += 1

                home['PTS'] += 1
                away['PTS'] += 1

        for team_id in table:
            team = table[team_id]
            team['GD'] = team['GF'] - team['GA']

        standings = list(table.values())

        standings.sort(
            key=lambda x: (
                -x['PTS'],
                -x['GD'],
                -x['GF'],
                x['name']
            )
        )

        lines = []
        lines.append(
            'POS TEAM MP W D L GF GA GD PTS'
        )

        pos = 1

        for team in standings:
            line = (
                str(pos) + '. ' +
                team['name'] + ' ' +
                str(team['MP']) + ' ' +
                str(team['W']) + ' ' +
                str(team['D']) + ' ' +
                str(team['L']) + ' ' +
                str(team['GF']) + ':' +
                str(team['GA']) + ' ' +
                str(team['GD']) + ' ' +
                str(team['PTS'])
            )

            lines.append(line)

            pos += 1

        return '\n'.join(lines)


standings_service = StandingsService()