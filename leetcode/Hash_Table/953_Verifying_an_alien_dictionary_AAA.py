"""
953. Verifying an Alien Dictionary
==================================
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
"""

from typing import List


def isAlienSorted(words: List[str], order: str) -> bool:
    orderIdx = {val: idx for idx, val in enumerate(order)}
    n = len(words)

    for i in range(n - 1):
        w1, w2 = words[i], words[i + 1]

        for j in range(len(w1)):
            if j == len(w2):
                return False

            if orderIdx[w1[j]] != orderIdx[w2[j]]:
                if orderIdx[w1[j]] > orderIdx[w2[j]]:
                    return False
                break
    return True


def isAlienSorted1(words: List[str], order: str) -> bool:
    orderIdx = {val: idx for idx, val in enumerate(order)}
    n = len(words)
    for i in range(n - 1):
        if orderIdx[words[i][0]] > orderIdx[words[i + 1][0]]:
            return False

        if orderIdx[words[i][0]] == orderIdx[words[i + 1][0]]:
            il, ir = 0, 0
            while il < len(words[i]) and ir < len(words[i + 1]):
                if orderIdx[words[i][il]] > orderIdx[words[i + 1][ir]]:
                    return False

                if orderIdx[words[i][il]] < orderIdx[words[i + 1][ir]]:
                    break

                il += 1
                ir += 1

            if len(words[i]) > len(words[i + 1]):
                return False

    return True


words, order = ["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"
words, order = ["apple", "app"], "abcdefghijklmnopqrstuvwxyz"
print(isAlienSorted(words, order))
