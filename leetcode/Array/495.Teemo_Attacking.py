"""
out hero teemo is attacking an enemy ashe with poison attacks! when teemo
attacks ashe, ashe get s poisned for a exactly duration seconds. More formally
an attack at second t will means ashe is poisoned during the inclusive time intervel
[t, t + duration - 1]. If Teemo attacks again before the poison effect ends, the timer for it is reset, and the poison effect will end duration seconds after the new attack.

You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i], and an integer duration.

Return the total number of seconds that Ashe is poisoned.

Example 1:

Input: timeSeries = [1,4], duration = 2
Output: 4
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.

Example 2:

Input: timeSeries = [1,2], duration = 2
Output: 3
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for seconds 2 and 3.
Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.
"""


def findPoisonedDuration(timeseries: list, duration: int) -> int:
    res, sec = 0, None
    for ts in timeseries:
        res += duration
        if sec is None:
            sec = ts + duration - 1
        elif ts <= sec:
            diff = sec - ts + 1
            res -= diff
            sec = ts + duration - 1
        else:
            sec = ts + duration - 1
        print(res, sec, ts)

    return res


# time, dur = [1, 4], 2
time, dur = [1, 4, 5], 2
print(findPoisonedDuration(time, dur))
