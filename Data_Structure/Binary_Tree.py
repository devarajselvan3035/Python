from Queue import Queue


class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, key) -> None:
        newNode = Node(key)
        if self.root is None:
            self.root = newNode

        else:
            ## Create queue for level order terversal
            queue = Queue()
            queue.enqueue(self.root)

            while True:
                temp = queue.dequeue()
                ### If left is empty add newNode else, add left node in queue
                if temp.left is None:
                    temp.left = newNode
                    break
                else:
                    queue.enqueue(temp.left)

                ### If right is empty add newNode else, add right node in queue
                if temp.right is None:
                    temp.right = newNode
                    break
                else:
                    queue.enqueue(temp.right)

    def _in_order_traversal(self, node) -> None:
        if node:
            self._in_order_traversal(node.left)
            print(node.key, end=" ")
            self._in_order_traversal(node.right)


if __name__ == "__main__":
    node = Node(5)
    print(node, node.key)

    bt = BinaryTree()
    bt.insert(4)
    bt.insert(2)
    bt.insert(6)
    bt.insert(1)
    bt.insert(3)
    bt.insert(5)
    bt.insert(7)
    bt._in_order_traversal(bt.root)

    print()

    ### Invert BinaryTree
    def invertBinaryTree(node: Node) -> None:
        if not node:
            return None
        node.left, node.right = node.right, node.left
        invertBinaryTree(node.left)
        invertBinaryTree(node.right)
        return node

    root_node = invertBinaryTree(bt.root)
    bt._in_order_traversal(root_node)
