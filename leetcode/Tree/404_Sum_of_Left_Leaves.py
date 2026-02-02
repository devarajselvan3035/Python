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
    queue = [root]

    while queue:
        curd = queue[0]
        queue = queue[1:]

        if curd.left and curd.left.value:
            queue.append(curd.left)
            if not curd.left.left and not curd.left.right:
                leftSum += curd.left.value

        if curd.right and curd.right.value:
            queue.append(curd.right)

    return leftSum


ip = [3, 9, 20, None, None, 15, 7]
# ip = [1, 2]
bt = BinaryTree()
for i in ip:
    bt.insert_queue(i)

PrintTree(bt.root)
print(sumOfLeftLeaves(bt.root))
