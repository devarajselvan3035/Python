"""
Find All Permutations
=====================
    Return all possible permutatins of a given array for unique integers. They
can be returned in any order.
Examples:
Input: nums = [4,5,6]
>[!note] -> Coding interview pattern(Book) - page.no 298
"""


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-2) + fibonacci(n-1)
print(fibonacci(5))
