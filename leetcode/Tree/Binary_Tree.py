class TreeNode:
    def __init__(self) -> None:
        self.val = None
        self.left = None
        self.right = None
        self.parent = None


class Tree:
    def __init__(self) -> None:
        self.head = TreeNode()
        self.queue = [self.head]

    def insert(self, values) -> None:
        for val in values:
            # basically queue(FIFO) datastructure vary userful for insert data in tree datastructure
            parent = self.queue[0]
            self.queue = self.queue[1:]
            # Set value for the selected parent node
            parent.val = val
            # Create left and right node for parent node
            leftNode = TreeNode()
            rightNode = TreeNode()
            # make connection between left and right node for parent node
            parent.left = leftNode
            parent.right = rightNode
            # Make connection between parent node to left and right node
            leftNode.parent = parent
            rightNode.parent = parent
            # Now add the two left and right node to the queue
            self.queue.append(leftNode)
            self.queue.append(rightNode)

    def bfs(self) -> None:
        curdNode = self.head
        inner_queue = [curdNode]
        while inner_queue:
            parentNode = inner_queue[0]
            inner_queue = inner_queue[1:]
            print(parentNode.val)

            if parentNode.left.val:
                inner_queue.append(parentNode.left)
            if parentNode.right.val:
                inner_queue.append(parentNode.right)

    def inOrder(self, node):
        if node:
            self.inOrder(node.left)
            print(node.val)
            self.inOrder(node.right)


arr = [1, 2, 3, None, 5]
tree = Tree()
tree.insert(arr)
tree.bfs()
tree.inOrder(tree.head)
