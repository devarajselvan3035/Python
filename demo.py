def intersection(arr1: list[int], arr2: list[int]) -> list[int]:
    arr1.sort()
    arr2.sort()
    l, r = 0, 0
    res = []
    idx = 0
    while l < len(arr1) and r < len(arr2):
        if arr1[l] == arr2[r]:
            res.append(arr1[l])
            l += 1
            r += 1
        elif arr1[l] < arr2[r]:
            l += 1
        elif arr2[r] < arr1[l]:
            r += 1
    return res


num1, num2 = [1, 2, 3, 1], [1, 3, 2, 1]
print(intersection(num1, num2))
