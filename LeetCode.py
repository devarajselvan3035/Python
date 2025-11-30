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
# p###rint(max)

##
# Examile 1:

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
#
# ---------------------------------------------------------------------------------------------
"""21. Merge two sorted lists
You are given the heads of two sorted linked list `list1` and `list2`
Merge the two lists into onne sorted list. The list should be made by splicing together
the nodes of the first tow lists. Return the head of the merged linked list

Examples:
Input 1 -> 2 -> 4, 1 -> 3 -> 4
Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4
"""

from re import A
from Data_Structure.Singel_LinkedList import LinkedList, Node

list1 = LinkedList(1, 2, 3)
list2 = LinkedList(1, 2, 4)
print(list1, list2)


def mergeTwoLinkedList(list1: Node, list2: Node):
    head = Node(0)
    tail = head
    while list1 and list2:
        if list1.value < list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list2 if list1 is None else list1
    return head.next


begin = mergeTwoLinkedList(list1.head, list2.head)
# while begin:
#     print(begin.value)
#     begin = begin.next


"""
9. Palindrome Number
====================
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise

Examples
Iniuts: x = 121
Output: true

Inputs: x = -121
output: False
"""
# x = -121
x = 121


def findPalindrome(x: int) -> bool:
    str_x = str(x)
    l, r = 0, len(str_x) - 1

    while l < r:
        if str_x[l] != str_x[r]:
            return False
        l += 1
        r -= 1

    return True


def simpleFindPalindrome(x: int) -> bool:
    str_x = str(x)
    return str_x == str_x[::-1]


# print(findPalindrome(x))
# print(simpleFindPalindrome(x))


"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

strs = ["flower", "flow", "flight"]
# strs = ["dog", "racecar", "car"]


# O(n^2) time complexity
def longestCommonPrefix(strs: list) -> str:
    res = strs[0][0]
    min_len = min([len(s) for s in strs])
    for idx in range(min_len):
        for s in strs:
            if s[: idx + 1] != res:
                return res[:-1]
        res += strs[0][idx + 1]
    return res


# O(n) time complexity
def simpleCommonPrefix(strs: list) -> str:
    if not strs:
        return ""

    prefix = ""
    for pairs in list(zip(*strs)):
        if len(set(pairs)) == 1:
            prefix += pairs[0]
        else:
            break

    return prefix


# print(list(zip(*strs)))
# print(longestCommonPrefix(strs))
# print(simpleCommonPrefix(strs))
#
"""
4. Median of Two sorted arrays
==============================
Given to sorted arrays num1 and num2 of size m and n respectively, return the median of the two sorted arrays.
Examples
Inputs: num1 = [1,2], nums2 = [3,4]
Output: 2.5000
"""


def findmedian(num1: list, num2: list):
    full_list = num1 + num2
    sort_list = sorted(full_list)
    l, r = 0, len(sort_list) - 1
    while l < r:
        l += 1
        r -= 1
    return (sort_list[l] + sort_list[r]) / 2


def findMedian2(num1: list, num2: list):
    full_list = num1 + num2
    sort_list = sorted(full_list)
    len_list = len(sort_list)
    if len_list % 2 == 1:
        return sort_list[(len_list // 2) + 1]
    else:
        return sum(sort_list[(len_list // 2) : (len_list // 2) + 2]) / 2


# print(findMedian2([1, 2], [3, 4]))
# print(findmedian([1, 2], [3, 4]))
#
"""
5. Logest Palindrome Substring
==============================
Given a string `s`, return longest palindrome substring in `s`.
Examples
Inputs: s = 'babad'
Output: "bab
"""

"""
26. Remove Duplicates from Sorted Array
=======================================
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


def removeDuplicates(nums: list):
    l, r = 1, 1
    while r < len(nums):
        if nums[l] != nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
        r += 1
    return nums


# print(removeDuplicates)

"""
94. Binary Tree Inorder Traversal
=================================
"""

"""
118. Pascal's Triangle
======================
"""


def PascalTriangle(numrows: int):
    res = []
    for r in range(1, numrows + 1):
        col = []
        for c in range(r):
            if c == 0 or c == r - 1:
                col.append(1)
            else:
                # print(res, r)
                need_col = res[r - 2]
                print(need_col, c)
                col.append(need_col[c] + need_col[c - 1])
        res.append(col)

    return res


# print(PascalTriangle(5))

"""
121. Best time to buy and shell stock
=====================================
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""
# arr = [7, 1, 5, 3, 6, 4]
arr = [7, 6, 4, 3, 1]


def maxProfit(prices: list) -> int:
    pass


# print(maxProfit(arr))

"""
168. Excel sheet column title
Given an integer colum number, return its corresponding column title.
For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
"""


def convertToTitle(colnum: int) -> str:
    ans = ""
    while colnum > 0:
        rem = colnum % 26
        if rem == 0:
            ans = "Z" + ans
        else:
            ans = chr(rem + 64) + ans
        colnum = (colnum - 1) // 26

    return ans


def convertToTitle2(colnum: int):
    if colnum < 27:
        return chr(colnum + 64)
    return convertToTitle2((colnum - 1) // 26) + chr(((colnum - 1) % 26) + 65)


# print(convertToTitle(701))
# print(convertToTitle2(701))
#
"""
88. Merge Sorted Array
======================
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""


def merge(nums1: list, n1: int, nums2: list, n2: int):
    ans = []
