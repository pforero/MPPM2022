"Score the final result of a Porra."

from itertools import compress

from mppm.porra.helper import GROUPS
from mppm.porra.tournament import Porra, Result, Progression
from mppm.porra.scoring import Scoring

class Outcome:
    """The final points outcome of a Porra.

    It requires a progression, a bet, a final result and a scoring system.

    Attributes
    ----------
    bet: Porra
    result: Porra
    points: Scoring
    """

    def __init__(
        self,
        progression: Progression,
        bet: Result,
        final: Result,
        points: Scoring
    ) -> None:

        self.bet = Porra(progression, bet)
        self.result = Porra(progression, final)
        self.points = points

    def get_single_group_points(self, group: str) -> int:
        "Calculate the points obtained in a group."

        if group not in GROUPS:
            raise ValueError(f"Group '{group}' not valid.")

        correct = [
            bet == result
            for bet, result in zip(
                self.bet.get_group(group),
                self.result.get_group(group)
            )
        ]

        return sum(list(compress(self.points.groups[group], correct)))

    def get_group_points(self) -> int:
        "Get the points from the group stage."

        points = 0
        for group in GROUPS:
            points += self.get_single_group_points(group)
        
        return points

    def get_octavos_points(self) -> int:
        "Get the points from octavos."

        correct = [
            bet == result
            for bet, result in zip(
                self.bet.get_octavos_winners(),
                self.result.get_octavos_winners()
            )
        ]

        return sum(list(compress(self.points.octavos, correct)))

    def get_quarter_points(self) -> int:
        "Get the points from quarter final."

        correct = [
            bet == result
            for bet, result in zip(
                self.bet.get_quarter_winners(),
                self.result.get_quarter_winners()
            )
        ]

        return sum(list(compress(self.points.quarter, correct)))

    def get_semi_points(self) -> int:
        "Get the points from semi final."

        correct = [
            bet == result
            for bet, result in zip(
                self.bet.get_semi_winners(),
                self.result.get_semi_winners()
            )
        ]

        return sum(list(compress(self.points.semi, correct)))

    def get_final_points(self) -> int:
        "Get the points from final."

        correct = [
            bet == result
            for bet, result in zip(
                self.bet.get_final_winners(),
                self.result.get_final_winners()
            )
        ]

        return sum(list(compress(self.points.final, correct)))

    def get_total_points(self) -> int:
        "Get total points of the Porra."
        
        points = (
            self.get_group_points()
            + self.get_octavos_points()
            + self.get_quarter_points()
            + self.get_semi_points()
            + self.get_final_points()
        )

        return points
