"""
82. Remove Duplicates form Sorted List II
=========================================
Given the head of a sorted linked list, delete all nodes that have duplicate numbers. leaving only distinct
numbers form the original list. Return the linked list sorted as well.
Example 1:
Input  : 1->1->1->2->3
Output : 2->3
"""

from Singel_LinkedList import LinkedList, Node
from typing import Optional


def deleteDuplicates(head: Optional[Node]) -> Optional[Node]:
    not_add = 101
    res = Node(0)
    curdNode = res
    while head.next:
        # NOTE: First we check the if not_add have the value or head next value is head's value or not
        if head.value == not_add or head.next.value == head.value:
            not_add = head.value
        else:
            curdNode.next = Node(head.value)
            curdNode = curdNode.next
        head = head.next

    # NOTE: we add the final value if it's not equal to not_add value
    if head.value != not_add:
        curdNode.next = Node(head.value)

    return res.next


# ip = [1, 1, 1, 2, 3]
# ip = [1, 2, 2]
ip = [1, 2, 3, 3, 4, 4, 5]
ll = LinkedList()
for i in ip:
    ll.append(i)

head = deleteDuplicates(ll.head)
while head:
    print(head.value)
    head = head.next
