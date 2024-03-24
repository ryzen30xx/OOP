from fraction import Fraction

def test_add():
    frac1 = Fraction(1, 2)
    frac2 = Fraction(1, 3)
    result = frac1.add(frac2)
    assert result.numerator == 5
    assert result.denominator == 6

def test_sub():
    frac1 = Fraction(3, 4)
    frac2 = Fraction(1, 4)
    result = frac1.sub(frac2)
    assert result.numerator == 3 * 4 - 1 * 4 
    assert result.denominator == 16



def test_mul():
    frac1 = Fraction(2, 3)
    frac2 = Fraction(3, 4)
    result = frac1.mul(frac2)
    assert result.numerator == 2 * 3 
    assert result.denominator == 3 * 4


def test_div():
    frac1 = Fraction(2, 3)
    frac2 = Fraction(1, 2)
    result = frac1.div(frac2)
    assert result.numerator == 4
    assert result.denominator == 3

def test_zero_division():
    frac1 = Fraction(2, 3)
    frac2 = Fraction(0, 1)
    try:
        result = frac1.div(frac2)
    except ValueError as e:
        assert str(e) == "Division by zero"
