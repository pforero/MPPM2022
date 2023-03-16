"A Porra Result."

from mppm.porra.helper import PorraGroups

from typing import Dict, List

class Result:
    """A Porra results.

    A Result is an outcome of the porra that focuses only on the group winners and
    stage progression.

    The Porra consists of 8 groups of 4 teams, and the Porra must correctly predict
    the final position of each team.

    Given the final classification of each group a draw is determined, and the porra
    must correctly bet the progression of each team through the draw.

    Attributes
    ----------
    groups: PorraGroups
    octavos: List of int of len 8
    quarter: List of int of len 4
    semi: List of int of len 2
    final: List of int of len 2
    """

    def __init__(
        self,
        groups: Dict[str, List[int]],
        octavos: List[int],
        quarter: List[int],
        semi: List[int],
        final: List[int]
    ) -> None:

        self.groups =  groups
        self.octavos = octavos
        self.quarter = quarter
        self.semi = semi
        self.final = final
