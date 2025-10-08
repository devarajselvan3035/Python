arr = [4,3,5,4,1,6,0]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        print('before merge')
        print(f'left {left}')
        print(f'right {right}')
        print()

        merge_sort(left)
        merge_sort(right)

        l, r, k = 0, 0, 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                arr[k] = left[l]
                l += 1
            else:
                arr[k] = right[r]
                r += 1
            k += 1

        while l < len(left):
            arr[k] = left[l]
            k += 1
            l += 1

        while r < len(right):
            arr[k] = right[r]
            k += 1
            r += 1
