def majorityElement(nums: list) -> int:
    sort_nums = sorted(nums)
    l, r = 0, 0
    while r <= len(nums):
        if r == len(nums) or sort_nums[l] != sort_nums[r]:
            count = len(sort_nums[l:r])
            if count > (len(nums) / 2):
                return sort_nums[l]
            l = r

        elif sort_nums[l] == sort_nums[r]:
            r += 1
    return -1


nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))
