from Binary_Tree import BinaryTree, Node

"""
100. Same Tree
===============
Given the roots of two binary trees 'p' and 'q', write a fucntion to check if
they are same or not. Two binary trees are considered the same if they are structurally 
identiacl, and the nodes have the same value.
"""
p_arr, q_arr = [1, 2, 3], [1, 2, 3]


def createTree(arr: list) -> Node:
    tree = BinaryTree()
    for v in arr:
        tree.insert(v)
    return tree.root


p = createTree(p_arr)
q = createTree(q_arr)


def isSameTree(p: Node, q: Node) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None or p.key != q.key:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# print(isSameTree(p, q))

"""
101.Symmetric Tree
====================
Given the root of a binary tree, check whether it is a mirror of itself
"""
# arr_val = [1,2,2,3,4,4,3,5,6,7,8,8,7,6,5]
arr_val = [1, 2, 2, 2, None, 2]

root = createTree(arr_val)


def isSymmetric(root: Node) -> bool:
    res = []

    def inorder(node: Node) -> None:
        if node:
            inorder(node.left)
            res.append(node.key)
            inorder(node.right)

    inorder(root)
    div = len(res) // 2
    # print(res[:div], res[div + 1 :][::-1])
    return res[:div] == res[div + 1 :][::-1]


# print(isSymmetric(root))

"""
104. Maximum Depth of Binary Tree
==================================
Given the root of binary tre, return its maximum depth

A binary tree's maximum depth is the number of nodes along the logest path
form the root node down to the farthest leaf node.
"""

# ip = [3, 9, 20, None, None, 15, 7]
ip = [1, None, 2]
root104 = createTree(ip)


def maxDepth(root: Node) -> int:
    def _maxDepth(inner_root: Node, depth: int) -> int:
        if inner_root is None:
            # print(depth)
            return 0

        return max(
            _maxDepth(inner_root.left, depth + 1),
            _maxDepth(inner_root.right, depth + 1),
        )

    return _maxDepth(root, 0)


# print(maxDepth(root104))

"""
111. Minimum Depth of Binary Tree
===================================
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path form 
the root node down to the nearest leaf node.
"""
ip = [3, 9, 20, None, None, 15, 7]
root111 = createTree(ip)


def minDepth(root: Node):
    if root is None:
        return 0
    left = 1 + minDepth(root.left)
    right = 1 + minDepth(root.right)

    print(left, right, root.key)

    return min(left, right)


print(minDepth(root111))

"""
112 Path Sum
============
Given the root of a binary tree and an integer targetsum, return true if the tree has a
root-to-leaf path such that adding up all the values along the path equals targetsum
"""
ip = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
target = 22

root = createTree(ip)


def hasPathSum(root: Node, target: int):
    pass


#
#
