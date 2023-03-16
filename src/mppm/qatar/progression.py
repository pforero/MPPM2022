"""Progression structure for Qatar."""

from mppm.porra.progression import Progression

GROUP_A = [
    "Qatar",
    "Ecuador",
    "Senegal",
    "Netherlands"
]

GROUP_B = [
    "England",
    "Iran",
    "USA",
    "Wales"
]

GROUP_C = [
    "Argentina",
    "Saudi Arabia",
    "Mexico",
    "Poland"
]

GROUP_D = [
    "France",
    "Denmark",
    "Tunisia",
    "Australia"
]

GROUP_E = [
    "Spain",
    "Germany",
    "Japan",
    "Costa Rica"
]

GROUP_F = [
    "Belgium",
    "Canada",
    "Morocco",
    "Croatia"
]

GROUP_G = [
    "Brazil",
    "Serbia",
    "Switzerland",
    "Cameroon"
]

GROUP_H = [
    "Portugal",
    "Ghana",
    "Uruguay",
    "South Korea"
]

GROUPS = {
    "A": GROUP_A,
    "B": GROUP_B,
    "C": GROUP_C,
    "D": GROUP_D,
    "E": GROUP_E,
    "F": GROUP_F,
    "G": GROUP_G,
    "H": GROUP_H,
}

OCTAVOS = [
    ({"group": "A", "pos": 0}, {"group": "B", "pos": 1}),
    ({"group": "C", "pos": 0}, {"group": "D", "pos": 1}),
    ({"group": "D", "pos": 0}, {"group": "C", "pos": 1}),
    ({"group": "B", "pos": 0}, {"group": "A", "pos": 1}),
    ({"group": "E", "pos": 0}, {"group": "F", "pos": 1}),
    ({"group": "G", "pos": 0}, {"group": "H", "pos": 1}),
    ({"group": "F", "pos": 0}, {"group": "E", "pos": 1}),
    ({"group": "H", "pos": 0}, {"group": "G", "pos": 1}),
]

QUARTER = [
    (0, 1),
    (4, 5),
    (3, 2),
    (6, 7),
]

SEMI = [
    (0, 1),
    (2, 3)
]

FINAL = [
    (0, 1),
    (0, 1),
]

QatarProgression = Progression(
    groups=GROUPS,
    octavos=OCTAVOS,
    quarter=QUARTER,
    semi=SEMI,
    final=FINAL
)
