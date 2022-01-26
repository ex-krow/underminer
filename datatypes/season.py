from datatypes.league import LeagueTable


class Season:
    rounds: int
    teams: int
    table: dict[str, LeagueTable]
    
