## Longest Substring Without Repeating Characters
#  ==============================================

# s = 'abcabcabb'

# left:int = 0
# right:int = 0

# char_set:str = ''
# max:int = 0
# while right < len(s):
#     if s[right] not in char_set:
#         char_set += s[right]
#         max = right - left + 1
#         right += 1
#     else:
#         char_set.replace(s[right], "")
#         left += 1
# print(max)

##
# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
s = 'MCMXCIV'

symbol_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
keys_dict = symbol_dict.keys()

right = 1
# left = 1
ans = 0

while right < len(s):

    if s[right] ==
