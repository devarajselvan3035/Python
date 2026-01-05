"""
594. Logest Harmonious Subsequence
==================================
We define a Harmonious array as an array where the difference between it s maximum value and
it's minimum value is exactly 1.

Given an integer array nums, return the length of its longest Harmonious Subsequence among all
its possible subsequences.

Example1:
Input: nums = [1,3,2,2,5,2,3,7]
output: 5
Explanation:
The longest harmonious subsequence is [3,2,2,2,3]
"""


def findLHS(nums: list) -> int:
    counts = {}
    for n in nums:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1

    ans = 0
    for num, count in counts.items():
        if num - 1 in counts:
            ans = max(ans, count + counts[num - 1])
    return ans


def findLHS1(nums: list) -> int:
    sort_nums = sorted(nums)
    lhs_dict = {}
    for v in sort_nums:
        if v - 1 not in lhs_dict:
            lhs_dict[v - 1] = []
        if v not in lhs_dict:
            lhs_dict[v] = []
        if v - 1 in lhs_dict:
            lhs_dict[v - 1].append(v)
        if v in lhs_dict:
            lhs_dict[v].append(v)

    for idx, val in lhs_dict.items():
        if len(set(val)) == 1:
            lhs_dict[idx] = []

    return len(max(lhs_dict.values(), key=len))


nums = [1, 3, 2, 2, 5, 2, 3, 7]
# nums = [1, 2, 3, 4]
# nums = [1, 1, 1, 1]
print(len(set(nums)))
print(findLHS(nums))
