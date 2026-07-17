"""
1588. Sum of All Odd Length Subarrays
=====================================
Given an array of positive integers arr, return the sum of all possible odd-lenght subarrays of arr.

A subarray is a contiguous subsequence of the array.

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

Example 2:
Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.

Example 3:
Input: arr = [10,11,12]
Output: 66
"""

from typing import List


def sumOddLengthSubarrays(arr: List[int]) -> int:
    com = (len(arr) + 1) // 2
    l, r = 0, len(arr) - 1
    res = 0
    while l <= r:
        print(com, res)
        if l == r:
            res += arr[l] * com
        else:
            res += (arr[l] * com) + (arr[r] * com)
        com = com + 1 if com + 1 < len(arr) else com
        l += 1
        r -= 1
    return res


def sumOddLengthSubarrays1(arr: List[int]) -> int:
    prefixSum = []
    temp = 0
    for n in arr:
        temp += n
        prefixSum.append(temp)

    res: int = 0
    for n in range(1, len(arr) + 1, 2):
        r, sub = n - 1, 0
        while r < len(arr):
            res += prefixSum[r] - sub
            r += 1
            sub = prefixSum[r - n]

    return res


arr = [1, 4, 2, 5, 3]
# arr = [1, 2]
# arr = [10, 11, 12]
print(sumOddLengthSubarrays(arr))
