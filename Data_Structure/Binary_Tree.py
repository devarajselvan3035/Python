class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None


if __name__ == "__main__":
    node = Node(5)
    print(node, node.key)
