## Define the node for store the data
class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.value = None
        self.parent = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    # Time complexity best and average => O(log n), Worst => O(n)
    def insert(self, key) -> None:
        newNode = Node(key)
        if self.root is None:
            self.root = newNode
        else:
            curdNode = self.root
            while True:
                if key < curdNode.key:
                    if curdNode.left is None:
                        curdNode.left = newNode
                        newNode.parent = curdNode
                        break
                    else:
                        curdNode = curdNode.left
                elif key > curdNode.key:
                    if curdNode.right is None:
                        curdNode.right = newNode
                        newNode.parent = curdNode
                        break
                    else:
                        curdNode = curdNode.right

    def delete(self, key) -> None:
        node = self.search(key)
        if node is None:
            raise ValueError("Given value not in the tree")
        else:
            self._delete(node)

    def search(self, key):
        curdNode = self.root
        while curdNode is not None:
            if curdNode.key == key:
                return curdNode
            elif key < curdNode.key:
                curdNode = curdNode.left
            else:
                curdNode = curdNode.right
        return None

    def _delete(self, node) -> None:
        ## Delete leaf node => Delete node without any child
        parentNode = node.parent
        if parentNode.right == node:
            parentNode.right = None
        else:
            parentNode.left = None

    def _in_oreder_traversel(self, node) -> None:
        if node:
            self._in_oreder_traversel(node.left)
            print(node.key, end=" ")
            self._in_oreder_traversel(node.right)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(8)
    bst.insert(9)
    bst.insert(1)
    bst.delete(1)
    bst._in_oreder_traversel(bst.root)
