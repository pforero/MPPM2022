"A Porra."

from typing import List, Tuple

from mppm.porra.helper import GROUPS
from mppm.porra.progression import Progression
from mppm.porra.result import Result

class Porra:
    """A Porra Tournament.

    Calculates the outcome given a progression structure and a result.

    Attributes
    ----------
    progression: Progression
    result: Result
    """

    def __init__(
        self,
        progression: Progression,
        result: Result
    ) -> None:
        
        self.progression = progression
        self.result = result

    def get_group(self, group: str) -> List[str]:
        "Get the outcome of a group."

        if group not in GROUPS:
            raise ValueError(f"Group '{group}' not valid.")
        
        return [self.progression.groups[group][res] for res in self.result.groups[group]]

    def get_group_team(self, group: str, pos: int) -> str:
        "Get the team in a given position of a group."

        if 0 <= pos < 4:
            return self.get_group(group)[pos]
        raise ValueError(f"Position {pos} must be between 0, 1 , 2 or 3.")
    
    def get_octavos_matches(self) -> List[Tuple[str, str]]:
        "Get the matches of the octavos."

        return [
            (
                self.get_group_team(
                    group=match[0]["group"],
                    pos=match[0]["pos"]
                ),
                self.get_group_team(
                    group=match[1]["group"],
                    pos=match[1]["pos"]
                )
            )
            for match in self.progression.octavos
        ]
    
    def get_octavos_winners(self) -> List[str]:
        "Get the winning teams of octavos."

        return [
            match[res]
            for match, res in zip(self.get_octavos_matches(), self.result.octavos)
        ]

    def get_quarter_matches(self) -> List[Tuple[str, str]]:
        "Get the matches of the quarter finals."

        return [
            (
                self.get_octavos_winners()[match[0]],
                self.get_octavos_winners()[match[1]],
            )
            for match in self.progression.quarter
        ]
    
    def get_quarter_winners(self) -> List[str]:
        "Get the winning teams of the quarter final."

        return [
            match[res]
            for match, res in zip(self.get_quarter_matches(), self.result.quarter)
        ]
    
    def get_semi_matches(self) -> List[Tuple[str, str]]:
        "Get the matches of the semi finals."

        return [
            (
                self.get_quarter_winners()[match[0]],
                self.get_quarter_winners()[match[1]],
            )
            for match in self.progression.semi
        ]
    
    def get_semi_winners(self) -> List[str]:
        "Get the winning teams of the semi final."

        return [
            match[res]
            for match, res in zip(self.get_semi_matches(), self.result.semi)
        ]
    
    def get_semi_losers(self) -> List[str]:
        "Get the losing teams of the semi final."

        return [
            match[abs(res - 1)]
            for match, res in zip(self.get_semi_matches(), self.result.semi)
        ]
    
    def get_final_matches(self) -> List[Tuple[str, str]]:
        "Get the matches of the final and thirds match."

        return [
            (
                self.get_semi_winners()[self.progression.final[0][0]],
                self.get_semi_winners()[self.progression.final[0][1]]
            ),
            (
                self.get_semi_losers()[self.progression.final[1][0]],
                self.get_semi_losers()[self.progression.final[1][1]]
            )
        ]
    
    def get_final_winners(self) -> List[str]:
        "Get the winning teams of the final and third match."

        return [
            match[res]
            for match, res in zip(self.get_final_matches(), self.result.final)
        ]
    
    def get_winner(self) -> List[str]:
        "Get the winning team of the tournament."

        return self.get_final_winners()[0]

    def get_third(self) -> List[str]:
        "Get the third team of the tournament."

        return self.get_final_winners()[1]
