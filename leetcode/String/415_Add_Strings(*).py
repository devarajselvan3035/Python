"""
415. Add Strings(*)
================
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string

You mus solve the problem without using any built-in libraty for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"
"""


def addStrings(num1: str, num2: str) -> str:
    res = []
    carry = 0

    # Start pointers at the end of both strings
    i = len(num1) - 1
    j = len(num2) - 1

    # Loop as long as there are digits to process or a leftover carry
    while i >= 0 or j >= 0 or carry:
        # Get the digit values (or 0 if we've run out of digits for that number)
        digit1 = ord(num1[i]) - ord("0") if i >= 0 else 0
        digit2 = ord(num2[j]) - ord("0") if j >= 0 else 0

        # Calculate sum and new carry
        total = digit1 + digit2 + carry
        carry = total // 10
        current_digit = total % 10

        # Append the current digit to our results list
        res.append(str(current_digit))

        # Move pointers left
        i -= 1
        j -= 1

    # Since we added digits from right to left, reverse the result list
    return "".join(res[::-1])


def addStrings1(num1: str, num2: str) -> str:
    res = ""
    rem = 0
    if len(num1) < len(num2):
        return addStrings(num2, num1)
    diff = len(num1) - len(num2)
    num2 = ("0" * diff) + num2
    for i in range(len(num1) - 1, -1, -1):
        add = (ord(num1[i]) + ord(num2[i])) - (2 * ord("0"))
        add += rem
        if add > 9:
            rem = add // 10
            add = add % 10
        else:
            rem = 0
        res = str(add) + res
    return str(rem) + res if rem != 0 else res


# num1, num2 = "11", "123"
# num1, num2 = "456", "77"
num1, num2 = "1", "9"
print(addStrings(num1, num2))


#
# for i in range(10):
#     print(ord(str(i)))
