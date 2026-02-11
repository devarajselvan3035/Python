from PrintTree import PrintTree


class Node:
    def __init__(self, value: None) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None
        self.queue = []
        self.leftChild = False
        self.rightChild = False

    def insert_queue(self, value) -> None:
        # NOTE: Check it the root node is empty and value without None otherwise if yes add first value to root node
        if self.root is None and value:
            self.root = Node(value)
            self.queue.append(self.root)
            return
        # NOTE: Below condition check curdNode both left and right nodes are filled something (value or None)
        if self.leftChild and self.rightChild:
            self.queue = self.queue[1:]
            self.leftChild, self.rightChild = False, False
        # NOTE: To ensure data integrity, the if statement validates that a node exists within the queue before any additional data is appended to it.
        if self.queue:
            curdNode = self.queue[0]
            # NOTE: Check if the left child is empty (without value or None) fill the value and change curdNode left child status to `True`.
            #
            if not self.leftChild:
                if value:
                    curdNode.left = Node(value)
                    self.queue.append(curdNode.left)
                self.leftChild = True

            # NOTE: Check if the right child is empty (without value or None) fill the value and change curdNode right child status to `True`.
            else:
                if value:
                    curdNode.right = Node(value)
                    self.queue.append(curdNode.right)
                self.rightChild = True
