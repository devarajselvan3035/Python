"""
345.Reverse Vowels of a String
==============================
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
"""


def reverseVowels(s: str) -> str:
    ls = list(s)
    vowels = "aeiouAEIOU"
    l, r = 0, len(s) - 1
    while l < r:
        if ls[l] in vowels and ls[r] in vowels:
            ls[l], ls[r] = ls[r], ls[l]
            l += 1
            r -= 1
        elif ls[l] in vowels and not ls[r] in vowels:
            r -= 1
        elif not ls[l] in vowels and ls[r] in vowels:
            l += 1
        else:
            r -= 1
            l += 1

    return "".join(ls)


def reverseVowels1(s: str) -> str:
    list_s = list(s)
    vowels = "aeiouAEIOU"
    vowels_dict = {i: v for i, v in enumerate(s) if v in vowels}
    idx = list(vowels_dict.keys())
    val = list(vowels_dict.values())
    for i, v in zip(idx[::-1], val):
        list_s[i] = v

    return "".join(list_s)


# s = "IceCreAm"
s = "leetcedo"
print(reverseVowels(s))
