class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    # O(1) -> Constant time complexity
    def append(self, data) -> None:
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    # O(1) -> constant time complexity
    def prepend(self, data) -> None:
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.size += 1

    def insert(self, data, idx) -> None:
        newNode = Node(data)
        if self.head is None:
            raise ValueError("List is Empty")
        elif idx == 0:
            self.prepend(data)
        elif idx == self.size:
            self.append(data)
        else:
            curdNode = self.head
            for _ in range(idx):
                curdNode = curdNode.next
            newNode.next = curdNode
            newNode.prev = curdNode.prev
            curdNode.prev.next = newNode
            curdNode.prev = newNode
        self.size += 1

    def pop(self):
        return_value = self.tail.data
        if self.head is None:
            raise ValueError("List is Empty")
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return return_value

    def pop_first(self):
        return_value = self.head.data
        if self.head is None:
            raise ValueError("List is Empty")
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return return_value

    def delete(self, idx):
        if self.head is None:
            raise ValueError("List is Empty")
        elif idx == 0:
            self.pop_first()
        elif idx == self.size:
            self.pop()
        else:
            curdNode = self.head
            for _ in range(idx):
                curdNode = curdNode.next
            curdNode.prev.next = curdNode.next
            curdNode.next.prev = curdNode.prev
        self.size -= 1

    def show_straight(self) -> None:
        curdNode = self.head
        vals = []
        while curdNode:
            vals.append(str(curdNode.data))
            curdNode = curdNode.next
        print(" <-> ".join(vals))

    def show_reverse(self) -> None:
        curdNode = self.tail
        vals = []
        while curdNode:
            vals.append(str(curdNode.data))
            curdNode = curdNode.prev
        print(" <-> ".join(vals))


if __name__ == "__main__":
    arr = DoublyLinkedList()
    arr.append(10)
    arr.append(11)
    arr.append(12)
    arr.prepend(9)
    arr.prepend(8)
    arr.prepend(7)
    arr.insert(5, 3)
    arr.insert(0, 0)
    arr.insert(arr.size, arr.size)
    arr.show_straight()
    print(arr.pop())
    print(arr.pop_first())
    arr.delete(0)
    arr.show_straight()
    arr.show_reverse()
