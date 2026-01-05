def missingNumber(nums: list) -> int:
    sort_nums = sorted(nums)
    l, r = 0, 1
    while r <= len(nums):
        if r == len(nums) or sort_nums[l] != sort_nums[r] - 1:
            return sort_nums[l] + 1
        l += 1
        r += 1


# nums = [3, 0, 1]
# nums = [0, 1]
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(missingNumber(nums))
