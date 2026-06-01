class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def insertAtBeginning(self, data) -> None:
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

        self.size += 1

    def insertAtEnd(self, data) -> None:
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

        self.size += 1

    def insertAtPosition(self, data, index: int) -> None:
        newNode = Node(data)
        if index == 0:
            self.insertAtBeginning(data)
        elif index == self.size:
            self.insertAtEnd(data)
        else:
            prevNode = self.head
            for _ in range(index - 1):
                prevNode = prevNode.next

            newNode.next = prevNode.next
            newNode.prev = prevNode
            prevNode.next.prev = newNode
            prevNode.next = newNode
        self.size += 1

    def deleteFromBeginning(self) -> None:
        if self.size == 0:
            print("LinkedList in Empty")
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1

    def deleteFromEnd(self) -> None:
        if self.size == 0:
            print("LinkedList is Empty")
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

    def deleteAtPosition(self, index: int) -> None:
        if index == 0:
            self.deleteFromBeginning()
        elif index == self.size - 1:
            self.deleteFromEnd()
        else:
            curdNode = self.head
            for _ in range(index):
                curdNode = curdNode.next

            curdNode.prev.next = curdNode.next
            curdNode.next.prev = curdNode.prev
        self.size -= 1

    def traverseForward(self) -> None:
        head = self.head
        while head:
            if head.next is None:
                print(str(head.data))
            else:
                print(f"{head.data} -> ", end=" ")
            head = head.next

    def traverseBackward(self) -> None:
        tail = self.tail
        while tail:
            if tail.prev is None:
                print(str(tail.data))
            else:
                print(f"{tail.data} -> ", end=" ")
            tail = tail.prev

    def length(self) -> int:
        return self.size


# ll = LinkedList()
# ll.insertAtBeginning(1)
# ll.insertAtEnd(2)
# ll.insertAtBeginning(3)
# ll.insertAtEnd(4)
# ll.insertAtPosition(5, 2)
# print(ll.length())
# ll.deleteFromBeginning()
# ll.deleteFromEnd()
# ll.deleteAtPosition(2)
# print(ll.length())
# ll.traverseForward()
# ll.traverseBackward()
# print(ll.length())
