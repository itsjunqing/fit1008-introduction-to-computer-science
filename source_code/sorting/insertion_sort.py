def insertion_sort(array):
	n = len(array)
	for i in range(1, n):
		value = array[i]
		index = i - 1
		while index >= 0 and array[index] > value:
			array[index+1] = array[index]
			index -= 1
		array[index+1] = value

a = [5, 15, 10, 30, 3, 1, 8, 4]
insertion_sort(a)
print(a)
