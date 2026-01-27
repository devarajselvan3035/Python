"""
101. Symmetric Tree
===================
Given the root of a binary tree, check whether it is a mirror of itself (i.e, Symmetric around its center)
Example 1:
    1
   /  \
  2    2
 / \\  / \
3   4 4  3

Input: root = [1,2,2,3,4,4,3]
Output: True
"""

from typing import Optional
from BinaryTree import BinaryTree, Node


def isSymmetric(root: Optional[Node]) -> bool:
    def _isSymmetric(left: Node, right: Node) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (
            left.value == right.value
            and _isSymmetric(left.left, right.right)
            and _isSymmetric(left.right, right.left)
        )

    return _isSymmetric(root.left, root.right)


# ip = [1, 2, 2, 3, 4, 4, 3]
ip = [1, 2, 2, None, 3, None, 3]

bt = BinaryTree()
for i in ip:
    bt.insert_queue(i)

print(isSymmetric(bt.root))
