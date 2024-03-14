from product import Product

def test_product_init_001():
	p = Product('apple', 10, 5);
	assert p.name == 'apple';
	assert p.price == 10;
	assert p.quantity == 5;


def test_product_init_002():
	p = Product('apple', 10, 5);
	p.name = 'Banana';
	assert p.name == 'Banana';

def test_product_init_003():
	p = Product('apple', 10, 5);
	p.price = 15;
	assert p.price == 15;


def test_product_init_004():
	p = Product('apple', 10, 5);
	p.quantity = 10;
	assert p.quantity == 10;


def test_product_init_005():
	p = Product('apple', 10, 5);
	try:
		p.name = "";
		assert False

	except Exception as e:
		assert str(e) == 'Name cannot empty';

def test_product_init_006():
	p = Product('apple', 10, 5);
	try:
		p.price = 0;
		assert False;

	except Exception as e:
		assert str(e) == 'Price must be positive number';

def test_product_init_007():
	p = Product('apple', 10, 5);
	try:
		p.quantity = 0;
		assert False;

	except Exception as e:
		assert str(e) == 'quantity must positive number';

