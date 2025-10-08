class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Linkdelist:

    def __init__(self, *args) -> None:
        self.head = None
        self.tail = None
        self.length = 0

        if args:
            i = 0
            while i < len(args):
                self.append(args[i])
                i+=1

    def append(self, data) -> None:
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
        self.length += 1

    def reverse(self) -> Node:
        curd_node = self.head
        prev_node = None
        while curd_node is not None:
            next_node = curd_node.next
            curd_node.next = prev_node
            prev_node = curd_node
            curd_node = next_node
        return prev_node

    def remove_wiht_index(self, pos) -> None:
        curd_node = self.head
        if pos == 1:
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
        id = 2
        next_node = curd_node.next
        while next_node is not None:
            if id == pos:
                curd_node.next = next_node.next
                break
                curd_node = next_node
                next_node = next_node.next


    def check_duplicate(self, arr, data) -> bool:
        curd_node = arr
        while curd_node is not None:
            if curd_node.data == data:
                return True
            curd_node = curd_node.next
        return False

    def remove_duplicate(self) -> None:
        temp_node = Node(self.head.data)
        nd_head = temp_node
        nd_tail = temp_node
        curd_node = self.head.next
        while curd_node is not None:
            print(f' current_data {curd_node.data}')
            if not self.check_duplicate(nd_head, curd_node.data):
                print(self.check_duplicate(nd_head, curd_node.data))
                new_node = Node(curd_node.data)
                nd_tail.next = new_node
                nd_tail = new_node
            curd_node = curd_node.next
        self.print(nd_head)

    def remove_duplicate_sorted(self) -> None:
        temp = Node(self.head.data)
        rds_head = temp
        rds_tail = temp
        curd_node = self.head.next
        while curd_node is not None:
            if curd_node.data != rds_tail.data:
                new_node = Node(curd_node.data)
                rds_tail.next = new_node
                rds_tail = new_node
            curd_node = curd_node.next
        self.print(rds_head)

    def len(self) -> int:
        length = 0
        curd_node = self.head
        while curd_node is not None:
            length += 1
            curd_node = curd_node.next
        return length

    def print(self, *head):
        curd_node = head[0] if head else self.head
        while curd_node is not None:
            print(curd_node.data, end=',')
            curd_node = curd_node.next



arr = Linkdelist(1,2,2,3,3,3,4,4,4,4,5,5,5,5,5)
# print(arr.check_duplicate(arr.head, 3))
# arr.remove_duplicate()
arr.remove_duplicate_sorted()
# print(arr.palindrome())
