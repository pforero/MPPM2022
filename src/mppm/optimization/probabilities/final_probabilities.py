"Calculate the conditional probabilities of quarter finals."

import numpy as np

from mppm.optimization.probabilities.semi_probabilities import SemiProbabilities, TeamProb

from itertools import combinations, product
from scipy.optimize import minimize

PROD = [x for x in product(combinations(range(0, 32), 2), range(0, 2))]
FIN = len(PROD)

class FinalProbabilities:
    "Probabilities of a team passing the final against another team."

    def __init__(self, semi: SemiProbabilities) -> None:
        self.semi = semi

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
        
        starting_final_prob = self._minimize_start().x
        prob_with_matches = {
            match: starting_final_prob[i]
            for i, match in enumerate(combinations(range(0, 32), 2))
        }

        prob = np.array(
            [prob_with_matches[match[0]] for match in PROD]
        )

        return prob
        
    
    def _get_win_probabilities(self) -> np.array:
        "Get the probabilities of each team reaching the final and winning."

        return np.array([self.semi[i]["W"]/100 for i in range(32)])

    def _get_lose_probabilities(self) -> np.array:
        "Get the probabilities of each team reaching the final and losing."

        return np.array(
            [
                (self.semi[i]["F"] - self.semi[i]["W"])/100
                for i in range(32)
            ]
        )

    def _minimize_start(self) -> np.array:
        "Minimization of starting probabilities."

        res = minimize(
            final_start_obj_function,
            [0.5]*TEAM_IN_MATCH.shape[1],
            args=[self.semi[i]["F"]/100 for i in range(32)],
            method='SLSQP',
            bounds=[(0, 1)]*TEAM_IN_MATCH.shape[1],
            constraints=({"type": "eq", "fun": final_constraint})
        )

        return res

    def _minimize(self) -> np.array:
        "Minimization of probabilities."

        res = minimize(
            final_obj_function,
            [0.5]*FIN,
            args=(
                self._get_starting_probabilities(),
                self._get_win_probabilities(),
                self._get_lose_probabilities()
            ),
            method='SLSQP',
            bounds=[(0, 1)]*FIN,
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


TEAM_IN_MATCH = np.array(
    [
        [1 if i in match else 0 for match in combinations(range(0, 32), 2)]
        for i in range(32)
    ]
)


def final_constraint(match_prob: np.array) -> float:
    "The starting probability of all finals must be one."
    return match_prob.sum() - 1


def final_start_obj_function(match_prob: np.array, final_probability: np.array) -> float:
    "Objective function the starting probabilities of the final."
    diff = np.dot(TEAM_IN_MATCH ,match_prob) - final_probability
    return np.dot(diff, diff)


IND_MATCH = np.array(
    [
        [1 if (i == (x*2)) or (i-1 == (x*2)) else 0 for i in range(FIN)]
        for x in range(int(FIN/2))
    ]
)

def individual_match_constraint(outcome_prob: np.array) -> float:
    "Make sure that the probabilities of winning or losing the same match add to one."
    diff = np.dot(IND_MATCH, outcome_prob) - np.array([1] * int(FIN/2))
    return np.dot(diff, diff)

WIN = np.array(
    [
        [1 if match[0][match[1]] == i else 0 for match in PROD]
        for i in range(32)
    ]
)

LOSE = np.array(
    [
        [1 if match[0][abs(match[1]-1)] == i else 0 for match in PROD]
        for i in range(32)
    ]
)

def final_obj_function(outcome_prob: np.array, match_prob: np.array, win_prob: np.array, lose_prob: np.array) -> float:
    "Objective function for the final probabilities compared to final outcome."

    group_matrix = np.concatenate(
        (np.multiply(WIN, match_prob), np.multiply(LOSE, match_prob))
    )

    position_prob = np.concatenate((win_prob, lose_prob))

    diff = np.dot(group_matrix ,outcome_prob) - position_prob
    return np.dot(diff, diff)
