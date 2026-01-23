"""
551. Student Attendance Record I
================================
You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

    'A': Absent.
    'L': Late.
    'P': Present.

The student is eligible for an attendance award if they meet both of the following criteria:

    The student was absent ('A') for strictly fewer than 2 days total.
    The student was never late ('L') for 3 or more consecutive days.

Return true if the student is eligible for an attendance award, or false otherwise.

Example 1:
Input: s = "PPALLP"
Output: true
Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.

Example 2:
Input: s = "PPALLL"
Output: false
Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.
"""


def checkRecord(s: str) -> bool:
    l, r = 0, 0
    count = 0
    while r <= len(s):
        if l >= len(s):
            break
        if r == len(s) or s[l] != s[r]:
            # print(s[l], count)
            if s[l] == "A" and count >= 2:
                return False
            if s[l] == "L" and count >= 3:
                return False
            count = 0
            l = r
            r -= 1
        elif s[l] == s[r]:
            count += 1
        r += 1
    return True


# s = "PPALLP"
# s = "PPALLL"
print(checkRecord(s))
