"""
739. Daily Temperature
======================
Given an array of integers Temperature represents the daily temperature, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no furture day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    stack = []
    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            idx = stack.pop()
            res[idx] = i - idx
        stack.append(i)
        print(stack)
    return res


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# temperatures = [30, 40, 50, 60]
print(dailyTemperatures(temperatures))
