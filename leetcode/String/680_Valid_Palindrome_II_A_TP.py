"""
680. Valid Palindrome II(*)(TP)
========================
Given a string s, return true if the s can be palindrome after deleting at most one chracter form it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false
"""


def validPalindrome(s: str) -> bool:
    # Helper function to check if a substring is a standard palindrome
    def is_palindrome(left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left = 0
    right = len(s) - 1

    while left < right:
        # If characters match, just move the pointers inward
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            # Mismatch found! Check both deletion options:
            # Option 1: Skip the left character -> check s[left + 1 : right]
            # Option 2: Skip the right character -> check s[left : right - 1]
            return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)

    return True


# s = "aba"
s = "abca"
# s = "abc"
print(validPalindrome(s))
