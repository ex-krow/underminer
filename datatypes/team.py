from datatypes import fixture
from datatypes.stats import StandardStats


class Team:
    name: str
    standard_stats: StandardStats
    fixtures: list[fixture.Fixture]

