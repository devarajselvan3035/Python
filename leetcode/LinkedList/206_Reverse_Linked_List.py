"""
206. Reverse Linked List
========================
Given the head of a singly linked list, reverse the list, and return the reversed list

Example 1:
1 -> 2 -> 3 -> 4 -> 5
5 -> 4 -> 3 -> 2 -> 1
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""

from Singel_LinkedList import LinkedList, Node
from typing import Optional


def reverseList(head: Optional[Node]) -> Optional[Node]:
    curdNode = head
    nextNode = None
    while curdNode:
        temp = curdNode.next
        curdNode.next = nextNode
        nextNode = curdNode
        curdNode = temp

    return nextNode


ip: list = [1, 2, 3, 4, 5]
ll = LinkedList()
for i in ip:
    ll.append(i)
head: Node = reverseList(ll.head)
while head:
    print(head.value)
    head = head.next
