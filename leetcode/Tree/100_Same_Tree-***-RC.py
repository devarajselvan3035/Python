"""
100. Same Tree (***)(RC)
==============
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p=[1,2,3], q=[1,2,3]
Output: True

Example 2:
Input: p=[1,2], q=[1, None, 2]
Output: False
"""

from BinaryTree import BinaryTree, Node
from typing import Optional


# NOTE: None node as a base coase for the recursion.
def isSameTree(p: Optional[Node], q: Optional[Node]) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None or p.value != q.value:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# p, q = [1, 2, 3], [1, 2, 3]
p, q = [1, None, 3], [1, 3]
ptree = BinaryTree()
qtree = BinaryTree()

for pv in p:
    ptree.insert_queue(pv)

for qv in q:
    qtree.insert_queue(qv)

print(isSameTree(ptree.root, qtree.root))
