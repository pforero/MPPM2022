"Scoring points of a Porra."

from mppm.porra.helper import PorraGroups

from typing import Dict, List

class Scoring:
    """Scoring structure.

    The points awarded for correctly guessing each stage of a Porra.

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
        groups: Dict[str, int],
        octavos: List[int],
        quarter: List[int],
        semi: List[int],
        final: List[int]
    ) -> None:

        self._groups =  groups
        self._octavos = octavos
        self._quarter = quarter
        self._semi = semi
        self._final = final

    @property
    def groups(self) -> PorraGroups:
        return self._groups
    
    @groups.setter
    def groups(self, value: Dict[str, int]) -> None:
        self._groups = PorraGroups(value)

    @property
    def octavos(self) -> list:
        return self._octavos
    
    @octavos.setter
    def octavos(self, value: list) -> None:

        if len(value) != 8:
            raise ValueError(f"Octavos must have eight matches.")
        self._octavos = value
    
    @property
    def quarter(self) -> list:
        return self._quarter
    
    @quarter.setter
    def quarter(self, value: list) -> None:

        if len(value) != 4:
            raise ValueError(f"Quarter must have four matches.")
        self._quarter = value

    @property
    def semi(self) -> list:
        return self._semi
    
    @semi.setter
    def semi(self, value: list) -> None:

        if len(value) != 2:
            raise ValueError(f"Semi final must have two matches.")
        self._semi = value

    @property
    def final(self) -> list:
        return self._final
    
    @final.setter
    def final(self, value: list) -> None:

        if len(value) != 2:
            raise ValueError(f"Final final must have two matches.")
        self._final = value

    def __repr__(self) -> str:
        pass