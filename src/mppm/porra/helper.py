"Helper objects for the Porra."

from typing import TypedDict


GROUPS = ["A", "B" , "C", "D", "E", "F", "G", "H"]

class PorraGroups(TypedDict):
    """Dictionary with group names and bets of the Porra."""
    A: list
    B: list
    C: list
    D: list
    E: list
    F: list
    G: list
    H: list