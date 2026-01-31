class Node:
    def __init__(self, value=None, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self) -> None:
        self.root = None
        self.stack = []

    # HACK: This insert method implemented using queue with the list function, This process
    def insert_queue(self, value) -> None:
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
        else:
            queue = []
            queue.append(self.root)

            while True:
                temp = queue[0]
                queue = queue[1:]

                if temp.left is None:
                    temp.left = newNode
                    break
                elif temp.left.value is not None:
                    queue.append(temp.left)

                if temp.right is None:
                    temp.right = newNode
                    break
                elif temp.right.value is not None:
                    queue.append(temp.right)

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
