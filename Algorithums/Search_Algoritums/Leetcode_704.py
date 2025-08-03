# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

def binary_search(arr:list, num:int, add:int=0):
    middle = len(arr) // 2
    print(arr, middle, add)
    if len(arr) == 1:
        return add if arr[0] == num else -1
    elif arr[middle] == num:
        return add+middle
    elif num < arr[middle]:
        return binary_search(arr[:middle], num, add)
    else:
        return binary_search(arr[middle+1:], num, add+middle)

nums = [-1,0,3,5,9,12]
print(binary_search(nums, 9))
