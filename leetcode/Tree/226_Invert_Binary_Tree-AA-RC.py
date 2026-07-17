"""
226. Invert Binary Tree (**)(RC)
=======================
Given the root of a binary tree, invert the tree, and return its root.

"""

#       4
#   /¯¯¯ ¯¯¯\
#   2       7
# /¯ ¯\   /¯ ¯\
# 1   3   6   9

from PrintTree import PrintTree
from BinaryTree import BinaryTree, Node
from typing import Optional


def invertTree(root: Optional[Node]) -> Optional[Node]:
    if not root or not root.value:
        return
    invertTree(root.left)
    invertTree(root.right)
    root.right, root.left = root.left, root.right

    return root


# ip = [4, 2, 7, 1, 3, 6, 9]
ip = [2, 1, 3]
bt = BinaryTree()
for i in ip:
    bt.insert_queue(i)

PrintTree(bt.root)
PrintTree(invertTree(bt.root))
