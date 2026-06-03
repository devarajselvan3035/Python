class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None


class Tree:
    def __init__(self) -> None:
        self.root = None
        self.depth = 0

    def insert(self, data) -> None:
        newNode = Node(data)
        if self.root is None:
            self.root = newNode

        else:
            queue = [self.root]

            while True:
                curdNode = queue[0]
                queue = queue[1:]

                if curdNode.left is None:
                    curdNode.left = newNode
                    return
                else:
                    queue.append(curdNode.left)

                if curdNode.right is None:
                    curdNode.right = newNode
                    return
                else:
                    queue.append(curdNode.right)

    def insert_bts(self, data: int) -> None:
        self.root = self._insert_bts_helper(self.root, data)

    def _insert_bts_helper(self, node: Node, val: int) -> Node:
        if node is None:
            return Node(val)

        if val < node.data:
            node.left = self._insert_bts_helper(node.left, val)
        else:
            node.right = self._insert_bts_helper(node.right, val)
        return node

    def traverseInOrder(self, node: Node) -> None:
        if node:
            self.traverseInOrder(node.left)
            print(node.data, end=" ")
            self.traverseInOrder(node.right)

    def traversePreorder(self, node: Node) -> None:
        if node:
            print(node.data, end=" ")
            self.traversePreorder(node.left)
            self.traversePreorder(node.right)

    def traversePostOrder(self, node: Node) -> None:
        if node:
            self.traversePostOrder(node.left)
            self.traversePostOrder(node.right)
            print(node.data, end=" ")


bt = Tree()
arr = [6, 3, 5, 7, 2, 9]
for val in arr:
    bt.insert_bts(val)

bt.traverseInOrder(bt.root)
print()
bt.traversePreorder(bt.root)
print()
bt.traversePostOrder(bt.root)
