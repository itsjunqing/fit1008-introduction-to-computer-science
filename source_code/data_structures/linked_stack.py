from data_structures.node import Node

class LinkedStack:
	def __init__(self):
		self.top = None
		self.stack_size = 0

	def is_empty(self):
		return self.stack_size == 0

	def is_full(self):
		return False

	def size(self):
		return self.stack_size

	def push(self, item):
		self.top = Node(item, self.top)
		self.stack_size += 1

	def pop(self):
		if self.is_empty():
			raise Exception("Stack is empty")
		item = self.top.item
		self.top.item = None
		self.top = self.top.link
		self.stack_size -= 1
		return item

	def reset(self):
		while not self.is_empty():
			self.pop()
		assert self.top is None
		assert self.is_empty()
