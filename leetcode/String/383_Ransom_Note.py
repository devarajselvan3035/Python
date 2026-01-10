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
    l, r = 0, 0
    while l < len(ransomNote) and r < len(magazine):
        if ransomNote[l] != magazine[r]:
            return False
        l += 1
        r += 1
    return True


rn, m = "aa", "aab"
print(canConstruct(rn, m))
