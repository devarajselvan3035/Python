"""
you are given row x col grid representing a map where grid[i][j]=1 represents land and grid[i][j]=0 represents water.

Grid cells are connected horizontally/vertically. The grid is completely surrounded by water, and there is exactly one island.

The island desn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
"""


def islandPerimeter(grid: list[list]) -> int:
    res = 0
    row, col = [], []
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                res += 4
                print(f"start : {res}")
                if c in col:
                    res -= 2
                if r in row:
                    res -= 2
                if r not in row:
                    row.append(r)
                if c not in col:
                    col.append(c)
                print(f"end {res}")
    return res


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(islandPerimeter(grid))
