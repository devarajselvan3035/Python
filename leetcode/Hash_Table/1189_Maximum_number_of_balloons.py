"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0
"""


def maxNumberOfBalloons(text: str) -> int:
    ans = len("balloons")
    balloonCount = {}
    for c in "balloon":
        balloonCount[c] = balloonCount.setdefault(c, 0) + 1

    textCount = {}
    for c in text:
        textCount[c] = textCount.setdefault(c, 0) + 1

    for val, cot in balloonCount.items():
        if val not in textCount:
            return 0
        ans = min(ans, (textCount[val] // balloonCount[val]))

    return ans


text = "loonbalxballpoon"
# text = "leetcode"
text = "balllllllllllloooooooooon"
print(maxNumberOfBalloons(text))
