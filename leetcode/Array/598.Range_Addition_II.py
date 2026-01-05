"""
598. Range Addition II
======================
You are given an mxn matirix M initialized with all 0's and an array of operations ops,
where ops[i]=[ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < b.

Count and return the number of maximum integers in the matrrix after performing
all the operations.
"""

from typing import List


def maxCount(m: int, n: int, ops: List[List[int]]) -> int:
    r, c = m, n
    for op in ops:
        r = min(op[0], r)
        c = min(op[1], c)
    return r * c


# m, n, ops = 3, 3, [[2, 2], [3, 3]]
# m, n, ops = (
#     3,
#     3,
#     [
#         [2, 2],
#         [3, 3],
#         [3, 3],
#         [3, 3],
#         [2, 2],
#         [3, 3],
#         [3, 3],
#         [3, 3],
#         [2, 2],
#         [3, 3],
#         [3, 3],
#         [3, 3],
#     ],
# )
m, n, ops = 3, 3, []
print(maxCount(m, n, ops))
