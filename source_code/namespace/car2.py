from data_structures.node import Node


class Lissy:
	def __init__(self):
		self.head = None
		self.size = 0

	def is_empty(self):
		return self.head is None

	def _get_node(self, index):
		assert index >= 0 and index < self.size, "index out of bounds"
		node = self.head
		for _ in range(index):
			node = node.link
		return node

	def insert(self, index, item):
		if index < 0:
			index = 0
		elif index > self.size:
			index = self.size

		if index == 0:
			node = Node(item, self.head)
			self.head = node
		else:
			node = self._get_node(index - 1)
			node.link = Node(item, node.link)
		self.size += 1

	def copy(self):
		copy = Lissy()
		current = self.head
		previous = None

		while current is not None:
			if previous is None:
				copy.head = Node(current.item)
				previous = copy.head
			else:
				previous.link = Node(current.item)
				previous = previous.link
			current = current.link
		print(copy)
		return copy


# question 11 2018 Semester 1
class Car:
	tyreNumber = 4
	steeringLocation = "Left"
	engineLocation = "Front"
	regionCode = 1770174

	def __init__(self, brand, enginePower):
		self.brand = brand
		self.enginePower = enginePower

	def setSeatNumber(self, numberOfSeat):
		self.seatNumber = numberOfSeat

	def setColour(self, colour):
		Car.colour = colour


if __name__ == '__main__':
	# new = Lissy()
	#
	# new.insert(0, "A")
	# new.insert(1, "B")
	# new.insert(2, "C")
	# new.insert(3, "D")
	#
	# new.copy()

	car2 = Car("Nissan", 2400)
	car2.setColour("Green")
	car2.engineLocation = "Back"
	car2.tyreNumber = 6

	car1 = Car("Toyota", 1000)
	car1.setSeatNumber(3)
	car1.steeringLocation = "Right"
	car1.colour = "Red"
	car1.regionCode = 100000

	print(car2.colour)
	print(car1.colour)
	print(car2.steeringLocation)
	print(car1.engineLocation)

	Car.tyreNumber = 3
	car1.enginePower = 500

	car3 = Car("Honda", 50000)
	print(car3.tyreNumber)

	print(car2.tyreNumber)
	print(car1.tyreNumber)
	print(car2.enginePower)
	print(car1.seatNumber)
