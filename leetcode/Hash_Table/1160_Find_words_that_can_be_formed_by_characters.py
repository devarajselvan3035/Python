"""
1160. Find Words That Can Be Formed By Characters
=================================================
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).

Return the sum of lengths of all good strings in words.

Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
"""

from typing import List


def countCharacters(words: List[str], chars: str) -> int:
    res = 0
    for word in words:
        flag = 0
        for char in word:
            if char not in chars:
                flag = 1
                break
        if flag == 0:
            res += len(word)

    return res


words, chars = ["cat", "bt", "hat", "tree"], "atach"
words, chars = ["hello", "world", "leetcode"], "welldonehoneyr"
print(countCharacters(words, chars))
