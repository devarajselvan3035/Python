"""
290. Word Pattern
=================
Given a pattern and a string s, find if s follows the same pattern

Here follow means a full match, such that there is a bijection between a letter in pattern
and a non-empty word in s. Specifically:

- Each letter in pattern maps to exactly one unique word in self.
- Each unique word in s maps to exactly one letter in pattern.
- No two letters map to the same word, and no two words map to the same letter.
"""

from re import split


def wordPattern(pattern: str, s: str) -> bool:
    pattern_dict = {}
    split_s = s.split(" ")
    if len(pattern) != len(split_s):
        return False
    for idx in range(len(pattern)):
        if pattern[idx] not in pattern_dict:
            if split_s[idx] in pattern_dict.values():
                return False
            pattern_dict[pattern[idx]] = split_s[idx]
        elif pattern_dict[pattern[idx]] != split_s[idx]:
            return False

    return True


pattern, s = "abbab", "dog cat cat dog"
pattern, s = "abba", "dog dog dog dog"
print(wordPattern(pattern, s))
