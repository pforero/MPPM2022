"""Progression structure for a Porra."""

from mppm.porra.helper import PorraGroups, GROUPS

from typing import Dict, List, Tuple, TypedDict


class GroupProgression(TypedDict):
    """Identifies the group and position that progresses."""
    group: str
    pos: int


class Progression:
    """The progression structure.

    Includes the teams in each group and the progression for each knock out stage.
    
    Attributes
    ----------
    groups: PorraGroups
    octavos: List of tuples of GroupProgression
    quarter: List of tuples
    semi: List of tuples
    final: List of tuples
    """

    def __init__(
        self,
        groups: Dict[str, List[str]],
        octavos: List[Tuple[dict, dict]],
        quarter: List[Tuple[int, int]],
        semi: List[Tuple[int, int]],
        final: List[Tuple[int, int]]
    ) -> None:
        
        self.groups = groups
        self.octavos = octavos
        self.quarter = quarter
        self.semi = semi
        self.final = final

    @property
    def groups(self) -> PorraGroups:
        return self._groups
    
    @groups.setter
    def groups(self, value: Dict[str, List[str]]) -> None:

        for group, teams in value.items():
            if group not in GROUPS:
                raise ValueError(f"Group {group} is not an acceptable group.")
            if len(teams) != 4:
                raise ValueError(f"Group {group} must have four teams.")

        self._groups = PorraGroups(value)

    @property
    def octavos(self) -> list:
        return self._octavos
    
    @octavos.setter
    def octavos(self, value: List[Tuple[Dict[str, int]]]) -> None:

        if len(value) != 8:
            raise ValueError(f"Octavos must have eight matches.")

        octavos = []
        for match in value:
            octavos.append((GroupProgression(match[0]), GroupProgression(match[1])))

        self._octavos = octavos
    
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
