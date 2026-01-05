"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the resul in any order

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
"""

import collections


def intersect(nums1: list, nums2: list) -> list:
    rest = []

    sort_nums1 = sorted(nums1)
    sort_nums2 = sorted(nums2)

    n1, n2 = 0, 0
    while n1 < len(nums1) and n2 < len(nums2):
        if sort_nums1[n1] == sort_nums2[n2]:
            rest.append(sort_nums1[n1])
            n1 += 1
            n2 += 1
        elif sort_nums1[n1] < sort_nums2[n2]:
            n1 += 1
        elif sort_nums2[n2] < sort_nums1[n1]:
            n2 += 1
    return rest


from collections import Counter


def intersect2(nums1: list, nums2: list) -> list:
    ## Optimization: count the smaller array to save space
    if len(nums1) > len(nums2):
        return intersect2(nums2, nums1)

    counts = Counter(nums1)
    result = []

    for num in nums2:
        if counts[num] > 0:
            result.append(num)
            counts[num] -= 1

    return result


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
#
# nums1 = [4, 9, 5]
# nums2 = [9, 4, 9, 8, 4]

print(intersect(nums1, nums2))
print(intersect2(nums1, nums2))

sorted()
