"""
86. Partition List (***)(TP)
==================
Given the head of a linked list and a value x, Partition it such that all nodes less than x come
before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the tow Partition.
Example 1:
1->4->3->2->5->2
1->2->2->3->3->5
"""

from Singel_LinkedList import LinkedList, Node
from typing import Optional


# NOTE: This process have 2 list of extra space.
def partition(head: Optional[Node], x: int) -> Optional[Node]:
    left, right = Node(), Node()
    ltail, rtail = left, right

    while head:
        if head.value < x:
            ltail.next = head
            ltail = ltail.next
        else:
            rtail.next = head
            rtail = rtail.next

        head = head.next

    ltail.next = right.next
    rtail.next = None
    return left.next


# NOTE: Properway way for the process without any extra list space
def partition1(head: Optional[Node], x: int) -> Optional[Node]:
    dummy = Node(0, head)
    left = dummy
    right = dummy

    while right and right.next:
        if right.next.value < x and left == right:
            left = left.next
            right = right.next

        elif right.next.value < x:
            temp = left.next
            left.next = right.next
            right.next = right.next.next
            left.next.next = temp

            left = left.next
        else:
            right = right.next

    return dummy.next


# ip = [1, 4, 3, 2, 5, 2]
# ip = [1, 2, 2, 4, 3, 5]
# ip, x = [2, 1], 2
ip, x = [1, 4, 3, 0, 2, 5, 2], 3
ll = LinkedList()
for i in ip:
    ll.append(i)

head = partition(ll.head, x)
while head:
    print(head.value, end=" ")
    head = head.next
