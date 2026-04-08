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
    res = []
    commonCount = wordCount(words[0])
    for word in words:
        count = wordCount(word)
        for cw, cc in commonCount.items():
            if cw in count:
                commonCount[cw] = min(cc, count[cw])
            else:
                commonCount[cw] = 0

    for w, c in commonCount.items():
        res += [w] * c

    return res


def wordCount(s: str) -> dict:
    count: dict = {}
    for c in s:
        count[c] = count.setdefault(c, 0) + 1
    return count


words = ["bella", "label", "roller"]
# words = ["cool", "lock", "cook"]
print(commonChars(words))
