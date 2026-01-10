"""
Given the heads of two singley Linked-lists headA and headB, return the node at which
the two list intersect. If the two linked lists have no intersection at all, return null.

"""

from Singel_LinkedList import LinkedList

arr = LinkedList(1, 2, 3, 4)
curdNode = arr.head
while curdNode:
    print(id(curdNode))
    curdNode = curdNode.next


arr = set()
arr.add(10)
