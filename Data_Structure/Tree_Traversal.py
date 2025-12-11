from Binary_Tree import BinaryTree, Node


class Traversal:

    def __init__(self, arr_val:list) -> None:
        self.arr_val = arr_val

    def createTree(self) -> Node:
        btree = BinaryTree()
        for v in self.arr_val:
            btree.insert(v)
        return btree.root
    
    def inorder(self) -> None:
        print("Inorder Traversal")
        treeNode = self.createTree()
        self._inorder(treeNode)

    def _inorder(self, root:Node) -> None:
        if root:
            self._inorder(root.left)
            print(root.key, end=' ')
            self._inorder(root.right)

    def preorder(self) -> None:
        print("\nPreOrder Traversal")
        treeNode = self.createTree()
        self._preorder(treeNode)

    def _preorder(self, root:Node) -> None:
        if root:
            print(root.key, end = ' ')
            self._preorder(root.left)
            self._preorder(root.right)

    def postorder(self) -> None:
        print("\nPostOrder Traversal")
        treeNode = self.createTree()
        self._postorder(treeNode)

    def _postorder(self, root:Node) -> None:
        if root:
            self._postorder(root.left)
            self._postorder(root.right)
            print(root.key, end=' ')


if __name__ == "__main__":
    arr = [1,2,2,3,4,4,3,5,6,7,8,8,7,6,5]
    print(len(arr)//2)
    traver = Traversal(arr)
    traver.inorder()
    traver.preorder()
    traver.postorder()

