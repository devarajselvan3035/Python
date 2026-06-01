def reverseSubstring(s: str) -> str:
    s = s + " "
    string = []
    substirng = ""
    for chr in s:
        if chr == " ":
            string.append(substirng)
            substirng = ""
        else:
            substirng = chr + substirng

    return " ".join(string)


print(reverseSubstring("hello world"))


def getSmallCommonValue(l1: list[int], l2: list[int]) -> float:
    min_val = float("inf")
    l, r = 0, 0
    while l < len(l1) and r < len(l2):
        if l1[l] == l2[r]:
            min_val = min(min_val, l1[l])
            l += 1
            r += 1
        elif l1[l] < l2[r]:
            l += 1
        else:
            r += 1
    return min_val


# print(getSmallCommonValue([1, 2, 3, 6], [2, 3, 4, 5]))
#
def moveZeros(arr: list[int]) -> list[int]:
    l = 0
    for r in range(len(arr)):
        if arr[r] != 0:
            arr[l]
