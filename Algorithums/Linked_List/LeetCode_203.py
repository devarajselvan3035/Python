# 203. Remove Linked List Elements
# Given the head of a linked list and an integer val, remove all the nodes of the
# linked list that has Node.val == val, and return the new head.

class Node:

    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self, *args) -> None:
        self.head = None
        self.tail = None
        self.length = None

        if args:
            for v in args:
                self.append(v)

    def append(self, data) -> None:
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode

    def remove_value(self, value) -> None:
        cur_node = self.head
        while cur_node is not None:
            next_node = cur_node.next
            if next_node is None:
                if cur_node.data == value:


            if next_node.data == value:
                cur_node.next = next_node.next
            else:
                cur_node = cur_node.next


    def print(self) -> None:
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data, end=',')
            cur_node = cur_node.next

arr = LinkedList(7,7,7,7)
arr.remove_value(7)
arr.print()
