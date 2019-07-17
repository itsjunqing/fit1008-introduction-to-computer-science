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


class myclass:
	def __init__(self, x):
		self.x = x

	def print(self):
		print(self.x)

	def a(self):
		self.x = self.x + 1

	def b(self):
		self.x = x + 2

	def c(self):
		x = self.x + 3


def a(x):
	x = x - 1


def b():
	x = x + 1


if __name__ == '__main__':
	# car2 = Car("Nissan", 2400)
	# car2.setColour("Green")
	# car2.engineLocation = "Back"
	# car2.tyreNumber = 6
	#
	# car1 = Car("Toyota", 1000)
	# car1.setSeatNumber(3)
	# car1.steeringLocation = "Right"
	# car1.colour = "Red"
	# car1.regionCode = 100000
	#
	# print(car2.colour)
	# print(car1.colour)
	# print(car2.steeringLocation)
	# print(car1.engineLocation)
	#
	# Car.tyreNumber = 3
	# car1.enginePower = 500
	#
	# car3 = Car("Honda", 50000)
	# print(car3.tyreNumber)
	#
	# print(car2.tyreNumber)
	# print(car1.tyreNumber)
	# print(car2.enginePower)
	# print(car1.seatNumber)
	x = 1
	myobject = myclass(x)
	myobject.print()
	x = 2

	myobject.print()
	myobject.x = 1
	myobject.a()
	myobject.print()
	myobject.b()
	myobject.print()
	myobject.c()
	myobject.print()
	a(x)
	print(x)
	myclass.x = 1
	myclass.print(myobject)
	myobject.x = 2
	myclass.print(myobject)
	myobject.c()
	print(myclass.x)
	yourobject = myclass(myobject.x)
	yourobject.a()
	myobject.print()
	b()
	print(x)
