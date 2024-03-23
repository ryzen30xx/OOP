from calculation import calculate_shipping_fee


def test_case_001():
    weight_unit = 'Pounds'
    weight = 10
    distance_unit = 'Miles'
    distance = 1
    selected_method = 'Standard'
    result = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert result == 5.5305

def test_case_002():
    weight_unit = 'Pounds'
    weight = 5
    distance_unit = 'Miles'
    distance = 2
    selected_method = 'Express'
    result = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert result == 11.5305

def test_case_003():
    weight_unit = 'Kilograms'
    weight = 15
    distance_unit = 'Kilometers'
    distance = 10
    selected_method = 'Priority'
    result = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert result == 30.0

def test_case_004():
    weight_unit = 'Pounds'
    weight = 0
    distance_unit = 'Miles'
    distance = 5
    selected_method = 'Standard'
    try:
        calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    except ValueError:
        assert True
    else:
        assert False

def test_case_005():
    weight_unit = 'Pounds'
    weight = 8
    distance_unit = 'Miles'
    distance = -2
    selected_method = 'Express'
    try:
        calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    except ValueError:
        assert True
    else:
        assert False

def test_case_006():
    weight_unit = 'Kilograms'
    weight = 20
    distance_unit = 'Kilometers'
    distance = 0
    selected_method = 'Priority'
    try:
        calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    except ValueError:
        assert True
    else:
        assert False

def test_case_007():
    weight_unit = 'Pounds'
    weight = -10
    distance_unit = 'Miles'
    distance = 3
    selected_method = 'Standard'
    try:
        calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    except ValueError:
        assert True
    else:
        assert False

def test_case_008():
    weight_unit = 'Pounds'
    weight = 12
    distance_unit = 'Miles'
    distance = 4
    selected_method = 'Express'
    result = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert result == 14.5305

def test_case_009():
    weight_unit = 'Kilograms'
    weight = 25
    distance_unit = 'Kilometers'
    distance = 20
    selected_method = 'Priority'
    result = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert result == 35.0

def test_case_010():
    weight_unit = 'Pounds'
    weight = 9
    distance_unit = 'Miles'
    distance = 6
    selected_method = 'Standard'
    result = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert result == 9.0305
