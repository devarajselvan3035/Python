
class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, data, id) -> None:
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            cur_node = self.head
            cur_id = 0
            while cur_id < id-1:
                cur_node = cur_node.next
                cur_id += 1
            next_node = cur_node.next

            cur_node.next = newnode
            next_node.prev = newnode
            newnode.prev = cur_node
            newnode.next = next_node
        self.length += 1

    def add_first(self, data) -> None:
        newnord = Node(data)
        if self.head is None:
            self.head = newnord
            self.tail = newnord
        else:
            temp = self.head
            self.head = newnord
            self.head.next = temp
            temp.prev = self.head
        self.length += 1

    def add_last(self, data) -> None:
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            temp = self.tail
            self.tail = newnode
            self.tail.prev = temp
            temp.next = self.tail
        self.length += 1

    def remove_first(self) -> None:
        if self.length == 0:
            print('list is empty')
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1

    def remove_last(self) -> None:
        if self.length == 0:
            print('List is empty')
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1

    def remove_index(self, id):
        if self.length == 0:
            print('List is empty')
        elif id == 0:
            self.head = self.head.next
            self.head.prev = None
        elif id == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            cur_node = self.head
            cur_id = 0
            while cur_id < id:
                cur_node = cur_node.next
                cur_id += 1

            cur_node.prev.next = cur_node.next
            cur_node.next.prev = cur_node.prev
        self.length -= 1

    def index(self, id) -> Node:
        cur_node = self.head
        cur_id = 0
        while cur_id < id:
            cur_node = cur_node.next
            cur_id += 1
        print(cur_node.data)
        return cur_node


    def print(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data, end = ' ')
            cur_node = cur_node.next


dll = DoubleLinkedList()
dll.add_last(1)
dll.add_last(2)
dll.add_last(3)
dll.add_first(2)
dll.add_first(3)
dll.add(0, 2)
dll.remove_first()
dll.remove_last()
dll.remove_index(1)
dll.remove_index(0)
dll.remove_index(1)
dll.print()
