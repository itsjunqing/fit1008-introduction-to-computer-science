class Item:
	def __init__(self, value, weight):
		self.value = value
		self.weight = weight


def knapsack_value(item_list, capacity):
	memory = [0] * (len(item_list) + 1)
	for i in range(len(memory)):
		memory[i] = [0] * (capacity + 1)

	# i to keep track of current row (item)
	i = 1  # item 1
	for item in item_list:
		for j in range(1, capacity + 1):
			# while the current knapsack capacity is less than the item's weight, then store the previous list's value of the index
			if item.weight > j:
				memory[i][j] = memory[i - 1][j]
			else:
				memory[i][j] = max(memory[i - 1][j],
								   item.value + memory[i - 1][j - item.weight])
		i += 1

	for line in memory:
		print(line)

	items = []
	j = capacity
	for i in range(len(item_list), 0, -1):
		if j == 0:
			break
		if memory[i][j] != memory[i - 1][j]:
			items.append(i)
			j -= item_list[i - 1].weight
	items = items[::-1]

	return memory[-1][-1], items


def knapsack_duplicate(item_list, capacity):
	memory = [0] * (len(item_list) + 1)
	for i in range(len(memory)):
		memory[i] = [0] * (capacity + 1)

	# i to keep track of current row (item)
	i = 1  # item 1
	for item in item_list:
		for j in range(1, capacity + 1):
			# while the current knapsack capacity is less than the item's weight, then store the previous list's value of the index
			if item.weight > j:
				memory[i][j] = memory[i - 1][j]
			else:
				memory[i][j] = max(memory[i - 1][j],
								   item.value + memory[i - 1][j - item.weight],
								   item.value + memory[i][j - item.weight])
		i += 1

	for line in memory:
		print(line)

	return memory[-1][-1]


itemList = []
# item = Item(4000, 20)
# itemList.append(item)
# item = Item(3500, 10)
# itemList.append(item)
# item = Item(1800, 9)
# itemList.append(item)
# item = Item(400, 4)
# itemList.append(item)
# item = Item(1000, 2)
# itemList.append(item)
# item = Item(200, 1)
# itemList.append(item)
# print(knapsack_value(itemList, 20))

item = Item(4, 3)
itemList.append(item)
item = Item(5, 4)
itemList.append(item)
item = Item(10, 7)
itemList.append(item)
item = Item(11, 8)
itemList.append(item)
item = Item(13, 9)
itemList.append(item)

# tutorial without duplicates
print(knapsack_value(itemList, 17))
# tutorial with duplicates
print(knapsack_duplicate(itemList, 17))
