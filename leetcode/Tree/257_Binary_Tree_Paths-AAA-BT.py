"""
257. Binary Tree Paths (***)(BackTrack)
===============================
Given the root of a binary tree, return all root to leaf paths in any order

A leaf is a Node with no children.
"""

#                    1
#                /¯¯¯ ¯¯¯\
#                2       3
#              /¯ ¯\
#              N   5
# Output: ["1->2->5", "1->3"]

from PrintTree import PrintTree
from BinaryTree import BinaryTree, Node
from typing import Optional, List


# NOTE: Breadth First Search (BFS), take less time complexity and easy for implement


def binaryTreePaths(root: Optional[Node]) -> list[str]:
    ans = []

    def dfs(node, path):
        if not node:
            return
        path += str(node.value)
        if not node.left and not node.right:
            ans.append(path)
        else:
            dfs(node.left, path + "->")
            dfs(node.right, path + "->")

    dfs(root, "")
    return ans


# NOTE: Depth First Search (DFS), take more time complexity and complex for implement
# WARN: IMPLEMENTED USING BACKTRACKING ALGORITHM


def binaryTreePaths1(root: Optional[Node]) -> List[str]:
    res, path = [], []

    def backtrack(node: Node) -> None:
        if node:
            path.append(str(node.value))
            if not node.left and not node.right:
                res.append("->".join(path))
                path.pop()
                return

            backtrack(node.left)
            backtrack(node.right)
            path.pop()

    backtrack(root)
    return res


ip = [1, 2, 3, None, 5]
# ip = [1]
bt = BinaryTree()

for i in ip:
    bt.insert_queue(i)

PrintTree(bt.root)
print(binaryTreePaths(bt.root))
