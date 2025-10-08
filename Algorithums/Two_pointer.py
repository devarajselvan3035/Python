# nums = [4,1,4,0,3,5]
# avg_list = []

# min_value:int = nums[0]
# max_value:int = nums[0]

# def remove(arr, value):
#     return [a for a in arr if arr not in value]

# for n in nums:
#     if n > max_value:
#         max_value = n
#     if n < min_value:
#         min_value = n

# print(min_value, max_value)

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# nums = [1,1,2]
j = 0
for i in range(1, len(nums)):
    if nums[i] > nums[j]:
        j += 1
        nums[j] = nums[i]
print(j + 1, nums)

# sentence = "i love eating"
# searchWord = "burg"
# position = 0
# sentence.split(' ')
# for id, word in enumerate(sentence.split(' ')): if word[:len(searchWord)] == searchWord:
#         position = id + 1
# if position == 0:
#     print(-1)
# print(position)


# Input: forts = [1,0,0,-1,0,0,0,0,1]
# Output: 4
# Explanation:
# - Moving the army from position 0 to position 3 captures 2 enemy forts, at 1 and 2.
# - Moving the army from position 8 to position 3 captures 4 enemy forts.
# Since 4 is the maximum number of enemy forts that can be captured, we return 4.
forts = [1, 0, 0, -1, 0, 0, 0, 0, 1]
# forts = [-1,0,-1,0,1,1,1,-1,-1,-1]

# max_value:int = 0
# count:int = 0
# start1:int = 0
# startm1:int = 0
# right:int = 0
# left:int = 0

# while right < len(forts):
#     if (start1 == 1 or startm1 == 1) and forts[right] == 0:
#         count += 1
#     if forts[right] == 1:
#         start1 = 1
#         if startm1 == 1:
#             max_value = max(max_value, count)
#         count = 0
#     if forts[right] == -1:
#         startm1 = 1
#         if start1 == 1:
#             max_value = max(max_value, count)
#         count = 0
#     right += 1
#     print(count, max_value)
# print(max_value)


# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
#
# s = "Let's take LeetCode contest"

# string:str = ''
# sub_str:str = ''

# for i in range(len(s)):
#     if s[i] == ' ':
#         string += sub_str+" "
#         sub_str = ''
#     elif i == len(s)-1:
#         string += sub_str
#     else:
#         sub_str = s[i]+sub_str
# print(string)


# Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
# Output: true
# s = "iloveleetcode"
# words = ["apple","i","love","leetcode","apples"]

# ptr:int = 0
# for w in words:
#     print(ptr, s[ptr:ptr+len(w)])
#     if w == s[ptr:ptr+len(w)]:
#         ptr += len(w)
#     else:
#         break
# print(ptr)


# Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
# Output: 2
# Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.
# nums1 = [1,2,3,6]
# nums2 = [1,3,4,5]

# nums1, nums2 = [1,2,3],[2,4]
# right, left = 0, 0
# min_value = float('inf')

# while right < len(nums1) and left < len(nums2):
#     if nums1[right] == nums2[left]:
#         min_value = min(min_value, nums1[right])
#         right += 1
#         left += 1
#     elif nums1[right] < nums2[left]:
#         right += 1
#     elif nums2[left] < nums1[right]:
#         left += 1
# print(min_value)


# Input: word = "abcdefd", ch = "d"
# Output: "dcbaefd"
#
# word, ch = "abcdefd","d"
# word, ch = "abcd","z"

# ans = ''
# flag = 0
# count = 0
# for w in word:
#     if w == ch and count < 1:
#         flag = 1
#         count += 1
#         ans = w + ans
#     elif flag == 0:
#         ans = w + ans
#     elif flag == 1:
#         ans = ans + w
# print(ans if flag != 0 else word)


### 88. Merge Sorted Array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
#
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# #
# # nums1 = [1]
# # m = 1
# # nums2 = []
# # n = 0
# #
# ans = []
# left, right = 0, 0

# while left <= m or right <= n:
#     if left == m:
#         ans += nums2[right:]
#         break
#     if right == n:
#         ans += nums1[left:]
#         break
#     if nums1[left] <= nums2[right]:
#         ans.append(nums1[left])
#         left += 1
#     elif nums2[right] <= nums1[left]:
#         ans.append(nums2[right])
#         right += 1
#     print(left, right)
# print(ans)


#### 2903. Find Indices With Index and Value Difference I
# You are given a 0-indexed integer array nums having length n, an integer indexDifference, and an integer valueDifference.
# Your task is to find two indices i and j, both in the range [0, n - 1], that satisfy the following conditions:
# abs(i - j) >= indexDifference, and
# abs(nums[i] - nums[j]) >= valueDifference
# Return an integer array answer, where answer = [i, j] if there are two such indices, and answer = [-1, -1] otherwise. If there are multiple choices for the two indices, return any of them.
# Note: i and j may be equal.
#
# Example 1:
# Input: nums = [5,1,4,1], indexDifference = 2, valueDifference = 4
# Output: [0,3]
# Explanation: In this example, i = 0 and j = 3 can be selected.
# abs(0 - 3) >= 2 and abs(nums[0] - nums[3]) >= 4.
# Hence, a valid answer is [0,3].
# [3,0] is also a valid answer.

# nums = [5, 1, 4, 1]
# indexDifference = 2
# valueDifference = 4

# nums = [2, 1]
# indexDifference = 0
# valueDifference = 0

# left, right = 0, 0

# while right < len(nums):
#     while left < len(nums):
#         if abs(right-left) >= indexDifference and (nums[right] - nums[left]) >= valueDifference:
#             print(right, left)
#             break
#         left += 1
#     right += 1


# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# s = "A man, a plan, a canal: Panama"

# left, right = 0, len(s)-1

# while left <= right:
#     # print(s[left], s[right])
#     if not s[left].isalpha():
#         right += 1
#     elif not s[right].isalpha():
#         left -= 1
#     elif s[left].lower() != s[right].lower():
#         print(False)
#     left += 1
#     right -= 1
# print(True)

# Input: nums = [5,14,13,8,12]
# Output: 673
# Explanation: Before performing any operation, nums is [5,14,13,8,12] and concatenation value is 0.
#  - In the first operation:
# We pick the first element, 5, and the last element, 12.
# Their concatenation is 512, and we add it to the concatenation value, so it becomes equal to 512.
# Then we delete them from the nums, so nums becomes equal to [14,13,8].
#  - In the second operation:
# We pick the first element, 14, and the last element, 8.
# Their concatenation is 148, and we add it to the concatenation value, so it becomes equal to 660.
# Then we delete them from the nums, so nums becomes equal to [13].
#  - In the third operation:
# nums has only one element, so we pick 13 and add it to the concatenation value, so it becomes equal to 673.
# Then we delete it from nums, so nums become empty.
# Since the concatenation value is 673 so the answer is 673.
# nums = [7,52,2,4]

# left, right = 0, len(nums)-1
# ans = 0

# while left <= right:
#     if left == right:
#         ans += nums[left]
#         break
#     value = int(str(nums[left]) + str(nums[right]))
#     ans += value
#     left += 1
#     right -= 1

# print(ans)

# 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# nums = [0,1,0,3,12]

# l, r = 0, 0
# while r < len(nums):
#     if nums[r] != 0:
#         nums[l],nums[r] = nums[r], nums[l]
#         l += 1
#     r += 1

# print(nums)


# 344. Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# s = ["h","e","l","l","o"]

# l, r = 0, len(s)-1
# while l < r:
#     s[l], s[r] = s[r], s[l]
#     l += 1
#     r -= 1
# print(s)

# 345. Reverse Vowels of a String
# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"
# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
# s = "IceCreAm"
# s = [l for l in s]

# l, r = 0, len(s)-1
# vowels = ['a', 'e', 'i', 'o', 'u']
# while l < r:
#     # print(s[l], s[r])
#     if s[l].lower() not in vowels:
#         l = l+1
#     elif s[r].lower() not in vowels:
#         r = r-1
#     elif s[l].lower() in vowels and s[r].lower() in vowels:
#         print(s[l], s[r])
#         temp = s[l]
#         s[l] = s[r]
#         s[r] = temp
#         l = l+1
#         r = r-1
# print("".join(s))


# 392. Is Subsequence
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# s = "axc"
# t = "ahbgdc"

# l, r, c = 0,0, 0

# while r < len(t) and l < len(s):
#     if s[l] == t[r]:
#         c += 1
#         l = l+1
#     r = r+1
# print(True if c == len(s) else False)


# 680. Valid Palindrome II
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Example 1:
# Input: s = "aba"
# Output: true
# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:
# Input: s = "abc"
# Output: false
# s = "tebbem"

# l, r, f = 0, len(s)-1, 0
# while l < r:
#     print(s[l], s[r])
#     if s[l] != s[r]:
#         print(l, r)
#         if s[l+1] == s[r]:
#             r = r+1
#         elif s[r-1] == s[l]:
#             l = l-1
#         f += 1
#     print(f)
#     if f == 2:
#         print(False)
#         break

#     l += 1
#     r -= 1
# print(True)


# 696. Count Binary Substrings
# Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
# Substrings that occur multiple times are counted the number of times they occur.

# Example 1:
# Input: s = "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

# s = "10101"

# g, t = 2, 0
# c = {'0':0, '1':0}
# while g < len(s):
#     l, r = 0, 0
#     while r < len(s):
#         c[s[r]] += 1
#         if (r-l+1) > g:
#             c[s[l]] -= 1
#             l += 1
#         r+= 1
#         if c['0'] == c['1']:
#             t += 1
#         print(r-l+1, c)
#     print(t)
#     g += 2


# 821. Shortest Distance to a Character
# Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.
# The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

# Example 1:
# Input: s = "loveleetcode", c = "e"
# Output: [3,2,1,0,1,0,0,1,2,2,1,0]

# s = "loveleetcode"
# c = "e"

# l, r, i = len(s), 0, 0
# ans = []

# while r < len(s):
#     if s[r] == c:
#         while i <= r:
#             ans.append(min(abs(i-l), abs(i-r)))
#             i += 1
#         l = r
#     r += 1

# i = l+1
# while i < r:
#     ans.append(abs(i-l))
#     i += 1
# print(ans)

# 832. Flipping an Image
# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
# To flip an image horizontally means that each row of the image is reversed.
# Example 1:
# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

# Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# image = [[1,1,0],[1,0,1],[0,0,0]]

# r, c = len(image[0]), len(image)

# for i in range(r*c):
#     if (i+1) % r == 1:
#         f, l, p = 0, r-1, (i+1) // r
#         print(f,l,p)
#         image[p][f], image[p][l] = abs(image[p][l]-1), abs(image[p][f]-1)
#     elif f <= l:
#         image[p][f], image[p][l] = abs(image[p][l]-1), abs(image[p][f]-1)
#     f += 1
#     l -= 1


# print(image)

# 844. Backspace String Compare
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.
# Example 1:
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# s = "ab#c"
# t = "c#d#"

# def te(x:str) -> str:
#     ans = ''
#     for w in x:
#         if w == '#':
#             ans = ans[:-1]
#         else:
#             ans += w
#     return ans


# a = te(s)
# b = te(t)
# print(a, b)


# 905. Sort Array By Parity
# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
# Return any array that satisfies this condition.
# Example 1:
# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# nums = [3,1,2,4]

# l, r = 0, 0
# while r < len(nums):
#     if nums[r]%2 == 0:
#         nums[r], nums[l] = nums[l], nums[r]
#         l += 1
#     r += 1
# print(nums)


# 917. Reverse Only Letters
# Given a string s, reverse the string according to the following rules:
# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.
# Example 1:
# Input: s = "ab-cd"
# Output: "dc-ba"
# Example 2:
# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# s = "Test1ng-Leet=code-Q!"

# s = list(s)
# l, r = 0, len(s)-1
# while l < r:
#     if not s[l].isalnum():
#         l += 1
#     if not s[r].isalnum():
#         r -= 1
#     s[l], s[r] = s[r], s[l]
#     l += 1
#     r -= 1
# print("".join(s))


# 922. Sort Array By Parity II
# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
# Return any answer array that satisfies this condition.
# Example 1:
# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
# nums = [3, 0, 4, 0, 2, 1, 3, 1, 3, 4, 1, 1]
#
# odd = [n for n in nums if n % 2 == 1]
# even = [n for n in nums if n % 2 == 0]
#
# ans = [0] * (max(len(odd), len(even)) * 2)
# e, o = 0, 0
# for i in range(len(ans)):
#     if i % 2 == 0 and e < len(even):
#         ans[i] = even[e]
#         e += 1
#     elif i % 2 == 1 and o < len(odd):
#         ans[i] = odd[o]
#         o += 1
# print(ans)


# 925. Long Pressed Name
# Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
# You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.
# Example 1:
# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.
# Example 2:
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it was not in the typed output.
name = "saeed"
typed = "ssaaeddef"

l, r, flag = 0, 0, 0
while r < len(typed) and l < len(name):
    if name[l] == typed[r]:
        flag += 1
        l += 1
    r += 1
print(r)
