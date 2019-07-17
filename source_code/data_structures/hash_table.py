class HashTable:
	def __init__(self, table_capacity=10, hash_base=10):
		"""
		Initializes an instance of the HashTable with a table_capcity and a hash_base.
		If capacity and base are not given, default figures of 10 are used.

		@param table_capacity:	the size of the table
		@param hash_base:		the base value for the hash function
		"""
		self.table = [None] * table_capacity
		self.table_capacity = table_capacity
		self.hash_base = hash_base
		self.count = 0

	def hash(self, key):
		"""
		Calculates the hash value for the given key by using the base value instantiated.

		@param key: 	the key to be hashed
		@complexity: 	best and worst-case is O(N) where N is the length of the key
		@return:		a hash value of the key
		"""
		value = 0
		for i in range(len(key)):
			value = (value * self.hash_base + ord(key[i])) % self.table_capacity
		return value

	def __contains__(self, key):
		"""
		Returns True if key is in the table and False otherwise.

		@param key:		the key to check
		@precondition:	none
		@postcondition: none
		@complexity: 	best-case is O(N) where N is the length of the key (used for obtaining hash value)
							and this happens when the key is immediately found at the position hashed (no probing occur)
						worst-case is O(N*M) where N is the length of the key (used for obtaining hash value)
							and M is the size of the table, this happens when key is not in the hash table
							and it is probed continuously
		@return:		True if the key is in hash table and False otherwise
		"""
		position = self.hash(key)
		for _ in range(self.table_capacity):
			if self.table[position] == None:
				return False
			elif self.table[position][0] == key:
				return True
			else:
				position = (position + 1) % self.table_capacity
		return False

	def __setitem__(self, key, value):
		"""
		Sets the value corresponding to key in the hash table to be value.
		If the hash table is full and the key does not exist in the table yet,
		it first calls the rehash method and then reinserts the key and value.

		@param key:		key to be hashed
		@param value:	value to associate with the key
		@precondition:	none
		@postcondition:	value is associated with the key at the hashed key position
		@complexity:	best-case is O(N) where N is the length of the key (used for obtaining hash value)
							and this happens when the None is found at the position hashed and immediately inserted
							without any probing
						worst-case is O(N*M) where N is the length of the key (used for obtaining hash value)
							and M is the size of the table, this happens when no empty slot is found and
							it is probed continuously until it calls the rehash method
		@return:		none
		"""
		position = self.hash(key)
		for _ in range(self.table_capacity):
			if self.table[position] == None:
				self.table[position] = (key, value)
				self.count += 1
				return
			elif self.table[position][0] == key:
				self.table[position] = (key, value)
				return
			else:
				position = (position + 1) % self.table_capacity
		self.rehash()
		self.__setitem__(key, value)

	def __getitem__(self, key):
		"""
		Returns the value corresponding to key in the hash table.

		@param key:		the key to access the item
		@precondition:	none
		@postcondition:	none
		@complexity:	best-case is O(N) where N is the length of the key (used for obtaining hash value)
							and this happens when position found is None or the key is found at the position
						worst-case is O(N*M) where N is the length of the key (used for obtaining hash value)
							and M is the size of the table, this happens when key is not in the hash table
							and it is probed continuously until it raises a KeyError
		@raises: 		KeyError if no such key is found in the hash table
		@return:		thee item found at the hashed key position
		"""
		position = self.hash(key)
		for _ in range(self.table_capacity):
			if self.table[position] == None:
				raise KeyError(key)
			elif self.table[position][0] == key:
				return self.table[position][1]
			else:
				position = (position + 1) % self.table_capacity
		raise KeyError(key)

	def rehash(self):
		"""
		Updates the size of the hash table with a prime number that is double the existing table size
		All keys are rehash according to the new table size.

		@precondition:	none
		@postcondition:	size of hash table is updated where the size is larger than the double existing size
						and table is updated where keys are hashed to new position
		@complexity:	best-case and worst-case is O(N*M) where N is the length of the key
							(used for obtaining hash value) and M is the size of the existing hash table
							and this happens when the value of hashed key in the new hash table is None
							and is inserted immediately without probing
		@raises:		ValueError if no prime number is found that is larger than the doubled size
		@return: 		none
		"""
		primes = [3, 7, 11, 17, 23, 29, 37, 47, 59, 71, 89, 107, 131, 163, 197, 239, 293, 353, 431, 521, 631, 761, 919,
				  1103, 1327, 1597, 1931, 2333, 2801, 3371, 4049, 4861, 5839, 7013, 8419, 10103, 12143, 14591, 17519,
				  21023, 25229, 30293, 36353, 43627, 52361, 62851, 75431, 90523, 108631, 130363, 156437, 187751, 225307,
				  270371, 324449, 389357, 467237, 560689, 672827, 807403, 968897, 1162687, 1395263, 1674319, 2009191,
				  2411033, 2893249, 3471899, 4166287, 4999559, 5999471, 7199369]
		new_size = self.table_capacity * 2
		size_changed = False
		for prime in primes:
			if prime > new_size:
				new_size = prime
				size_changed = True
				break
		if not size_changed:
			raise ValueError("No prime found")

		new_hash_table = HashTable(new_size, self.hash_base)
		for i in range(self.count):
			key = self.table[i][0]
			value = self.table[i][1]
			new_hash_table[key] = value

		self.table = new_hash_table.table
		self.table_capacity = new_size
