from Binary_Tree import BinaryTree, Node
"""
100. Same Tree
===============
Given the roots of two binary trees 'p' and 'q', write a fucntion to check if
they are same or not. Two binary trees are considered the same if they are structurally 
identiacl, and the nodes have the same value.
"""
p_arr, q_arr = [1, 2, 3], [1, 2, 3]

def createTree(arr:list) -> Node:
    tree = BinaryTree()
    for v in arr:
        tree.insert(v)
    return tree.root

p = createTree(p_arr)
q = createTree(q_arr)

def isSameTree(p:Node, q:Node) -> bool:
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
arr_val = [1,2,2,2,None,2]

root = createTree(arr_val) 

def isSymmetric(root:Node) -> bool:
    res = [] 
    def inorder(node:Node) -> None:
        if node:
            inorder(node.left)
            res.append(node.key)
            inorder(node.right)
    inorder(root)
    div = len(res) // 2
    print(res[:div], res[div+1:][::-1])
    return res[:div] == res[div+1:][::-1]

print(isSymmetric(root))





