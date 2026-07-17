"""
696. Count Binary Substrings(**)(TP)
============================
Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:
Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
"""


def countBinarySubstrings(s: str) -> int:
    ans = 0
    prev_group = 0
    curr_group = 1  # Start at 1 because we always have at least the first character

    for i in range(1, len(s)):
        # If the character changes, the group changes
        if s[i] != s[i - 1]:
            # Add the valid combinations formed by the last two groups
            ans += min(prev_group, curr_group)
            # Move current group to previous, reset current group to 1
            prev_group = curr_group
            curr_group = 1
        else:
            # Same character, increment the current group size
            curr_group += 1

    # Don't forget to add the combinations for the very last group pair!
    ans += min(prev_group, curr_group)

    return ans


s = "00110011"
# s = "10101"
print(countBinarySubstrings(s))
