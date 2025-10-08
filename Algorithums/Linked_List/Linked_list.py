class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, *args) -> None:
        self.head = None
        self.tail = None
        self.length = 0

        if args:
            i = 0
            while i < len(args):
                self.add_last(args[i])
                i+=1

    # Add data inside the linked list with index. If mentioned out of the range index
    # it raise errorr.
    # Args:
    #     Data, id (index for the data)
    def add(self,data, id):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        elif id == 0:
            temp = self.head
            self.head = newnode
            self.head.next = temp
        elif id == self.length:
            self.tail.next = newnode
            self.tail = newnode
        elif id > self.length-1:
            print('index out of the range')
        else:
            cur_node = self.head
            cur_id = 0
            while cur_id < id-1:
                cur_node = cur_node.next
            next_node = cur_node.next
            cur_node.next = newnode
            newnode.next = next_node
        self.length += 1

    # Add data in tail of the Linked list
    # args => data
    def add_last(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
        self.length += 1

    # Add data in head of the Linked List
    # Args => data
    def add_first(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode
        self.length += 1

    # Remove data from given index inside the Linked List
    # Args => data, id
    def remove(self, id):
        if self.head is None:
            print('List is empty')
        elif id == 0:
            self.head = self.head.next
        else:
            prv_node = self.head
            cur_id = 1
            while cur_id < id:
               prv_node = prv_node.next
               cur_node = prv_node.next
               cur_id += 1
               prv_node.next = cur_node.next
        self.length -= 1


    # Remove data from tail of the Linked list
    # Args => No
    def remove_last(self):
        if self.head is None:
            print('your list is empty')
        elif self.head.next is None:
            self.head = None
        else:
            cur = self.head
            while cur.next.next is not None:
                cur = cur.next
            cur.next = None
        self.length -= 1

    # Remove data from head of the Linkde List
    # Args => no
    def remove_first(self):
        if self.head is None:
            print('your list is empty')
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
        self.length -= 1

    # Remove all given values from the linked list
    # Args => Data
    def remove_values(self, data):
        curd_node = self.head
        while curd_node is not None:
            next_node = curd_node.next
            if next_node.data == data:
                curd_node.next = next_node.next
                curd_node = curd_node.next


    # Print the given index value (index start form the 0)
    # Args => id
    def index(self, id):
        if id >= self.length:
            print('index out of the range')
        else:
            cur_id = 0
            value_id = self.head
            while cur_id < id:
                value_id = value_id.next
                cur_id += 1
            print(value_id.data)

    # Pring full length for the Linked List
    def len(self):
        print(self.length)

    # Pring all the value inside the Linked List with space seperated
    # Args => No
    def print(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.next

# ll.append(0)
ll = LinkedList(1,2,6,3,4,5,6)
# ll.add_first(1)
# ll.add_last(2)
# ll.add_first(3)
# ll.add_last(4)
ll.index(4)
# ll.print()
# ll.len()

# ll.add(1, 5)
# ll.add(2, 0)
# ll.add(4, 1)
# ll.add_first(10)
# # ll.add(5, 1)
# ll.remove(0)
# ll.remove(4)
ll.print()
