"""
1346. Check If N and Its Double Exist (**)(UQ)
=====================================
Given an array arr of integers, check if there exist two indices i and j such that :
- i != j
- 0 <= i, j < arr.length
- arr[i] == 2 * arr[j]

Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:
Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
"""

from typing import List


def checkIfExist(arr: List[int]) -> bool:
    checks = set()
    for n in arr:
        if n in checks:
            print(n, checks)
            return True
        checks.add(n * 2)
        checks.add(n / 2)
    return False


# arr = [10, 2, 5, 3]
arr = [3, 1, 7, 11]
print(checkIfExist(arr))
