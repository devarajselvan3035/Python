class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    """
    enqueue(): These methods are used to add an element to the tail of the enqueue
    """

    # O(1) - constant time complexity
    def enqueue(self, data) -> None:
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    """
    dequeue(): This method are used to remove and return the element at the head of the queue
    """

    # O(1) - constant time complexity
    def dequeue(self):
        if self.head is None:
            raise ValueError("Queue is Empty")
        else:
            return_value = self.head.data
            self.head = self.head.next
        self.length -= 1
        return return_value

    """
    peek(): This method are used to retrive, but not remove, the elemetn at the head of the Queue
    """

    # O(1) - constant time complexity
    def peek(self):
        if self.head is None:
            raise ValueError("Queue is Empty")
        else:
            return self.head.data

    """
    isEmpty(): This method checks if the queue contains any elements and return True if it's empty,
    False otherwise
    """

    # O(1) - constant time complexity
    def isEmpty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False

    """
    size(): This method returns the total number of elements currently in the queue
    """

    # O(1) - constant time complexity
    def size(self) -> int:
        return self.length

    """
    show(): This method print all the elements inside the Queue
    """

    # O(1) - constant time complexity
    def show(self):
        curdNode = self.head
        while curdNode:
            print(curdNode.data)
            curdNode = curdNode.next


if __name__ == "__main__":
    que = Queue()
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    print(f"dequeue value {que.dequeue()}")
    que.show()
