from src.repositories.matches_repo import MatchesRepo

repo = MatchesRepo()


class MatchesService:

    def set_result(self, match_id, home, away, hg, ag):
        repo.update_result(match_id, hg, ag)
        return f"Записан резултат: {home}-{away} {hg}:{ag}"

    def add_goal(self, match_id, player, club, minute):
        repo.insert_goal(match_id, player, club, minute)
        return f"Гол: {player} ({minute} мин)"

    def add_card(self, match_id, player, club, card_type, minute):
        repo.insert_card(match_id, player, club, card_type, minute)
        return f"Картон {card_type}: {player}"

    def get_events(self, match_id):
        goals = repo.get_goals(match_id)
        cards = repo.get_cards(match_id)

        return {
            "goals": goals,
            "cards": cards
        }