def next_greater_element(nums):
    ans = []
    stack = []
    for a in arr[::-1]:
        while stack and a >= stack[-1]:
            stack.pop()
        if not stack:
            ans = [-1] + ans
        else:
            ans = [stack[-1]] + ans
        stack.append(a)
    return ans


def next_smallest_element(nums):
    ans = []
    stack = []
    for a in arr[::-1]:
        while stack and a <= stack[-1]:
            stack.pop()
        if not stack:
            ans = [-1] + ans
        else:
            ans = [stack[-1]] + ans
        stack.append(a)
    return ans


def previous_greater_element(nums):
    ans = []
    stack = []
    for a in arr:
        while stack and a >= stack[-1]:
            stack.pop()
        if not stack:
            ans.append(-1)
        else:
            ans.append(stack[0])
        stack.append(a)
    return ans


def previous_smallest_element(nums):
    ans = []
    stack = []
    for a in arr:
        while stack and a <= stack[-1]:
            stack.pop()
        if not stack:
            ans.append(-1)
        else:
            ans.append(stack[0])
        stack.append(a)
    return ans


arr = [2, 1, 2, 4, 3]
print(next_greater_element(arr))
print(next_smallest_element(arr))
print(previous_greater_element(arr))
print(previous_smallest_element(arr))
