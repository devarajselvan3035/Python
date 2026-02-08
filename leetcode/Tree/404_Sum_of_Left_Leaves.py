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

    def LeftLeaves(root: Node, flag: str) -> int:
        if not root.left and not root.right and flag == "l":
            return root.value
        if not root.left and not root.right and flag == "r":
            return 0
        return LeftLeaves(root.left, "l") + LeftLeaves(root.right, "r")

    return LeftLeaves(root, "r")


# root = [3, 9, 20, None, None, 15, 7]
root = [1]
bt = BinaryTree()
for i in root:
    bt.insert_queue(i)

PrintTree(bt.root)
print(sumOfLeftLeaves(bt.root))
