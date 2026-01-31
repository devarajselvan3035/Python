"""
112. Path Sum (***)(RC)
=============
Given the root of a binary tree and an integer targetsum, return true if the tree has a root-to-leaf
path such that adding up all the values along the path equals targetsum

A leaf is a node with no children
"""

#               5
#       /¯¯¯¯¯¯   ¯¯¯¯¯¯\
#       4               8
#   /¯¯¯ ¯¯¯\       /¯¯¯ ¯¯¯\
#  11       N      13       4
# /¯ ¯\   /¯ ¯\   /¯ ¯\
# 7   2   N   N   N   1
# Input: root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], sum = 22
# Output: true
# Explanation: [5,4,11,2] path have sum of 22 so it's true


from PrintTree import PrintTree
from BinaryTree import BinaryTree, Node
from typing import Optional


def hasPathSum(root: Optional[Node], targetSum: int) -> bool:

    def _hasPathSum(node, cursum) -> bool:
        if not node or node.value is None:
            return False

        cursum += node.val
        if not node.left and not node.right:
            return cursum == targetSum

        return _hasPathSum(node.left, cursum) or _hasPathSum(node.right, cursum)

    return _hasPathSum(root, 0)


def hasPathSum1(root: Optional[Node], targetsum: int) -> bool:
    if root is None:
        return False

    def _hasPathSum(root: Node, sum: int, targetsum: int) -> bool:
        if not root or root.value is None:
            if (sum) == targetsum:
                return True
            else:
                return False

        print(f"root value {root.value}, root sum {sum}")
        return _hasPathSum(root.left, sum + root.value, targetsum) or _hasPathSum(
            root.right, sum + root.value, targetsum
        )

    return _hasPathSum(root, 0, targetsum)


# ip, sum = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22
# ip, sum = [1, 2, 3], 5
ip, sum = [], 0
bt = BinaryTree()
for i in ip:
    bt.insert_queue(i)

print(hasPathSum(bt.root, sum))
