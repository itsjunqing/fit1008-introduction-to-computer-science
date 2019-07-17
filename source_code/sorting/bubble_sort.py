def bubble_sort(array):
	n = len(array)
	for j in range(n - 1, 0, -1):
		swapped = False
		for i in range(j):
			if array[i] > array[i + 1]:
				swap(array, i, i + 1)
				swapped = True
		if not swapped:
			break


def swap(array, i, j):
	array[i], array[j] = array[j], array[i]


a = [5, 15, 10, 30, 3, 1, 8, 4]
bubble_sort(a)
print(a)
