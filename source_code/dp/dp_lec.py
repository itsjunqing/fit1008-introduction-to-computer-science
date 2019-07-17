def longest_positive_sequence(the_list):
	"""
	Function that given a list, it returns the longest number of positive numbers.
	If it returns 3, then there exists 3 consecutive positive numbers.

	@param the_list:	an array of integers
	@complexity:		best-case and worst-case is O(N) where N is the length of the list
						this happens when the loop iterates the entire given list to compute
						the number of consecutive positive numbers and store them in a memory
	@return:			longest number of positive numbers
	"""
	memory = [0] * len(the_list)
	# base case
	if the_list[0] > 0:
		memory[0] = 1

	# counter to keep track of the longest count of positive numbers
	longest_length = memory[0]

	# dynamic approach
	for i in range(1, len(the_list)):
		if the_list[i] > 0:
			memory[i] = 1 + memory[i-1]

		if memory[i] > longest_length:
			longest_length = memory[i]

	print(memory)
	print(longest_length)

	return longest_length

longest_positive_sequence([1,2,0,5,1,7,8,9,0,1,0,0,-5,-9,-7,1])

def max_subsequent_sum(the_list):
	"""
	Function that returns the maximum sum of consecutive numbers in a list.

	@param the_list:	an array with integers
	@return:			maximum sum of consecutive numbers in the list
	"""
	memory = [0] * len(the_list)
	memory[0] = the_list[0]

	for i in range(1, len(the_list)):
		memory[i] = max(the_list[i], the_list[i] + memory[i-1])

	print(memory)
	return max(memory)

print(max_subsequent_sum([1,2,0,-4,1,2,96,-1,-100,99,0,0,-5,-9,-7,25]))
print(max_subsequent_sum([90,90,0,-200,1,2,96,-1,-100,99,0,0,-5,-9,-7,25]))


def A(num):
	array = [0] * (num+1)
	array[0] = 1
	array[1] = 1
	return A_aux(num, array, 2)

def A_aux(num, array, k):
	if k > num:
		return array
	else:
		array[k] = array[k-1]+ (2*array[k-2])
		return A_aux(num, array, k+1)

A(6)