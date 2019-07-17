# using normal recursive method
def fib_normal(n):
	return fib_aux_normal(n)

def fib_aux_normal(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

# using tail recursion where it passes the base case into the auxilary method
def fib(n):
	return fib_aux(n, 0, 1)

def fib_aux(n, before_last, last):
	if n == 0:
		return before_last
	else:
		return fib_aux(n-1, last, before_last+last)

# using dynamic programming
def dp_fib(n):
	memo = [0] * (n + 1)
	memo[0] = 0
	memo[1] = 1
	for i in range(2, n + 1):
		memo[i] = memo[i - 1] + memo[i - 2]
	return memo[n]

def coins(coins):
	coins_value = [0] * (len(coins) + 1)
	coins_value[1] = coins[0]
	for i in range(2, len(coins)+1):
		coins_value[i] = max(coins_value[i-1], coins_value[i-2] + coins[i-1])
	return coins_value[-1]

# using normal recursive way
def binomial(n, k):
	# assumes that k <= n so no checking is done
	# base case starts here, where k = 0 or k = n, like 3C0 = 3C3 = 1
	if k == 0 or k == n:
		return 1
	else:
		return binomial(n-1, k-1) + binomial(n-1, k)

# using dp approach
def dp_binomial(n, k):
	table = [0] * (n+1)
	for i in range(len(table)):
		table[i] = [0] * (k+1)

	for i in range(1, n+1):
		for j in range(k+1):
			# base case
			if i == j or j == 0:
				table[i][j] = 1
			else:
				table[i][j] = table[i-1][j] + table[i-1][j-1]

	return table[n][k]



if __name__ == '__main__':
	print(dp_fib(5))
	print(fib(5))
	print(fib_normal(5))

	print(coins([7, 2, 10, 12, 5]))

	print(binomial(3, 1))
	print(binomial(3, 2))

	print(dp_binomial(3, 0))
	print(dp_binomial(3, 1))
	print(dp_binomial(3, 2))
	print(dp_binomial(3, 3))
