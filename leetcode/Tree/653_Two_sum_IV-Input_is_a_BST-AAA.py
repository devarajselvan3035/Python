"""
653. Two Sum IV - Input is a BST
Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.
"""
#       5
#   /¯¯¯ ¯¯¯\
#   3       6
# /¯ ¯\      ¯\
# 2   4       7
#
# Example 1:
# root = [5, 3, 6, 2, 4, None, 7], k=9
# true
#
# Example 2:
# root = [5, 3, 6, 2, 4, None, 7], k=28
# false

from BinaryTree import BinaryTree, Node
from PrintTree import PrintTree
from typing import Optional


def findTarget(root: Optional[Node], k: int) -> bool:
    seen = set()

    def dfs(node) -> bool:
        if not node:
            return False

        if k - node.value in seen:
            return True

        seen.add(node.value)

        return dfs(node.left) or dfs(node.right)

    return dfs(root)


root = [5, 3, 6, 2, 4, None, 7]
bt = BinaryTree()

for r in root:
    bt.insert_queue(r)

print(findTarget(bt.root, k=28))
PrintTree(bt.root)
