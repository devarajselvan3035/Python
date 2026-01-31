"""
303. Range Sum Query - Immutable (**)
================================
"""


class NumArray:

    def __init__(self, Array: list) -> None:
        self.Array = Array
        self.prefixSum = []
        temp = 0
        for n in Array:
            temp += n
            self.prefixSum.append(temp)

    def sumRange(self, left: int, right: int) -> int:
        left = left - 1
        return (
            self.prefixSum[right]
            if left < 0
            else self.prefixSum[right] - self.prefixSum[left]
        )


ip = [1, 2, 3, 4, 5]
na = NumArray(ip)
print(na.prefixSum)
print(na.sumRange(1, 2))
