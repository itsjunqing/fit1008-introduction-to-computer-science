from data_structures.node import Node

class LinkedQueue:
	def __init__(self):
		self.front = None
		self.rear = None
		self.queue_size = 0

	def is_empty(self):
		return self.queue_size == 0

	def is_full(self):
		return False

	def size(self):
		return self.queue_size

	def append(self, item):
		node = Node(item)
		if self.is_empty():
			self.front = node
		else:
			self.rear.link = node
		self.rear = node
		self.queue_size += 1

	def serve(self):
		if self.is_empty():
			raise Exception("Queue is empty")
		item = self.front.item
		self.front.item = None
		self.front = self.front.link
		self.queue_size -= 1
		if self.front is None:
			self.rear = None
		return item

	def reset(self):
		while not self.is_empty():
			self.serve()
		assert self.front is None
		assert self.rear is None
		assert self.is_empty()

if __name__ == "__main__":
	queue = LinkedQueue()
	queue.append(5)
	print(queue.front)
	print(queue.rear)
	queue.append(3)
	queue.append(4)

	print(queue.serve())
	print(queue.serve())
	print(queue.serve())

	print(str([1,2,3,4,5]))