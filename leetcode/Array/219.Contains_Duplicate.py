def containsNearbyDuplicate(nums: list, k: int) -> bool:
    arr_dict = {}
    for i in range(len(nums)):
        if nums[i] in arr_dict and abs(i - arr_dict[nums[i]]) <= k:
            return True
        arr_dict[nums[i]] = i
    return False


nums = [1, 2, 3, 1, 2, 3]
k = 2
print(containsNearbyDuplicate(nums, k))
