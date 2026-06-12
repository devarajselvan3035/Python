def check_palindrome(arr: list[list[str]]) -> list[str]:
    result = []
    tol_row = len(arr) - 1
    tol_col = len(arr[0]) - 1

    def backtrack(pos: list[int], path: list[str]):
        if pos in [[tol_row, tol_col + 1]]:
            str_list = "".join(path)
            result.append(str_list)
            return
        elif pos[0] > tol_row or pos[1] > tol_col:
            return

        row = pos[0]
        col = pos[1]

        path.append(arr[row][col])
        backtrack(pos=[row, col + 1], path=path)
        path.pop()

        path.append(arr[row][col])
        backtrack(pos=[row + 1, col], path=path)
        path.pop()

    backtrack([0, 0], [])
    return result


arr = [["a", "x", "a"], ["x", "a", "x"], ["a", "x", "a"]]
arr = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]

print(check_palindrome(arr))
