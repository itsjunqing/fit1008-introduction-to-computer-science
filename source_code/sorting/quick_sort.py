def quick_sort(array):
	start = 0
	end = len(array) - 1
	quick_sort_aux(array, start, end)


def quick_sort_aux(array, start, end):
	if start < end:
		pivot = partition(array, start, end)
		quick_sort_aux(array, start, pivot - 1)
		quick_sort_aux(array, pivot + 1, end)


def partition(array, start, end):
	pivot = (start + end) // 2

	pivot_value = array[pivot]
	swap(array, start, pivot)
	index = start
	for i in range(start + 1, end + 1):
		if array[i] < pivot_value:
			index += 1
			swap(array, index, i)
	swap(array, index, start)
	return index


def swap(array, i, j):
	array[i], array[j] = array[j], array[i]


a = [5, 15, 10, 30, 3, 1, 8, 4]
quick_sort(a)
print(a)
