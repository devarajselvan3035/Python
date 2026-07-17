"""
1684. Count the Number of Consistent Strings (**)
============================================

You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

Example 1:
Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

Example 2:
Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.

Example 3:
Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
"""

from typing import List


def countConsistentStrings(allowed: str, words: List[str]) -> int:
    ans = 0
    for word in words:
        cnt = 1
        for chr in word:
            if chr not in allowed:
                cnt = 0
                break

        ans += cnt
    return ans


def countConsistentStrings1(allowed: str, words: List[str]) -> int:
    def count(s: str) -> dict:
        res: dict = dict()
        for c in s:
            res[c] = res.setdefault(c, 0) + 1
        return res

    res = 0
    for word in words:
        wordCount = count(word)
        total = 0
        for chr in allowed:
            if chr in wordCount:
                total += wordCount[chr]
        if total == len(word):
            res += 1
    return res


allowed, words = "ab", ["ad", "bd", "aaab", "baa", "badab"]
allowed, words = "abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]
allowed, words = "cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
print(countConsistentStrings(allowed, words))
