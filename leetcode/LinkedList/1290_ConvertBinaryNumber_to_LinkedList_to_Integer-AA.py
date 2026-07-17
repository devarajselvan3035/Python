"""
1290. Convert Binary Number in a Linked List to Integer
=======================================================
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in linked list

The most significant bit is at the head of the linked list.
"""

from Singel_LinkedList import LinkedList, Node
from typing import Optional, get_args


def getDecimalValue(head: Optional[Node]) -> int:
    decimal: int = 0
    while head:
        decimal = (2 * decimal) + head.value
        head = head.next
    return decimal


def getDecimalValue1(head: Optional[Node]) -> int:
    binary_list: list = []
    decimal: int = 0
    while head:
        binary_list.append(head.value)
        head = head.next
    power = len(binary_list) - 1
    for b in binary_list:
        decimal += b * (2**power)
        power -= 1
    return decimal


ip = [1, 0, 1]
ll = LinkedList()
for i in ip:
    ll.append(i)
print(getDecimalValue(ll.head))
