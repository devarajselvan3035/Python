"""
Reverse String using Recursion
===============================
ip = hello world
op = dlrow olleh
"""


def reverse(string: str) -> str:
    if len(string) == 1:
        return string[0]
    return reverse(string[1:]) + string[0]


# print(reverse("hello world"))

"""
check Palindrome using Recursion
===================================
Check given ip and reverced ip both are same

ip = kayak
op = True
"""


def Palindrome(string: str) -> bool:
    if len(string) == 1 or len(string) == 0:
        return True
    if string[0] == string[-1]:
        return Palindrome(string[1:-1])
    return False


# print(Palindrome("raccar"))

"""
Decimal to Binary
====================
ip = 233
op = 11101001
"""


def decimalTobinary(dec: int) -> str:
    if dec <= 1:
        return str(dec)
    return decimalTobinary(dec // 2) + str(dec % 2)


print(decimalTobinary(233))

"""
Sum of Natural Numbers
"""
