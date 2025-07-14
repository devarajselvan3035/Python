class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Linkdelist:

    def __init__(self, *args) -> None:
        self.head = None
        self.tail = None
        self.lenght = None

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

    def __str__(self) -> str:
        cur_node = self.head
        ans = ''
        while cur_node is not None:
            ans += (str(cur_node.data) + ',')
            cur_node = cur_node.next
        return ans


list1 = Linkdelist(1,2,4)
list2 = Linkdelist(1,3,5)
print(list1, list2)

ans = Linkdelist()
while list1 and list2:
    print(ans)
    if list1 is not None and list1.head.data <= list2.head.data:
        ans.append(list1.head.data)
        list1.head = list1.head.next
    elif list2 is not None and list2.head.data < list1.head.data:
        ans.append(list2.head.data)
        list2.head = list2.head.next
