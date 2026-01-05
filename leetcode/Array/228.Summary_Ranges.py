def summaryRanges(nums: list) -> list:
    res = []
    l, r, t = 0, 1, 0
    while r <= len(nums):
        if r == len(nums) or nums[l] != nums[r] - 1:
            if nums[t] == nums[l]:
                res.append(str(nums[l]))
            else:
                res.append(f"{nums[t]}->{nums[l]}")
            t = r
            l = r
            r += 1
        else:
            l += 1
            r += 1
    return res


nums1 = [0, 1, 2, 4, 5, 7]
nums = [0, 2, 3, 4, 6, 8, 9]
print(summaryRanges(nums1))
print(summaryRanges(nums))
