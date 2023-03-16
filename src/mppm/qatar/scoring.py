"Scoring structure for Qatar."

from mppm.porra.scoring import Scoring

GROUP_SCORE = [10, 6, 6, 6]

GROUPS = {
    "A": GROUP_SCORE,
    "B": GROUP_SCORE,
    "C": GROUP_SCORE,
    "D": GROUP_SCORE,
    "E": GROUP_SCORE,
    "F": GROUP_SCORE,
    "G": GROUP_SCORE,
    "H": GROUP_SCORE,
}

OCTAVOS = [15] * 8
QUARTER = [20] * 4
SEMI = [30] * 2
FINAL = [40, 10]

QatarScoring = Scoring(
    groups=GROUPS,
    octavos=OCTAVOS,
    quarter=QUARTER,
    semi=SEMI,
    final=FINAL
)
