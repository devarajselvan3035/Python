from typing import List

print("hello world")


def find(nums: List[int]) -> int:
    n = len(nums)
    left = None
    leftStack = []

    for i in range(n):
        while leftStack and nums[i] < nums[leftStack[-1]]:
            left = leftStack.pop()
            break

        if left is not None:
            break

        leftStack.append(i)
        print(nums[i], leftStack[-1])
        print(leftStack)

    print(left)


nums = [2, 6, 4, 8, 10, 9, 15]
# nums = [1, 2, 3, 4]
# nums = [1]
# nums = [5, 4, 3, 2, 1]
# nums = [1, 3, 2, 2, 2]
# nums = [1, 2, 3, 3, 3]
print(find(nums))
print("hello")
