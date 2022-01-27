from datatypes import fixture, stats
from datatypes.league import LeagueTable


class Season:
    rounds: int
    teams: int
    league_table: dict[str, LeagueTable]
    team_standard_stats: dict[str, stats.StandardStats]
    team_goalkeeping_stata: dict[str, stats.GoalkeepingStats]
    team_shooting_stats: dict[str, stats.ShootingStats]
    team_passing_stats: dict[str, stats.PassingStats]
    team_passtype_stats: dict[str, stats.PassTypeStats]
    team_goal_and_shot_creation: dict[str, stats.GoalAndShotCreationStats]
    team_defensive_actions: dict[str, stats.DefensiveActionStats]
    team_possession_stats: dict[str, stats.PossessionStats]
    fixtures: list[fixture.Fixture]
