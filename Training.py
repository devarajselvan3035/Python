class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

node = Node(1)
print(node)
