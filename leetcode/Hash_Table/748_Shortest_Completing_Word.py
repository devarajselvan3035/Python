"""
748. Shortest Completing Word
=============================
Given a string licensePlate and an array of strings words, find the shortest completing word in words.
A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.
For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".
Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.

Example 1:
Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
Output: "steps"
Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
"step" contains 't' and 'p', but only contains 1 's'.
"steps" contains 't', 'p', and both 's' characters.
"stripe" is missing an 's'.
"stepple" is missing an 's'.
Since "steps" is the only word containing all the letters, that is the answer.

Example 2:
Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
Output: "pest"
Explanation: licensePlate only contains the letter 's'. All the words contain 's', but among these "pest", "stew", and "show" are shortest. The answer is "pest" because it is the word that appears earliest of the 3.
"""

from typing import is_protocol


def shortestCompletingWord(licensePlate: str, words: List[str]) -> str:
    maxVal, res = 0, ""
    lpCount = Count(licensePlate)

    for word in words:
        wordCount = Count(word)
        count = 0
        for w in wordCount:
            if w in lpCount:
                count += min(lpCount[w], wordCount[w])

        if count > maxVal:
            maxVal = count
            res = word

        elif count == maxVal:
            res = min([res, word], key=len)

    return res


def Count(s: str) -> dict:
    s = s.lower()
    count = {}
    for c in s:
        count[c] = count.setdefault(c, 0) + 1
    return count


licensePlate, words = "1s3 PSt", ["step", "steps", "stripe", "stepple"]
licensePlate, words = "1s3 456", ["looks", "pest", "stew", "show"]
print(shortestCompletingWord(licensePlate, words))
