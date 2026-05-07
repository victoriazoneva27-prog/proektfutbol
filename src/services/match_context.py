class MatchContext:
    active_match_id = None

    @classmethod
    def set_match(cls, match_id):
        cls.active_match_id = match_id

    @classmethod
    def get_match(cls):
        return cls.active_match_id