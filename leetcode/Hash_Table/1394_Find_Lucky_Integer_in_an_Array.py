"""
1394. Find Lucky Integer in an Array
====================================

Given an array of integers arr, a lucky intgers in an integers that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.

Example 1:
Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

Example 2:
Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

Example 3:
Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.
"""

from typing import List


def findLucky(arr: List[int]) -> int:
    arrCount = {}
    for a in arr:
        arrCount[a] = arrCount.setdefault(a, 0) + 1

    res = -1

    for val, cot in arrCount.items():
        if val == cot and val > res:
            res = val

    return res


arr = [2, 2, 3, 4]
arr = [1, 2, 2, 3, 3, 3]
arr = [2, 2, 2, 3, 3]
print(findLucky(arr))
