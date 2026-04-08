"""
1275. Find Winner on a Tic Tac Toe Game
=======================================

Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

    Players take turns placing characters into empty squares ' '.
    The first player A always places 'X' characters, while the second player B always places 'O' characters.
    'X' and 'O' characters are always placed into empty squares, never on filled ones.
    The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
    The game also ends if all squares are non-empty.
    No more moves can be played if the game is over.

Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

Example 1:
Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.

Example 2:
Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: B wins.

Example 3:
Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
"""

from typing import List


def tictactoe(moves: List[List[int]]) -> str:
    xRow, xCol, oRow, oCol = [], [], [], []
    for idx, move in enumerate(moves):
        if idx // 2 == 0:
            xRow.append(move[0])
            xCol.append(move[1])
        else:
            oRow.append(move[0])
            oCol.append(move[1])

    xRowLen, xColLen, oRowLen, oColLen = (
        len(set(xRow)),
        len(set(xCol)),
        len(set(oRow)),
        len(set(oCol)),
    )
    print(xRow, xCol, oRow, oCol)
    if (
        (xRowLen == 3 and xColLen == 3)
        or (xRowLen == 3 and xColLen == 1)
        or (xColLen == 3 and xRowLen == 1)
    ):
        return "A"
    elif (
        (oRowLen == 3 and oColLen == 3)
        or (oRowLen == 3 and oColLen == 1)
        or (oColLen == 3 and oRowLen == 2)
    ):
        return "B"
    else:
        return "Draw"


moves = [[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]
moves = [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]
print(tictactoe(moves))
