"""
17. Letter Combinations of a Phone Number
=========================================
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = "2"
Output: ["a","b","c"]
"""


def letterCombinations(s: str) -> list[str]:
    letters = ["", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    result = []

    def backtracking(val: str, ans: str):
        if len(val) == 0:
            result.append(ans)
            return

        for let in letters[int(val[0]) - 1]:
            backtracking(val[1:], ans + let)

    backtracking(s, "")
    return result


print(letterCombinations("2"))
