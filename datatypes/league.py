import season

class League:
    seasons: list[season.Season]


class LeagueTable:
    matches_played: int
    matches_won: int
    matches_drawn: int
    matches_lost: int
    goals_scored: int
    goals_conceded: int
    goal_difference: int
    points: int
    expected_goals_scored: float
    expected_goals_conceded: float
    expected_goal_difference: float
    expected_goal_difference_per_match: float
    attendance_per_game: int



