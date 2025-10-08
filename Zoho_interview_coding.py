# # Code No 1
# =============
s = "have a Good Good day       !"
substring = "Goodday"

# Solution 1
# -----------
# ans:str = ''
# for i in range(len(s)):
#     if s[i] == substring[0]:
#         str_id:int = i
#         substrId:int = 0
#         ans = ''
#         while substrId < len(substring):
#             if s[str_id] == substring[substrId]:
#                 ans += s[str_id]
#                 substrId += 1
#             if s[str_id] == ' ':
#                 ans += s[str_id]
#             else:
#                 pass
#             str_id += 1
# print(ans)

# Solution 2
# ----------
# ans:str = ''
# for i in range(len(s)):
#     if s[i] == substring[0]:
#         str_id:int = i
#         substrId:int = 0
#         ans = ''
#         while substrId < len(substring) and (s[str_id] == substring[substrId] or s[str_id] == ' '):
#             ans += s[str_id]
#             if s[str_id] == substring[substrId]:
#                 substrId += 1
#             str_id += 1
# print(ans)


# ---------------------------------------------------------------
# Code No 2
# ==========

# format_s = '{NAME1_____}   {AGE}'
# source_s = 'NAME1'
# target_s = 'Ravi'

# pattern:str = ''
# output:str = ''
# for i in range(len(format_s)):
#     if format_s[i] == '{':
#         temp_pattern:str = ''
#         str_id:int = i
#         while format_s[str_id] != '}':
#             temp_pattern += format_s[str_id]
#             str_id += 1
#         if source_s in temp_pattern:
#             pattern = temp_pattern[1:]


# if len(target_s) > len(pattern):
#     target_s = target_s[:len(pattern)]
# if len(target_s) <= len(pattern):
#     space = len(pattern) - len(target_s)
#     target_s = target_s + "".join([' ']*space)

# output = format_s.replace(pattern, target_s)
# print(output)

"""
Code No 3 - shuffled card
==========
Inputs : arr = [[3,4],[1,2],[4,5],[2,3]]
Outputs = [1,2,3,4]
"""

# arr = [[3, 4], [1, 2], [4, 5], [2, 3]]
arr = [[10, 1], [5, 3], [7, 10], [1, 5]]


def shuffledCard(arr: list):
    first = [a[0] for a in arr]
    last = [a[1] for a in arr]
    paired = dict(zip(first, last))

    res = [n for n in first if n not in last]
    temp = res[0]
    for _ in first:
        res.append(paired[temp])
        temp = paired[temp]
    return res


print(shuffledCard(arr))
"""
Code No 4 
==========
Replace given integer 0 values to 5
Inputs: numb = 1001
Outputs: 1551
"""


def replace_zero(num: int):
    res = 0
    deli = 0
    while num > 0:
        rem = num % 10
        if rem == 0:
            res = (5 * (10**deli)) + res
        else:
            res = (rem * (10**deli)) + res
        deli += 1
        num = num // 10
    return res


# print(replace_zero(1002))

"""
Code No 5
=========
Find the given 2 Strings are Anagram of each other
INPUT:
str1 = tests
str2 = esstt
OUTPUT:
true
INPUT:
str1 = skyblue
str2 = kysllueb
OUTPUT:
false
"""


def Anagram(str1: str, str2: str):

    def counter(ip: str):
        count = dict()
        for s in ip:
            if s in count:
                count[s] += 1
            else:
                count[s] = 0

        return count

    dict1 = counter(str1)
    dict2 = counter(str2)

    print(dict1 == dict2)


# Anagram("tests", "essttt")
