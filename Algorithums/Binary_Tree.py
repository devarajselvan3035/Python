class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
"""
This balanced binary tree utilizes a recursive insertion method, 
where the decision to insert data is governed by a conditional input, 
such as a "yes" or "no" response.

For instance, if the insertion process is navigating to a node and the condition for proceeding to the left subtree is evaluated as "no" (or false), the following actions occur:
    1.The left child node's value is set to null (or None).
    2.The recursion then proceeds to evaluate the right subtree for 
    potential insertion.

This structure is characteristic of a basic balanced binary search tree.
"""

class binaryTree:
    def __init__(self) -> None:
        self.root = None
        self.val_list = []

    def add(self) -> None:
        data = int(input("Enter the data : "))
        newNode = Node(data)
        self.root = newNode
        self._add(self.root)
        print("Binary Tree is completed")

    def _add(self, node):
        left_ip = input(f"Enter y or n for left node of {node.data} : ")
        if left_ip == 'y':
            data = int(input("Enter the left node data : "))
            newNode = Node(data)
            node.left = newNode
            self._add(node.left)
        
        right_ip = input(f"Enter y or n for right node of {node.data} : ")
        if right_ip == 'y':
            data = int(input("Enter the right node data : "))
            newNode = Node(data)
            node.right = newNode
            self._add(node.right)

    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.left)
            self.val_list.append(node.data)
            print(node.data)
            self.inOrder(node.right)
