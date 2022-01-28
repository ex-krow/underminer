from enum import Enum

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


class GoalkeepingAdvancedStats:
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
    passes_completed: int
    passes_made: int
    pass_completion_percentage: float
    total_pass_percent: int
    progressive_pass_distance: int
    short_passes_completed: int
    short_passes_attempted: int
    short_passes_accuracy: int
    mid_passes_completed: int
    mid_passes_attempted: int
    mid_passes_accuracy: int
    long_passes_completed: int
    long_passes_attempted: int
    long_passes_accuracy: int
    assists: int
    expected_assists: float
    assists_minus_expected_assists: float
    passes_leading_to_shot: float
    passes_in_final_third: float
    passes_completed_in_penalty_box: int
    crosses_into_penalty_box: int
    progressive_passes: int


class PassTypeStats:
    passes_attempted: int
    live_ball_passes: int
    dead_ball_passes: int
    free_kick_passes: int
    through_balls: int
    passes_made_under_press: int
    sideways_passes: int
    crosses: int
    corner_kicks: int
    in_swinging_corner_kicks: int
    out_swinging_corner_kicks: int
    straight_hit_corner_kicks: int
    ground_passes: int
    low_altitude_passes: int
    high_altitude_passes: int
    left_foot_passes: int
    right_foot_passes: int
    head_passes: int
    throw_ins: int
    other_body_part_passes: int
    passes_completed: int
    offside_passes: int
    out_of_bounds_passes: int
    intercepted_passes: int
    blocked_passes: int

class GoalAndShotCreationStats:
    shot_creating_actions: int
    shot_creating_actions_per_game: float
    live_ball_passes_leading_to_shot: int
    dead_ball_passes_leading_to_shot: int
    dribbles_leading_to_shot: int
    shots_leading_to_shot: int
    fouls_leading_to_shot: int
    defensive_actions_leading_to_shot: int
    goal_creating_actions: int
    goal_creating_actions_per_match: float
    goal_creating_live_ball_passes: int
    goal_creating_dead_ball_passes: int
    dribbles_leading_to_goal: int
    shots_leading_to_goal_scoring_shot: int
    fouls_leading_to_goal: int
    defensive_actions_leading_to_goal: int

class DefensiveActionStats:
    total_tackles: int
    tackles_won: int
    tackles_in_defensive_third: int
    tackles_in_midfield: int
    tackles_in_final_third: int
    number_of_dribbles_tackled: int
    number_of_dribbles_faced: int
    tackle_percent: float
    dribbled_past: int
    press_count: int
    successfull_press_count: int
    successfull_press_percent: float
    presses_in_defensive_third: int
    presses_in_midfield: int
    presses_in_attacking_third: int
    blocked_shots: int
    shots_intercepted: int
    shots_on_target_blocked: int
    passes_intercepted: int
    interceptions: int
    tackles_plus_interceptions: int
    clearances: int
    mistakes_leading_to_a_shot: int


class PossessionStats:
    average_ball_possession_percent: float
    total_touches: int
    touches_in_penalty_box: int
    touches_in_defensive_third: int
    touches_in_midfield: int
    touches_in_final_third: int
    touches_in_opponent_penalty_box: int
    live_ball_touch: int
    successfull_dribbles: int
    attempted_dribbles: int
    successfull_dribble_percent: int
    number_of_players_dribbled_past: int
    number_of_nutmegs: int
    number_of_carries: int
    progressive_carry_distance: int
    progressive_carries: int
    carries_into_final_third: int
    carries_into_penalty_box: int
    mispossessions: int
    dispossessions: int
    pass_target: int
    passes_received: int
    pass_receive_percent: float
    progressive_passes_received: float


class MiscellaneousStats:
    yellow_cards: int
    red_cards: int
    second_yellow_cards: int
    fouls_commited: int
    fouls_drawn: int
    offsides: int
    crosses: int
    interceptions: int
    tackles_won: int
    penalties_awarded: int
    penalties_conceded: int
    own_goals: int
    loose_ball_recoveries: int
    aerials_won: int
    aerials_lost: int
    aerials_win_percent: float




class PlayerSummaryStats:
    kit_number: int
    position: int
    age: str
    minutes: int
    goals_scored: int
    assists: int
    penalties_scored: int
    penalties_awarded: int
    total_shots: int
    shots_on_target: int
    yellow_cards: int
    red_cards: int
    touches: int
    press_count: int
    total_tackles: int
    interceptions: int
    shots_blocked: int
    expected_goals: float
    non_penalty_expected_goals: float
    expected_assists: float
    shot_creating_actions: int
    goal_creating_actions: int
    passes_completed: int
    passes_made: int
    pass_completion_percentage: float
    progressive_passes: int
    carries: int
    progressive_carries: int
    successfull_dribbles: int
    dribble_attempts: int







class ShotOutCome(Enum):
    OffTarget = "Off Target"
    Blocked = "Blocked"
    Saved = "Saved"

class PlayerShotsStats:
    minute: int
    squad: str
    shot_outcome: ShotOutCome
    distance: int
    body_part: int
    notes: str
    shot_creating_action_num_one: tuple[str, str]
    shot_creating_action_num_two: tuple[str, str]

class GoalkeeperStats:
    shots_on_target_conceded: int
    goals_conceded: int
    saves: int
    save_percent: float
    post_shot_expected_goals: float
    launched_passes_completed: int
    launched_passes_attempted: int
    launched_completion_percent: float
    passes_attempted: int
    throws_attempted: int
    launched_percent_of_passes: float
    average_pass_length: float
    goal_kicks: int
    goal_kick_launch_percent: float
    average_launch_length: float
    crosses_faced: int
    crosses_stopped: int
    crosses_stop_percent: int
    defensive_actions_outside_the_box: int
    defensive_action_average_distance_from_goal: float


class MatchStats:
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
    player_stats_summary: dict[str, PlayerSummaryStats]
    player_passing_stats: dict[str, PassingStats]
    player_passtype_stats: dict[str, PassTypeStats]
    player_possession_stats: dict[str, PossessionStats]
    player_defensive_stats: dict[str, DefensiveActionStats]
    player_miscellaneous: dict[str, MiscellaneousStats]
