nums = [0, 0, 0, 1, 1, 0, 0]
l, r = 0, len(nums)

while l < r:
    mid = (l+r) // 2
    left_sum = sum(nums[:mid+1])
    right_sum = sum(nums[mid+1:])
    print(l,r, mid, left_sum, right_sum)
    if left_sum < right_sum or right_sum==0:
        r = mid
    elif left_sum > right_sum or left_sum==0:
        l = mid
    else:
        r = mid
    # break

print(l, r)

