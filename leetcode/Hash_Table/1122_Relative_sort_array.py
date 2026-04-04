"""
1122. Relative Sort Array
=========================

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

Example 1:
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

Example 2:
Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]
"""

from typing import List, reveal_type


def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    relativeDict = {}
    extraValue = []
    res = []

    for val in arr1:
        if val in arr2:
            if val not in relativeDict:
                relativeDict[val] = [val]
            else:
                relativeDict[val].append(val)

        else:
            extraValue.append(val)

    for val in arr2:
        res += relativeDict[val]

    res += sorted(extraValue)
    return res


# arr1, arr2 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]
arr1, arr2 = [28, 6, 22, 8, 44, 17], [22, 28, 8, 6]
print(relativeSortArray(arr1, arr2))
