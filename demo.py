from typing import Counter


nums = [1, 1, 2, 2, 2, 3]
freq = {}

func = lambda n: (freq[n], -n)

for n in nums:
    freq[n] = freq.setdefault(n, 0) + 1

print(sorted(list(map(func, nums))))
