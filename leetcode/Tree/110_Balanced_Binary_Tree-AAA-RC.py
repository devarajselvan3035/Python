"""
110. Balanced Binary Tree (***)(RC)
=========================
Given a binary tree, determine if it is height-balanced.

Note: Difference between left and right node depth greater than 1
called as Un-Balanced Binary Tree
"""

# Example 1
#               1
#       /¯¯¯¯¯¯   ¯¯¯¯¯¯\
#       2               2
#   /¯¯¯ ¯¯¯\       /¯¯¯ ¯¯¯\
#   3       3       N       N
# /¯ ¯\
# 4   4
# Output: False
#
# Example 2:
#       9
#   /¯¯¯ ¯¯¯\
#   9      20
# /¯ ¯\   /¯ ¯\
# n   N  15   7
# Output: True

from PrintTree import PrintTree
from BinaryTree import BinaryTree, Node
from typing import Optional, List


# HACK: O(n) Time complexity
def isBalanced(root: Optional[Node]) -> bool:

    def depth(root: Node) -> List:
        if not root or not root.value:
            return [True, 0]
        left, right = depth(root.left), depth(root.right)
        balanced = (left[0] and right[0]) and (abs(left[1] - right[1]) <= 1)

        return [balanced, 1 + max(left[1], right[1])]

    return depth(root)[0]


# HACK: O(n^2) time complexity
def isBalanced1(root: Optional[Node]) -> bool:

    def depth(root: Node) -> int:
        if not root or not root.value:
            return 0
        return 1 + max(depth(root.left), depth(root.right))

    return (
        abs(depth(root.left) - depth(root.right)) <= 1
        and isBalanced(root.left)
        and isBalanced(root.right)
    )


# ip = [1, 2, 2, 3, 3, None, None, 4, 4]
# ip = [9, 9, 20, None, None, 15, 7]
# ip = [1, 2, 3, 4, 5, 6, None, 8]
ip = [1, 2, 2, 3, None, None, 3, 4, None, None, 4]
bt = BinaryTree()
for i in ip:
    bt.insert_queue(i)

PrintTree(bt.root)
print(isBalanced(bt.root))
