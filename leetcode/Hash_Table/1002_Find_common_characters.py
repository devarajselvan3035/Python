"""
1002. Find Common Characters
============================
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]
"""

from typing import List


def commonChars(words: List[str]) -> List[str]:
    minWord = min(words, key=len)
    minWordCount = wordCount(minWord)

:wqa:w===

def wordCount(s: str) -> dict
    count = {}
    for c in s:
        count[c] = count.setdefault(c, 0) + 1
    return count

      


words = ["bella", "label", "roller"]
print(commonChars(words))
