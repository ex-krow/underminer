import datetime
from enum import Enum
from datatypes.stats import  MatchStats


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
    report: MatchStats
   


