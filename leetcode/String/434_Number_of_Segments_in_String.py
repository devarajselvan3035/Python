"""
434. Number of Segments in a String
===================================
Given a string s, return the number of segments in the string

A segment is defined to be a contiguous sequence of non-space characters.

Example 1:
Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

Example 2:
Input: s = "Hello"
Output: 1
"""


def countSegments(s: str) -> int:
    split_s = s.split()
    return len(split_s)


def countSegments1(s: str) -> int:
    split_s = s.split(" ")
    res = 0
    for w in split_s:
        if w != "":
            res += 1

    return res


# s = "Hello, my name is John"
# s = "hello"
s = "            "
print(countSegments(s))
