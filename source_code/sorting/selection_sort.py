def selection_sort(array):
	n = len(array)
	for start in range(n - 1):
		min_index = get_minimum(array, start)
		swap(array, start, min_index)

def get_minimum(array, index):
	min_index = index
	n = len(array)
	for i in range(index + 1, n):
		if array[i] < array[min_index]:
			min_index = i
	return min_index


def swap(array, i, j):
	array[i], array[j] = array[j], array[i]

a = [5, 15, 10, 30, 3, 1, 8, 4]
selection_sort(a)
print(a)
