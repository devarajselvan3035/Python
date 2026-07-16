"""
67. Add Binary (*)
Given two binary strings a and b, return their sum as a binary strings.

Example 1:
Input: a = '11', b = '1'
Output: '100'
"""


def addBinary(a: str, b: str) -> str:
    res = []
    carry = 0

    # Start pointers at the end of both strings
    i = len(a) - 1
    j = len(b) - 1

    # Loop as long as there are digits to process or a leftover carry
    while i >= 0 or j >= 0 or carry:
        # Get the digital value (or 0 if we've run out of digits)
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0

        # Calculate the sum for the current column
        total = digit_a + digit_b + carry

        # Determine the binary digit to write down and the new carry
        current_digit = total % 2
        carry = total // 2

        # Append the digit to our result list
        res.append(str(current_digit))

        # Move pointers left
        i -= 1
        j -= 1

    # Since we added digits from right to left, reverse the result list
    return "".join(res[::-1])


def addBinary2(a: str, b: str) -> str:
    return str(bin(int(a, 2) + int(b, 2))[2:1])


def addBinary1(a: str, b: str) -> str:
    if len(a) < len(b):
        return addBinary(b, a)

    res: str = ""
    rem: int = 0
    diff: int = len(a) - len(b)
    b = "0" * diff + b

    for i in range(len(a) - 1, -1, -1):
        add: int = (ord(a[i]) + ord(b[i])) - (2 * ord("0")) + rem
        if add == 2:
            add = 0
            rem = 1
        else:
            rem = 0
        res = str(add) + res
        print(add, res, rem)

    return str(rem) + res if rem == 1 else res


a, b = "1010", "1011"
print(addBinary(a, b))
