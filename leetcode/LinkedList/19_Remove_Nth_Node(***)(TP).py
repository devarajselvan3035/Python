"""
19. Remove Nth Node from end of list (***)(TP)
====================================
Given the head of a linked list, removes the nth node form the end of the list and return its head.
Example 1:
Input:
1->2->3->4->5
Output:
1->2->3->5
"""

from Singel_LinkedList import LinkedList, Node
from typing import Optional


# NOTE: Using TWO POINTER
"""
If we proceed without dummy node we moved one node extra
1 -> 2 -> 3 -> 4 -> 5 -> None
               l          R     
with the above format it's very difficult for remove 4 form the linked list 

with the dummy node,
Start with,
dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> None
  L      R     
End with,
dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> None
                   l               R
"""


def removeNthFromEnd(head: Optional[Node], n: int) -> Optional[Node]:
    dummy = Node(0, head)
    left = dummy
    right = head
    count = 0
    while count < n:
        right = right.next
        count += 1
    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy.next


# NOTE: using STACK or LIST
def removeNthFromEnd1(head: Optional[Node], n: int) -> Optional[Node]:
    length: int = 0
    curdNode = head
    while curdNode:
        length += 1
        curdNode = curdNode.next
    print(length)
    idx = length - n

    idxNode = head
    for _ in range(idx - 1):
        idxNode = idxNode.next

    idxNode.next = idxNode.next.next
    return head


# ip = [1, 2, 3, 4, 5]
ip = [1]
ll = LinkedList()
for i in ip:
    ll.append(i)
head = removeNthFromEnd(ll.head, 1)
while head:
    print(head.value)
    head = head.next
