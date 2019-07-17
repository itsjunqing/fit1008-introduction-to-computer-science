from data_structures.ADT_stack import Stack

class Queue:
	def __init__(self, size=20):
		self.front = 0
		self.rear = 0
		self.count = 0
		self.array = [None] * size

	def is_empty(self):
		return self.count == 0

	def is_full(self):
		return self.count >= len(self.array)

	def length(self):
		return self.count

	def reset(self):
		self.front = 0
		self.rear = 0
		self.count = 0

	# operations for circular queue method starts here
	def push(self, item):
		if self.is_full():
			raise Exception("Queue is full")
		self.array[self.rear] = item
		self.count += 1
		# self.rear += 1
		# using circular method to prevent slot wastage:
		self.rear = (self.rear + 1) % len(self.array)

	def serve(self):
		if self.is_empty():
			raise Exception("Queue is empty")
		item = self.array[self.front]
		self.array[self.front] = None
		# self.front += 1
		# using circular method to prevent slot wastage:
		self.front = (self.front + 1) % len(self.array)
		self.count -= 1
		return item

	def print_all(self):
		index = self.front
		for _ in range(self.count):
			print(self.array[index])
			index = (index + 1) % len(self.array)



def reverse(my_queue):
	temp_queue = Queue()
	temp_stack = Stack()

	while not my_queue.is_empty():
		item = my_queue.serve()
		temp_queue.push(item)
		temp_stack.push(item)

	while not temp_stack.is_empty():
		item = temp_stack.pop()
		my_queue.append(temp_queue.serve())
		if item:
			temp_queue.push(item)

	return temp_queue


def interleave(queue1, queue2):
	queue = Queue()

	while not queue1.is_empty() and not queue2.is_empty():
		queue.push(queue1.serve())
		queue.push(queue2.serve())

	while not queue1.is_empty():
		queue.push(queue1.serve())

	while not queue2.is_empty():
		queue.push(queue2.serve())
	return queue

if __name__ == "__main__":

	queue = Queue()
	queue.push(1)
	queue.push(2)
	queue.push(3)
	queue.push(4)
	queue.push("")
	queue.push("bye")

	reverse(queue).print_all()

