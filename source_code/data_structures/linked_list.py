from data_structures.node import Node


class LinkedList:
	def __init__(self):
		self.head = None
		self.list_size = 0

	def is_empty(self):
		return self.list_size == 0

	def is_full(self):
		return False

	def __len__(self):
		return self.list_size

	def size(self):
		return self.list_size

	def _get_node(self, index):
		assert index >= 0 and index < self.list_size, "index out of bounds"
		node = self.head
		for _ in range(index):
			node = node.link
		return node

	def insert(self, index, item):
		if index < 0:
			index = 0
		elif index > self.list_size:
			index = self.list_size

		if index == 0:
			node = Node(item, self.head)
			self.head = node
		else:
			node = self._get_node(index - 1)
			node.link = Node(item, node.link)
		self.list_size += 1

	def delete(self, index):
		assert not self.is_empty(), "list is empty"
		assert index >= 0 and index < self.list_size, "index out of bounds"

		if index == 0:
			self.head = self.head.link
		else:
			node = self._get_node(index - 1)
			node.link = node.link.link
		self.list_size -= 1

	def __str__(self):
		ret = ""

		current = self.head
		while current is not None:
			ret = ret + str(current.item) + ","
			current = current.link
		return ret

	def copy(self):
		new_list = LinkedList()
		self.copy_aux(self.head, new_list)
		return new_list

	# complexity of O(N2) cause insert inserts at the end of the list, needs to iterate
	def copy_aux(self, current, new_list):
		if current is not None:
			new_list.insert(len(new_list), current.item)
			self.copy_aux(current.link, new_list)

	# complexity of O(N) cause insert inserts at the front of the list, no need to iterate
	def copy_aux2(self, current, new_list):
		if current is not None:
			self.copy_aux(current.link, new_list)
			new_list.insert(0, current.item)

	def periodic_delete(self, n):
		# change the pointer of self.head
		for _ in range(n):
			if self.head is not None:
				self.head = self.head.link
		current = self.head
		while current is not None:
			previous = current
			current = current.link
			# keep the next n-1 unchanged
			for _ in range(n - 1):
				if current is not None:
					previous = current
					current = current.link
			# delete the next n
			for _ in range(n):
				if current is not None:
					previous.link = current.link
					current = current.link

	def periodic_delete2(self, n):
		self.head = self.get_node(self.head, n)
		current = self.head
		while current is not None:
			# keep the next n-1 unchanged
			previous = self.get_node(current, n - 1)
			# every time when get_node is called, we need to check if the returned result is None before proceeding next step
			if previous is not None:
				# delete the next n by changing the pointer of previous to the next n node
				current = self.get_node(previous.link, n)
				previous.link = current
			else:
				# if the previous is None, means the next n-1 (at most) is unchanged, so current = None to stop loop
				current = None

	def get_node(self, current, n):
		while current is not None and n > 0:
			current = current.link
			n -= 1
		return current

	def double_list(self):
		current = self.head
		while current is not None:
			node = Node(current.item, current.link)
			current.link = node
			current = current.link.link


	def add_sorted(self, item):
		if self.head is None:
			self.head = Node(item)
			self.count += 1
			return
		current = self.head
		previous = None
		while current is not None:
			if current.item < item:
				previous = current
				current = current.link
			else:
				break

		if previous is not None:
			node = Node(item, previous.link)
			previous.link = node
			self.count += 1
		else:
			self.head = Node(item, self.head)
			self.count += 1





if __name__ == '__main__':
	a_list = LinkedList()
	# a_list.insert(0, 13)
	# a_list.insert(0, 12)
	# a_list.insert(0, 11)
	# a_list.insert(0, 10)
	# a_list.insert(0, 9)
	# a_list.insert(0, 8)
	# a_list.insert(0, 7)
	# a_list.insert(0, 6)
	# a_list.insert(0, 5)
	a_list.insert(0, 4)
	a_list.insert(0, 3)
	a_list.insert(0, 2)
	a_list.insert(0, 1)
	print(a_list)

	# a_list.periodic_delete(4)
	# print(a_list)
	a_list.double_list()
	print(a_list)
