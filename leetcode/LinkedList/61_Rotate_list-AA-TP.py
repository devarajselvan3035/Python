"""
61. Rotate List (**)(TP)
===============
Given the head of linked list, rotate the list to the right by k places.

Example 1
input    : 1->2->3->4->5
rotate 1 : 5->1->2->3->4
rotate 2 : 4->5->1->2->3
"""

from Singel_LinkedList import LinkedList, Node
from typing import Optional


def rotateRight(head: Optional[Node], k: int) -> Optional[Node]:
    right = head
    left = head
    length = 0
    curdNode = head
    while curdNode:
        length += 1
        curdNode = curdNode.next

    k %= length

    while 0 < k and right:
        right = right.next
        k -= 1
        if right is None:
            right = head

    if left == right:
        return head

    while right.next:
        left = left.next
        right = right.next

    print(right.value, left.value)
    #
    right.next = head
    head = left.next
    left.next = None

    return head


ip, k = [1, 2, 3, 4, 5], 10
# ip, k = [0, 1, 2], 4
ll = LinkedList()
for i in ip:
    ll.append(i)
head = rotateRight(ll.head, k)

while head:
    print(head.value)
    head = head.next
