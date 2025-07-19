# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self, *args) -> None:
        self.head = None
        self.tail = None
        self.length = 0

        for v in args:
            self.append(v)

    def append(self, data) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def print(self, *head) -> None:
        curd_node = head[0] if head else self.head
        while curd_node is not None:
            print(curd_node.data, end=',')
            curd_node = curd_node.next
        print()

arr1 = LinkedList(2,4,3)
arr2 = LinkedList(5,6,4)

def revers_list(head) -> int:
    curd_node = head
    ans = 0
    multi = 1
    while curd_node is not None:
        ans += curd_node.data * multi
        multi *= 10
        curd_node = curd_node.next
    return ans

sum = revers_list(arr1.head) + revers_list(arr2.head)

while sum > 0:
    print(sum % 10)
    sum = sum // 10


arr1.print()
arr2.print()

print(revers_list(arr1.head) + revers_list(arr2.head))
