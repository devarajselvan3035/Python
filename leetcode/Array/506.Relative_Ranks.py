"""
506. Relative Ranks
===================

You are given an integer array score of size n. where score[i] is the score of the ith athlete in
a competition. All the scores are guaranteed to the unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score,
The 2nd place athelete has the 2nd highest score, and so on. The placement of each athelete determines
their ranks:


    The 1st place athlete's rank is "Gold Medal".
    The 2nd place athlete's rank is "Silver Medal".
    The 3rd place athlete's rank is "Bronze Medal".
    For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").

Return an array answer of size n where answer[i] is the rank of the ith athlete.

Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].
"""


def findRelativeRanks(score: list) -> list:
    score_dict = {s: i for i, s in enumerate(score)}
    res = [""] * len(score)

    score_sort = sorted(score, reverse=True)

    for i, ss in enumerate(score_sort):
        res_idx = score_dict[ss]
        if i == 0:
            res[res_idx] = "Gold Medal"
        elif i == 1:
            res[res_idx] = "Silver Medal"
        elif i == 2:
            res[res_idx] = "Bronze Medal"
        else:
            res[res_idx] = str(i + 1)

    return res


# score = [5, 4, 3, 2, 1]
score = [10, 3, 8, 9, 4]
print(findRelativeRanks(score))
