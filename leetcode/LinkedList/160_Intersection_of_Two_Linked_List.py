"""
Given the heads of two singley Linked-lists headA and headB, return the node at which
the two list intersect. If the two linked lists have no intersection at all, return null.

#Example 1
1->4->1
       \
        8->4->5
       /
5->6->1
Input: headA = [1,4,1,8,4,5], headB = [5,6,1,8,4,5]
Output: 8
"""

from Singel_LinkedList import LinkedList, Node


def getIntersectionNode(headA: Node, headB: Node) -> Node:
    headA_add = []
    while headA:
        headA_add.append(headA)
        headA = headA.next
    print(headA_add)


llA = LinkedList()
llB = LinkedList()
llC = LinkedList()

for A in range(3, 6):
    llA.append(A)

for B in range(1, 4):
    llB.append(B)

for C in range(8, 10):
    llB.append(C)

llACurdNode = llA.head
while llACurdNode.next:
    llACurdNode = llACurdNode.next
llACurdNode.next = llC.head

llBCurdNode = llB.head
while llBCurdNode.next:
    llBCurdNode = llBCurdNode.next
llBCurdNode.next = llC.head

headA = llA.head
while headA:
    print(headA.value)
    headA = headA.next


# print(getIntersectionNode(llA.head, llB.head))
