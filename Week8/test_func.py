
def add(a, b):
	c = a + b
	return c


def multiply(n):
	result = 1
	if n < 0:
		raise ValueError('No factorial for negative number');
	else:
		for i in range(1, n+1):
			result *= i

		return result


