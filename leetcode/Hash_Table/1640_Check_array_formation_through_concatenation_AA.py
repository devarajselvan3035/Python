"""
1640. Check Array Formation Through Concatenation (**)
==================================================

You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].

Return true if it is possible to form the array arr from pieces. Otherwise, return false.

Example 1:
Input: arr = [15,88], pieces = [[88],[15]]
Output: true
Explanation: Concatenate [15] then [88]

Example 2:
Input: arr = [49,18,16], pieces = [[16,18,49]]
Output: false
Explanation: Even though the numbers match, we cannot reorder pieces[0].

Example 3:
Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
Output: true
Explanation: Concatenate [91] then [4,64] then [78]
"""

from copyreg import pickle
from typing import List


def canFormArray(arr: List[int], pieces: List[List[int]]) -> bool:
    for pie in pieces:
        if pie[0] not in arr:
            return False
    arrRank = {}
    for idx, a in enumerate(arr):
        arrRank[a] = idx
    pieces.sort(key=lambda x: arrRank[x[0]])

    res = []
    for pie in pieces:
        res += pie

    return res == arr


arr, pieces = [15, 88], [[88], [15]]
arr, pieces = [49, 18, 16], [[16, 18, 49]]
arr, pieces = [91, 4, 64, 78], [[78], [4, 64], [91]]
print(canFormArray(arr, pieces))
