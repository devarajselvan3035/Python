"""
404. Sum of Left Leaves
=======================
Given the root of a binary tree, return the sum of all leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
"""

#       3
#   /¯¯¯ ¯¯¯\
#   9      20
# /¯ ¯\   /¯ ¯\
# N   N  15   7
# Output: 24
# Explanation: there are two left leaves in the binary tree, with values 9 and 15 respectively.
#

from PrintTree import PrintTree
from BinaryTree import BinaryTree, Node
from typing import Optional


def sumOfLeftLeaves(root: Optional[Node]) -> int:
    leftSum = 0

    def leftLeaves(root: Node, flag: str) -> int:
        if (
            (not root.left or not root.left.value)
            and (not root.right or not root.right.value)
            and flag == "L"
        ):
            return root.value
        if (
            (not root.left or not root.left.value)
            and (not root.right or not root.right.value)
            and flag == "R"
        ):
            return 0
        leftVal = leftLeaves(root.left, "L")
        rightVal = leftLeaves(root.right, "R")
        print(f"root {root.value}, sum {leftVal + rightVal}")
        return leftVal + rightVal

    return leftLeaves(root, "")


ip = [3, 9, 20, None, None, 15, 7]
bt = BinaryTree()
for i in ip:
    bt.insert_queue(i)

PrintTree(bt.root)
print(sumOfLeftLeaves(bt.root))
