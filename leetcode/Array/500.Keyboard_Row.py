"""
Given an array of stirngs words, return the words that can be typed using letters of the alphabet on
only one row of american keyboard like the image below.

Note that the strings are case insensitive, both lowercased and uppercased of the same letter are
treated as if they are at the same row.

In the American keyboard:
- The first consists of the chracters 'qwertyuiop'
- The second row consists of the chracters 'asdfghjkl'
- The third row consists of the characters 'zxcvbnm'

Examples:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Explanation:
Both "a" and "A" are in the 2nd row of the American keyboard due to case insensitivity.
"""


def findWords(words: list) -> list:
    # Step 1: Define the rows as sets for fast lookup
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")

    res = []

    for word in words:
        # step 2: Convert word to lowercase for comparision
        lower_word = set(word.lower())

        # Step 3: Check fi the word's chracters are a subset of any row
        if lower_word <= row1 or lower_word <= row2 or lower_word <= row3:
            res.append(word)
    return res


def findWords1(words: list) -> list:
    first = "qwertyuiop"
    second = "asdfghjkl"
    third = "zxcvbnm"

    res = []

    flag = None

    for main_word in words:
        word = main_word.lower()
        if word[0] in first:
            flag = check(word, first)
        elif word[0] in second:
            flag = check(word, second)
        elif word[0] in third:
            flag = check(word, third)

        if flag:
            res.append(main_word)

    return res


def check(word: str, pattern: str) -> bool:
    for w in word:
        if w not in pattern:
            return False
    return True


words = ["Hello", "Alaska", "Dad", "Peace"]
# words = ["omk"]
print(findWords(words))
