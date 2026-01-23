"""
234. Palindrome Linked List (***)(TP)(STACK)
===========================
Given the head of a singly linked list, return true if it is a palindrome or false otherwise

Example 1:
1 -> 2 -> 2 -> 1
Input: head = [1,2,2,1]
output: True

Example 2
1 -> 2
Input: head = [1, 2]
Output: False
"""

from Singel_LinkedList import Node, LinkedList


# NOTE: O(n) Time Complexity and O(1) Space cimplexity using TWO POINTER
def isPalindrome(head: Node) -> bool:
    """
            The Slow and Fast Pointer technique involves two pointers moving through a data structure at different speeds. Typically, while the slow pointer advances by one node ($+1$), the fast pointer advances by two ($+2$). This method is an efficient algorithm for determining the midpoint of a linked list in a single pass.

    Step 1
        s
        1 2 3 2 1
        f

    Step 2
          s
        1 2 3 2 1
            f
    final Step
            s
        1 2 3 4 5
                f
    """
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    """
"The following method is utilized to reverse the nodes located after the slow pointer. This operation modifies the structure of the linked list as illustrated in the format below."
    Example 1:
    linked list 1->2->3->2->1
    l
    1 -> 2 
           \
            3 -> None
           /
    1 -> 2
    r
    2 next value address same for both nodes
    
    Example 2:
    linked list 1->2
    l
    1 
     \
      2 -> None
      r

    """
    nextNode = None
    while slow:
        temp = slow.next
        slow.next = nextNode
        nextNode = slow
        slow = temp

    left, right = head, nextNode
    while right:
        if left.value != right.value:
            return False
        left = left.next
        right = right.next

    return True


# NOTE: O(n+n) Time Complexity and O(n) Space Complexity With STACK
def isPalindrome1(head: Node) -> bool:
    stack = []
    curdNode = head
    while curdNode:
        stack.append(curdNode.value)
        curdNode = curdNode.next

    while head:
        if head.value != stack.pop():
            return False
        head = head.next

    return True


# ip = [1, 2, 3, 2, 1]
# ip = [1, 2]
ip = [1, 1, 2, 1]
ll = LinkedList()
for i in ip:
    ll.append(i)
print(isPalindrome(ll.head))
