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

    def insert(self, val) -> None:
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

    def preorder(self) -> None:
        curdNode = self.head
        self._preorder(curdNode)

    def _preorder(self, node):
        if node.val is None:
            return

        print(node.val)
        self._preorder(node.left)
        self._preorder(node.right)


if __name__ == "__main__":
    # list_val = [1, 2, 3, 4, 5]
    list_val = [1, 2, 4, 5, 3]

    tree = Tree()

    for val in list_val:
        tree.insert(val)

    print("BFS (Breath first search")
    tree.bfs()

    print("DFS (Depth first search) - preorder")
    tree.preorder()
