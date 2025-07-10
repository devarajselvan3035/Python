# # Code No 1
# =============
s = 'have a Good Good day       !'
substring = 'Goodday'

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
