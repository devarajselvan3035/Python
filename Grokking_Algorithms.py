# def count(arr):
# 	if len(arr) == 0:
# 		return 0
# 	else:
# 		return 1 + count(arr[1:])
# print(count([1,2,3,4]))

# def max(arr):
# 	if len(arr) == 2:
# 		return arr[0] if arr[0] > arr[1] else arr[1]
# 	return arr[0] if arr[0] > max(arr[1:]) else max(arr[1:])
# print(max([2,5,10,1]))

#### Quick Sort

# def quicksort(arr):
# 	if len(arr) < 2:
# 		return arr
# 	else:
# 		pivot = arr[0]
# 		less_than = [n for n in arr if n<pivot]
# 		greter_than = [n for n in arr if n>pivot]

# 		return quicksort(less_than) + [pivot] + quicksort(greter_than)
# print(quicksort([2,5,1,6,3,9]))


# Creating a multiplication table with all the elements in the array. So
# if your array is [2, 3, 7, 8, 10], you first multiply every element by 2,
# then multiply every element by 3, then by 7, and so on.

ans = []
def matrix(arr, *args):
	if len(arr) == 1:
		return args
	else:
		return matrix(arr[1:], arr)

def binarySearch(arr, value):




# ## Tree
# from os import listdir
# from os.path import isfile, join

# def tree(path):
# 	for p in listdir(path):
# 		full_path = join(path, p)
# 		if isfile(full_path):
# 			print(p)
# 		else:
# 			tree(full_path)
# tree('/home/devselvan/Documents/Python/Github')


def powtwo(val):
	print(val)
	if val == 1:
		return True
	elif val%2 == 1:
		return False
	else:
		return powtwo(val//2)
print(powtwo(124))
