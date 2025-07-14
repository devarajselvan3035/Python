arr = [1,2,3,4,5]
find = 0

low = 0
high = len(arr)-1

while low <= high:
    mid = (low + high) // 2
    print(mid, low, high)
    if arr[mid] == find:
        print(mid)
        break
    elif arr[mid] < find:
        low = mid + 1
    else:
        high = mid - 1
