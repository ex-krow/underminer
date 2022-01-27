class FixtureStats:
    y: int


class StandardStats:
    number_of_different_players_used: int
    average_team_age: float
    average_ball_possession_percent: float
    matches_played: int
    goals_scored: int
    assists: int
    goals_plus_assists: int
    non_penalty_goals: int
    penalties_played: int
    penalties_scored: int
    yellow_cards: int
    red_cards: int
    goals_per_match: float
    assists_per_match: float
    goals_plus_assists_per_match: float
    non_penalty_goals_per_match: float
    non_penalty_goals_plus_assist_per_match: float
    expected_goals_scored: float
    expected_non_penalty_goals: float
    expected_assists: float
    expected_non_penalty_goals_plus_assist_per_match: float
    expected_goals_per_match: float
    expected_assists_per_match: float
    expected_goals_plus_assist_per_match: float
    expected_non_penalty_goals: float
    expected_non_penalty_goals_plus_assist_per_match: float


class GoalkeepingStats:
    goals_conceded: int
    goals_conceded_per_match: float
    shots_on_target_conceded: int
    saves: int
    save_percent: float
    clean_sheets: int
    clean_sheet_percent: float
    penalties_faced: int
    penalties_saved: int
    penalty_goals_conceded: int
    penalty_save_percent: float
    penalties_off_target_conceded: float
    free_kick_goals_conceded: int
    corner_kick_goals_conceded: int
    own_goals: int
    post_shot_expected_goals: float
    post_shot_expected_goals_per_shot_on_target: float
    post_shot_expected_goal_difference: float
    post_shot_expected_goal_difference_per_match: float
    launched_passes_completed: int
    launched_passes_made: int
    pass_accuracy_percent: float
    non_goal_kick_passes: int
    throws: int
    launched_percent_of_passes: float
    average_pass_length: float
    goal_kicks_played: int
    goal_kick_launch_percent: float
    goal_kicks_average_length: float
    crosses_faced: int
    crosses_stopped: int
    stop_percent: float
    defensive_action_outside_the_box: int
    defensive_action_outside_the_box_per_game: float
    defensive_action_average_distance_from_goal: float

class ShootingStats:
    goals_scored: int
    shots: int
    shots_on_target: int
    shots_on_target_percent: float
    shots_per_match: float
    shots_on_target_per_match: float
    goals_per_shot: float
    goals_per_shot_on_target: float
    average_shot_distance_from_goal: float
    free_kick_shots: int
    penalty_goals_scored: int
    penalties_played: int
    expected_goals_scored: float
    expected_non_penalty_goals: float
    expected_goals_per_shot: float
    goals_scored_minus_expected_goals: float
    non_penalty_goals_minus_expected_non_penalty_goals: float

class PassingStats:
    d = 0


class PassTypeStats:
    d = 0

class GoalAndShotCreationStats:
    d = 0

class DefensiveActionStats:
    d = 0

class PossessionStats:
    d = 0


