"""
501. Find Mode in Binary Search Tree
====================================
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.
If the tree has more than one mode, return them in any order.
Assume a BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than or equal to the node's key.
- The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
- Both the left and right subtrees must also be binary search trees.
"""
# Example 1:
#        1
#        ¯¯¯\
#           2
#         /¯
#        2
# Input: root = [1,null,2,2]
# Output: [2]
#
# Example 2:
# Input: root = [0]
# Output: [0]
#

from BinaryTree import BinaryTree, Node
from PrintTree import PrintTree
from typing import Optional, List


def findMode(self, root: Optional[Node]) -> List[int]:
    pass


ans = {1: 1, 2: 2, 3: 3}
print(list(filter(lambda x: ans[x] > 1, ans)))

ip = [1, None, 2, 2]
bt = BinaryTree()
for i in ip:
    bt.insert_queue(i)

# PrintTree(bt.root)
