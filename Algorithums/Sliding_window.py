## Question 1
#  ============
# Maximum Sum Subarray of Size K (Fixed Size)
# Given an array and an integer k, find the maximum sum of a subarray of size k.
# Example: arr = [1, 4, 2, 10, 2, 3, 1, 0, 20], k = 4. The maximum sum is 36 (from [2, 10, 2, 3]).
#
# Solution 1
# ----------
# arr = [1, 30, 2, 10, 2, 3, 1, 0, 20]
# k = 4

# left:int = 0
# max_value:int = 0
# value_list:list = []

# for right in range(len(arr)):
#     if len(value_list) > k-1:
#         value_list.remove(arr[left])
#         left += 1
#     value_list.append(arr[right])
#     print(value_list)
#     print(sum(value_list))
#     if sum(value_list) > max_value:
#         max_value = sum(value_list)

# print(max_value)
# ------------------------------------------------------------
## Question 2
#  =========
# Given an array of positive integers nues and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return o instead.
# Example 1:
# Input: target 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:
# Input: target 4, nums [1,4,4]
# Output: 1
# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# output = 0
# nums sum is not equal to target, so the output is 0

# target = 7
# nums = [2,3,1,2,4,3]

# target ,nums = 11, [1,1,1,1,1,1,1,1]
# target, nums = 4, [1,4,4]

# left, min_length = 0, float('inf')
# value_list:int = 0
# sum_list:list = []

# for right in range(len(nums)):
#     #Expand window
#     value_list += nums[right]

#     # Shrink Window
#     while value_list > target:
#         value_list -= nums[left]
#         left += 1

#     if value_list == target:
#         min_length = min(min_length, right-left+1)
#     print(value_list)

# if min_length == float('inf'):
#     print(0)
# else:
#     print(min_length)
# ------------------------------------------------------
# # Question 3
# Description: Given two strings s and t, find the minimum window in s which will contain all the characters in t.

# Example: Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# s, t = "BANC","ABC"
# left = 0
# sub_str:list = []
# min_length = float('inf')
# real:str = ''

# def find_flag(sub, t) -> int:
#     flag:int = 0
#     for w in sub:
#         if w in t:
#             flag += 1
#     return flag

# for right in range(len(s)):
#     # Expand window
#     sub_str += s[right]

#     # Shrink window
#     flag = find_flag(sub_str, t)
#     print(flag)
#     while flag > len(t)-1:
#         real = "".join(sub_str)
#         sub_str.remove(s[left])
#         left += 1
#         flag = find_flag(sub_str, t)
#     print(real)
# --------------------------------------------------------------------------------------------
## Question 4
# ============
# You are given an array nums of n integers and two integers k and x.

# The x-sum of an array is calculated by the following procedure:

# Count the occurrences of all elements in the array.
# Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
# Calculate the sum of the resulting array.
# Note that if an array has less than x distinct elements, its x-sum is the sum of the array.

# Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].



# Example 1:

# Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2

# Output: [6,10,12]

# Explanation:

# For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence, answer[0] = 1 + 1 + 2 + 2.
# For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence, answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.
# For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence, answer[2] = 2 + 2 + 2 + 3 + 3.
# Example 2:

# Input: nums = [3,8,7,8,7,5], k = 2, x = 2

# Output: [11,15,15,15,12]

# Explanation:

# Since k == x, answer[i] is equal to the sum of the subarray nums[i..i + k - 1].

# nums, k, x = [1,1,2,2,3,4,2,3], 6, 2
nums, k, x = [3,8,7,8,7,5], 2, 2

def find_counter(arr:list):
    temp:dict = {}
    for i in arr:
        if i not in temp.keys():
            temp[i] = 1
        else:
            temp[i] += 1
    filter_dict = {k:v for k,v in temp.items() if v != 1}
    return list(filter_dict.keys())

for i in range(len(nums)-k+1):
    sub_nums = nums[i:k+i]
    sum_value:int = 0
    final_list:list = []
    counter = find_counter(sub_nums)
    no_duplicate = list(set(sub_nums))
    while len(counter) != x:
        counter.append(max(no_duplicate))
        no_duplicate.remove(max(no_duplicate))

    for v in sub_nums:
        if v in counter:
            sum_value += v

    print(sum_value)
