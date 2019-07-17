from data_structures.heap_array import Heap

def heap_sort(array):
	heap = Heap()
	for item in array:
		heap.add(item, "")
	i = len(array) - 1
	while not heap.is_empty():
		array[i] = heap.get_max()
		i -= 1

a = [5, 15, 10, 30, 3, 1, 8, 4]
heap_sort(a)
print(a)
