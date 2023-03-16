"Probabilities for teams final outcome."

from typing import TypedDict

class TeamProb(TypedDict):
    "Probabilities for a to a team to reach a stage."
    first: float
    second: float
    third: float
    fourth: float
    Q: float
    S: float
    F: float
    W: float


################ GROUP A ###############################################################

NETHERLANDS = TeamProb({
    "first": 65.43,
    "second": 22.07,
    "third": 9.17,
    "fourth": 3.33,
    "Q": 54.19,
    "S": 27.68,
    "F": 13.68,
    "W": 7.02,
})


SENEGAL = TeamProb({
    "first": 15.16,
    "second": 30.79,
    "third": 30.24,
    "fourth": 23.81,
    "Q": 19.24,
    "S": 7.16,
    "F": 2.58,
    "W": 0.91,
})


ECUADOR = TeamProb({
    "first": 13.46,
    "second": 29.16,
    "third": 30.83,
    "fourth": 26.55,
    "Q": 16.73,
    "S": 5.48,
    "F": 1.67,
    "W": 0.51,
})


QATAR = TeamProb({
    "first": 5.94,
    "second": 17.99,
    "third": 29.76,
    "fourth": 46.31,
    "Q": 8.76,
    "S": 2.64,
    "F": 0.85,
    "W": 0.28,
})


################ GROUP B ###############################################################

ENGLAND = TeamProb({
    "first": 64.2,
    "second": 22.24,
    "third": 9.75,
    "fourth": 3.81,
    "Q": 56.53,
    "S": 31.35,
    "F": 17.42,
    "W": 9.08,
})


USA = TeamProb({
    "first": 15.86,
    "second": 31.48,
    "third": 29.38,
    "fourth": 23.28,
    "Q": 19.25,
    "S": 6.55,
    "F": 2.2,
    "W": 0.75,
})


WALES = TeamProb({
    "first": 13.41,
    "second": 28.35,
    "third": 31.29,
    "fourth": 26.95,
    "Q": 17.0,
    "S": 5.8,
    "F": 1.93,
    "W": 0.53,
})


IRAN = TeamProb({
    "first": 6.53,
    "second": 17.94,
    "third": 29.58,
    "fourth": 45.95,
    "Q": 8.29,
    "S": 2.27,
    "F": 0.66,
    "W": 0.16,
})


################ GROUP C ###############################################################

ARGENTINA = TeamProb({
    "first": 65.7,
    "second": 22.84,
    "third": 9.01,
    "fourth": 2.45,
    "Q": 56.76,
    "S": 37.44,
    "F": 22.19,
    "W": 13.29,
})


MEXICO = TeamProb({
    "first": 14.19,
    "second": 32.84,
    "third": 34.88,
    "fourth": 18.09,
    "Q": 16.87,
    "S": 6.96,
    "F": 2.28,
    "W": 0.73,
})


POLAND = TeamProb({
    "first": 17.48,
    "second": 34.74,
    "third": 32.4,
    "fourth": 15.38,
    "Q": 18.15,
    "S": 6.98,
    "F": 2.53,
    "W": 0.72,
})


SAUDI_ARABIA = TeamProb({
    "first": 2.63,
    "second": 9.58,
    "third": 23.72,
    "fourth": 64.07,
    "Q": 2.98,
    "S": 0.86,
    "F": 0.18,
    "W": 0.04,
})


################ GROUP D ###############################################################

FRANCE = TeamProb({
    "first": 58.4,
    "second": 30.38,
    "third": 8.61,
    "fourth": 2.61,
    "Q": 57.04,
    "S": 36.56,
    "F": 21.52,
    "W": 11.77,
})


DENMARK = TeamProb({
    "first": 34.66,
    "second": 45.79,
    "third": 14.77,
    "fourth": 4.78,
    "Q": 38.98,
    "S": 19.15,
    "F": 8.51,
    "W": 3.47,
})


AUSTRALIA = TeamProb({
    "first": 2.92,
    "second": 10.33,
    "third": 37.38,
    "fourth": 49.37,
    "Q": 3.91,
    "S": 1.33,
    "F": 0.36,
    "W": 0.1,
})


TUNISIA = TeamProb({
    "first": 4.02,
    "second": 13.5,
    "third": 39.24,
    "fourth": 43.24,
    "Q": 5.32,
    "S": 1.8,
    "F": 0.48,
    "W": 0.16,
})


################ GROUP E ###############################################################

SPAIN = TeamProb({
    "first": 52.00,
    "second": 33.94,
    "third": 11.66,
    "fourth": 2.4,
    "Q": 54.13,
    "S": 30.52,
    "F": 16.34,
    "W": 8.65,
})


GERMANY = TeamProb({
    "first": 39.42,
    "second": 39.87,
    "third": 15.92,
    "fourth": 4.79,
    "Q": 48.69,
    "S": 27.16,
    "F": 14.8,
    "W": 7.31,
})


JAPAN = TeamProb({
    "first": 7.14,
    "second": 19.71,
    "third": 48.6,
    "fourth": 24.55,
    "Q": 9.6,
    "S": 3.41,
    "F": 1.16,
    "W": 0.33,
})


COSTA_RICA = TeamProb({
    "first": 1.44,
    "second": 6.49,
    "third": 23.81,
    "fourth": 68.26,
    "Q": 2.3,
    "S": 0.67,
    "F": 0.14,
    "W": 0.02,
})


################ GROUP F ###############################################################

BELGIUM = TeamProb({
    "first": 51.25,
    "second": 27.16,
    "third": 14.77,
    "fourth": 6.82,
    "Q": 39.85,
    "S": 21.59,
    "F": 10.88,
    "W": 5.03,
})


CROATIA = TeamProb({
    "first": 29.02,
    "second": 33.76,
    "third": 23.14,
    "fourth": 14.08,
    "Q": 26.26,
    "S": 11.41,
    "F": 4.76,
    "W": 1.9,
})


MOROCCO = TeamProb({
    "first": 11.79,
    "second": 21.5,
    "third": 32.3,
    "fourth": 34.41,
    "Q": 10.4,
    "S": 3.63,
    "F": 1.24,
    "W": 0.36,
})


CANADA = TeamProb({
    "first": 7.93,
    "second": 17.58,
    "third": 29.79,
    "fourth": 44.7,
    "Q": 8.77,
    "S": 3.33,
    "F": 1.27,
    "W": 0.44,
})


################ GROUP G ###############################################################

BRAZIL = TeamProb({
    "first": 69.5,
    "second": 20.78,
    "third": 7.64,
    "fourth": 2.08,
    "Q": 65.38,
    "S": 41.82,
    "F": 26.68,
    "W": 16.79,
})


SWITZERLAND = TeamProb({
    "first": 14.47,
    "second": 34.62,
    "third": 32.64,
    "fourth": 18.27,
    "Q": 21.66,
    "S": 8.27,
    "F": 3.05,
    "W": 1.0,
})


SERBIA = TeamProb({
    "first": 13.06,
    "second": 31.94,
    "third": 33.15,
    "fourth": 21.85,
    "Q": 20.31,
    "S": 7.84,
    "F": 2.79,
    "W": 0.99,
})


CAMEROON = TeamProb({
    "first": 2.97,
    "second": 12.66,
    "third": 26.57,
    "fourth": 57.8,
    "Q": 5.59,
    "S": 1.75,
    "F": 0.5,
    "W": 0.16,
})


################ GROUP H ###############################################################

PORTUGAL = TeamProb({
    "first": 54.7,
    "second": 27.18,
    "third": 12.56,
    "fourth": 5.56,
    "Q": 44.45,
    "S": 22.72,
    "F": 11.46,
    "W": 5.35,
})


URUGUAY = TeamProb({
    "first": 28.61,
    "second": 35.62,
    "third": 22.77,
    "fourth": 13.00,
    "Q": 26.91,
    "S": 11.04,
    "F": 4.4,
    "W": 1.7,
})


SOUTH_KOREA = TeamProb({
    "first": 8.97,
    "second": 19.13,
    "third": 32.57,
    "fourth": 39.33,
    "Q": 8.1,
    "S": 2.4,
    "F": 0.74,
    "W": 0.21,
})


GHANA = TeamProb({
    "first": 7.72,
    "second": 18.07,
    "third": 32.1,
    "fourth": 42.11,
    "Q": 7.61,
    "S": 2.45,
    "F": 0.76,
    "W": 0.22,
})

ALL_TEAMS = [
    BRAZIL,
    ARGENTINA,
    FRANCE,
    ENGLAND,
    SPAIN,
    GERMANY,
    NETHERLANDS,
    PORTUGAL,
    BELGIUM,
    DENMARK,
    CROATIA,
    URUGUAY,
    SWITZERLAND,
    SERBIA,
    SENEGAL,
    USA,
    MEXICO,
    POLAND,
    WALES,
    ECUADOR,
    CANADA,
    MOROCCO,
    JAPAN,
    QATAR,
    GHANA,
    SOUTH_KOREA,
    IRAN,
    TUNISIA,
    CAMEROON,
    AUSTRALIA,
    SAUDI_ARABIA,
    COSTA_RICA,
]

__all__ = [
    "BRAZIL",
    "ARGENTINA",
    "FRANCE",
    "ENGLAND",
    "SPAIN",
    "GERMANY",
    "NETHERLANDS",
    "PORTUGAL",
    "BELGIUM",
    "DENMARK",
    "CROATIA",
    "URUGUAY",
    "SWITZERLAND",
    "SERBIA",
    "SENEGAL",
    "USA",
    "MEXICO",
    "POLAND",
    "WALES",
    "ECUADOR",
    "CANADA",
    "MOROCCO",
    "JAPAN",
    "QATAR",
    "GHANA",
    "SOUTH_KOREA",
    "IRAN",
    "TUNISIA",
    "CAMEROON",
    "AUSTRALIA",
    "SAUDI_ARABIA",
    "COSTA_RICA",
    "ALL_TEAMS",
]