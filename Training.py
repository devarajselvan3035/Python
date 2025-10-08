# nums = [-3, -5, -2, 3, 4, 6]
# # target = 7
# #

# def merge_sort(arr):
#     if len(arr) > 2:
#         mid = len(arr) // 2
#         left = arr[:mid]
#         right = arr[mid:]

#         merge_sort(left)
#         merge_sort(right)

#         l, r, k = 0, 0, 0
#         while l < len(left) and r < len(right):
#             if left[l] < right[r]:
#                 arr[k] = left[l]
#                 l += 1
#             else:
#                 arr[k] = right[r]
#                 r += 1
#             k += 1

#         while l < len(left):
#             arr[k] = left[l]
#             k += 1
#             l += 1

#         while r < len(right):
#             arr[k] = right[r]
#             k += 1
#             r += 1

# merge_sort(nums)
# print(nums)

# from typing import List
# def pair_sum(arr:List[int], target:int) -> List[int]:
#     l, r = 0, len(arr)-1

#     while l < r:
#         if arr[l] + arr[r] == target:
#             return [l,r]
#         elif arr[l] + arr[r] < target:
#             l += 1
#         else:
#             r -= 1
#     return []
# print(pair_sum(nums, 7))

# def pair_sum_rc(arr:List[int], target:int) -> List[int]:
#     if len(arr) == 0:
#         return []
#     elif arr[0] + arr[-1] == target:
#         return [arr[0], arr[1]]
#     elif arr[0] + arr[-1] < target:
#         return pair_sum_rc(arr[1:], target)
#     else:
#         return pair_sum_rc(arr[:-1], target)
# print(pair_sum_rc(nums, 7))


from Algorithums.Sorting_Algorithums.Merge_sort import merge_sort

arr = [3, 5, 1, 8, 0, 4]
merge_sort(arr)
print(arr)

print()
