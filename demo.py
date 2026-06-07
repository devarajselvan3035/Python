def matrix(mat: list[list[str]]) -> list[str]:

    result = []

    def backtracking(position: list[int], path: list[str]):
        if position[0] == len(mat) or position[-1] == len(mat[0]):
            return
        elif position == [len(mat) - 1, len(mat[0]) - 1]:
            print("inner", position, path)
            path_str = "".join(path)
            result.append(path_str)
            return

        path = path + [mat[position[0]][position[-1]]]
        print(position, path)

        backtracking([position[0], position[-1] + 1], path)
        path.pop()

        path = path + [mat[position[0]][position[-1]]]
        backtracking(
            [position[0] + 1, position[-1]], path + [mat[position[0]][position[-1]]]
        )
        path.pop()

    backtracking([0, 0], [])
    return result


mat = [["a", "b"], ["b", "c"]]
mat = [["a", "x", "a"], ["x", "a", "x"], ["a", "x", "a"]]

print(matrix(mat))
