def containsDuplicate(nums: list) -> bool:
    sort_nums = sorted(nums)
    l, r = 0, 1
    while r < len(nums):
        if sort_nums[l] == sort_nums[r]:
            return True
        l += 1
        r += 1
    return False


def containsDuplicate2(nums: list) -> bool:
    no_duplicate = set(nums)


nums = [1, 2, 3, 4]
print(containsDuplicate(nums))
