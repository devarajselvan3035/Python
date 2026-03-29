"""
819. Most Common Word
=====================
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insentive and the answer should be returned in lowercase.

Node: that words can not contain punctuation sysmbols.
"""

from re import split
from typing import List


def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    l, r = 0, 0
    flag = 0
    yes = False
    res = ""
    maxcount = 0
    count = {}
    while r < len(paragraph):
        if not paragraph[r].isalpha():
            yes = True
            if flag == 0:
                lowstr = paragraph[l:r].lower()
                count[lowstr] = count.setdefault(lowstr, 0) + 1
                if count[lowstr] > maxcount and lowstr not in banned:
                    res = lowstr
                    maxcount = count[lowstr]
            flag = 1
            r += 1
            l = r
        else:
            flag = 0
            r += 1

    return res if yes else paragraph


paragraph, banned = "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]
# paragraph, banned = "a.", []
# paragraph, banned = "Bob", []
print(mostCommonWord(paragraph, banned))
