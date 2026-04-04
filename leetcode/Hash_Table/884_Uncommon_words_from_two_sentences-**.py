"""
884. Uncommon Words form Two Sentence
=====================================

A sentence is a string of single-space separated words where each word consists only of lowercase letters.
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

Example 1:
Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Explanation:
The word "sweet" appears only in s1, while the word "sour" appears only in s2.

Example 2:
Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]
"""

from typing import List


def uncommonFromSetntences(s1: str, s2: str) -> List[str]:
    allWords = s1.split() + s2.split()
    wordCount = {}
    for aw in allWords:
        wordCount[aw] = wordCount.setdefault(aw, 0) + 1
    return [word for word, count in wordCount.items() if count == 1]


def uncommonFromSetntences1(s1: str, s2: str) -> List[str]:

    res = []

    def wordCount(s: str) -> dict:
        count = {}
        for w in s.split():
            count[w] = count.setdefault(w, 0) + 1
        return count

    s1Count = wordCount(s1)
    s2Count = wordCount(s2)

    print(s1Count, s2Count)

    for w, c in s1Count.items():
        if w not in s2Count and c == 1:
            res.append(w)

    for w, c in s2Count.items():
        if w not in s1Count and c == 1:
            res.append(w)

    return res


s1, s2 = "this apple is sweet", "this apple is sour"
s1, s2 = "apple", "banana"
s1, s2 = "d b zu d t", "udb zu ap"
print(uncommonFromSetntences(s1, s2))
