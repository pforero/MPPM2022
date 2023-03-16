"Calculate the conditional probabilities of knock out stages."

import numpy as np

from mppm.optimization.probabilities.group_probabilities import GroupProbabilities, TeamProb

from itertools import product
from scipy.optimize import minimize

PROD = [match for match in product(range(0,4), range(0,4), range(0,2))]
OCT= len(PROD)

class OctavoProbabilities:
    "Probabilities of a team passing Octavos against another team."

    def __init__(self, group1: GroupProbabilities, group2: GroupProbabilities) -> None:
        self.group1 = group1
        self.group2 = group2
    
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
                (
                    self.group1[match[0]]["first"] / 100
                    * self.group2[match[1]]["second"] / 100
                ) + (
                    self.group1[match[0]]["second"] / 100
                    * self.group2[match[1]]["first"] / 100
                )
                for match in PROD
            ]
        )

        return prob
    
    def _get_win_probabilities(self) -> np.array:
        "Get the probabilities of each team reaching octavos and winning."

        return np.array(
            [self.group1[i]["Q"]/100 for i in range(4)]
            + [self.group2[i]["Q"]/100 for i in range(4)]
        )

    def _get_lose_probabilities(self) -> np.array:
        "Get the probabilities of each team reaching octavos and losing."

        return np.array(
            [
                (
                    self.group1[i]["first"]
                    + self.group1[i]["second"]
                    - self.group1[i]["Q"]
                )/100
                for i in range(4)
            ]
            + [
                (
                    self.group2[i]["first"]
                    + self.group2[i]["second"]
                    - self.group2[i]["Q"]
                )/100
                for i in range(4)
            ]
        )

    def _minimize(self) -> np.array:
        "Minimization of probabilities."

        res = minimize(
            octavo_obj_function,
            [0.5]*OCT,
            args=(
                self._get_starting_probabilities(),
                self._get_win_probabilities(),
                self._get_lose_probabilities()
            ),
            method='SLSQP',
            bounds=[(0, 1)]*OCT,
            constraints=({"type": "eq", "fun": individual_match_constraint})
        )

        return res

    def __getitem__(self, key: int) -> TeamProb:
        if key == 0:
            return self.group1.team1
        if key == 1:
            return self.group1.team2
        if key == 2:
            return self.group1.team3
        if key == 3:
            return self.group1.team4
        if key == 4:
            return self.group2.team1
        if key == 5:
            return self.group2.team2
        if key == 6:
            return self.group2.team3
        if key == 7:
            return self.group2.team4

        raise KeyError ()


IND_MATCH = np.array(
    [
        [1 if (i == (x*2)) or (i-1 == (x*2)) else 0 for i in range(OCT)]
        for x in range(int(OCT/2))
    ]
)

def individual_match_constraint(outcome_prob: np.array) -> float:
    "Make sure that the probabilities of winning or losing the same match add to one."
    diff = np.dot(IND_MATCH, outcome_prob) - np.array([1] * int(OCT/2))
    return np.dot(diff, diff)

WIN = np.array(
    [
        [1 if (match[0] == 0) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[0] == 1) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[0] == 2) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[0] == 3) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 0) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 1) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 2) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 3) and (match[2] == 1) else 0 for match in PROD],
    ]
)

LOSE = np.array(
    [
        [1 if (match[0] == 0) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[0] == 1) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[0] == 2) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[0] == 3) and (match[2] == 1) else 0 for match in PROD],
        [1 if (match[1] == 0) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 1) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 2) and (match[2] == 0) else 0 for match in PROD],
        [1 if (match[1] == 3) and (match[2] == 0) else 0 for match in PROD],
    ]
)

def octavo_obj_function(outcome_prob: np.array, match_prob: np.array, win_prob: np.array, lose_prob: np.array) -> float:
    "Objective function for the octavo probabilities compared to final outcome."

    group_matrix = np.concatenate(
        (np.multiply(WIN, match_prob), np.multiply(LOSE, match_prob))
    )

    position_prob = np.concatenate((win_prob, lose_prob))

    diff = np.dot(group_matrix ,outcome_prob) - position_prob
    return np.dot(diff, diff)
