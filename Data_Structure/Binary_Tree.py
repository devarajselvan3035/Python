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
    """
    100. Same Tree
    ===============
    Given the roots of two binary trees 'p' and 'q', write a fucntion to check if
    they are same or not. Two binary trees are considered the same if they are structurally 
    identiacl, and the nodes have the same value.
    """
    p_arr, q_arr = [1, 2, 3], [1, 2, 3]

    def createTree(arr:list) -> Node:
        tree = BinaryTree()
        for v in arr:
            tree.insert(v)
        return tree.root

    p = createTree(p_arr)
    q = createTree(q_arr)

    def isSameTree(p:Node, q:Node) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None or p.key != q.key:
            return False
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

    print(isSameTree(p, q))


  
