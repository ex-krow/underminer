import datetime



class MatchReport:
    possession: tuple[float, float]
    shots: tuple[int, int]
    shots_on_target: tuple[float, float]
    saves: tuple[float, float]
    red_cards: tuple[int, int]
    yellow_cards: tuple[int, int]
    fouls: tuple[int, int]
    corners: tuple[int, int]
    crosses: tuple[int, int]
    touches: tuple[int, int]
    tackles: tuple[int, int]
    interceptions: tuple[int, int]
    aerials_won: tuple[int, int]
    clearances: tuple[int, int]
    offsides: tuple[int, int]
    goal_kicks: tuple[int, int]
    throw_ins:  tuple[int, int]
    long_balls: tuple[int, int]

class Fixture:
    round: int
    date: datetime.date
    time: datetime.time
    home_team: str
    expected_home_goals: float
    scores: tuple[int, int]
    away_team: str
    expected_away_goals: float
    attendance: int
    venue: str
    referee: str
    report: MatchReport
    
