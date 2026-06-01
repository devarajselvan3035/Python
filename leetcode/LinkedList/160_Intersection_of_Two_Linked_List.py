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


def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    hashsetA = set()
    while headA:
        hashsetA.add(headA)
        headA = headA.next

        while headB:
            if headB in hashsetA:
                return headB
            headB = headB.next
        return None
