def binary_search_iterative(arr, target):
    """
    Performs an iterative binary search to find the target element in a sorted array.

    Args:
        arr: The sorted list or array to search within.
        target: The element to search for.

    Returns:
        The index of the target element if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:  # arr[mid] > target
            high = mid - 1
    return -1

# Example Usage:
sorted_list = [1, 2, 4, 5, 7, 9]
search_target_1 = 7
search_target_2 = 3

index_1 = binary_search_iterative(sorted_list, search_target_1)
index_2 = binary_search_iterative(sorted_list, search_target_2)

if index_1 != -1:
    print(f"Binary Search (Iterative): {search_target_1} found at index {index_1}")
else:
    print(f"Binary Search (Iterative): {search_target_1} not found")

if index_2 != -1:
    print(f"Binary Search (Iterative): {search_target_2} found at index {index_2}")
else:
    print(f"Binary Search (Iterative): {search_target_2} not found")
