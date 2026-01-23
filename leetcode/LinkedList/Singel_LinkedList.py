class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, *values) -> None:
        self.head = None
        self.tail = None
        self.length = 0

        if values:
            for val in values:
                self.append(val)

    def __repr__(self) -> str:
        curNode = self.head
        vals = []
        while curNode:
            vals.append(str(curNode.value))
            curNode = curNode.next
        return ",".join(vals)

    def __contains__(self):
        pass

    # O(1) - Constant time complexity
    def __len__(self) -> int:
        return self.length

    # O(1) - Constant time complexity
    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    # O(1) - Constant time complexity
    def prepend(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insert(self, data, index):
        newNode = Node(data)
        if self.head is None:
            raise ValueError("List is Empty")
        elif index > self.length:
            raise IndexError("Index is out of the range")
        elif index == 0:
            self.prepend(data)
        else:
            curdNode = self.head
            for _ in range(index - 1):
                curdNode = curdNode.next
            newNode.next = curdNode.next
            curdNode.next = newNode

    def delete(self, data):
        curdNode = self.head
        if curdNode is None:
            raise ValueError("List is Empty")
        elif curdNode.value == data:
            self.head = curdNode.next
        else:
            while curdNode.next:
                if curdNode.next.value == data:
                    curdNode.next = curdNode.next.next
                    break
                curdNode = curdNode.next

    def pop(self):
        curdNode = self.head
        if self.head is None:
            raise ValueError("List is Empty")
        elif curdNode.next is None:
            self.head = None
        else:
            while curdNode.next.next:
                curdNode = curdNode.next
            curdNode.next = None

    def delete_idx(self, idx):
        curdNode = self.head
        if self.head is Node:
            raise ValueError("List is Empty")
        elif idx == 0:
            self.head = curdNode.next
        else:
            for _ in range(idx - 1):
                curdNode = curdNode.next
            curdNode.next = curdNode.next.next

    def reverse(self):
        self.head = self._reverse(self.head)

    def _reverse(self, node: Node = None):
        if node.next is None or node is None:
            return node
        head = self._reverse(node.next)
        curdNode = head
        while curdNode.next is not None:
            curdNode = curdNode.next

        node.next = None
        curdNode.next = node
        return head

    """
    intersect the two linked List
    1 -> 2 ->
              \
               -> 3 -> 4
              / 
         2 ->
    these two linked list intersect in one point
    """

    def intersect(self, list1: Node, list2: Node):
        pass

    def print(self):
        pass


arr = LinkedList(1, 2, 3, 4)
# arr.append(10)
# arr.append(11)
# arr.append(12)
# arr.prepend(9)
# arr.prepend(8)
# arr.insert(2, 2)
# arr.insert(5, 0)
# arr.delete(10)
# arr.delete(5)
# arr.pop()
# arr.pop()
# arr.delete_idx(0)
# arr.reverse()
# print(arr)
