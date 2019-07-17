class Stack:
	def __init__(self, size=20):
		self.top = -1
		self.count = 0
		self.array = [None] * size

	def is_empty(self):
		return self.count == 0

	def is_full(self):
		return self.count >= len(self.array)

	def length(self):
		return self.count

	def push(self, item):
		if self.is_full():
			raise Exception("Stack is full")
		self.top += 1
		self.array[self.top] = item
		self.count += 1

	def pop(self):
		if self.is_empty():
			raise Exception("Stack is empty")
		item = self.array[self.top]
		self.array[self.top] = None
		self.top -= 1
		self.count -= 1
		return item

	def reset(self):
		while not self.is_empty():
			self.pop()
		return self.is_empty()


def isBalanced(string):
	left_brackets = "{(["
	right_brackets = "])}"

	stack = Stack()
	for char in string:
		if char in left_brackets:
			stack.push(char)
		elif char in right_brackets:
			if stack.is_empty():
				return False
			left_char = stack.pop()
			left_index = left_brackets.index(left_char)
			right_index = right_brackets.index(char)
			if left_index != right_index:
				return False
	return stack.is_empty()
