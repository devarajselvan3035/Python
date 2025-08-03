from Algorithums.Sorting_Algorithums.Merge_sort import merge_sort
from typing import List

nums = [0, -1, 2, -3, 1]
merge_sort(nums)

def triplet_sum(arr: List[int]) -> List[List]:
    temp_ans = []
    for i in range(len(arr)):
        l, r = 0, len(arr)-1
        print(l, r, i)
        while l < r:
            if arr[l]+arr[r]+arr[i] == 0 and l!=i and r!=i:
                value_list = list([arr[l], arr[r], arr[i]])
                value_list = sorted(value_list)
                if value_list not in temp_ans:
                    temp_ans.append(value_list)
                l += 1
                r -= 1
            elif arr[l]+arr[r] < (-1*arr[i]):
                l += 1
            else:
                r -= 1
    return temp_ans
print(triplet_sum(nums))