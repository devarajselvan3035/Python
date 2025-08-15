class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class doublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        curdNode = self.head
        vals = []
        while curdNode:
            vals.append(str(curdNode.data))
            curdNode = curdNode.next
        return "".join(vals)

    def __len__(self) -> int:
        pass

    def append(self, data) -> None:
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def prepend(self, data) -> None:
        newNode = Node(data)
        if self.head is Node:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            sefl.head = newNode

    def insert(self, data, idx) -> None:
        pass

    def delete(self, data):
        pass

    def pop(self):
        pass

    def delete_idx(self, idx):
        pass


if __name__ == "__main__":
    arr = doublyLinkedList()
    arr.append(10)
    arr.prepend(9)
    print(arr)
