class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    """
    Creates a node and points its next pointer to the current head, then makes this new node the head.
    """

    def insertAtBeginning(self, data) -> None:
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            newNode.next = self.head
            self.head = newNode
        self.size += 1

    """
    Traverses to the end of the list, updates the last node's next pointer to point to the newly created node.
    """

    def insertAtEnd(self, data) -> None:
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    """: Traverses to the node just before the target index, adjusts pointers to splice the new node into the chain"""

    def insertAtPosition(self, data, index: int) -> None:
        newNode = Node(data)
        if index == 0:
            self.insertAtBeginning(data)
        elif index == self.size:
            self.insertAtEnd(data)
        else:
            start = self.head
            for _ in range(index - 1):
                start = start.next
                # print(start.data)

            newNode.next = start.next
            start.next = newNode
        self.size += 1

    """
    Removes the head node and promotes the next node in the chain to be the new head.
    """

    def deleteFromBeginning(self) -> None:
        if self.size == 0:
            print("LinkedList is Empty")
        else:
            self.head = self.head.next
        self.size -= 1

    """
    Traverses to the second-to-last node and sets its next pointer to null.
    """

    def deleteFromEnd(self) -> None:
        if self.size == 0:
            print("LinkedList is Empty")
        else:
            start = self.head
            for _ in range(self.size - 2):
                start = start.next
            start.next = None
            self.tail = start
        self.size -= 1

    """
    Skips over the node being deleted by updating the next pointer of the previous node to point to the node after it.
    """

    def deleteAtPosition(self, index: int) -> None:
        if index == 0:
            self.deleteFromBeginning()
        elif index == self.size - 1:
            self.deleteFromEnd()
        else:
            start = self.head
            for _ in range(index - 1):
                start = start.next
            start.next = start.next.next
        self.size -= 1

    """
    Steps sequentially from the head node to the tail, typically used to print the data in the list.
    """

    def traverse(self) -> None:
        start = self.head
        while start:
            if start.next is None:
                print(str(start.data))
            else:
                print(f"{start.data} -> ", end="")
            start = start.next

    """
    Traverses the list and checks if a specific value or key exists in any of the nodes.
    """

    def search(self, data) -> bool:
        start = self.head
        while start:
            if start.data == data:
                return True
        return False

    """
    Iterates through the chain while counting the nodes to return the total number of elements.
    """

    def Size(self) -> int:
        return self.size

    """
    Iteratively or recursively flips the direction of the next pointers so the tail becomes the new head.
    """

    def reverseList(self) -> None:
        curdNode = self.head
        nextNode = None

        while curdNode:
            temp = curdNode.next
            curdNode.next = nextNode
            nextNode = curdNode
            curdNode = temp

        self.head = nextNode
        
    def cycleList(self) -> None:
        self.tail.next = self.head


# ll = LinkedList()
# ll.insertAtBeginning(1)
# ll.insertAtBeginning(2)
# ll.insertAtEnd(3)
# ll.insertAtEnd(4)
# ll.insertAtPosition(8, 3)
# ll.deleteFromBeginning()
# ll.deleteFromEnd()
# ll.deleteAtPosition(1)
# ll.traverse()
# print(ll.search(1))
# print(ll.Size())
# ll.reverseList()
# ll.traverse()
