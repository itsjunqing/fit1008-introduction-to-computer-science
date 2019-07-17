def merge_sort(alist):
	start = 0
	end = len(alist) - 1
	temp = [0] * len(alist)
	return merge_sort_aux(alist, start, end, temp)


def merge_sort_aux(alist, start, end, temp):
	if start < end:
		mid = (start + end) // 2
		merge_sort_aux(alist, start, mid, temp)
		merge_sort_aux(alist, mid+1, end, temp)
		merge_arrays(alist, start, mid, end, temp)
		# recopy the sorted elements from start to end into the original array
		for k in range(start, end + 1):
			alist[k] = temp[k]


# must use temp array to store the sorted arrays because we are unable to swap elements while moving from one to another and vice versa
def merge_arrays(alist, start, mid, end, temp):
	i = start
	j = mid + 1
	for k in range(start, end + 1):
		if i > mid:
			temp[k] = alist[j]
			j += 1
		elif j > end:
			temp[k] = alist[i]
			i += 1
		elif alist[i] > alist[j]:
			temp[k] = alist[j]
			j += 1
		else:
			temp[k] = alist[i]
			i += 1


a = [5, 15, 10, 30, 3, 1, 8, 4]
merge_sort(a)
print(a)
