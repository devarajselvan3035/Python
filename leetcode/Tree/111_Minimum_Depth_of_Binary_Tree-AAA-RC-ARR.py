"""
111. Minimum Depth of Binary Tree (***)(RC)(ARR)
=================================
Given a binary tree, find its minimum Depth

The minimum depth is the number of nodes along the shortest path form the root node down to the nearest leaf node.

Note: A leaf is a node with no children
"""

#        3
#    /¯¯¯ ¯¯¯\
#    9      20
#  /¯ ¯\   /¯ ¯\
#  N   N  15   7
#
# Input: root = [3,9,20,None,None<15,7]
# Output: 2


from BinaryTree import BinaryTree, Node
from typing import Optional
from PrintTree import PrintTree


# HACK: using RECURSION
def minDepth_DFS(root: Optional[Node]) -> int:
    if root is None or root.value is None:
        return 0
    left = 1 + minDepth_DFS(root.left)
    right = 1 + minDepth_DFS(root.right)

    if left == 1:
        return right
    elif right == 1:
        return left
    else:
        return left if left < right else right


# HACK: using ARRAY or QUEUE
def minDepth_BFS(root: Optional[Node]) -> int:
    if not root:
        return 0
    queue = [root]
    level = 1
    while queue:
        for _ in range(len(queue)):
            node = queue[0]
            queue = queue[1:]
            if (not node.left or node.left.value is None) and (
                not node.right or node.right.value is None
            ):
                return level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1
    return level


ip = [3, 9, 20, None, None, 15, 7]
# ip = [2, None, 3, None, 4, None, 5, None, 6]
bt = BinaryTree()
for i in ip:
    bt.insert_queue(i)

PrintTree(bt.root)

print(minDepth_DFS(bt.root))
print(minDepth_BFS(bt.root))
