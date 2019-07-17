"""
4 operations:
1) add
2) get max
3) sink
4) rise

rise is executed by add where the new item rises upwards
sink is executed by get max where the root sinks downwards
"""


class Heap:
	def __init__(self, size=100):
		self.array = [None] * size
		self.count = 0

	def __len__(self):
		return self.count

	def is_empty(self):
		return self.count == 0

	def is_full(self):
		return self.count + 1 == len(self.array)

	def swap(self, i, j):
		self.array[i], self.array[j] = self.array[j], self.array[i]

	# main operations starts here

	def add(self, key, value):
		item = (key, value)
		if self.is_full():
			raise Exception("Heap is full")
		self.count += 1
		self.array[self.count] = item
		self.rise(self.count)

	def rise(self, k):
		while k > 1 and self.array[k][0] > self.array[k // 2][0]:
			self.swap(k, k // 2)
			k //= 2

	def get_max(self):
		item = self.array[1][0]
		self.array[1] = self.array[self.count]
		self.count -= 1
		self.sink(1)
		return item

	def sink(self, k):
		while 2 * k <= self.count:
			child = self.get_largest_child(k)
			if self.array[k][0] >= self.array[child][0]:
				break
			self.swap(child, k)
			k = child

	def get_largest_child(self, k):
		if 2 * k == self.count or self.array[2 * k][0] > self.array[2 * k + 1][0]:
			return 2 * k
		else:
			return 2 * k + 1

	def is_valid_max(self):
		k = 1
		while 2 * k <= self.count:
			child = self.get_largest_child(k)
			if self.array[k][0] < self.array[child][0]:
				return False
			k += 1
		return True

	def __str__(self):
		empty = ""
		for i in range(1, self.count + 1):
			empty += str(self.array[i]) + " "
		return empty

	def swap_children(self):
		k = 1
		# must have two children
		while 2 * k + 1 <= self.count:
			self.swap(2 * k, 2 * k + 1)
			self.sink(2 * k)
			self.sink(2 * k + 1)
			k += 1

if __name__ == '__main__':
	myheap = Heap()
	myheap.add(5, "test")
	myheap.add(3, "test1")
	myheap.add(1, "test3")
	myheap.add(4, "tes5")
	myheap.add(6, "tes8")
	myheap.add(10, "test9")
	# myheap.add(12, "test10")

	print(myheap)
	print(myheap.is_valid_max())
	myheap.swap_children()
	print(myheap)
