"""
104. Maximum Depth of Binary Tree (***)(RC)(ARR)
=================================
Given the root of a binary tree, returns its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path formthe root
node down to the farthest leaf node.
"""

#        3
#    /¯¯¯ ¯¯¯\
#    9      20
#  /¯ ¯\   /¯ ¯\
#  N   N  15   7
#
# Input: root = [3,9,20,None,None<15,7]
# Output: 3


# NOTE: YouTube - NeetCode => maximum depth of binary tree

from PrintTree import PrintTree
from BinaryTree import BinaryTree, Node
from typing import Optional


# HACK: using RECURSION
def maxDepth_DFS(root: Optional[Node]) -> int:
    if root is None or root.value is None:
        return 0
    left = 1 + maxDepth_DFS(root.left)
    right = 1 + maxDepth_DFS(root.right)

    return left if left > right else right


# HACK: Using ARRAY or QUEUE
def maxDepth_BFS(root: Optional[Node]) -> int:
    if not root:
        return 0

    level = 0
    queue = [root]
    while queue:
        for _ in range(len(queue)):
            node = queue[0]
            queue = queue[1:]
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1
    return level


# HACK: STACK ITERATE way Using PREORDER method
def maxDepth_DFS_iter(root: Optional[Node]) -> int:
    stack = [[root, 1]]
    res = 0

    while stack:
        node, depth = stack.pop()

        if node:
            res = max(res, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    return res


# ip = [3, 9, 20, None, None, 15, 7]
ip = [1, None, 2]
bt = BinaryTree()

for i in ip:
    bt.insert_queue(i)

print(maxDepth_DFS(bt.root))
print(maxDepth_BFS(bt.root))
print(maxDepth_DFS_iter(bt.root))
