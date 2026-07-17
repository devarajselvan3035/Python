"""
24. Swap Nodes in Pairs
=======================
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem
without modifying the values in the list's nodes (i.e, only nodes themselves may be changed)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]
Explanation
1->2->3->4
2->1->4->3
"""

from Singel_LinkedList import LinkedList, Node
from typing import Optional


def swapPairs(head: Optional[Node]) -> Optional[Node]:
    if head is None:
        return None
    dummy = Node(0, head)
    left = head
    right = head.next
    head = dummy

    # print(left.value, right.value, dummy.value, head.value)

    while left and right:
        temp = right.next
        dummy.next = right
        right.next = left
        left.next = temp
        dummy = left

        left, right = right, left

        # print(f"left : {left.value} right : {right.value} dummy : {dummy.value}")

        if not left.next.next or not right.next.next:
            break
        left = left.next.next
        right = right.next.next
    return head.next


# ip = [1, 2, 3, 4]
ip = [1, 2, 3]
ll = LinkedList()
for i in ip:
    ll.append(i)

head = swapPairs(ll.head)
# head = ll.head
while head:
    print(head.value)
    head = head.next
