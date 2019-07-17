def max_repetitions(alist):
	if len(alist) == 0:
		return None
	memo = [0] * (max(alist) + 1)
	for item in alist:
		memo[item] += 1
	max_times = max(memo)
	return memo.index(max_times)

print(max_repetitions([1,1,2,2,2,3,2]))
print(max_repetitions([1,1,1,1,1,1,1]))
print(max_repetitions([]))
print(max_repetitions([1,2,3,4,5,6]))
