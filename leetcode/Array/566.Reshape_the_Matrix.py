"""
566. Reshape the matrix
=======================
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
"""


def matrixReshape(mat: list, r: int, c: int) -> list:
    temp = []
    res = []
    for r1 in range(len(mat)):
        for c1 in range(len(mat[r1])):
            temp.append(mat[r1][c1])

    idx = 0
    for _ in range(r):
        col = []
        for _ in range(c):
            col.append(temp[idx])
            idx += 1
        res.append(col)
    return res


mat = [[1, 2], [3, 4]]
print(matrixReshape(mat, 4, 1))
