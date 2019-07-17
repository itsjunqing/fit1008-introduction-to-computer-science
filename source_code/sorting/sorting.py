from data_structures.ADT_queue import Queue
from data_structures.ADT_stack import Stack
from data_structures.heap_array import Heap

def bubble_sort(the_list):
	"""
	Bubble sorting.

	@complexity:	best-case and worst-case is O(N^2)
	"""
	n = len(the_list)
	for j in range(n - 1, 0, -1):
		for i in range(j):
			if the_list[i] > the_list[i + 1]:
				swap(the_list, i, i + 1)


def bubble_sort2(the_list):
	"""
	Bubble sorting version 2.

	@complexity:	best-case is O(N) when items are sorted and not swapped, so only inner loop runs n times
					worst-case is O(N^2) when items are not sorted, so both loop runs n times
	@stability:		it is stable, the items are sorted such that it is compared with the item adjacent to it,
					so comparison is strict where it must be compared with >= instead of >
	@incremental:	yes if the element is added to the front because the loop will only need to run once to put the
					new element in the right position. no if the element is added to the back, because the loop needs
					to keep iterating until it reaches to the "final position" to put it in the right position
	"""
	n = len(the_list)
	for j in range(n - 1, 0, -1):
		swapped = False
		for i in range(j):
			if the_list[i] > the_list[i + 1]:
				swap(the_list, i, i + 1)
				swapped = True
		if not swapped:
			break


def selection_sort(the_list):
	"""
	Selection sort.

	@complexity: 	best case is O(N^2) when the list is sorted, but the loop for searching minimum index runs according to outer loop
					worst-case is O(N^2) when the list is unsorted, both loop runs and sorted accordingly
	@stability: 	not stable as the elements in a relative order might be swapped (swapping non consecutive elements)
	@incremental:	not incremental because the minimum index is selected and swap so if the new element is the largest
					as compared to all the elements, irregardless of adding to the front or back, then the loop will
					run N^2 times until it puts the new element in the right position
	"""
	n = len(the_list)
	for start in range(n - 1):
		min_index = get_minimum(the_list, start)
		swap(the_list, start, min_index)


def get_minimum(the_list, index):
	min_index = index
	n = len(the_list)
	for i in range(index + 1, n):
		if the_list[i] < the_list[min_index]:
			min_index = i
	return min_index


def swap(the_list, i, j):
	the_list[i], the_list[j] = the_list[j], the_list[i]


def insertion_sort(the_list):
	"""

	@complexity: 	best-case is O(N) when list is already sorted so the while loop won't run as the element before
					the marked's element is always less than the marked's element, so no swapping occur
					worst-case is O(N^2) when the list is in reversed order so both outer and inner loop runs
	@stability:		stable, because element is compared with the element adjacent to it and only swap if the
					element before is > and not >=, so the relative order of the elements will be maintained
	@incremental:	yes if the new element is added to the back as the "mark" could iterate the new element and put into
					the right position. no if the new element is added to the front as both loops would have to
					re-iterate N^2 times to find the "right position" for the new element
	"""
	n = len(the_list)
	for index in range(1, n):
		value = the_list[index]
		i = index - 1  # represent the index adjacent to the current index (index)
		while i >= 0 and the_list[i] > value:
			the_list[i + 1] = the_list[i]
			i -= 1
		the_list[i + 1] = value


def insertsort(alist):
	n = len(alist)
	for i in range(1, n):
		mark = alist[i]
		while i > 0 and alist[i-1] > mark:
			alist[i] = alist[i-1]
			i -= 1
		alist[i] = mark


def binary_search(the_list, target):
	n = len(the_list)
	lower = 0
	upper = n - 1

	while lower <= upper:
		mid = (lower + upper) // 2
		if target == the_list[mid]:
			return mid
		elif target > the_list[mid]:
			lower = mid + 1
		else:
			upper = mid - 1
	return -1


def merge_sort(the_list):
	temp = [0] * len(the_list)
	start = 0
	end = len(the_list) -1
	merge_sort_aux(the_list, start, end, temp)

def merge_sort_aux(the_list, start, end, temp):
	if start != end:
		mid = (start + end) // 2

		merge_sort_aux(the_list, start, mid, temp)
		merge_sort_aux(the_list, mid+1, end, temp)

		merge_arrays(the_list, start, mid, end, temp)

		for i in range(start, end+1):
			the_list[i] = temp[i]


def merge_arrays(the_list, start, mid, end, temp):
	i = start
	j = mid+1

	for k in range(start, end+1):
		if i > mid:
			temp[k] = the_list[j]
			j += 1
		elif j > end:
			temp[k] = the_list[i]
			i += 1
		elif the_list[i] > the_list[j]:
			temp[k] = the_list[j]
			j += 1
		else:
			temp[k] = the_list[i]
			i += 1

a = [5,15,10,30,3,1,8,4]
merge_sort(a)


def quick_sort(the_list):
	start = 0
	end = len(the_list) -1
	quick_sort_aux(the_list, start, end)

def quick_sort_aux(the_list, start, end):
	if start < end:
		pivot_index = partition(the_list, start, end)
		quick_sort_aux(the_list, start, pivot_index-1)
		quick_sort_aux(the_list, pivot_index+1, end)


def partition(the_list, start, end):
	mid = (start + end) // 2
	# pivot = the_list[mid]
	swap(the_list, start, mid)
	index = start

	for i in range(start+1, end+1):
		if the_list[i] < the_list[start]:
			index += 1
			swap(the_list, index, i)
	swap(the_list, start, index)
	return index

a = [5,15,10,30,3,1,8,4]
# print(partition(a, 0, 3))
# print(a)
quick_sort(a)


def test_bubble_sort():
	a = [5, 4, 3, 2, 1]
	bubble_sort(a)
	assert a == [1, 2, 3, 4, 5], "sorting failed"

	a = [1, 2, 3, 4]
	bubble_sort(a)
	assert a == [1, 2, 3, 4], "sorting failed, should not sort"

	a = [5, 4, 3, 2, 1]
	bubble_sort2(a)
	assert a == [1, 2, 3, 4, 5], "sorting failed"

	a = [1, 2, 3, 4]
	bubble_sort2(a)
	assert a == [1, 2, 3, 4], "sorting failed, should not sort"


def test_selection_sort():
	a = [5, 4, 3, 2, 1]
	selection_sort(a)
	assert a == [1, 2, 3, 4, 5], "sorting failed"
	print(a)


def test_insertion_sort():
	a = [5, 3, 4, 6, 2]
	insertion_sort(a)
	assert a == [2, 3, 4, 5, 6], "sorting failed"


def duplicates2(alist):
	duplicate = []
	queue = Queue(len(alist))
	for item in alist:
		queue.push(item)

	for i in range(1, len(alist)):
		item = queue.serve()
		if item in alist[i:] and item not in duplicate:
			duplicate.append(item)

	for num in duplicate:
		print(num)

def duplicates(alist):
	count = [0] * (max(alist) + 1)

	for num in alist:
		count[num] += 1

	for i in range(len(count)):
		if count[i] > 1:
			print(i)


def magnitude(a_queue):
	temp_queue = Queue()
	temp_stack = Stack()

	while not a_queue.is_empty():
		item = a_queue.serve()
		if item < 0:
			temp_stack.push(item)
		else:
			temp_queue.push(item)

	queue = Queue()

	if temp_queue.is_empty():
		while not temp_stack.is_empty():
			queue.push(temp_stack.pop())

	if temp_stack.is_empty():
		while not temp_queue.is_empty():
			queue.push(temp_queue.serve())

	if not temp_queue.is_empty() and not temp_stack.is_empty():
		stack_item = temp_stack.pop()
		queue_item = temp_queue.serve()

		while True:
			# comparing all elements
			if abs(stack_item) <= queue_item:
				queue.push(stack_item)
				if temp_stack.is_empty():
					queue.push(queue_item)
					while not temp_queue.is_empty():
						queue.push(temp_queue.serve())
					break
				# before pop, we need to check if it is empty, otherwise it will raise exception
				stack_item = temp_stack.pop()
			else:
				queue.push(queue_item)
				if temp_queue.is_empty():
					queue.push(stack_item)
					while not temp_stack.is_empty():
						queue.push(temp_stack.pop())
					break
				queue_item = temp_queue.serve()

	return queue

def heap_sort(array):
	heap = Heap()
	for item in array:
		heap.add(item, "")
	i = len(array) - 1
	while not heap.is_empty():
		array[i] = heap.get_max()
		i -= 1

if __name__ == '__main__':
	test_bubble_sort()
	test_selection_sort()
	test_insertion_sort()

	a = [5, 3, 8, 6, 4]
	print(a[1:])
	print(a[2:])
	print(a[3:])
	print(a[4:])
	insertsort(a)


	duplicates2([6, 10, 6, 11, 6, 4, 5, 4])
	duplicates([6,10,6,11,6,4,5,4])

	x = Queue(15)
	x.push(-322)
	x.push(-180)
	x.push(-5)
	x.push(3)
	x.push(7)
	x.push(10)
	x.push(180)
	x.push(360)

	print(magnitude(x).array)
	a = [5,15,10,30,3,1,8,4]
	heap_sort(a)
	print(a)
