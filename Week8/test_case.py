from test_func import add, multiply

def test_add_001():
	a = 4
	b = 0
	c = add(a, b)
	assert c == 4 # expected output

def test_add_002():
	a = 0
	b = 0
	c = add(a, b)
	assert c == 0 # expected output


def test_add_003():
	a = 0
	b = 4
	c = add(a, b)
	assert c == 4


def test_multi_001():
	n = 4
	re = multiply(n)
	assert re == 24

def test_multi_002():
	n = 1
	re = multiply(n)
	assert re == 1

def test_multi_003():
	n = 0
	re = multiply(n)
	assert re == 1

def test_multi_004():
	n = -1
	try:
		re = multiply(n)
		assert False
	except ValueError as e:
		assert str(e) == 'No factorial for negative number'
		


