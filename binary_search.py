from typing import List
import bisect

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)

        # Find the end of the strictly increasing prefix.
        prefix_end = 0
        while prefix_end + 1 < n and nums[prefix_end] < nums[prefix_end + 1]:
            prefix_end += 1

        # If the whole array is sorted, any subarray is incremovable.
        if prefix_end == n - 1:
            return n * (n + 1) // 2

        # Find the start of the strictly increasing suffix.
        suffix_start = n - 1
        while suffix_start - 1 >= 0 and nums[suffix_start - 1] < nums[suffix_start]:
            suffix_start -= 1

        count = 0

        # 3. Iterate through each valid prefix (from empty to nums[0...prefix_end]) and count valid suffixes for it.
        for i in range(prefix_end + 2):
            # The prefix is nums[0...i-1]. If i=0, the prefix is empty.

            # Get the last value of the prefix. Use a very small number for an empty prefix.
            last_prefix_val = nums[i-1] if i > 0 else float('-inf')

            # 4. Use binary search to find the first element in the sorted suffix
            # that is greater than last_prefix_val.

            # bisect_right finds an insertion point which comes after (to the right of)
            # any existing entries of last_prefix_val in a sorted list.
            insertion_point = bisect.bisect_right(nums, last_prefix_val, lo=suffix_start)

            # The number of valid suffixes is the number of elements from the
            # insertion point to the end of the array.
            num_valid_suffixes = n - insertion_point

            # Add 1 for the case where we keep the prefix and an empty suffix
            # (i.e., remove the rest of the array).
            count += num_valid_suffixes + 1

        return count
