arr = [2,5,1,4,3]

### With For Loop
def bubble_sort_for_loop(arr):
    n = len(arr)
    # Outer loop for passes
    for i in range(n):
        swapped = False  # Flag to optimize: if no swaps in a pass, list is sorted
        # Inner loop for comparisons and swaps
        # The last 'i' elements are already in their sorted positions
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped by inner loop, then break
        # This means the array is already sorted
        if not swapped:
            break
    return arr

### Bubble sort with while loop
def bubble_sort_while_loop(arr):
    flag = 1
    l, r = 0, 1
    while r < len(arr):
        if arr[l] > arr[r]:
            arr[l], arr[r] = arr[r], arr[l]
            flag = 0
        elif r == len(arr)-1:
            l, r = 0, 1
            if flag == 1:
                break
            flag = 1
        else:
            l += 1
            r += 1
    return arr
print(bubble_sort_while_loop(arr))

### Bubble sort with recurion
def bubble_sort_rc(arr:list) -> list:
    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr

    temp = [arr[0]] + bubble_sort_rc(arr[1:])
    if temp[0] > temp[1]:
        temp[0], temp[1] = temp[0], temp[1]
    return temp
for _ in range(len(arr)):
    arr = bubble_sort_rc(arr)
print(arr)
