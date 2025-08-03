def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element of the unsorted part
        # This places the smallest element at its correct sorted position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# Example Usage:
my_list = [64, 25, 12, 22, 11]
print("Original list:", my_list)
sorted_list = selection_sort(my_list)
print("Sorted list:", sorted_list) # Output: Sorted list: [11, 12, 22, 25, 64]

another_list = [5, 4, 3, 2, 1]
print("Original list:", another_list)
sorted_another_list = selection_sort(another_list)
print("Sorted list:", sorted_another_list) # Output: Sorted list: [1, 2, 3, 4, 5]
