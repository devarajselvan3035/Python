class Node:
    def __init__(self, value=None, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self) -> None:
        self.root = None
        self.stack = []

    # HACK: This insert method implemented using stack with the list function, This process
    def insert_arr(self, value):
        leftNode = Node()
        rightNode = Node()

        if self.root is None:
            newNode = Node(value)
            self.root = newNode

            self.root.left = leftNode
            self.root.right = rightNode

        else:
            node = self.stack[0]
            self.stack = self.stack[1:]

            node.value = value

            node.left = leftNode
            node.right = rightNode

        self.stack.append(leftNode)
        self.stack.append(rightNode)

    # HACK: Insert value binary tree using recursion
    def insert_recursion(self, value) -> None:
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return
        self._recursiveInsert(self.root, value)

    def _recursiveInsert(self, root, value):
        if root.left is None:
            root.left = Node(value)
        elif root.right is None:
            root.right = Node(value)
        else:
            self._recursiveInsert(root.left, value)

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.value)
            self.inOrder(root.right)

    def DFS(self, root):
        if root is None:
            return None
        queue = [root]
        while queue:
            node = queue[0]
            queue = queue[1:]
            print(node.value, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


ip = [1, 2, 3, 4, 5, 5, 6]
tree = BinaryTree()
for i in ip:
    tree.insert_recursion(i)

tree.DFS(tree.root)
# root = tree.root
# print(root.left.value)
# print(root.right.value)
# print(root.value)
# print(root.left.left.value)
# print(root.left.left.left.value)
