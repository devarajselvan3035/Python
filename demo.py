def findMin(arr: list) -> int:
    l, r = 0, len(arr) - 1
    min_value = None
    idx = None

    while l < r:
        if arr[l] < arr[r]:
            min_value = arr[l]
            idx = l
            r -= 1
        else:
            min_value = arr[r]
            idx = r
            l += 1
        # else:
        #     min_value = arr[l]
        #     l += 1
        #     r += 1
    print(idx)
    return min_value


arr = [3, 7, 1, -10, 5, 9, 0]
print(findMin(arr))


# Revers string using recursion
#
def reverse(string: str) -> str:
    if len(string) == 1:
        return string[0]
    return reverse(string[1:]) + string[0]


print(reverse("hello world"))
