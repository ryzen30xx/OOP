from calculation import calculate_shipping_fee

def test_case_001():
    weight_unit = 'Pounds'
    weight = 10
    distance_unit = 'Miles'
    distance = 1
    selected_method = 'Standard'
    result = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert result == 5.5305  # Expected output

def test_case_002():
    weight_unit = 'Kilograms'
    weight = 20
    distance_unit = 'Kilometers'
    distance = 10
    selected_method = 'Express'
    result = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert result == 12.5

def test_case_003():
    weight_unit = 'Pounds'
    weight = 0
    distance_unit = 'Miles'
    distance = 1
    selected_method = 'Priority'
    try:
        result = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    except ValueError as e:
        assert str(e) == "Weight must be greater than 0"

def test_case_004():
    weight_unit = 'Kilograms'
    weight = 20
    distance_unit = 'Miles'
    distance = 0
    selected_method = 'Standard'
    try:
        result = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    except ValueError as e:
        assert str(e) == "Distance must be greater than 0"

def test_case_005():
    weight_unit = 'Pounds'
    weight = 10
    distance_unit = 'Miles'
    distance = 1
    selected_method = 'Priority'
    try:
        result = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    except KeyError as e:
        assert str(e) == "Priority"

def test_case_006():
    weight_unit = 'Kilograms'
    weight = 20
    distance_unit = 'Miles'
    distance = 10
    selected_method = 'Standard'
    result = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert result == 20.8055

def test_case_007():
    weight_unit = 'Pounds'
    weight = 10
    distance_unit = 'Kilometers'
    distance = 1
    selected_method = 'Express'
    result = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert result == 18.1555

def test_case_008():
    weight_unit = 'Kilograms'
    weight = 20
    distance_unit = 'Miles'
    distance = 10
    selected_method = 'Priority'
    result = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert result == 40.8055

def test_case_009():
    weight_unit = 'Pounds'
    weight = 0.5
    distance_unit = 'Kilometers'
    distance = 1
    selected_method = 'Standard'
    result = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert result == 7.5305

def test_case_010():
    weight_unit = 'Kilograms'
    weight = 1
    distance_unit = 'Miles'
    distance = 0.5
    selected_method = 'Express'
    result = calculate_shipping_fee(weight_unit, weight, distance_unit, distance, selected_method)
    assert result == 14.7555
