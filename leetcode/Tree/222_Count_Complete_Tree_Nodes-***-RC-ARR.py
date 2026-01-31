"""
222. Count Complete Tree Nodes(***)(RC)(ARR)
==============================
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to wikipedia, every level, except possibly the last, is completely filled in a complete binary tree,
and all nodes in the last level are as far left as possible. It can have between 1 an 2^h nodes inclusive at the last level h.
"""

#      1
#   /¯¯¯ ¯¯¯\
#   2       3
# /¯ ¯\   /¯
# 4   5   6

from PrintTree import PrintTree
from BinaryTree import BinaryTree, Node
from typing import Optional


# HACK: using Recursion with DFS method
def countNodes_DFS(root: Optional[Node]) -> int:
    leftroot, rightroot = root, root
    leftMost, rightMost = 0, 0
    while leftroot and leftroot.value:
        leftMost += 1
        leftroot = leftroot.left

    while rightroot and rightroot.value:
        rightMost += 1
        rightroot = rightroot.right

    if leftMost == rightMost:
        return 2 ** (leftMost) - 1
    else:
        return 1 + countNodes(root.left) + countNodes(root.right)


# HACK: Using ARRAY or QUEUE using BFS method
def countNodes_BFS(root: Optional[Node]) -> int:
    if not root:
        return 0
    node_count = 1
    queue = [root]
    while queue:
        node = queue[0]
        queue = queue[1:]
        if node.left and node.left.value is not None:
            queue.append(node.left)
            node_count += 1
        if node.right and node.right.value is not None:
            queue.append(node.right)
            node_count += 1

    return node_count


ip = [1, 2, 3, 4, 5, 6, 7]
# ip = [1]
bt = BinaryTree()
for i in ip:
    bt.insert_queue(i)

# PrintTree(bt.root)
print(countNodes_DFS(bt.root))
