def linear_search(arr, target):
    """
    Performs a linear search to find the target element in the given array.

    Args:
        arr: The list or array to search within.
        target: The element to search for.

    Returns:
        The index of the target element if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example Usage:
my_list = [4, 2, 7, 1, 9, 5]
search_target_1 = 7
search_target_2 = 10

index_1 = linear_search(my_list, search_target_1)
index_2 = linear_search(my_list, search_target_2)

if index_1 != -1:
    print(f"Linear Search: {search_target_1} found at index {index_1}")
else:
    print(f"Linear Search: {search_target_1} not found")

if index_2 != -1:
    print(f"Linear Search: {search_target_2} found at index {index_2}")
else:
    print(f"Linear Search: {search_target_2} not found")

# -----------------------------------------------------------------------------------------------------------------
# With simple for loop
#
arr = [1,2,3,4]
x = 2
x = 10

for i in range(len(arr)):
    if arr[i] == x:
        print(i)
        break
else:
    print(f'{x} not in list')
