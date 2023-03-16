"Calculate the probabilities of a group outcome given the team odds."

import numpy as np

from mppm.optimization.probabilities.team_prob import TeamProb

from scipy.optimize import minimize

from itertools import permutations


GROUP_POS = ["first", "second", "third", "fourth"]


class GroupProbabilities:
    """Probabilities of team final position.

    We use the odds and normalize them by team and position to calculate probabilities.
    
    Attributes
    ----------
    team1: TeamProb
    team2: TeamProb
    team3: TeamProb
    team4: TeamProb
    """

    def __init__(
        self,
        team1: TeamProb,
        team2: TeamProb,
        team3: TeamProb,
        team4: TeamProb
    ) -> None:
        self.team1 = team1
        self.team2 = team2
        self.team3 = team3
        self.team4 = team4
    

    def group_probabilities(self) -> None:
        "Obtains the probability of each possible group outcome."

        pos_prob = np.array(
            [team[pos]/100 for pos in GROUP_POS for team in [
                self.team1, self.team2, self.team3, self.team4
                ]
            ]
        )

        res = minimize(
            group_obj_function,
            [1/24]*24,
            args=(pos_prob),
            method='SLSQP',
            bounds=[(0, 1)]*24
        )

        return {perm: res.x[i] for i, perm in enumerate(permutations(np.arange(0, 4)))}

    def __getitem__(self, key: int) -> TeamProb:
        if key == 0:
            return self.team1
        if key == 1:
            return self.team2
        if key == 2:
            return self.team3
        if key == 3:
            return self.team4
        
        raise KeyError ()


GROUP_MATRIX = np.array(
    [
        [1 if res[0] == 0 else 0 for res in permutations(np.arange(0, 4))],
        [1 if res[1] == 0 else 0 for res in permutations(np.arange(0, 4))],
        [1 if res[2] == 0 else 0 for res in permutations(np.arange(0, 4))],
        [1 if res[3] == 0 else 0 for res in permutations(np.arange(0, 4))],
        [1 if res[0] == 1 else 0 for res in permutations(np.arange(0, 4))],
        [1 if res[1] == 1 else 0 for res in permutations(np.arange(0, 4))],
        [1 if res[2] == 1 else 0 for res in permutations(np.arange(0, 4))],
        [1 if res[3] == 1 else 0 for res in permutations(np.arange(0, 4))],
        [1 if res[0] == 2 else 0 for res in permutations(np.arange(0, 4))],
        [1 if res[1] == 2 else 0 for res in permutations(np.arange(0, 4))],
        [1 if res[2] == 2 else 0 for res in permutations(np.arange(0, 4))],
        [1 if res[3] == 2 else 0 for res in permutations(np.arange(0, 4))],
        [1 if res[0] == 3 else 0 for res in permutations(np.arange(0, 4))],
        [1 if res[1] == 3 else 0 for res in permutations(np.arange(0, 4))],
        [1 if res[2] == 3 else 0 for res in permutations(np.arange(0, 4))],
        [1 if res[3] == 3 else 0 for res in permutations(np.arange(0, 4))],
    ]
)


def group_obj_function(outcome_prob: np.array, position_prob: np.array) -> float:
    "Objective function for the group probabilities compared to final outcome."

    diff = np.dot(GROUP_MATRIX ,outcome_prob) - position_prob
    return np.dot(diff, diff)
