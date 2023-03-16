"Calculate the conditional probabilities of quarter finals."

import numpy as np

from mppm.optimization.probabilities.quarter_probabilities import QuarterProbabilities, TeamProb

from itertools import product
from scipy.optimize import minimize

PROD = [match for match in product(range(0,16), range(0,16), range(0,2))]
SEMI = len(PROD)

class SemiProbabilities:
    "Probabilities of a team passing semi final against another team."

    def __init__(self, quart1: QuarterProbabilities, quart2: QuarterProbabilities) -> None:
        self.quart1 = quart1
        self.quart2 = quart2
    
    def get_probabilities(self, ind: bool = True) -> dict:
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
                (self.quart1[match[0]]["S"] * self.quart2[match[1]]["S"])/20000
                for match in PROD
            ]
        )

        return prob
    
    def _get_win_probabilities(self) -> np.array:
        "Get the probabilities of each team reaching semifinal and winning."

        return np.array(
            [self.quart1[i]["F"]/100 for i in range(16)]
            + [self.quart2[i]["F"]/100 for i in range(16)]
        )

    def _get_lose_probabilities(self) -> np.array:
        "Get the probabilities of each team reaching semifinal and losing."

        return np.array(
            [
                (self.quart1[i]["S"] - self.quart1[i]["F"])/100
                for i in range(16)
            ]
            + [
                (self.quart2[i]["S"] - self.quart2[i]["F"])/100
                for i in range(16)
            ]
        )

    def _minimize(self) -> np.array:
        "Minimization of probabilities."

        res = minimize(
            semi_obj_function,
            [0.5]*SEMI,
            args=(
                self._get_starting_probabilities(),
                self._get_win_probabilities(),
                self._get_lose_probabilities()
            ),
            method='SLSQP',
            bounds=[(0, 1)]*SEMI,
            constraints=({"type": "eq", "fun": individual_match_constraint})
        )

        return res

    def __getitem__(self, key: int) -> TeamProb:
        if key == 0:
            return self.quart1.oct1.group1.team1
        if key == 1:
            return self.quart1.oct1.group1.team2
        if key == 2:
            return self.quart1.oct1.group1.team3
        if key == 3:
            return self.quart1.oct1.group1.team4
        if key == 4:
            return self.quart1.oct1.group2.team1
        if key == 5:
            return self.quart1.oct1.group2.team2
        if key == 6:
            return self.quart1.oct1.group2.team3
        if key == 7:
            return self.quart1.oct1.group2.team4
        if key == 8:
            return self.quart1.oct2.group1.team1
        if key == 9:
            return self.quart1.oct2.group1.team2
        if key == 10:
            return self.quart1.oct2.group1.team3
        if key == 11:
            return self.quart1.oct2.group1.team4
        if key == 12:
            return self.quart1.oct2.group2.team1
        if key == 13:
            return self.quart1.oct2.group2.team2
        if key == 14:
            return self.quart1.oct2.group2.team3
        if key == 15:
            return self.quart1.oct2.group2.team4
        if key == 16:
            return self.quart2.oct1.group1.team1
        if key == 17:
            return self.quart2.oct1.group1.team2
        if key == 18:
            return self.quart2.oct1.group1.team3
        if key == 19:
            return self.quart2.oct1.group1.team4
        if key == 20:
            return self.quart2.oct1.group2.team1
        if key == 21:
            return self.quart2.oct1.group2.team2
        if key == 22:
            return self.quart2.oct1.group2.team3
        if key == 23:
            return self.quart2.oct1.group2.team4
        if key == 24:
            return self.quart2.oct2.group1.team1
        if key == 25:
            return self.quart2.oct2.group1.team2
        if key == 26:
            return self.quart2.oct2.group1.team3
        if key == 27:
            return self.quart2.oct2.group1.team4
        if key == 28:
            return self.quart2.oct2.group2.team1
        if key == 29:
            return self.quart2.oct2.group2.team2
        if key == 30:
            return self.quart2.oct2.group2.team3
        if key == 31:
            return self.quart2.oct2.group2.team4

        raise KeyError ()


IND_MATCH = np.array(
    [
        [1 if (i == (x*2)) or (i-1 == (x*2)) else 0 for i in range(SEMI)]
        for x in range(int(SEMI/2))
    ]
)

def individual_match_constraint(outcome_prob: np.array) -> float:
    "Make sure that the probabilities of winning or losing the same match add to one."
    diff = np.dot(IND_MATCH, outcome_prob) - np.array([1] * int(SEMI/2))
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
        [1 if (match[0] == 8) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[0] == 9) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[0] == 10) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[0] == 11) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[0] == 12) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[0] == 13) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[0] == 14) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[0] == 15) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 0) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 1) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 2) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 3) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 4) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 5) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 6) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 7) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 8) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 9) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 10) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 11) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 12) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 13) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 14) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 15) and (match[2] == 1) else 0 for match in PROD],
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
        [1 if (match[0] == 8) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[0] == 9) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[0] == 10) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[0] == 11) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[0] == 12) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[0] == 13) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[0] == 14) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[0] == 15) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 0) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 1) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 2) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 3) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 4) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 5) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 6) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 7) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 8) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 9) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 10) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 11) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 12) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 13) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 14) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 15) and (match[2] == 0) else 0 for match in PROD],
    ]
)

def semi_obj_function(outcome_prob: np.array, match_prob: np.array, win_prob: np.array, lose_prob: np.array) -> float:
    "Objective function for the semi probabilities compared to final outcome."

    group_matrix = np.concatenate(
        (np.multiply(WIN, match_prob), np.multiply(LOSE, match_prob))
    )

    position_prob = np.concatenate((win_prob, lose_prob))

    diff = np.dot(group_matrix ,outcome_prob) - position_prob
    return np.dot(diff, diff)
