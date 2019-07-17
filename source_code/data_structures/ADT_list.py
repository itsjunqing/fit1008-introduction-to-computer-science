class List:
	def __init__(self, size):
		# self.count represents the number of elements in the list, initially there is no element, so 0
		self.count = 0
		self.array = [None] * size

	def is_empty(self):
		return self.count == 0

	def is_full(self):
		return self.count >= len(self.array)

	def length(self):
		return self.count

	# operations starts here
	def add(self, item):
		has_space_left = not self.is_full()
		if has_space_left:
			self.array[self.count] = item
			self.count += 1
		return has_space_left

	def delete(self, index):
		# the given index must be within the range of possible count
		# eg: if the list is [1,2,3,4,5], self.count is 5, check must happen between 0 and 5 (inclusive)
		# this is to ensure that such index with an item actually exists in the list
		valid_index = index >= 0 and index < self.count
		if valid_index:
			# eg: index = 2, after removing index 2, list = [1,2,4,5,None]
			for i in range(index, self.count-1):
				self.array[i] = self.array[i+1]
			self.array[self.count-1] = None
			self.count -= 1
		return valid_index

	def print_all(self):
		for i in range(self.count):
			print(self.array[i], end=" ")


