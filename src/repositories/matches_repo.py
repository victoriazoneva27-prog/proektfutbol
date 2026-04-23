from src.database.db import db


class MatchesRepository:

    def get_match(self, match_id):
        return db.fetch_one(
            'SELECT * FROM matches WHERE id=?',
            (match_id,)
        )

    def get_round_matches(self, league_id, round_no):
        return db.fetch_all(
            '''
            SELECT m.id,
                   h.name as home_team,
                   a.name as away_team,
                   m.home_goals,
                   m.away_goals,
                   m.status
            FROM matches m
            JOIN clubs h ON m.home_club_id = h.id
            JOIN clubs a ON m.away_club_id = a.id
            WHERE m.league_id=? AND m.round_no=?
            ''',
            (league_id, round_no)
        )

    def find_match(self, league_id, home_id, away_id):
        return db.fetch_one(
            '''
            SELECT * FROM matches
            WHERE league_id=? AND home_club_id=? AND away_club_id=?
            ''',
            (league_id, home_id, away_id)
        )

    def set_result(self, match_id, home_goals, away_goals):
        db.execute(
            '''
            UPDATE matches
            SET home_goals=?, away_goals=?, status='played'
            WHERE id=?
            ''',
            (home_goals, away_goals, match_id)
        )

    def add_goal(self, match_id, player_id, club_id, minute):
        db.execute(
            '''
            INSERT INTO goals (match_id, player_id, club_id, minute)
            VALUES (?, ?, ?, ?)
            ''',
            (match_id, player_id, club_id, minute)
        )

    def add_card(self, match_id, player_id, club_id, minute, card_type):
        db.execute(
            '''
            INSERT INTO cards (match_id, player_id, club_id, minute, card_type)
            VALUES (?, ?, ?, ?, ?)
            ''',
            (match_id, player_id, club_id, minute, card_type)
        )

    def get_events(self, match_id):
        goals = db.fetch_all(
            '''
            SELECT minute, p.full_name as player, c.name as club, 'GOAL' as type
            FROM goals g
            JOIN players p ON g.player_id = p.id
            JOIN clubs c ON g.club_id = c.id
            WHERE g.match_id=?
            ''',
            (match_id,)
        )

        cards = db.fetch_all(
            '''
            SELECT minute, p.full_name as player, c.name as club, card_type as type
            FROM cards ca
            JOIN players p ON ca.player_id = p.id
            JOIN clubs c ON ca.club_id = c.id
            WHERE ca.match_id=?
            ''',
            (match_id,)
        )

        return goals + cards


matches_repo = MatchesRepository()