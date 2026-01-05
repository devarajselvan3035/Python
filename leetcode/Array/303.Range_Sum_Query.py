class NumArray:

    def __init__(self, nums) -> None:
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        res = 0
        for i in range(left, right + 1):
            res += self.nums[i]
        return res


if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    print(obj.sumRange(0, 2))
    print(obj.sumRange(2, 5))
    print(obj.sumRange(0, 5))
