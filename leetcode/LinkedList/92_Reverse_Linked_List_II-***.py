"""
92.Reverse Linked List II(***)
=========================
Given the head of a singly linked list and two integers left and right where left <= right.
Reverse the nodes of the list from position left to position right, and return the reversed list.

Example:
Input  : 1->2->3->4->5
Output : 1->4->3->2->5

Input : head = [1,2,3,4,5], left=2, right=4
Output: [1,4,3,2,5]
"""

from Singel_LinkedList import LinkedList, Node
from typing import Optional


# NOTE: O(n) time complexity and O(1) space complexity
def reverseBetween(head: Optional[Node], left: int, right: int) -> Optional[Node]:
    dummy = Node(0, head)
    curd = head
    count = 1
    leftmost = dummy

    while curd and curd.next:
        if count == left - 1:
            leftmost = curd
            curd = curd.next

        elif left <= count and count <= right:
            temp = leftmost.next
            leftmost.next = curd.next
            curd.next = curd.next.next
            leftmost.next.next = temp

        else:
            curd = curd.next
        count += 1

    return dummy.next


ip, l, r = [1, 2, 3, 4, 5], 2, 4
# ip, l, r = [5], 1, 1
ll = LinkedList()
for i in ip:
    ll.append(i)
head = reverseBetween(ll.head, l, r)
while head:
    print(head.value)
    head = head.next
