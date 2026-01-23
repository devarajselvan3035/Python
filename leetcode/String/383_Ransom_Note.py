"""
383. Ransom Note
================
can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
"""


def canConstruct(ransomNote: str, magazine: str) -> bool:
    for c in ransomNote:
        idx = magazine.find(c)
        if idx == -1:
            return False
        else:
            magazine = magazine[:idx] + magazine[idx + 1 :]
    return True


rn, m = "aa", "aab"
print(canConstruct(rn, m))
