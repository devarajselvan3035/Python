def sum(arr):
    if len(arr) <= 2:
        return arr[0]
    return sum(arr[1:]) + sum(arr[2:])


def reverse(s):
    if len(s) == 2:
        return s[1] + s[0]
    return reverse(s[1:]) + s[0]


def length(val):
    if len(val) == 0:
        return 0
    return 1 + length(val[1:])


def minimum(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] < arr[1] else arr[1]
    return arr[0] if arr[0] < minimum(arr[1:]) else minimum(arr[1:])


def maximum(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    return arr[0] if arr[0] > maximum(arr[1:]) else maximum(arr[1:])
# print(maximum([1,2,3,4,0]))

def duplicate(s):
    if len(s) == 1:
        return s[0]
    elif s[0] == s[1]:
        return s[2:]
    else:
        return s[0] + duplicate(s[1:])



def pyramid(n):
    if n == 0:
        pass
    else:
        pyramid(n-1)
    print("".join(['*']*n))

def find_word(r, l, word, find):
    if len(find)-1 == l:
        return find[-1]
    if word[r] == find[l]:
        return word[r] + find_word(r+1, l+1, word, find)
    if word[r] == ' ':
        return word[r] + find_word(r+1, l, word, find)
    else:
        return find_word(r, 0, word, find)

# s = 'hel   loooo world'
# f = 'helloo'
# print(find_word(0, 0, s, f))
#

# Input: k = 5
# Output: "b"
# Explanation:
# Initially, word = "a". We need to do the operation three times:
#     Generated string is "b", word becomes "ab".
#     Generated string is "bc", word becomes "abbc".
#     Generated string is "bccd", word becomes "abbcbccd".
#
def gen(s:str, k:int):
    if len(s) >= k:
        return s[k-1]
    n, i = len(s), 0
    while i < n:
        a = ord(s[i])
        s += chr(a+1)
        i += 1
    return gen(s, k)
print(gen('a', 5))
