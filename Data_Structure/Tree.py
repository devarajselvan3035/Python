class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = None


class Tree:
    def __init__(self) -> None:
        self.root = None

    def add(self, data, parentNode=None) -> None:
        if not self.root:
            self.root

    def findnode(self, data, startNode):
        if startNode.data == data:
            return startNode
        else:
            for child in startNode.children:
                self.findnode(data, child)  # pyright: ignore[reportUnusedCallResult]

