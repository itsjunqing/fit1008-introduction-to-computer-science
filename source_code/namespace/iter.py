from data_structures.node import Node

# ListIterator class to iterate a list through the command "for xxx in xxx"
# Class will consists of the __init__, __iter__, and __next__ method
# all three methods are needed to construct an iterable list
class ListIterator:
	def __init__(self, head):
		# this ListIterator uses linked node implementation
		self.current = head

	def __iter__(self):
		return self

	def __next__(self):
		if self.current is None:
			raise StopIteration
		item_list = self.current.item
		self.current = self.current.link
		return item_list

		# Alternative method below by using try-catch block
		# try:
		# 	item_required = self.current.item
		# 	self.current = self.current.link
		# 	return item_required
		# except AttributeError:
		# 	raise StopIteration

class List:
	def __init__(self):
		self.head = None
		self.count = 0

	def __iter__(self):
		return ListIterator(self.head)

	def is_empty(self):
		return self.count == 0

	def is_full(self):
		return False

	def _get_node(self, index):
		assert 0 <= index < self.count, "index out of bound"
		node = self.head
		for _ in range(index):
			node = node.link
		return node

	def insert(self, index, item):
		if self.is_full():
			return False
		if index < 0:
			index = 0
		elif index > self.count:
			index = self.count

		if index == 0:
			self.head = Node(item, self.head)
		else:
			node = self._get_node(index - 1)
			node.link = Node(item, node.link)
		self.count += 1
		return True

	def delete(self, index):
		valid_index = index >= 0 and index < self.count
		if self.is_empty():
			return False

		if valid_index:
			if index == 0:
				self.head = self.head.next
			else:
				node = self._get_node(index - 1)
				node.link= node.link.link
			self.count -= 1

		return valid_index

	def __str__(self):
		ret = ""

		current = self.head
		while current is not None:
			ret = ret + str(current.item) + ","
			current = current.link
		return ret

	def __len__(self):
		return self.count


a_list = List()
a_list.insert(0, 4)
a_list.insert(0, 3)
a_list.insert(0, 2)
a_list.insert(0, 1)
# itera = iter(a_list)
# print(next(itera))
# print(next(itera))
# print(next(itera))
# print(next(itera))
# print(str(a_list))
#
# # similar to calling next(itera)
# for item in a_list:
# 	print(item)


class MyRange:
	def __init__(self, start, end):
		self.current = start
		self.end = end

	def __iter__(self):
		return self

	def __next__(self):
		if self.current >= self.end:
			raise StopIteration
		item = self.current
		self.current += 1
		return item


class MyRange2:
	def __init__(self, head):
		self.current = head

	def __iter__(self):
		return self

	def __next__(self):
		if self.current is None:
			raise StopIteration
		item = self.current.item
		self.current = self.current.link
		return item

myrange = MyRange(1, 10)
myrangeiter = iter(myrange)
print(next(myrangeiter))

for item in myrange:
	print(item)

myrange2 = MyRange2()