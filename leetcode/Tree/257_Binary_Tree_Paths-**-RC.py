"""
257. Binary Tree Paths (**)(RC)
======================
Given the root of a binary tree, return all root to leaf paths in any order

A leaf is a Node with no children.
"""

#                    1
#                /¯¯¯ ¯¯¯\
#                2       3
#              /¯ ¯\
#              N   5
# Output: ["1->2->5", "1->3"]

from PrintTree import PrintTree
from BinaryTree import BinaryTree, Node
from typing import Optional, List


def binaryTreePaths(root: Optional[Node]) -> List[str]:
    pathList = []

    def paths(root: Node, path: str):
        if not root.left and not root.right:
            fullpath = path + f"{root.value}"
            pathList.append(fullpath)
            return

        if root.left.value:
            paths(root.left, path + f"{root.value}->")
        if root.right.value:
            paths(root.right, path + f"{root.value}->")

    paths(root, "")
    return pathList


# ip = [1, 2, 3, None, 5]
ip = [1]
bt = BinaryTree()

for i in ip:
    bt.insert_queue(i)

PrintTree(bt.root)
print(binaryTreePaths(bt.root))
