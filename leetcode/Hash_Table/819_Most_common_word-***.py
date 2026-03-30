"""
819. Most Common Word (***)
=====================
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insentive and the answer should be returned in lowercase.

Node: that words can not contain punctuation sysmbols.
"""

from re import split
from typing import List


def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    wordCount = {}
    banned_words = set(banned)

    normParagraph = "".join([c.lower() if c.isalpha() else " " for c in paragraph])

    for word in normParagraph.split():
        if word not in banned_words:
            wordCount[word] = wordCount.setdefault(word, 0) + 1

    return max(wordCount, key=wordCount.get)


paragraph, banned = "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]
# paragraph, banned = "a.", []
# paragraph, banned = "Bob", []
print(mostCommonWord(paragraph, banned))
