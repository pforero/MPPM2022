"Calculate the conditional probabilities of quarter finals."

import numpy as np

from mppm.optimization.probabilities.octavo_probabilities import OctavoProbabilities, TeamProb

from itertools import product
from scipy.optimize import minimize

PROD = [match for match in product(range(0,8), range(0,8), range(0,2))]
QUART = len(PROD)

class QuarterProbabilities:
    "Probabilities of a team passing quarter final against another team."

    def __init__(self, oct1: OctavoProbabilities, oct2: OctavoProbabilities) -> None:
        self.oct1 = oct1
        self.oct2 = oct2
    
    def get_probabilities(self) -> dict:
        "Get the probabilities of occurring each possible outcome."
        
        match_prob = self._minimize().x
        final_prob = np.multiply(match_prob, self._get_starting_probabilities())

        prob = {match: final_prob[i] for i, match in enumerate(PROD)}

        return prob

    def get_cond_prob(self) -> dict:
        "Get the each team winning a match."
        
        match_prob = self._minimize().x

        prob = {match: match_prob[i] for i, match in enumerate(PROD)}

        return prob

    def _get_starting_probabilities(self) -> np.array:
        "Get the probabilities of each match occurring to start with."
        
        prob = np.array(
            [
                (self.oct1[match[0]]["Q"] * self.oct2[match[1]]["Q"])/20000
                for match in PROD
            ]
        )

        return prob
    
    def _get_win_probabilities(self) -> np.array:
        "Get the probabilities of each team reaching quarter final and winning."

        return np.array(
            [self.oct1[i]["S"]/100 for i in range(8)]
            + [self.oct2[i]["S"]/100 for i in range(8)]
        )

    def _get_lose_probabilities(self) -> np.array:
        "Get the probabilities of each team reaching quarter final and losing."

        return np.array(
            [
                (self.oct1[i]["Q"] - self.oct1[i]["S"])/100
                for i in range(8)
            ]
            + [
                (self.oct2[i]["Q"] - self.oct2[i]["S"])/100
                for i in range(8)
            ]
        )

    def _minimize(self) -> np.array:
        "Minimization of probabilities."

        res = minimize(
            quarter_obj_function,
            [0.5]*QUART,
            args=(
                self._get_starting_probabilities(),
                self._get_win_probabilities(),
                self._get_lose_probabilities()
            ),
            method='SLSQP',
            bounds=[(0, 1)]*QUART,
            constraints=({"type": "eq", "fun": individual_match_constraint})
        )

        return res

    def __getitem__(self, key: int) -> TeamProb:
        if key == 0:
            return self.oct1.group1.team1
        if key == 1:
            return self.oct1.group1.team2
        if key == 2:
            return self.oct1.group1.team3
        if key == 3:
            return self.oct1.group1.team4
        if key == 4:
            return self.oct1.group2.team1
        if key == 5:
            return self.oct1.group2.team2
        if key == 6:
            return self.oct1.group2.team3
        if key == 7:
            return self.oct1.group2.team4
        if key == 8:
            return self.oct2.group1.team1
        if key == 9:
            return self.oct2.group1.team2
        if key == 10:
            return self.oct2.group1.team3
        if key == 11:
            return self.oct2.group1.team4
        if key == 12:
            return self.oct2.group2.team1
        if key == 13:
            return self.oct2.group2.team2
        if key == 14:
            return self.oct2.group2.team3
        if key == 15:
            return self.oct2.group2.team4

        raise KeyError ()


IND_MATCH = np.array(
    [
        [1 if (i == (x*2)) or (i-1 == (x*2)) else 0 for i in range(QUART)]
        for x in range(int(QUART/2))
    ]
)

def individual_match_constraint(outcome_prob: np.array) -> float:
    "Make sure that the probabilities of winning or losing the same match add to one."
    diff = np.dot(IND_MATCH, outcome_prob) - np.array([1] * int(QUART/2))
    return np.dot(diff, diff)

WIN = np.array(
    [
        [1 if (match[0] == 0) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[0] == 1) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[0] == 2) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[0] == 3) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[0] == 4) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[0] == 5) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[0] == 6) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[0] == 7) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 0) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 1) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 2) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 3) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 4) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 5) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 6) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 7) and (match[2] == 1) else 0 for match in PROD],
    ]
)

LOSE = np.array(
    [
        [1 if (match[0] == 0) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[0] == 1) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[0] == 2) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[0] == 3) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[0] == 4) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[0] == 5) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[0] == 6) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[0] == 7) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 0) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 1) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 2) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 3) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 4) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 5) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 6) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 7) and (match[2] == 0) else 0 for match in PROD],
    ]
)

def quarter_obj_function(outcome_prob: np.array, match_prob: np.array, win_prob: np.array, lose_prob: np.array) -> float:
    "Objective function for the quarter probabilities compared to final outcome."

    group_matrix = np.concatenate(
        (np.multiply(WIN, match_prob), np.multiply(LOSE, match_prob))
    )

    position_prob = np.concatenate((win_prob, lose_prob))

    diff = np.dot(group_matrix ,outcome_prob) - position_prob
    return np.dot(diff, diff)
